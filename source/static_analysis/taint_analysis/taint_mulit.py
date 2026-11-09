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
    "ARM": ["r0", "r1", "r2", "r3"],
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

# 创建污点追踪插件
class TaintTrackingPlugin(angr.SimStatePlugin):
    def __init__(self):
        super().__init__()
        self.tainted_data = {}  # 用于存储被污染的寄存器和内存地址
        self.taint_history = []  # 用于记录污点传播历史
    
    @property
    def _copy_ignores(self):
        return ["taint_history"]
    
    def copy(self, memo):
        copied = TaintTrackingPlugin()
        copied.tainted_data = dict(self.tainted_data)
        copied.taint_history = list(self.taint_history)
        return copied
    
    def merge(self, others, merge_conditions, common_ancestor=None):
        return False
    
    def widen(self, others):
        return False
    
    def taint(self, key, taint_label, location=None):
        self.tainted_data[key] = taint_label
        if location:
            self.taint_history.append({"pc": location, "key": key, "label": taint_label})
        
    def is_tainted(self, key):
        return key in self.tainted_data
    
    def get_taint_label(self, key):
        return self.tainted_data.get(key, None)
    
    def get_all_tainted(self):
        return list(self.tainted_data.keys())

# 注册污点插件
angr.SimState.register_default('taint', TaintTrackingPlugin)

# **Hook websGetVar**
class HookWebsGetVar(angr.SimProcedure):
    def run(self, a1, name_addr, default_addr):
        global memory_offset_counter
        try:
            # 获取变量名
            varname = self.state.mem[name_addr].string.concrete.decode('utf-8', 'ignore')
            pc = self.state.solver.eval(self.state.regs.pc)
            
            # 为每个新变量创建符号变量
            if varname not in global_var_symbols:
                sym_var = claripy.BVS(varname, 32 * 8)  # 32 字节符号变量
                global_var_symbols[varname] = sym_var
                print(f"[HOOK] {hex(pc)}: Intercepted websGetVar key: {varname}")
                
                # 为每个变量分配唯一的内存区域
                # 使用固定基址 + 偏移量的方式分配内存
                base_addr = 0x10000000  # 使用一个远离栈和堆的基址
                tmp_addr = base_addr + (memory_offset_counter * 0x1000)  # 每个变量间隔4KB
                memory_offset_counter += 1
            
                # 在内存中存储符号变量
                self.state.memory.store(tmp_addr, sym_var)
                self.state.memory.store(tmp_addr + 31, claripy.BVV(0, 8))  # Null 终止
            
                # 标记返回值为污点数据
                ret_value = tmp_addr  # 返回的是指针地址
            
                # 使用污点插件记录污点信息
                self.state.taint.taint(ret_value, varname, self.state.addr)
            
                # 记录对应的内存区域也被污染
                for i in range(32):
                    tainted_addresses.add(tmp_addr + i)
                    self.state.taint.taint(tmp_addr + i, varname, self.state.addr)
            
                taint_path_entry = {
                    "type": "SOURCE",
                    "pc": pc, 
                    "varname": varname,
                    "address": tmp_addr
                }
                taint_propagation_paths.append(taint_path_entry)
            
                print(f"[污点生成] 变量 {varname} 被存储在地址 {safe_hex(tmp_addr)}，返回值为 {safe_hex(ret_value)}")
                return ret_value
            else:
                print(f"[HOOK] {hex(pc)}: websGetVar key {varname} already exists")
                
                
        except Exception as e:
            print(f"[ERROR] websGetVar hook error: {e}")
            return self.state.solver.BVV(0, self.arch.bits)

class HookwebsGetVarWithValidate(angr.SimProcedure):
    def run(self,wp,cgi_name,val_item):
        global memory_offset_counter
        try:
            varname = self.state.mem[cgi_name].string.concrete.decode('utf-8', 'ignore')
            pc = self.state.solver.eval(self.state.regs.pc)
            
            # 为每个新变量创建符号变量
            if varname not in global_var_symbols:
                sym_var = claripy.BVS(varname, 32 * 8)  # 32 字节符号变量
                global_var_symbols[varname] = sym_var
                print(f"[HOOK] {hex(pc)}: Intercepted websGetVarWithValidate key: {varname}")
                
                # 为每个变量分配唯一的内存区域
                # 使用固定基址 + 偏移量的方式分配内存
                base_addr = 0x10000000  # 使用一个远离栈和堆的基址
                tmp_addr = base_addr + (memory_offset_counter * 0x1000)  # 每个变量间隔4KB
                memory_offset_counter += 1
            
                # 在内存中存储符号变量
                self.state.memory.store(tmp_addr, sym_var)
                self.state.memory.store(tmp_addr + 31, claripy.BVV(0, 8))  # Null 终止
            
                # 标记返回值为污点数据
                ret_value = tmp_addr  # 返回的是指针地址
            
                # 使用污点插件记录污点信息
                self.state.taint.taint(ret_value, varname, self.state.addr)
            
                # 记录对应的内存区域也被污染
                for i in range(32):
                    tainted_addresses.add(tmp_addr + i)
                    self.state.taint.taint(tmp_addr + i, varname, self.state.addr)
            
                taint_path_entry = {
                    "type": "SOURCE",
                    "pc": pc, 
                    "varname": varname,
                    "address": tmp_addr
                }
                taint_propagation_paths.append(taint_path_entry)
            
                print(f"[污点生成] 变量 {varname} 被存储在地址 {safe_hex(tmp_addr)}，返回值为 {safe_hex(ret_value)}")
                return ret_value
            else:
                print(f"[HOOK] {hex(pc)}: websGetVar key {varname} already exists")
                
        except Exception as e:
            print(f"[ERROR] websGetVar hook error: {e}")
            return self.state.solver.BVV(0, self.arch.bits)
              
class SkipFunction(angr.SimProcedure):
    def run(self):
        return 0  # 可以根据需要返回特定值
# **检查值是否被污染**
def check_taint(state, value, context=""):
    try:
        # 检查具体值
        if isinstance(value, (int, claripy.ast.BV)) and not state.solver.symbolic(value):
            concrete_val = state.solver.eval(value)
            if state.taint.is_tainted(concrete_val):
                varname = state.taint.get_taint_label(concrete_val)
                print(f"[污点传播] {context}: 值 {safe_hex(concrete_val)} 被 {varname} 污染")
                return True, varname
        
        # 如果是指针，检查它指向的内存是否被污染
        if isinstance(value, claripy.ast.BV) and not state.solver.symbolic(value):
            try:
                concrete_val = state.solver.eval(value)
                if 0x10000 <= concrete_val <= 0x7FFFFFFF:  # 可能的有效地址范围
                    # 尝试读取此地址的内容
                    mem_content = state.memory.load(concrete_val, 4)
                    #print(f"[DEBUG] 读取地址 {safe_hex(concrete_val)} 的内容: {mem_content}")
                    is_tainted, varname = check_taint(state, mem_content, f"{context} 指针解引用")
                    if is_tainted:
                        return True, varname
            except Exception as e:
                # 指针解引用错误可以忽略
                pass
        return False, None
    except Exception as e:
        print(f"[ERROR] 检查污点时出错: {e}")
        return False, None

def get_arity(p, b_addr):
    """
    Retrieves the arity by inspecting a funciton call

    :param p: angr project
    :param b_addr: basic block address
    :return: arity of the function
    """
    set_params = []
    b = p.factory.block(b_addr)
    for reg_off in ordered_argument_regs[p.arch.name]:
        put_stmts = [s for s in b.vex.statements if s.tag == 'Ist_Put' and s.offset == reg_off]
        if not put_stmts:
            break
        put_stmt = put_stmts[-1]
        set_params.append(put_stmt)
    return len(set_params)
# **添加内存读写钩子以进行更精确的污点跟踪**
class MemoryReadWriteHooks:
    @staticmethod
    def hook_memory_read(state):
        try:
            # 获取读取的地址和大小
            addr = state.inspect.mem_read_address
            size = state.inspect.mem_read_length
            value=state.inspect.mem_read_expr
            # 检查这个地址是否被污染
            concrete_addr = state.solver.eval(addr)
            is_tainted = False
            varname = None
            #is_tainted, varname = check_taint(state, value, f"{safe_hex(state.addr)}: 内存读取")
            for i in range(state.solver.eval(size)):
                curr_addr = concrete_addr + i
                if curr_addr in tainted_addresses:
                    is_tainted = True
                    varname = state.taint.get_taint_label(curr_addr)
                    if varname:
                        break
            if is_tainted and varname:
                pc = state.addr
                print(f"[内存读取] {safe_hex(pc)}: 从地址 {safe_hex(concrete_addr)} 读取的数据被 {varname} 污染")
                tmp,tmpname=check_taint(state, value, f"{safe_hex(state.addr)}: 内存读取")
                # 当内存被读取时，记录读取的目标（可能是寄存器）也被污染
                expr = state.inspect.mem_read_expr
                taint_propagation_paths.append({
                    "type": "MEM_READ",
                    "pc": pc,
                    "src_addr": concrete_addr,
                    "varname": varname
                })
                
                # 如果读取的内容被存入寄存器，标记该寄存器为污染
                if hasattr(state.inspect, "mem_read_dest") and state.inspect.mem_read_dest is not None:
                    dest = state.inspect.mem_read_dest
                    if isinstance(dest, str) and dest.startswith("reg_"):
                        reg_name = dest[4:]  # 去掉 "reg_" 前缀
                        state.taint.taint(reg_name, varname, pc)
                        print(f"[污点传播] {safe_hex(pc)}: 寄存器 {reg_name} 被 {varname} 污染")
        except Exception as e:
            print(f"[ERROR] 内存读取钩子出错: {e}")
    
    @staticmethod
    def hook_memory_write(state):
        try:
            # 检查写入的数据是否被污染
            data = state.inspect.mem_write_expr
            addr = state.inspect.mem_write_address
            concrete_addr = state.solver.eval(addr)
            pc = state.addr
            
            # 检查写入的数据是否被污染
            is_tainted, varname = check_taint(state, data, f"{safe_hex(pc)}: 内存写入")
            
            if is_tainted:
                print(f"[内存写入] {safe_hex(pc)}: 往地址 {safe_hex(concrete_addr)} 写入的数据被 {varname} 污染")
                
                # 标记该内存地址为污染
                tainted_addresses.add(concrete_addr)
                state.taint.taint(concrete_addr, varname, pc)
                
                taint_propagation_paths.append({
                    "type": "MEM_WRITE",
                    "pc": pc,
                    "dst_addr": concrete_addr,
                    "varname": varname
                })
        except Exception as e:
            print(f"[ERROR] 内存写入钩子出错: {e}")
class CallParamCheckHooks:
    @staticmethod
    def is_library_function(addr):
        """判断一个函数是否是库函数"""
        # 检查是否在主程序中
        if not project.loader.main_object.contains_addr(addr):
            return True
        
        # 检查是否有符号且是导入的
        for sym in project.loader.symbols:
            if sym.rebased_addr == addr and sym.is_import:
                return True
        
        return False
    @staticmethod
    def is_dangerous_function(name):
        """检查函数是否是危险函数"""
        # 检查函数名是否在危险函数列表中
        if name in summary_func.ALL_DANGEROUS_FUNCS:
            return True
        return False
    @staticmethod
    def hook_function_call(state):
        try:
            # 获取函数调用地址和目标
            pc = state.addr
            history=state.history.addr
            target_addr_expr = state.inspect.function_address
            
            # 如果目标地址是符号的，尝试具体化它
            if target_addr_expr is None:
                print(f"[函数调用] {safe_hex(pc)}: 无法获取目标函数地址")
                return
            
            # 安全地尝试获取具体的目标地址
            try:
                if state.solver.symbolic(target_addr_expr):
                    # 尝试获取可能的具体值
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
                
            # 获取目标函数名称 - 安全处理
            target_name = f"func_{safe_hex(target_addr)}"  # 默认名称
            try:
                for sym in project.loader.symbols:
                    if sym.rebased_addr == target_addr:
                        target_name = sym.name
                        break
            except Exception as e:
                print(f"[警告] 获取函数名称时出错: {e}")
               
            #跳过排除的函数分析
            if target_name in remove_functions:
                print(f"[INFO] 跳过排除函数的调用分析: {target_name}")
                project.hook(target_addr, SkipFunction())
                return
             
            print(f"[函数调用] {safe_hex(pc)}: 即将调用 {target_name} ({safe_hex(target_addr)})")
            # 检查参数寄存器
            arch_name = project.arch.name
            if arch_name not in func_params_regs:
                print(f"[警告] 不支持的架构 {arch_name} 的参数寄存器检查")
                return
                
            reg_names = func_params_regs[arch_name]
            tainted_params = []
            call_reg_num=get_arity(project, history)
            # 检查每个参数寄存器
            for i, reg_name in enumerate(reg_names):
                if i >= call_reg_num:
                    break
                try:
                    # 直接尝试读取寄存器，如果不存在会抛出异常
                    reg_val = state.registers.load(reg_name)
                    is_tainted, varname = check_taint(state, reg_val, 
                                                     f"{safe_hex(pc)}: 调用前参数寄存器 {reg_name}")
                    if is_tainted:
                        tainted_params.append((i, reg_name, varname))
                        print(f"[污点流] {safe_hex(pc)}: 调用 {target_name} 时参数 {i} (寄存器 {reg_name}) 含有污点 {varname}")
                except Exception as reg_error:
                    # 如果寄存器不存在，会捕获到异常
                    print(f"[DEBUG] 无法读取寄存器 {reg_name}: {reg_error}")
                    continue
                
            # 如果有污染的参数，记录此次调用
            if tainted_params:
                # 记录到污点传播路径
                taint_propagation_paths.append({
                    "type": "FUNC_CALL",
                    "pc": pc,
                    "target_addr": target_addr,
                    "target_name": target_name,
                    "tainted_params": [(idx, reg, var) for idx, reg, var in tainted_params]
                })
                if not(CallParamCheckHooks.is_library_function(target_addr)) or CallParamCheckHooks.is_dangerous_function(target_name):
                    print(f"\n[路径约束求解]")
                    current_solution = {}
                    for i,reg_name, varname in tainted_params:
                        critical_variables.add(varname)
                    # 对所有符号变量进行约束求解，重点关注关键变量
                    for varname, sym_var in global_var_symbols.items():
                        try:
                            if state.solver.satisfiable():
                                concrete_solution = state.solver.eval(sym_var, cast_to=bytes)
                                concrete_solution = concrete_solution.replace(b'\x00', b'')
                                concrete_solution_str = concrete_solution.decode('utf-8', 'ignore')
                                current_solution[varname] = concrete_solution_str
                        except Exception as e:
                            print(f"[错误] 求解变量 {varname} 时出错: {e}")
                    if current_solution and not any(s == current_solution for s in global_constraint_solutions):
                        global_constraint_solutions.append(current_solution)
                        print(f"[路径约束] 已保存新的完整约束解决方案 #{len(global_constraint_solutions)}")                        
            else:
                #print(f"[DEBUG] {safe_hex(pc)} func{target_name}: 未检测到污点参数")
                return
                

        except Exception as e:
            print(f"[ERROR] 函数调用钩子出错: {e}")

def extract_info(json_file):
    """
    从JSON文件中提取程序路径、函数名和调用者名称，并去除重复调用者
    
    Args:
        json_file: JSON文件路径
    
    Returns:
        提取的信息字典
    """
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
                remove_functions.append(func)  # 简单的函数名
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
    
def print_results():
    """输出污点分析结果"""
    print("\n[INFO] 污点分析完成。")
    
    # 输出污点传播摘要
    print("\n----- 污点传播摘要 -----")
    for varname in global_var_symbols:
        print(f"变量 {varname} 被用作污点源")
    
    # 输出污点路径
    print("\n----- 污点传播路径 -----")
    for i, path in enumerate(taint_propagation_paths):
        if path["type"] == "SOURCE":
            print(f"{i}. [来源] PC:{safe_hex(path['pc'])} 变量: {path['varname']} 存储于: {safe_hex(path['address'])}")
        elif path["type"] == "FUNC_CALL":
            print(f"{i}. [函数调用] PC:{safe_hex(path['pc'])} 函数: {path['target_name']} ({safe_hex(path['target_addr'])}) 受污染参数: {[(idx, reg, var) for idx, reg, var in path['tainted_params']]}")
    
    print("\n----- 关键污点变量 -----")
    for varname in critical_variables:
        print(f"关键变量: {varname}")
    
    print("\n----- 全局约束解决方案 -----")
    for i, solution in enumerate(global_constraint_solutions):
        print(f"约束解决方案 #{i+1}:")
        for varname, value in solution.items():
            print(f"{varname}={value}")

def save_results(output_dir, target_func, critical_vars, constraint_solutions):
    """保存分析结果到指定目录"""
    # 创建以函数名命名的目录
    func_name = target_func.get("name", "unknown")
    func_addr = target_func.get("address")
    
    if isinstance(func_addr, int):
        func_dir_name = f"{func_name}"
    
    func_dir = os.path.join(output_dir, func_dir_name)
    
    # 如果没有约束解，则跳过保存
    if not constraint_solutions:
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
            for var in critical_vars:
                f.write(f"{var}\n")
        print(f"[INFO] 已保存关键变量到: {os.path.join(config_dir, 'taint.txt')}")
    except Exception as e:
        print(f"[ERROR] 保存关键变量失败: {e}")
    
    # 保存每个约束解为文本文件
    for i, solution in enumerate(constraint_solutions):
        try:
            seed_file = os.path.join(input_dir, f"seed_{i}.bin")
            
            # 使用文本格式，每行一个变量=值
            with open(seed_file, "w") as f:  # 注意这里改为"w"，表示文本模式
                for varname, value in solution.items():
                    try:
                        # 写入变量=值格式
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
    parser.add_argument("-t","--threads", type=int, default=1, help="线程数，默认为1")
    return parser.parse_args()

def analyze_target_function(args):
    """单个函数的分析逻辑，供进程池调用
    
    Args:
        args: 包含分析所需参数的元组 (binary_path, target_func, output_dir, IO_funcs, remove_functions)
    
    Returns:
        分析结果信息
    """
    binary_path, target_func, output_dir, IO_funcs, remove_functions = args
    
    # 为该进程初始化全局变量
    global project, global_var_symbols, critical_variables, tainted_addresses
    global taint_propagation_paths, global_constraint_solutions, memory_offset_counter
    
    global_var_symbols = {}
    critical_variables = set()
    tainted_addresses = set()
    taint_propagation_paths = []
    global_constraint_solutions = []
    memory_offset_counter = 0
    
    func_name = target_func.get("name")
    func_addr = target_func.get("address")
    
    print(f"\n[INFO] [进程 {os.getpid()}] 开始分析函数: {func_name} ({hex(func_addr)})")
    
    try:
        # 在每个进程中独立加载二进制文件
        project = angr.Project(binary_path, arch='mipsel', auto_load_libs=False, use_sim_procedures=True)
        # 设置钩子
        for hook_func_name, hook_func_addr in IO_funcs.items():
            if hook_func_name == "websGetVar":
                project.hook(hook_func_addr, HookWebsGetVar())
                print(f"[INFO] 为函数 {hook_func_name} 设置钩子, 地址: {hex(hook_func_addr)}")
            elif hook_func_name == "websGetVarWithValidate":
                project.hook(hook_func_addr, HookwebsGetVarWithValidate())
                print(f"[INFO] 为函数 {hook_func_name} 设置钩子, 地址: {hex(hook_func_addr)}")
        
        state = project.factory.call_state(func_addr)
        state.inspect.b('call', when=angr.BP_BEFORE, action=CallParamCheckHooks.hook_function_call)
        simgr = project.factory.simgr(state)
        simgr.use_technique(angr.exploration_techniques.Timeout(30))
        step_count = 0
        max_steps = 50  # 增加步数上限以获得更完整的覆盖
        
        while simgr.active and step_count < max_steps:
            try:
                simgr.step()
                step_count += 1
                print(f"[进程 {os.getpid()} 函数:{func_name}] [STEP {step_count}] Active Paths: {len(simgr.active)}, Deadended: {len(simgr.deadended)}")      
            except Exception as e:
                print(f"[进程 {os.getpid()} 函数:{func_name}] [ERROR] 符号执行步骤出错: {e}")
                break
        tmp_active=simgr.active[:]
        if hasattr(simgr, 'timeout'):
        # 将所有超时状态添加到列表中
            tmp_active.extend(simgr.timeout)
        if hasattr(simgr, 'deadended'):
            tmp_active.extend(simgr.deadended)
                    
        # 如果没有找到任何关键变量，但有符号变量，尝试从最后状态求解
        if not critical_variables and global_var_symbols and tmp_active:
            print(f"\n[进程 {os.getpid()} 函数:{func_name}] [INFO] 未找到关键变量，尝试从最终状态计算约束解...")
            
            # 确保有足够多的活动路径可供选择
            if len(tmp_active) >= 3:
                # 1. 按路径长度排序
                sorted_states = sorted(tmp_active, key=lambda s: len(s.history.bbl_addrs))
                
                # 2. 选择三种不同的状态：最短、最长和中间
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
                # 如果路径数量不足3个，使用所有可用路径
                states_to_analyze = [
                    (f"路径 {i}", state) for i, state in enumerate(tmp_active)
                ]
            
            # 3. 从每个选定的状态中获取求解结果
            for path_desc, state in states_to_analyze:
                print(f"\n[进程 {os.getpid()} 函数:{func_name}] [INFO] 从{path_desc}计算约束解...")
                current_solution = {}
                
                # 对所有符号变量进行约束求解
                for varname, sym_var in global_var_symbols.items():
                    try:
                        if state.solver.satisfiable():
                            concrete_solution = state.solver.eval(sym_var, cast_to=bytes)
                            concrete_solution = concrete_solution.replace(b'\x00', b'')
                            concrete_solution_str = concrete_solution.decode('utf-8', 'ignore')
                            current_solution[varname] = concrete_solution_str
                            print(f"[进程 {os.getpid()} 函数:{func_name}] [约束解] [{path_desc}] 变量 {varname} = '{concrete_solution_str}'")
                    except Exception as e:
                        print(f"[进程 {os.getpid()} 函数:{func_name}] [错误] 求解变量 {varname} 时出错: {e}")
                        
                if current_solution and not any(s == current_solution for s in global_constraint_solutions):
                    global_constraint_solutions.append(current_solution)
                    print(f"[进程 {os.getpid()}] 函数:{func_name} [路径约束] 已保存新的完整约束解决方案 #{len(global_constraint_solutions)}")
        
        # 保存每个进程的分析结果
        save_results(output_dir, target_func, critical_variables, global_constraint_solutions)
        
        # 返回分析结果概要
        return {
            "func_name": func_name,
            "func_addr": func_addr,
            "critical_vars": list(critical_variables),
            "solutions_count": len(global_constraint_solutions),
            "taint_paths_count": len(taint_propagation_paths)
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
    global project, IO_funcs, remove_functions
    args= parse_args()
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
    
    info=extract_info(json_file)
    if not info:
        print("[ERROR] 没有提取到有效信息，退出分析")
        return
    binary_path = info.get("program_path")
    if not binary_path or not os.path.exists(binary_path):
        print(f"[ERROR] 无效的程序路径: {binary_path}")
        return
    
    print("[INFO] 开始污点分析...")
    print(f"[INFO] 加载二进制文件: {binary_path}")
    project = angr.Project(binary_path, arch='mipsel', auto_load_libs=False, use_sim_procedures=True)
    
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
    
    target_funcs=[]
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
        # 每个函数的分析参数
        process_args.append((binary_path, func, output_dir, IO_funcs, remove_functions))
    
    # 使用进程池执行分析任务
    try:
        with Pool(processes=threads_num,maxtasksperchild=1) as pool:
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
    # 全局变量初始化
    global_var_symbols = {}
    critical_variables = set()
    tainted_addresses = set()
    taint_propagation_paths = []
    global_constraint_solutions = []
    memory_offset_counter = 0
    
    # 执行主函数
    main()