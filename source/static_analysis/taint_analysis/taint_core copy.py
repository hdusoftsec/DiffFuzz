import angr
import claripy
import logging
import archinfo
import summary_func
import json
import sys
import os
import argparse
import multiprocessing
from multiprocessing import Pool

# 配置日志级别
logging.getLogger('angr').setLevel(logging.ERROR)

arch_mips32 = archinfo.ArchMIPS32()  # 创建MIPS32架构实例
arch_armel = archinfo.ArchARMEL()    # 创建ARMEL架构实例

# 正确定义ordered_argument_regs
ordered_argument_regs = {
    'ARMEL': [
        arch_armel.registers['r0'][0],
        arch_armel.registers['r1'][0],
        arch_armel.registers['r2'][0],
        arch_armel.registers['r3'][0],
    ],
    'MIPS32': [
        arch_mips32.registers['a0'][0],
        arch_mips32.registers['a1'][0],
        arch_mips32.registers['a2'][0],
        arch_mips32.registers['a3'][0],
    ],
}
func_params_regs = {
    "MIPS32": ["a0", "a1", "a2", "a3"],
    "ARMEL": ["r0", "r1", "r2", "r3"],
}

# 辅助函数，安全地将值转换为十六进制字符串
def safe_hex(value):
    """将值安全地转换为十六进制字符串，处理BV对象"""
    try:
        if isinstance(value, claripy.ast.BV):
            if value.symbolic:
                return "<symbolic>"
            else:
                return hex(value.args[0])
        return hex(value)
    except (TypeError, ValueError):
        return str(value)

class CoreTaint:
    """污点管理核心类，负责污点的创建、检查和传播追踪"""
    
    def __init__(self, project):
        self.project = project
        self.tainted_data = {}  # 存储被污染的数据 {key: taint_label}
        self.taint_history = []  # 污点传播历史
        self.global_var_symbols = {}  # 全局符号变量
        self.critical_variables = set()  # 关键变量
        self.tainted_addresses = set()  # 被污染的内存地址
        self.taint_propagation_paths = []  # 污点传播路径
        self.global_constraint_solutions = []  # 约束解
        self.memory_offset_counter = 0  # 内存偏移计数器
        self.taint_buf = "TAINT"  # 污点标识符
        
    def create_taint_var(self, name, bits=32*8):
        """创建污点符号变量"""
        taint_name = f"{self.taint_buf}_{name}"
        sym_var = claripy.BVS(taint_name, bits)
        return sym_var
    
    def apply_taint(self, state, varname, pc=None):
        """应用污点到内存并返回地址"""
        if varname not in self.global_var_symbols:
            # 创建符号变量
            sym_var = self.create_taint_var(varname)
            self.global_var_symbols[varname] = sym_var
            
            # 分配内存地址
            base_addr = 0x10000000
            tmp_addr = base_addr + (self.memory_offset_counter * 0x1000)
            self.memory_offset_counter += 1
            
            # 存储到内存
            state.memory.store(tmp_addr, sym_var)
            state.memory.store(tmp_addr + 31, claripy.BVV(0, 8))  # Null终止
            
            # 标记污点
            self.mark_taint(tmp_addr, varname, pc)
            
            # 记录内存区域污染
            for i in range(32):
                self.tainted_addresses.add(tmp_addr + i)
                self.mark_taint(tmp_addr + i, varname, pc)
            
            # 记录污点路径
            self.record_taint_path("SOURCE", pc, varname, tmp_addr)
            
            print(f"[污点生成] 变量 {varname} 被存储在地址 {safe_hex(tmp_addr)}")
            return tmp_addr
        else:
            print(f"[HOOK] 变量 {varname} 已存在")
            return None
    
    def mark_taint(self, key, taint_label, location=None):
        """标记数据为污点"""
        self.tainted_data[key] = taint_label
        if location:
            self.taint_history.append({
                "pc": location,
                "key": key,
                "label": taint_label
            })
    
    def is_tainted(self, key):
        """检查数据是否被污染"""
        return key in self.tainted_data
    
    def get_taint_label(self, key):
        """获取污点标签"""
        return self.tainted_data.get(key, None)
    
    def is_tainted_symbolic(self, value):
        """检查符号变量是否包含污点"""
        if isinstance(value, claripy.ast.BV):
            # 检查变量名是否包含污点标识符
            var_str = str(value)
            return self.taint_buf in var_str
        return False
    
    def check_taint(self, state, value, context=""):
        """检查值是否被污染（包括具体值和符号值）"""
        try:
            # 检查符号变量
            if self.is_tainted_symbolic(value):
                # 从符号变量名中提取污点标签
                var_str = str(value)
                print(f"[污点传播] {context}: 符号变量 {var_str} 包含污点标识符 {self.taint_buf}")
                for varname in self.global_var_symbols:
                    if varname in var_str:
                        print(f"[污点传播] {context}: 符号变量含有污点 {varname}")
                        return True, varname
            
            # 检查具体值
            if isinstance(value, (int, claripy.ast.BV)) and not state.solver.symbolic(value):
                concrete_val = state.solver.eval(value)
                if self.is_tainted(concrete_val):
                    varname = self.get_taint_label(concrete_val)
                    print(f"[污点传播] {context}: 值 {safe_hex(concrete_val)} 被 {varname} 污染")
                    return True, varname
            
            # 检查指针解引用
            if isinstance(value, claripy.ast.BV) and not state.solver.symbolic(value):
                try:
                    concrete_val = state.solver.eval(value)
                    if 0x10000 <= concrete_val <= 0x7FFFFFFF:
                        mem_content = state.memory.load(concrete_val, 4)
                        is_tainted, varname = self.check_taint(state, mem_content, f"{context} 指针解引用")
                        if is_tainted:
                            return True, varname
                except Exception:
                    pass
            
            return False, None
            
        except Exception as e:
            print(f"[ERROR] 检查污点时出错: {e}")
            return False, None
    
    def record_taint_path(self, path_type, pc, varname=None, address=None, target_name=None, target_addr=None, tainted_params=None):
        """记录污点传播路径"""
        path_entry = {
            "type": path_type,
            "pc": pc
        }
        
        if path_type == "SOURCE":
            path_entry.update({
                "varname": varname,
                "address": address
            })
        elif path_type == "FUNC_CALL":
            path_entry.update({
                "target_addr": target_addr,
                "target_name": target_name,
                "tainted_params": tainted_params
            })
        
        self.taint_propagation_paths.append(path_entry)
    
    def add_critical_variable(self, varname):
        """添加关键变量"""
        self.critical_variables.add(varname)
    
    def solve_constraints(self, state):
        """求解当前状态的约束"""
        current_solution = {}
        for varname, sym_var in self.global_var_symbols.items():
            try:
                if state.solver.satisfiable():
                    concrete_solution = state.solver.eval(sym_var, cast_to=bytes)
                    concrete_solution = concrete_solution.replace(b'\x00', b'')
                    concrete_solution_str = concrete_solution.decode('utf-8', 'ignore')
                    current_solution[varname] = concrete_solution_str
            except Exception as e:
                print(f"[错误] 求解变量 {varname} 时出错: {e}")
        
        if current_solution and not any(s == current_solution for s in self.global_constraint_solutions):
            self.global_constraint_solutions.append(current_solution)
            print(f"[路径约束] 已保存新的完整约束解决方案 #{len(self.global_constraint_solutions)}")
        
        return current_solution
    
    def get_all_tainted(self):
        """获取所有被污染的数据"""
        return list(self.tainted_data.keys())
    
    def print_results(self):
        """输出污点分析结果"""
        print("\n[INFO] 污点分析完成。")
        
        # 输出污点传播摘要
        print("\n----- 污点传播摘要 -----")
        for varname in self.global_var_symbols:
            print(f"变量 {varname} 被用作污点源")
        
        # 输出污点路径
        print("\n----- 污点传播路径 -----")
        for i, path in enumerate(self.taint_propagation_paths):
            if path["type"] == "SOURCE":
                print(f"{i}. [来源] PC:{safe_hex(path['pc'])} 变量: {path['varname']} 存储于: {safe_hex(path['address'])}")
            elif path["type"] == "FUNC_CALL":
                print(f"{i}. [函数调用] PC:{safe_hex(path['pc'])} 函数: {path['target_name']} ({safe_hex(path['target_addr'])}) 受污染参数: {path['tainted_params']}")
        
        print("\n----- 关键污点变量 -----")
        for varname in self.critical_variables:
            print(f"关键变量: {varname}")
        
        print("\n----- 全局约束解决方案 -----")
        for i, solution in enumerate(self.global_constraint_solutions):
            print(f"约束解决方案 #{i+1}:")
            for varname, value in solution.items():
                print(f"{varname}={value}")

# **Hook websGetVar**
class HookWebsGetVar(angr.SimProcedure):
    def run(self, name_addr):
        try:
            # 获取变量名
            varname = self.state.mem[name_addr].string.concrete.decode('utf-8', 'ignore')
            pc = self.state.solver.eval(self.state.regs.pc)
            
            # 使用CoreTaint管理污点
            core_taint = self.state.globals.get('core_taint')
            if core_taint is None:
                print("[ERROR] CoreTaint对象未初始化")
                return self.state.solver.BVV(0, self.arch.bits)
            
            # 应用污点并返回地址
            ret_addr = core_taint.apply_taint(self.state, varname, pc)
            if ret_addr is not None:
                return ret_addr
            else:
                # 变量已存在，返回已有地址
                return self.state.solver.BVV(0, self.arch.bits)
                
        except Exception as e:
            print(f"[ERROR] websGetVar hook error: {e}")
            return self.state.solver.BVV(0, self.arch.bits)

class SkipFunction(angr.SimProcedure):
    def run(self):
        return 0

def get_arity(p, b_addr):
    """获取函数调用的参数数量"""
    num=0
    b = p.factory.block(b_addr)
    for reg_off in ordered_argument_regs[p.arch.name]:
        put_stmts = [s for s in b.vex.statements if s.tag == 'Ist_Put' and s.offset == reg_off]
        if put_stmts:
            tmp_index=ordered_argument_regs[p.arch.name].index(reg_off)+1
            num=max(num,tmp_index)
    return num

# **添加内存读写钩子以进行更精确的污点跟踪**
class CallParamCheckHooks:
    @staticmethod
    def is_library_function(addr):
        """判断一个函数是否是库函数"""
        if not project.loader.main_object.contains_addr(addr):
            return True
        
        for sym in project.loader.symbols:
            if sym.rebased_addr == addr and sym.is_import:
                return True
        
        return False
    
    @staticmethod
    def is_dangerous_function(name):
        """检查函数是否是危险函数"""
        if name in summary_func.ALL_DANGEROUS_FUNCS:
            return True
        return False
    
    @staticmethod
    def hook_function_call(state):
        try:
            # 获取CoreTaint对象
            core_taint = state.globals.get('core_taint')
            if core_taint is None:
                return
            
            # 获取函数调用地址和目标
            pc = state.addr
            history = state.history.addr
            target_addr_expr = state.inspect.function_address
            
            if target_addr_expr is None:
                print(f"[函数调用] {safe_hex(pc)}: 无法获取目标函数地址")
                return
            
            # 获取具体的目标地址
            try:
                if state.solver.symbolic(target_addr_expr):
                    possible_addrs = state.solver.eval_upto(target_addr_expr, 2)
                    if len(possible_addrs) == 1:
                        target_addr = possible_addrs[0]
                    else:
                        print(f"[函数调用] {safe_hex(pc)}: 目标地址不唯一，有 {len(possible_addrs)} 个可能值")
                        return
                else:
                    target_addr = state.solver.eval_one(target_addr_expr)
            except:
                print(f"[函数调用] {safe_hex(pc)}: 无法解析目标地址")
                return
                
            # 获取目标函数名称
            target_name = f"func_{safe_hex(target_addr)}"
            try:
                for sym in project.loader.symbols:
                    if sym.rebased_addr == target_addr:
                        target_name = sym.name
                        break
            except Exception as e:
                print(f"[警告] 获取函数名称时出错: {e}")
               
            # 跳过排除的函数分析
            if target_name in remove_functions:
                print(f"[INFO] 跳过排除函数的调用分析: {target_name}")
                project.hook(target_addr, SkipFunction())
                return
             
            print(f"[进程 {os.getpid()}][函数调用] {safe_hex(pc)}: 即将调用 {target_name} ({safe_hex(target_addr)})")
            
            # 检查参数寄存器
            arch_name = project.arch.name
            if arch_name not in func_params_regs:
                print(f"[警告] 不支持的架构 {arch_name} 的参数寄存器检查")
                return
                
            reg_names = func_params_regs[arch_name]
            tainted_params = []
            call_reg_num = get_arity(project, history)
            
            # 检查每个参数寄存器
            for i, reg_name in enumerate(reg_names):
                if i >= call_reg_num:
                    break
                try:
                    reg_val = state.registers.load(reg_name)
                    is_tainted, varname = core_taint.check_taint(state, reg_val, 
                                                               f"{safe_hex(pc)}: 调用前参数寄存器 {reg_name}")
                    if is_tainted:
                        tainted_params.append((i, reg_name, varname))
                        print(f"[污点流] {safe_hex(pc)}: 调用 {target_name} 时参数 {i} (寄存器 {reg_name}) 含有污点 {varname}")
                except Exception as reg_error:
                    print(f"[DEBUG] 无法读取寄存器 {reg_name}: {reg_error}")
                    continue
                
            # 如果有污染的参数，记录此次调用
            if tainted_params:
                # 记录到污点传播路径
                core_taint.record_taint_path("FUNC_CALL", pc, target_name=target_name, 
                                           target_addr=target_addr, tainted_params=tainted_params)
                
                if not(CallParamCheckHooks.is_library_function(target_addr)) or CallParamCheckHooks.is_dangerous_function(target_name):
                    print(f"\n[路径约束求解]")
                    
                    for i, reg_name, varname in tainted_params:
                        core_taint.add_critical_variable(varname)
                    
                    # 求解约束
                    core_taint.solve_constraints(state)

        except Exception as e:
            print(f"[ERROR] 函数调用钩子出错: {e}")

def extract_info(json_file):
    """从JSON文件中提取程序路径、函数名和调用者名称"""
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # 提取程序路径
        program_path = data.get("program_path", "未找到程序路径")
        
        # 使用字典来跟踪已处理的调用者，避免重复
        processed_callers = {}
        
        # 提取函数及调用者信息
        functions_info = []
        for func in data.get("extract_functions", []):
            func_name = func.get("name", "未命名函数")
            func_addr = func.get("address", "无地址")
            
            # 提取调用者信息
            callers = []
            for caller in func.get("callers", []):
                caller_name = caller.get("name", "未命名调用者")
                caller_addr = caller.get("address", "无地址")
                
                # 使用地址作为唯一标识符来去重
                caller_key = f"{caller_name}_{caller_addr}"
                
                if caller_key not in processed_callers:
                    processed_callers[caller_key] = {
                        "name": caller_name,
                        "address": caller_addr
                    }
                    callers.append(processed_callers[caller_key])
            
            functions_info.append({
                "name": func_name,
                "address": func_addr,
                "callers": callers
            })
        
        # 提取需要排除的函数
        remove_functions = []
        for func in data.get("remove_functions", []):
            if isinstance(func, str):
                remove_functions.append(func)
            elif isinstance(func, dict):
                func_name = func.get("name", "")
                if func_name:
                    remove_functions.append(func_name)
            
        return {
            "program_path": program_path,
            "functions": functions_info,
            "remove_functions": remove_functions
        }
        
    except Exception as e:
        print(f"处理JSON文件时出错: {e}")
        return None

def save_results(output_dir, target_func, core_taint):
    """保存分析结果到指定目录"""
    # 创建以函数名命名的目录
    func_name = target_func.get("name", "unknown")
    func_addr = target_func.get("address")
    
    if isinstance(func_addr, int):
        func_dir_name = f"{func_name}"
    
    func_dir = os.path.join(output_dir, func_dir_name)
    
    # 如果没有约束解，则跳过保存
    if not core_taint.global_constraint_solutions:
        print(f"[警告] 函数 {func_name} 没有约束解，跳过保存")
        return
        
    # 创建主目录
    try:
        os.makedirs(func_dir, exist_ok=True)
        print(f"[INFO] 创建目录: {func_dir}")
        
        # 创建input和config子目录
        input_dir = os.path.join(func_dir, "input")
        config_dir = os.path.join(func_dir, "config")
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(config_dir, exist_ok=True)
        print(f"[INFO] 创建子目录: {input_dir} 和 {config_dir}")
    except Exception as e:
        print(f"[ERROR] 创建目录失败: {e}")
        return
    
    # 保存关键变量到taint.txt
    try:
        with open(os.path.join(config_dir, "taint.txt"), "w") as f:
            for var in core_taint.critical_variables:
                f.write(f"{var}\n")
        print(f"[INFO] 已保存关键变量到: {os.path.join(config_dir, 'taint.txt')}")
    except Exception as e:
        print(f"[ERROR] 保存关键变量失败: {e}")
    
    # 保存每个约束解为文本文件
    for i, solution in enumerate(core_taint.global_constraint_solutions):
        try:
            seed_file = os.path.join(input_dir, f"seed_{i}.bin")
            
            with open(seed_file, "w") as f:
                for varname, value in solution.items():
                    try:
                        f.write(f"{varname}={value}\n")
                    except Exception as conv_err:
                        print(f"[警告] 写入变量 {varname} 时出错: {conv_err}")
            
            print(f"[INFO] 已保存约束解 #{i+1} 到: {seed_file}")
        except Exception as e:
            print(f"[ERROR] 保存约束解 #{i+1} 失败: {e}")

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="污点分析工具")
    parser.add_argument("json_file", help="提取结果的JSON文件路径")
    parser.add_argument("-o", "--output-dir", default="output", help="输出目录，默认为'output'")
    parser.add_argument("-t", "--threads", type=int, default=1, help="线程数，默认为1")
    return parser.parse_args()

def analyze_target_function(args):
    """单个函数的分析逻辑，供进程池调用"""
    binary_path, target_func, output_dir, IO_funcs, remove_functions = args
    
    func_name = target_func.get("name")
    func_addr = target_func.get("address")
    
    print(f"\n[INFO] [进程 {os.getpid()}] 开始分析函数: {func_name} ({hex(func_addr)})")
    
    try:
        # 在每个进程中独立加载二进制文件
        project = angr.Project(binary_path, auto_load_libs=False, use_sim_procedures=True)
        
        # 创建CoreTaint对象
        core_taint = CoreTaint(project)
        
        # 设置钩子
        for hook_func_name, hook_func_addr in IO_funcs.items():
            project.hook(hook_func_addr, HookWebsGetVar())
            print(f"[INFO] [进程 {os.getpid()}] 为函数 {hook_func_name} 设置钩子, 地址: {hex(hook_func_addr)}")
        project.hook_symbol("nvram_safe_get", HookWebsGetVar())
        print(f"[INFO] [进程 {os.getpid()}] 设置跳过函数的Hook...")
        skipped_count = 0
        for sym in project.loader.symbols:
            if sym.name in remove_functions:
                try:
                    project.hook(sym.rebased_addr, SkipFunction())
                    print(f"[INFO] [进程 {os.getpid()}] 已Hook跳过函数: {sym.name} at {hex(sym.rebased_addr)}")
                    skipped_count += 1
                except Exception as e:
                    print(f"[WARNING] [进程 {os.getpid()}] Hook函数 {sym.name} 失败: {e}")
        # 创建调用状态
        state = project.factory.call_state(func_addr)
        
        # 将CoreTaint对象存储到状态中
        state.globals['core_taint'] = core_taint
        
        # 设置函数调用钩子
        state.inspect.b('call', when=angr.BP_BEFORE, action=CallParamCheckHooks.hook_function_call)
        
        simgr = project.factory.simgr(state)
        simgr.use_technique(angr.exploration_techniques.Timeout(30))
        step_count = 0
        max_steps = 50
        
        while simgr.active and step_count < max_steps:
            try:
                simgr.step()
                step_count += 1
                print(f"[进程 {os.getpid()} 函数:{func_name}] [STEP {step_count}] Active Paths: {len(simgr.active)}, Deadended: {len(simgr.deadended)}")      
            except Exception as e:
                print(f"[进程 {os.getpid()} 函数:{func_name}] [ERROR] 符号执行步骤出错: {e}")
                break
        
        # 收集所有状态
        tmp_active = simgr.active[:]
        if hasattr(simgr, 'timeout'):
            tmp_active.extend(simgr.timeout)
        if hasattr(simgr, 'deadended'):
            tmp_active.extend(simgr.deadended)
                    
        # 如果没有找到任何关键变量，但有符号变量，尝试从最后状态求解
        if not core_taint.critical_variables and core_taint.global_var_symbols and tmp_active:
            print(f"\n[进程 {os.getpid()} 函数:{func_name}] [INFO] 未找到关键变量，尝试从最终状态计算约束解...")
            
            # 从不同状态获取约束解
            if len(tmp_active) >= 3:
                sorted_states = sorted(tmp_active, key=lambda s: len(s.history.bbl_addrs))
                
                shortest_state = sorted_states[0]
                longest_state = sorted_states[-1]
                middle_idx = len(sorted_states) // 2
                middle_state = sorted_states[middle_idx]
                
                states_to_analyze = [
                    ("最短路径", shortest_state),
                    ("最长路径", longest_state),
                    ("中间路径", middle_state)
                ]
            else:
                states_to_analyze = [
                    (f"路径 {i}", state) for i, state in enumerate(tmp_active)
                ]
            
            # 从每个选定的状态中获取求解结果
            for path_desc, state in states_to_analyze:
                print(f"\n[进程 {os.getpid()} 函数:{func_name}] [INFO] 从{path_desc}计算约束解...")
                core_taint.solve_constraints(state)
        
        # 保存分析结果
        save_results(output_dir, target_func, core_taint)
        
        # 返回分析结果概要
        return {
            "func_name": func_name,
            "func_addr": func_addr,
            "critical_vars": list(core_taint.critical_variables),
            "solutions_count": len(core_taint.global_constraint_solutions),
            "taint_paths_count": len(core_taint.taint_propagation_paths)
        }
        
    except Exception as e:
        print(f"[进程 {os.getpid()}] [ERROR] 分析函数 {func_name} 时发生错误: {e}")
        return {
            "func_name": func_name,
            "func_addr": func_addr,
            "error": str(e)
        }

def main():
    """主函数，执行污点分析流程"""
    global project, remove_functions
    
    args = parse_args()
    json_file = args.json_file
    output_dir = args.output_dir
    threads_num = args.threads

    # 创建输出目录
    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"[INFO] 使用输出目录: {output_dir}")
    except Exception as e:
        print(f"[ERROR] 创建输出目录失败: {e}")
        return
    
    info = extract_info(json_file)
    if not info:
        print("[ERROR] 没有提取到有效信息，退出分析")
        return
    
    binary_path = info.get("program_path")
    if not binary_path or not os.path.exists(binary_path):
        print(f"[ERROR] 无效的程序路径: {binary_path}")
        return
    
    print("[INFO] 开始污点分析...")
    print(f"[INFO] 加载二进制文件: {binary_path}")
    project = angr.Project(binary_path, auto_load_libs=False, use_sim_procedures=True)
    
    remove_functions = info.get("remove_functions", [])   
    if remove_functions:
        print(f"[INFO] 将跳过以下函数的深入分析: {', '.join(remove_functions)}")
        
    IO_funcs = {}
    for function in info.get("functions", []):
        func_name = function.get("name", "")
        addr_str = function.get("address", "")
        
        if addr_str:
            if addr_str.startswith("0x"):
                func_addr = int(addr_str, 16)
            else:
                func_addr = int(addr_str)
                
            IO_funcs[func_name] = func_addr
            print(f"[INFO] 从JSON中获取 IO函数 {func_name} 地址: {hex(func_addr)}")
    
    target_funcs = []
    processed_target_funcs = {}
    for function in info.get("functions", []):
        # 遍历其所有调用者
        for caller in function.get("callers", []):
            caller_name = caller.get("name", "unknown")
            caller_addr_str = caller.get("address", "")
            
            if caller_name in remove_functions:
                print(f"[INFO] 跳过函数 {caller_name} 的深入分析")
                continue
            
            if caller_addr_str:
                if caller_addr_str.startswith("0x"):
                    caller_addr = int(caller_addr_str, 16)
                else:
                    caller_addr = int(caller_addr_str)
                
                caller_key = caller_addr
            
                # 如果函数尚未处理，则添加到目标函数列表
                if caller_key not in processed_target_funcs:
                    processed_target_funcs[caller_key] = {
                        "name": caller_name,
                        "address": caller_addr
                    }
    
    target_funcs = list(processed_target_funcs.values())
                    
    if not target_funcs:
        print("[ERROR] 未找到任何调用IO的函数，退出分析")
        return
        
    # 使用多进程进行函数分析
    print(f"[INFO] 使用 {threads_num} 个进程进行并行分析...")
    
    # 准备每个进程的参数
    process_args = []
    for func in target_funcs:
        process_args.append((binary_path, func, output_dir, IO_funcs, remove_functions))
    
    # 使用进程池执行分析任务
    try:
        with Pool(processes=threads_num, maxtasksperchild=1) as pool:
            results = pool.map(analyze_target_function, process_args)
            
        # 汇总并打印分析结果
        print("\n[INFO] 所有函数分析完成。汇总结果:")
        for result in results:
            if "error" in result:
                print(f"  - 函数 {result['func_name']} ({hex(result['func_addr'])}) 分析失败: {result['error']}")
            else:
                print(f"  - 函数 {result['func_name']} ({hex(result['func_addr'])}):")
                print(f"    关键变量: {', '.join(result['critical_vars']) if result['critical_vars'] else '无'}")
                print(f"    约束解数量: {result['solutions_count']}")
                print(f"    污点传播路径数量: {result['taint_paths_count']}")
                
    except Exception as e:
        print(f"[ERROR] 多进程执行过程中发生错误: {e}")

if __name__ == "__main__":
    main()