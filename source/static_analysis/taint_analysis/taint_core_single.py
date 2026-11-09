import angr
import claripy
import logging
import archinfo
import summary_func
import json
import sys
import os
import argparse

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
        self.var_address_map = {}  # 变量名到地址的映射
        
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
            
            # 存储地址映射
            self.var_address_map[varname] = tmp_addr
            
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
            
            print(f"[污点生成] 变量 {varname} 被存储在地址 {safe_hex(tmp_addr)}，污点符号: {str(sym_var)}")
            return tmp_addr
        else:
            # 变量已存在，返回已有地址
            existing_addr = self.var_address_map.get(varname)
            if existing_addr is not None:
                print(f"[污点复用] 变量 {varname} 已存在，返回地址 {safe_hex(existing_addr)}")
                # 记录重复使用
                self.record_taint_path("REUSE", pc, varname, existing_addr)
                return existing_addr
            else:
                # 如果没有地址映射，重新计算（向后兼容）
                base_addr = 0x10000000
                var_index = list(self.global_var_symbols.keys()).index(varname)
                existing_addr = base_addr + (var_index * 0x1000)
                self.var_address_map[varname] = existing_addr
                print(f"[污点复用] 变量 {varname} 地址重新计算为 {safe_hex(existing_addr)}")
                return existing_addr
    
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
    
    def check_taint(self, state, value, context="", max_depth=3, current_depth=0):
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
            
            # # 检查具体值
            # if isinstance(value, (int, claripy.ast.BV)) and not state.solver.symbolic(value):
            #     concrete_val = state.solver.eval(value)
            #     if self.is_tainted(concrete_val):
            #         varname = self.get_taint_label(concrete_val)
            #         print(f"[污点传播] {context}: 值 {safe_hex(concrete_val)} 被 {varname} 污染")
            #         return True, varname
            
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
            "pc": pc,
            "timestamp": len(self.taint_propagation_paths)
        }
        
        if path_type == "SOURCE":
            path_entry.update({
                "varname": varname,
                "address": address
            })
        elif path_type == "REUSE":
            path_entry.update({
                "varname": varname,
                "address": address,
                "note": "变量重复使用"
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
        print(f"[关键变量] 添加关键变量: {varname}")
    
    def solve_constraints(self, state):
        """求解当前状态的约束"""
        print(f"[约束求解] 开始求解约束，已有变量: {list(self.global_var_symbols.keys())}")
        current_solution = {}
        for varname, sym_var in self.global_var_symbols.items():
            try:
                if state.solver.satisfiable():
                    concrete_solution = state.solver.eval(sym_var, cast_to=bytes)
                    concrete_solution = concrete_solution.replace(b'\x00', b'')
                    concrete_solution_str = concrete_solution.decode('utf-8', 'ignore')
                    current_solution[varname] = concrete_solution_str
                    print(f"[约束求解] 变量 {varname} 解为: {concrete_solution_str}")
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
            elif path["type"] == "REUSE":
                print(f"{i}. [重用] PC:{safe_hex(path['pc'])} 变量: {path['varname']} 地址: {safe_hex(path['address'])}")
            elif path["type"] == "FUNC_CALL":
                print(f"{i}. [函数调用] PC:{safe_hex(path['pc'])} 函数: {path['target_name']} ({safe_hex(path['target_addr'])}) 受污染参数: {path['tainted_params']}")
        
        print("\n----- 关键污点变量 -----")
        for varname in self.critical_variables:
            print(f"关键变量: {varname}")
        
        print("\n----- 全局约束解决方案 -----")
        for i, solution in enumerate(self.global_constraint_solutions):
            print(f"约束解决方案 #{i+1}:")
            for varname, value in solution.items():
                print(f"  {varname}={value}")

# **Hook websGetVar**
class Hook_one_param_GetVar(angr.SimProcedure):
    def run(self, name_addr):
        try:
            # 获取变量名
            varname = self.state.mem[name_addr].string.concrete.decode('utf-8', 'ignore')
            pc = self.state.solver.eval(self.state.regs.pc)
            
            print(f"[HOOK] getvar_one_param class 被调用，参数: '{varname}' at PC: {safe_hex(pc)}")
            
            # 使用CoreTaint管理污点
            core_taint = self.state.globals.get('core_taint')
            if core_taint is None:
                print("[ERROR] CoreTaint对象未初始化")
                return self.state.solver.BVV(0, self.arch.bits)
            
            # 应用污点并返回地址
            ret_addr = core_taint.apply_taint(self.state, varname, pc)
            
            if ret_addr is not None:
                print(f"[HOOK] getvar_one_param('{varname}') 返回地址: {safe_hex(ret_addr)}")
                return self.state.solver.BVV(ret_addr, self.arch.bits)
            else:
                print(f"[ERROR] 无法为变量 {varname} 获取地址")
                return self.state.solver.BVV(0, self.arch.bits)
                
        except Exception as e:
            print(f"[ERROR] getvar_one_param hook error: {e}")
            return self.state.solver.BVV(0, self.arch.bits)

class Hook_two_param_GetVar(angr.SimProcedure):
    def run(self,wp,name_addr):
        try:
            # 获取变量名
            varname = self.state.mem[name_addr].string.concrete.decode('utf-8', 'ignore')
            pc = self.state.solver.eval(self.state.regs.pc)
            
            print(f"[HOOK] getvar_two_param class 被调用，参数: '{varname}' at PC: {safe_hex(pc)}")
            
            # 使用CoreTaint管理污点
            core_taint = self.state.globals.get('core_taint')
            if core_taint is None:
                print("[ERROR] CoreTaint对象未初始化")
                return self.state.solver.BVV(0, self.arch.bits)
            
            # 应用污点并返回地址
            ret_addr = core_taint.apply_taint(self.state, varname, pc)
            
            if ret_addr is not None:
                print(f"[HOOK] getvar_two_param('{varname}') 返回地址: {safe_hex(ret_addr)}")
                return self.state.solver.BVV(ret_addr, self.arch.bits)
            else:
                print(f"[ERROR] 无法为变量 {varname} 获取地址")
                return self.state.solver.BVV(0, self.arch.bits)
                
        except Exception as e:
            print(f"[ERROR] getvar_two_param hook error: {e}")
            return self.state.solver.BVV(0, self.arch.bits)

class Hook_three_param_GetVar(angr.SimProcedure):
    def run(self,wp,name_addr,default_value):
        try:
            # 获取变量名
            varname = self.state.mem[name_addr].string.concrete.decode('utf-8', 'ignore')
            pc = self.state.solver.eval(self.state.regs.pc)
            
            print(f"[HOOK] getvar_three_param class 被调用，参数: '{varname}' at PC: {safe_hex(pc)}")
            
            # 使用CoreTaint管理污点
            core_taint = self.state.globals.get('core_taint')
            if core_taint is None:
                print("[ERROR] CoreTaint对象未初始化")
                return self.state.solver.BVV(0, self.arch.bits)
            
            # 应用污点并返回地址
            ret_addr = core_taint.apply_taint(self.state, varname, pc)
            
            if ret_addr is not None:
                print(f"[HOOK] getvar_three_param('{varname}') 返回地址: {safe_hex(ret_addr)}")
                return self.state.solver.BVV(ret_addr, self.arch.bits)
            else:
                print(f"[ERROR] 无法为变量 {varname} 获取地址")
                return self.state.solver.BVV(0, self.arch.bits)
                
        except Exception as e:
            print(f"[ERROR] getvar_three_param hook error: {e}")
            return self.state.solver.BVV(0, self.arch.bits)

class Hook_four_param_GetVar(angr.SimProcedure):
    def run(self,wp,name_addr,default_value,len):
        try:
            # 获取变量名
            varname = self.state.mem[name_addr].string.concrete.decode('utf-8', 'ignore')
            pc = self.state.solver.eval(self.state.regs.pc)
            
            print(f"[HOOK] getvar_four_param class 被调用，参数: '{varname}' at PC: {safe_hex(pc)}")
            
            # 使用CoreTaint管理污点
            core_taint = self.state.globals.get('core_taint')
            if core_taint is None:
                print("[ERROR] CoreTaint对象未初始化")
                return self.state.solver.BVV(0, self.arch.bits)
            
            # 应用污点并返回地址
            ret_addr = core_taint.apply_taint(self.state, varname, pc)
            
            if ret_addr is not None:
                print(f"[HOOK] getvar_four_param('{varname}') 返回地址: {safe_hex(ret_addr)}")
                return self.state.solver.BVV(ret_addr, self.arch.bits)
            else:
                print(f"[ERROR] 无法为变量 {varname} 获取地址")
                return self.state.solver.BVV(0, self.arch.bits)
                
        except Exception as e:
            print(f"[ERROR] getvar_four_param hook error: {e}")
            return self.state.solver.BVV(0, self.arch.bits)
# 参数数量到Hook类的映射
PARAM_COUNT_TO_HOOK = {
    1: Hook_one_param_GetVar,
    2: Hook_two_param_GetVar,
    3: Hook_three_param_GetVar,
    4: Hook_four_param_GetVar,
}            
def get_hook_class_by_param_count(param_count):
    """根据参数数量获取对应的Hook类"""
    if param_count in PARAM_COUNT_TO_HOOK:
        return PARAM_COUNT_TO_HOOK[param_count]
    else:
        print(f"[WARNING] 不支持参数数量为 {param_count} 的Hook，使用默认Hook (1个参数)")
        return Hook_one_param_GetVar
        
class EnhancedSkipFunction(angr.SimProcedure):
    """增强的跳过函数，提供更多调试信息"""
    
    def run(self, *args, **kwargs):
        # 获取函数名（如果可能）
        try:
            project = self.state.globals.get('project')
            func_name = "unknown"
            if project:
                for sym in project.loader.symbols:
                    if sym.rebased_addr == self.state.addr:
                        func_name = sym.name
                        break
            
            print(f"[跳过函数] {func_name} at {safe_hex(self.state.addr)} - 参数: {[safe_hex(arg) if hasattr(arg, 'args') else arg for arg in args]}")
        except:
            print(f"[跳过函数] 地址: {safe_hex(self.state.addr)}")
        
        # 返回0（表示函数执行成功但无特殊返回值）
        return 0

class SmartBlockingHandler(angr.SimProcedure):
    """智能处理阻塞函数的Hook"""
    
    def run(self, *args, **kwargs):
        # 获取函数名
        try:
            project = self.state.globals.get('project')
            func_name = "unknown"
            if project:
                for sym in project.loader.symbols:
                    if sym.rebased_addr == self.state.addr:
                        func_name = sym.name
                        break
            
            print(f"[阻塞函数] 处理 {func_name} at {safe_hex(self.state.addr)}")
            
            # 根据函数类型返回不同的模拟结果
            if func_name in ['fgets', 'gets']:
                # 对于字符串读取函数，返回一个空字符串指针
                return 0
            elif func_name in ['fread', 'read']:
                # 对于读取函数，返回0表示没有读取到数据
                return 0
            elif func_name in ['scanf']:
                # scanf返回0表示没有成功匹配任何项目
                return 0
            else:
                # 其他函数返回0或NULL
                return 0
                
        except Exception as e:
            print(f"[ERROR] 处理阻塞函数时出错: {e}")
            return 0

class EnhancedSprintfHook(angr.SimProcedure):
    """增强的sprintf Hook,栈上的参数暂时不考虑"""    
    def run(self, dst_ptr, fmt_ptr, *args):
        try:
            # 获取CoreTaint对象
            core_taint = self.state.globals.get('core_taint')
            project = self.state.globals.get('project')
            
            if core_taint is None or project is None:
                print("[ERROR] sprintf hook: CoreTaint或project对象未初始化")
                return 0
            
            pc = self.state.solver.eval(self.state.regs.pc)
            print(f"[SPRINTF HOOK] 被调用 at PC: {safe_hex(pc)}")
            
            # 读取格式化字符串
            fmt_str = ""
            try:
                # 尝试读取格式化字符串
                if not self.state.solver.symbolic(fmt_ptr):
                    fmt_addr = self.state.solver.eval(fmt_ptr)
                    # 读取最多256字节的格式化字符串
                    fmt_bytes = self.state.memory.load(fmt_addr, 256)
                    
                    # 转换为字符串
                    fmt_str_bytes = []
                    for i in range(256):
                        try:
                            byte_val = self.state.solver.eval(fmt_bytes.get_byte(i))
                            if byte_val == 0:  # null终止符
                                break
                            if 32 <= byte_val <= 126:  # 可打印ASCII字符
                                fmt_str_bytes.append(chr(byte_val))
                            else:
                                fmt_str_bytes.append('?')
                        except:
                            break
                    
                    fmt_str = ''.join(fmt_str_bytes)
                    print(f"[SPRINTF HOOK] 格式化字符串: '{fmt_str}'")
                else:
                    print(f"[SPRINTF HOOK] 格式化字符串是符号值，无法解析")
            except Exception as e:
                print(f"[SPRINTF HOOK] 读取格式化字符串失败: {e}")
            
            # 分析格式化字符串，计算参数数量
            param_count = 0
            has_tainted_params = False
            tainted_param_indices = []
            tainted_sources = []  # 收集被污染的源变量
            
            if fmt_str:
                # 计算格式化参数数量
                param_count = fmt_str.count('%s') + fmt_str.count('%d')
                
                print(f"[SPRINTF HOOK] 检测到 {param_count} 个格式化参数")
            
            # 检查参数寄存器中的污点（从第3个参数开始，前两个是dst和fmt）
            arch_name = project.arch.name
            if arch_name in func_params_regs:
                reg_names = func_params_regs[arch_name]
                
                # 检查每个格式化参数对应的寄存器
                for i in range(min(param_count, len(reg_names) - 2)):  # -2 因为前两个是dst和fmt
                    param_reg_idx = i + 2  # 参数从第3个寄存器开始
                    
                    if param_reg_idx < len(reg_names):
                        reg_name = reg_names[param_reg_idx]
                        try:
                            reg_val = self.state.registers.load(reg_name)
                            print(f"[SPRINTF HOOK] 检查参数 {i+1} (寄存器 {reg_name}): {safe_hex(reg_val)}")
                            
                            # 检查寄存器值是否被污染
                            is_reg_tainted, reg_varname = core_taint.check_taint(self.state, reg_val, 
                                                                               f"sprintf参数{i+1}寄存器{reg_name}")
                            
                            if is_reg_tainted :
                                has_tainted_params = True
                                tainted_param_indices.append(i + 1)
                                varname = reg_varname
                                tainted_sources.append(varname) 
                                print(f"[SPRINTF HOOK] 参数 {i+1} 含有污点: {varname}")
                                
                                # 添加为关键变量
                                if varname:
                                    core_taint.add_critical_variable(varname)
                                    core_taint.solve_constraints(self.state)
                                    print(f"[SPRINTF HOOK] 进行符号求解，添加关键变量: {varname}")
                        except Exception as e:
                            print(f"[SPRINTF HOOK] 检查参数 {i+1} 时出错: {e}")
            
            # 处理目标缓冲区
            if has_tainted_params:
                print(f"[SPRINTF HOOK] 发现被污染的参数: {tainted_param_indices}")
                
                # 创建污点符号变量作为sprintf的输出
                lable=f"sprintf_output"
                for i, varname in enumerate(tainted_sources):
                        # 创建污点符号变量
                        lable +=f"_{i+1}_{varname}"
                print(f"[SPRINTF HOOK] 创建污点输出变量: {lable}")
                tainted_output = core_taint.create_taint_var(lable, bits=256*8)

                
                # 将污点输出存储到目标缓冲区
                try:
                    if not self.state.solver.symbolic(dst_ptr):
                        dst_addr = self.state.solver.eval(dst_ptr)
                        self.state.memory.store(dst_addr, tainted_output)
                        
                        # 标记目标缓冲区被污染
                        core_taint.mark_taint(dst_addr, lable, pc)
                        
                        # 记录污点传播路径
                        core_taint.record_taint_path("FUNC_CALL", pc, 
                                                   target_name="sprintf",
                                                   target_addr=self.state.addr,
                                                   tainted_params=tainted_param_indices)
                        
                        print(f"[SPRINTF HOOK] 污点输出写入目标缓冲区: {safe_hex(dst_addr)}")
                        
                        # 将新的污点变量添加到全局符号表
                        # core_taint.global_var_symbols[lable] = tainted_output
                        
                        # 返回写入的字节数（估算值）
                        return len(fmt_str) + sum([8 for _ in range(param_count)])  # 粗略估算
                    else:
                        print(f"[SPRINTF HOOK] 目标地址是符号值，无法处理")
                        return 0
                except Exception as e:
                    print(f"[SPRINTF HOOK] 处理污点输出时出错: {e}")
                    return 0
            else:
                print(f"[SPRINTF HOOK] 未发现被污染的参数，创建非污点输出")
                
                # 创建非污点的符号输出
                try:
                    if not self.state.solver.symbolic(dst_ptr):
                        dst_addr = self.state.solver.eval(dst_ptr)
                        # 创建一个有限长度的符号变量
                        clean_output = claripy.BVS(f"sprintf_clean_{safe_hex(pc)}", 256*8)
                        self.state.memory.store(dst_addr, clean_output)
                        print(f"[SPRINTF HOOK] 非污点输出写入目标缓冲区: {safe_hex(dst_addr)}")
                        return len(fmt_str) + sum([8 for _ in range(param_count)])  # 粗略估算
                    else:
                        return 0
                except Exception as e:
                    print(f"[SPRINTF HOOK] 处理非污点输出时出错: {e}")
                    return 0
            
        except Exception as e:
            print(f"[ERROR] sprintf hook 出错: {e}")
            import traceback
            traceback.print_exc()
            return 0

class EnhancedSnprintfHook(angr.SimProcedure):
    """增强的snprintf Hook，与sprintf功能一致，但多了长度限制参数"""    
    def run(self, dst_ptr, size_param, fmt_ptr, *args):
        try:
            # 获取CoreTaint对象
            core_taint = self.state.globals.get('core_taint')
            project = self.state.globals.get('project')
            
            if core_taint is None or project is None:
                print("[ERROR] snprintf hook: CoreTaint或project对象未初始化")
                return 0
            
            pc = self.state.solver.eval(self.state.regs.pc)
            print(f"[SNPRINTF HOOK] 被调用 at PC: {safe_hex(pc)}")
            
            # 读取长度限制参数
            buffer_size = 0
            try:
                if not self.state.solver.symbolic(size_param):
                    buffer_size = self.state.solver.eval(size_param)
                    print(f"[SNPRINTF HOOK] 缓冲区大小限制: {buffer_size}")
                else:
                    print(f"[SNPRINTF HOOK] 缓冲区大小是符号值，无法解析")
                    buffer_size = 256  # 默认大小
            except Exception as e:
                print(f"[SNPRINTF HOOK] 读取缓冲区大小失败: {e}")
                buffer_size = 256  # 默认大小
            
            # 读取格式化字符串
            fmt_str = ""
            try:
                # 尝试读取格式化字符串
                if not self.state.solver.symbolic(fmt_ptr):
                    fmt_addr = self.state.solver.eval(fmt_ptr)
                    # 读取最多256字节的格式化字符串
                    fmt_bytes = self.state.memory.load(fmt_addr, 256)
                    
                    # 转换为字符串
                    fmt_str_bytes = []
                    for i in range(256):
                        try:
                            byte_val = self.state.solver.eval(fmt_bytes.get_byte(i))
                            if byte_val == 0:  # null终止符
                                break
                            if 32 <= byte_val <= 126:  # 可打印ASCII字符
                                fmt_str_bytes.append(chr(byte_val))
                            else:
                                fmt_str_bytes.append('?')
                        except:
                            break
                    
                    fmt_str = ''.join(fmt_str_bytes)
                    print(f"[SNPRINTF HOOK] 格式化字符串: '{fmt_str}'")
                else:
                    print(f"[SNPRINTF HOOK] 格式化字符串是符号值，无法解析")
            except Exception as e:
                print(f"[SNPRINTF HOOK] 读取格式化字符串失败: {e}")
            
            # 分析格式化字符串，计算参数数量
            param_count = 0
            has_tainted_params = False
            tainted_param_indices = []
            tainted_sources = []  # 收集被污染的源变量
            
            if fmt_str:
                # 计算格式化参数数量
                param_count = fmt_str.count('%s') + fmt_str.count('%d')
                
                print(f"[SNPRINTF HOOK] 检测到 {param_count} 个格式化参数")
            
            # 检查参数寄存器中的污点（从第4个参数开始，前三个是dst、size、fmt）
            arch_name = project.arch.name
            if arch_name in func_params_regs:
                reg_names = func_params_regs[arch_name]
                
                # 检查每个格式化参数对应的寄存器
                for i in range(min(param_count, len(reg_names) - 3)):  # -3 因为前三个是dst、size、fmt
                    param_reg_idx = i + 3  # 参数从第4个寄存器开始
                    
                    if param_reg_idx < len(reg_names):
                        reg_name = reg_names[param_reg_idx]
                        try:
                            reg_val = self.state.registers.load(reg_name)
                            print(f"[SNPRINTF HOOK] 检查参数 {i+1} (寄存器 {reg_name}): {safe_hex(reg_val)}")
                            
                            # 检查寄存器值是否被污染
                            is_reg_tainted, reg_varname = core_taint.check_taint(self.state, reg_val, 
                                                                               f"snprintf参数{i+1}寄存器{reg_name}")
                            
                            if is_reg_tainted:
                                has_tainted_params = True
                                tainted_param_indices.append(i + 1)
                                varname = reg_varname
                                tainted_sources.append(varname) 
                                print(f"[SNPRINTF HOOK] 参数 {i+1} 含有污点: {varname}")
                                
                                # 添加为关键变量
                                if varname:
                                    core_taint.add_critical_variable(varname)
                                    core_taint.solve_constraints(self.state)
                                    print(f"[SNPRINTF HOOK] 进行符号求解，添加关键变量: {varname}")
                        except Exception as e:
                            print(f"[SNPRINTF HOOK] 检查参数 {i+1} 时出错: {e}")
            
            # 处理目标缓冲区
            if has_tainted_params:
                print(f"[SNPRINTF HOOK] 发现被污染的参数: {tainted_param_indices}")
                
                # 创建污点符号变量作为snprintf的输出
                lable = f"snprintf_output"
                for i, varname in enumerate(tainted_sources):
                    # 创建污点符号变量
                    lable += f"_{i+1}_{varname}"
                print(f"[SNPRINTF HOOK] 创建污点输出变量: {lable}")
                
                # 考虑长度限制，使用较小的值作为输出大小
                actual_output_bits = min(buffer_size * 8, 256 * 8) if buffer_size > 0 else 256 * 8
                tainted_output = core_taint.create_taint_var(lable, bits=actual_output_bits)

                # 将污点输出存储到目标缓冲区
                try:
                    if not self.state.solver.symbolic(dst_ptr):
                        dst_addr = self.state.solver.eval(dst_ptr)
                        self.state.memory.store(dst_addr, tainted_output)
                        
                        # 标记目标缓冲区被污染
                        core_taint.mark_taint(dst_addr, lable, pc)
                        
                        # 记录污点传播路径
                        core_taint.record_taint_path("FUNC_CALL", pc, 
                                                   target_name="snprintf",
                                                   target_addr=self.state.addr,
                                                   tainted_params=tainted_param_indices)
                        
                        print(f"[SNPRINTF HOOK] 污点输出写入目标缓冲区: {safe_hex(dst_addr)}，长度限制: {buffer_size}")
                        
                        # 返回写入的字节数（考虑长度限制）
                        estimated_length = len(fmt_str) + sum([8 for _ in range(param_count)])
                        actual_length = min(estimated_length, buffer_size - 1) if buffer_size > 0 else estimated_length
                        return actual_length
                    else:
                        print(f"[SNPRINTF HOOK] 目标地址是符号值，无法处理")
                        return 0
                except Exception as e:
                    print(f"[SNPRINTF HOOK] 处理污点输出时出错: {e}")
                    return 0
            else:
                print(f"[SNPRINTF HOOK] 未发现被污染的参数，创建非污点输出")
                
                # 创建非污点的符号输出
                try:
                    if not self.state.solver.symbolic(dst_ptr):
                        dst_addr = self.state.solver.eval(dst_ptr)
                        # 创建一个有限长度的符号变量，考虑长度限制
                        actual_output_bits = min(buffer_size * 8, 256 * 8) if buffer_size > 0 else 256 * 8
                        clean_output = claripy.BVS(f"snprintf_clean_{safe_hex(pc)}", actual_output_bits)
                        self.state.memory.store(dst_addr, clean_output)
                        print(f"[SNPRINTF HOOK] 非污点输出写入目标缓冲区: {safe_hex(dst_addr)}，长度限制: {buffer_size}")
                        
                        # 返回写入的字节数（考虑长度限制）
                        estimated_length = len(fmt_str) + sum([8 for _ in range(param_count)])
                        actual_length = min(estimated_length, buffer_size - 1) if buffer_size > 0 else estimated_length
                        return actual_length
                    else:
                        return 0
                except Exception as e:
                    print(f"[SNPRINTF HOOK] 处理非污点输出时出错: {e}")
                    return 0
            
        except Exception as e:
            print(f"[ERROR] snprintf hook 出错: {e}")
            import traceback
            traceback.print_exc()
            return 0

class EnhancedStrcpyHook(angr.SimProcedure):
    """增强的strcpy Hook，继承源的符号变量"""    
    def run(self, dst_ptr, src_ptr):
        try:
            # 获取CoreTaint对象
            core_taint = self.state.globals.get('core_taint')
            project = self.state.globals.get('project')
            
            if core_taint is None or project is None:
                print("[ERROR] strcpy hook: CoreTaint或project对象未初始化")
                return dst_ptr
            
            pc = self.state.solver.eval(self.state.regs.pc)
            print(f"[STRCPY HOOK] 被调用 at PC: {safe_hex(pc)}")
            
            # 检查参数寄存器中的污点
            arch_name = project.arch.name
            if arch_name not in func_params_regs:
                print(f"[STRCPY HOOK] 不支持的架构: {arch_name}")
                return dst_ptr
            
            reg_names = func_params_regs[arch_name]
            has_tainted_params = False
            tainted_param_indices = []
            tainted_sources = []  # 收集被污染的源变量
            source_symbol_var = None  # 存储源的符号变量
            
            # 只检查第2个参数寄存器（源参数，索引为1）
            if len(reg_names) > 1:
                reg_name = reg_names[1]  # 第2个参数寄存器（src）
                try:
                    reg_val = self.state.registers.load(reg_name)
                    print(f"[STRCPY HOOK] 检查源参数 (寄存器 {reg_name}): {safe_hex(reg_val)}")
                    
                    # 检查寄存器值是否被污染
                    is_reg_tainted, reg_varname = core_taint.check_taint(self.state, reg_val, 
                                                                       f"strcpy源参数寄存器{reg_name}")
                    
                    if is_reg_tainted:
                        has_tainted_params = True
                        tainted_param_indices.append(2)  # 源参数是第2个参数
                        varname = reg_varname
                        tainted_sources.append(varname) 
                        print(f"[STRCPY HOOK] 源参数含有污点: {varname}")
                        
                        # 获取源变量的符号变量（用于继承）
                        if varname in core_taint.global_var_symbols:
                            source_symbol_var = core_taint.global_var_symbols[varname]
                            print(f"[STRCPY HOOK] 找到源符号变量: {source_symbol_var}")
                        
                        # 添加为关键变量
                        if varname:
                            core_taint.add_critical_variable(varname)
                            core_taint.solve_constraints(self.state)
                            print(f"[STRCPY HOOK] 进行符号求解，添加关键变量: {varname}")
                            
                except Exception as e:
                    print(f"[STRCPY HOOK] 检查源参数时出错: {e}")
            
            # 额外检查源地址指向的内容是否被污染
            if not self.state.solver.symbolic(src_ptr):
                try:
                    src_addr = self.state.solver.eval(src_ptr)
                    print(f"[STRCPY HOOK] 源地址: {safe_hex(src_addr)}")
                    
                    # 检查源地址的内容是否被污染
                    src_content = self.state.memory.load(src_addr, 8*32)  
                    is_content_tainted, content_varname = core_taint.check_taint(self.state, src_content, 
                                                                               f"strcpy源内容@{safe_hex(src_addr)}")
                    if is_content_tainted:
                        if not has_tainted_params:  # 如果寄存器检查没有发现污点
                            has_tainted_params = True
                            tainted_param_indices.append(2)  # 源参数
                        
                        if content_varname and content_varname not in tainted_sources:
                            tainted_sources.append(content_varname)
                            print(f"[STRCPY HOOK] 源内容包含污点: {content_varname}")
                            
                            # 如果还没有找到源符号变量，尝试从内容中获取
                            if source_symbol_var is None and content_varname in core_taint.global_var_symbols:
                                source_symbol_var = core_taint.global_var_symbols[content_varname]
                                print(f"[STRCPY HOOK] 从源内容找到符号变量: {source_symbol_var}")
                            
                            # 添加为关键变量
                            core_taint.add_critical_variable(content_varname)
                            core_taint.solve_constraints(self.state)
                            print(f"[STRCPY HOOK] 进行符号求解，添加关键变量: {content_varname}")
                            
                except Exception as e:
                    print(f"[STRCPY HOOK] 检查源内容时出错: {e}")
            
            # 处理目标缓冲区
            if has_tainted_params:
                print(f"[STRCPY HOOK] 发现被污染的源参数: {tainted_param_indices}")
                
                # 决定使用继承的符号变量还是创建新的
                if source_symbol_var is not None:
                    # 直接继承源的符号变量
                    tainted_output = source_symbol_var
                    label = f"strcpy_inherited_{tainted_sources[0]}"  # 使用第一个污点源的名称
                    print(f"[STRCPY HOOK] 继承源符号变量: {tainted_output}")
                else:
                    # 创建新的污点符号变量（备用方案）
                    label = f"strcpy_output"
                    for i, varname in enumerate(tainted_sources):
                        label += f"_{i+1}_{varname}"
                    print(f"[STRCPY HOOK] 创建新污点输出变量: {label}")
                    tainted_output = core_taint.create_taint_var(label, bits=256*8)

                # 将污点输出存储到目标缓冲区
                try:
                    if not self.state.solver.symbolic(dst_ptr):
                        dst_addr = self.state.solver.eval(dst_ptr)
                        self.state.memory.store(dst_addr, tainted_output)
                        
                        # 标记目标缓冲区被污染
                        core_taint.mark_taint(dst_addr, label, pc)
                        
                        # 标记一个范围的地址被污染（假设最多复制256字节）
                        for i in range(256):
                            addr = dst_addr + i
                            core_taint.tainted_addresses.add(addr)
                            core_taint.mark_taint(addr, label, pc)
                        
                        # 记录污点传播路径
                        core_taint.record_taint_path("FUNC_CALL", pc, 
                                                   target_name="strcpy",
                                                   target_addr=self.state.addr,
                                                   tainted_params=tainted_param_indices)
                        
                        print(f"[STRCPY HOOK] 污点输出写入目标缓冲区: {safe_hex(dst_addr)}")
                        
                        # 返回目标指针
                        return dst_ptr
                    else:
                        print(f"[STRCPY HOOK] 目标地址是符号值，无法处理")
                        return dst_ptr
                except Exception as e:
                    print(f"[STRCPY HOOK] 处理污点输出时出错: {e}")
                    return dst_ptr
            else:
                print(f"[STRCPY HOOK] 源参数未发现污点，执行标准复制")
                
                # 执行标准的字符串复制（非污点情况）
                try:
                    if (not self.state.solver.symbolic(src_ptr) and 
                        not self.state.solver.symbolic(dst_ptr)):
                        
                        src_addr = self.state.solver.eval(src_ptr)
                        dst_addr = self.state.solver.eval(dst_ptr)
                        
                        # 直接复制源内容到目标
                        src_content = self.state.memory.load(src_addr, 256)  # 复制256字节
                        self.state.memory.store(dst_addr, src_content)
                        
                        print(f"[STRCPY HOOK] 标准复制完成")
                        return dst_ptr
                    else:
                        return dst_ptr
                except Exception as e:
                    print(f"[STRCPY HOOK] 标准复制时出错: {e}")
                    return dst_ptr
            
        except Exception as e:
            print(f"[ERROR] strcpy hook 出错: {e}")
            import traceback
            traceback.print_exc()
            return dst_ptr

class EnhancedStrncpyHook(angr.SimProcedure):
    """增强的strncpy Hook，继承源的符号变量，但多了长度限制参数"""    
    def run(self, dst_ptr, src_ptr, size_param):
        try:
            # 获取CoreTaint对象
            core_taint = self.state.globals.get('core_taint')
            project = self.state.globals.get('project')
            
            if core_taint is None or project is None:
                print("[ERROR] strncpy hook: CoreTaint或project对象未初始化")
                return dst_ptr
            
            pc = self.state.solver.eval(self.state.regs.pc)
            print(f"[STRNCPY HOOK] 被调用 at PC: {safe_hex(pc)}")
            
            # 读取长度限制参数
            copy_size = 0
            try:
                if not self.state.solver.symbolic(size_param):
                    copy_size = self.state.solver.eval(size_param)
                    print(f"[STRNCPY HOOK] 复制长度限制: {copy_size}")
                else:
                    print(f"[STRNCPY HOOK] 复制长度是符号值，无法解析")
                    copy_size = 256  # 默认大小
            except Exception as e:
                print(f"[STRNCPY HOOK] 读取复制长度失败: {e}")
                copy_size = 256  # 默认大小
            
            # 检查参数寄存器中的污点
            arch_name = project.arch.name
            if arch_name not in func_params_regs:
                print(f"[STRNCPY HOOK] 不支持的架构: {arch_name}")
                return dst_ptr
            
            reg_names = func_params_regs[arch_name]
            has_tainted_params = False
            tainted_param_indices = []
            tainted_sources = []  # 收集被污染的源变量
            source_symbol_var = None  # 存储源的符号变量
            
            # 只检查第2个参数寄存器（源参数，索引为1）
            if len(reg_names) > 1:
                reg_name = reg_names[1]  # 第2个参数寄存器（src）
                try:
                    reg_val = self.state.registers.load(reg_name)
                    print(f"[STRNCPY HOOK] 检查源参数 (寄存器 {reg_name}): {safe_hex(reg_val)}")
                    
                    # 检查寄存器值是否被污染
                    is_reg_tainted, reg_varname = core_taint.check_taint(self.state, reg_val, 
                                                                       f"strncpy源参数寄存器{reg_name}")
                    
                    if is_reg_tainted:
                        has_tainted_params = True
                        tainted_param_indices.append(2)  # 源参数是第2个参数
                        varname = reg_varname
                        tainted_sources.append(varname) 
                        print(f"[STRNCPY HOOK] 源参数含有污点: {varname}")
                        
                        # 获取源变量的符号变量（用于继承）
                        if varname in core_taint.global_var_symbols:
                            source_symbol_var = core_taint.global_var_symbols[varname]
                            print(f"[STRNCPY HOOK] 找到源符号变量: {source_symbol_var}")
                        
                        # 添加为关键变量
                        if varname:
                            core_taint.add_critical_variable(varname)
                            core_taint.solve_constraints(self.state)
                            print(f"[STRNCPY HOOK] 进行符号求解，添加关键变量: {varname}")
                            
                except Exception as e:
                    print(f"[STRNCPY HOOK] 检查源参数时出错: {e}")
            
            # 额外检查源地址指向的内容是否被污染
            if not self.state.solver.symbolic(src_ptr):
                try:
                    src_addr = self.state.solver.eval(src_ptr)
                    print(f"[STRNCPY HOOK] 源地址: {safe_hex(src_addr)}")
                    
                    # 检查源地址的内容是否被污染（限制在copy_size范围内）
                    check_size = min(copy_size, 256) if copy_size > 0 else 256
                    src_content = self.state.memory.load(src_addr, check_size)  
                    is_content_tainted, content_varname = core_taint.check_taint(self.state, src_content, 
                                                                               f"strncpy源内容@{safe_hex(src_addr)}")
                    if is_content_tainted:
                        if not has_tainted_params:  # 如果寄存器检查没有发现污点
                            has_tainted_params = True
                            tainted_param_indices.append(2)  # 源参数
                        
                        if content_varname and content_varname not in tainted_sources:
                            tainted_sources.append(content_varname)
                            print(f"[STRNCPY HOOK] 源内容包含污点: {content_varname}")
                            
                            # 如果还没有找到源符号变量，尝试从内容中获取
                            if source_symbol_var is None and content_varname in core_taint.global_var_symbols:
                                source_symbol_var = core_taint.global_var_symbols[content_varname]
                                print(f"[STRNCPY HOOK] 从源内容找到符号变量: {source_symbol_var}")
                            
                            # 添加为关键变量
                            core_taint.add_critical_variable(content_varname)
                            core_taint.solve_constraints(self.state)
                            print(f"[STRNCPY HOOK] 进行符号求解，添加关键变量: {content_varname}")
                            
                except Exception as e:
                    print(f"[STRNCPY HOOK] 检查源内容时出错: {e}")
            
            # 处理目标缓冲区
            if has_tainted_params:
                print(f"[STRNCPY HOOK] 发现被污染的源参数: {tainted_param_indices}")
                
                # 决定使用继承的符号变量还是创建新的
                if source_symbol_var is not None:
                    # 直接继承源的符号变量
                    tainted_output = source_symbol_var
                    label = f"strncpy_inherited_{tainted_sources[0]}"  # 使用第一个污点源的名称
                    print(f"[STRNCPY HOOK] 继承源符号变量: {tainted_output}")
                else:
                    # 创建新的污点符号变量（备用方案）
                    label = f"strncpy_output"
                    for i, varname in enumerate(tainted_sources):
                        label += f"_{i+1}_{varname}"
                    print(f"[STRNCPY HOOK] 创建新污点输出变量: {label}")
                    
                    # 考虑长度限制，使用较小的值作为输出大小
                    actual_output_bits = min(copy_size * 8, 256 * 8) if copy_size > 0 else 256 * 8
                    tainted_output = core_taint.create_taint_var(label, bits=actual_output_bits)

                # 将污点输出存储到目标缓冲区
                try:
                    if not self.state.solver.symbolic(dst_ptr):
                        dst_addr = self.state.solver.eval(dst_ptr)
                        self.state.memory.store(dst_addr, tainted_output)
                        
                        # 标记目标缓冲区被污染
                        core_taint.mark_taint(dst_addr, label, pc)
                        
                        # 标记一个范围的地址被污染（考虑长度限制）
                        actual_copy_range = min(copy_size, 256) if copy_size > 0 else 256
                        for i in range(actual_copy_range):
                            addr = dst_addr + i
                            core_taint.tainted_addresses.add(addr)
                            core_taint.mark_taint(addr, label, pc)
                        
                        # 记录污点传播路径
                        core_taint.record_taint_path("FUNC_CALL", pc, 
                                                   target_name="strncpy",
                                                   target_addr=self.state.addr,
                                                   tainted_params=tainted_param_indices)
                        
                        print(f"[STRNCPY HOOK] 污点输出写入目标缓冲区: {safe_hex(dst_addr)}，长度限制: {copy_size}")
                        
                        # 返回目标指针
                        return dst_ptr
                    else:
                        print(f"[STRNCPY HOOK] 目标地址是符号值，无法处理")
                        return dst_ptr
                except Exception as e:
                    print(f"[STRNCPY HOOK] 处理污点输出时出错: {e}")
                    return dst_ptr
            else:
                print(f"[STRNCPY HOOK] 源参数未发现污点，执行标准复制")
                
                # 执行标准的字符串复制（非污点情况）
                try:
                    if (not self.state.solver.symbolic(src_ptr) and 
                        not self.state.solver.symbolic(dst_ptr)):
                        
                        src_addr = self.state.solver.eval(src_ptr)
                        dst_addr = self.state.solver.eval(dst_ptr)
                        
                        # 直接复制源内容到目标（考虑长度限制）
                        actual_copy_size = min(copy_size, 256) if copy_size > 0 else 256
                        src_content = self.state.memory.load(src_addr, actual_copy_size)
                        self.state.memory.store(dst_addr, src_content)
                        
                        print(f"[STRNCPY HOOK] 标准复制完成，复制长度: {actual_copy_size}")
                        return dst_ptr
                    else:
                        return dst_ptr
                except Exception as e:
                    print(f"[STRNCPY HOOK] 标准复制时出错: {e}")
                    return dst_ptr
            
        except Exception as e:
            print(f"[ERROR] strncpy hook 出错: {e}")
            import traceback
            traceback.print_exc()
            return dst_ptr

class EnhancedStrcatHook(angr.SimProcedure):
    """增强的strcat Hook，继承源的符号变量，但需要追加到目标字符串末尾"""    
    def run(self, dst_ptr, src_ptr):
        try:
            # 获取CoreTaint对象
            core_taint = self.state.globals.get('core_taint')
            project = self.state.globals.get('project')
            
            if core_taint is None or project is None:
                print("[ERROR] strcat hook: CoreTaint或project对象未初始化")
                return dst_ptr
            
            pc = self.state.solver.eval(self.state.regs.pc)
            print(f"[STRCAT HOOK] 被调用 at PC: {safe_hex(pc)}")
            
            # 检查参数寄存器中的污点
            arch_name = project.arch.name
            if arch_name not in func_params_regs:
                print(f"[STRCAT HOOK] 不支持的架构: {arch_name}")
                return dst_ptr
            
            reg_names = func_params_regs[arch_name]
            has_tainted_params = False
            tainted_param_indices = []
            tainted_sources = []  # 收集被污染的源变量
            source_symbol_var = None  # 存储源的符号变量
            
            # 只检查第2个参数寄存器（源参数，索引为1）
            if len(reg_names) > 1:
                reg_name = reg_names[1]  # 第2个参数寄存器（src）
                try:
                    reg_val = self.state.registers.load(reg_name)
                    print(f"[STRCAT HOOK] 检查源参数 (寄存器 {reg_name}): {safe_hex(reg_val)}")
                    
                    # 检查寄存器值是否被污染
                    is_reg_tainted, reg_varname = core_taint.check_taint(self.state, reg_val, 
                                                                       f"strcat源参数寄存器{reg_name}")
                    
                    if is_reg_tainted:
                        has_tainted_params = True
                        tainted_param_indices.append(2)  # 源参数是第2个参数
                        varname = reg_varname
                        tainted_sources.append(varname) 
                        print(f"[STRCAT HOOK] 源参数含有污点: {varname}")
                        
                        # 获取源变量的符号变量（用于继承）
                        if varname in core_taint.global_var_symbols:
                            source_symbol_var = core_taint.global_var_symbols[varname]
                            print(f"[STRCAT HOOK] 找到源符号变量: {source_symbol_var}")
                        
                        # 添加为关键变量
                        if varname:
                            core_taint.add_critical_variable(varname)
                            core_taint.solve_constraints(self.state)
                            print(f"[STRCAT HOOK] 进行符号求解，添加关键变量: {varname}")
                            
                except Exception as e:
                    print(f"[STRCAT HOOK] 检查源参数时出错: {e}")
            
            # 额外检查源地址指向的内容是否被污染
            if not self.state.solver.symbolic(src_ptr):
                try:
                    src_addr = self.state.solver.eval(src_ptr)
                    print(f"[STRCAT HOOK] 源地址: {safe_hex(src_addr)}")
                    
                    # 检查源地址的内容是否被污染
                    src_content = self.state.memory.load(src_addr, 8*32)  
                    is_content_tainted, content_varname = core_taint.check_taint(self.state, src_content, 
                                                                               f"strcat源内容@{safe_hex(src_addr)}")
                    if is_content_tainted:
                        if not has_tainted_params:  # 如果寄存器检查没有发现污点
                            has_tainted_params = True
                            tainted_param_indices.append(2)  # 源参数
                        
                        if content_varname and content_varname not in tainted_sources:
                            tainted_sources.append(content_varname)
                            print(f"[STRCAT HOOK] 源内容包含污点: {content_varname}")
                            
                            # 如果还没有找到源符号变量，尝试从内容中获取
                            if source_symbol_var is None and content_varname in core_taint.global_var_symbols:
                                source_symbol_var = core_taint.global_var_symbols[content_varname]
                                print(f"[STRCAT HOOK] 从源内容找到符号变量: {source_symbol_var}")
                            
                            # 添加为关键变量
                            core_taint.add_critical_variable(content_varname)
                            core_taint.solve_constraints(self.state)
                            print(f"[STRCAT HOOK] 进行符号求解，添加关键变量: {content_varname}")
                            
                except Exception as e:
                    print(f"[STRCAT HOOK] 检查源内容时出错: {e}")
            
            # 检查目标字符串是否已经包含污点
            dst_already_tainted = False
            dst_existing_varname = None
            if not self.state.solver.symbolic(dst_ptr):
                try:
                    dst_addr = self.state.solver.eval(dst_ptr)
                    print(f"[STRCAT HOOK] 目标地址: {safe_hex(dst_addr)}")
                    
                    # 检查目标地址的内容是否被污染
                    dst_content = self.state.memory.load(dst_addr, 8*32)  
                    is_dst_tainted, dst_varname = core_taint.check_taint(self.state, dst_content, 
                                                                       f"strcat目标内容@{safe_hex(dst_addr)}")
                    if is_dst_tainted:
                        dst_already_tainted = True
                        dst_existing_varname = dst_varname
                        print(f"[STRCAT HOOK] 目标字符串已包含污点: {dst_varname}")
                        
                except Exception as e:
                    print(f"[STRCAT HOOK] 检查目标内容时出错: {e}")
            
            # 处理目标缓冲区
            if has_tainted_params or dst_already_tainted:
                print(f"[STRCAT HOOK] 发现被污染的源参数: {tainted_param_indices}")
                
                # 决定如何处理污点
                if dst_already_tainted and has_tainted_params:
                    # 如果目标和源都有污点，创建混合污点变量
                    all_tainted_sources = []
                    if dst_existing_varname:
                        all_tainted_sources.append(dst_existing_varname)
                    all_tainted_sources.extend(tainted_sources)
                    
                    label = f"strcat_mixed"
                    for i, varname in enumerate(all_tainted_sources):
                        label += f"_{i+1}_{varname}"
                    print(f"[STRCAT HOOK] 创建混合污点输出变量: {label}")
                    tainted_output = core_taint.create_taint_var(label, bits=256*8)
                    
                elif dst_already_tainted and not has_tainted_params:
                    # 如果只有目标有污点，保持目标的污点
                    label = f"strcat_preserved_{dst_existing_varname}"
                    print(f"[STRCAT HOOK] 保持目标现有污点: {label}")
                    
                    if dst_existing_varname in core_taint.global_var_symbols:
                        tainted_output = core_taint.global_var_symbols[dst_existing_varname]
                    else:
                        tainted_output = core_taint.create_taint_var(label, bits=256*8)
                        
                elif not dst_already_tainted and has_tainted_params:
                    # 如果只有源有污点，按照原来的逻辑处理
                    if source_symbol_var is not None:
                        # 直接继承源的符号变量
                        tainted_output = source_symbol_var
                        label = f"strcat_inherited_{tainted_sources[0]}"  # 使用第一个污点源的名称
                        print(f"[STRCAT HOOK] 继承源符号变量: {tainted_output}")
                    else:
                        # 创建新的污点符号变量（备用方案）
                        label = f"strcat_output"
                        for i, varname in enumerate(tainted_sources):
                            label += f"_{i+1}_{varname}"
                        print(f"[STRCAT HOOK] 创建新污点输出变量: {label}")
                        tainted_output = core_taint.create_taint_var(label, bits=256*8)

                # 将污点输出存储到目标缓冲区
                try:
                    if not self.state.solver.symbolic(dst_ptr):
                        dst_addr = self.state.solver.eval(dst_ptr)
                        self.state.memory.store(dst_addr, tainted_output)
                        
                        # 标记目标缓冲区被污染
                        core_taint.mark_taint(dst_addr, label, pc)
                        
                        # 标记一个范围的地址被污染（strcat可能产生更长的字符串）
                        for i in range(512):  # strcat可能产生更长的字符串，所以用512字节
                            addr = dst_addr + i
                            core_taint.tainted_addresses.add(addr)
                            core_taint.mark_taint(addr, label, pc)
                        
                        # 记录污点传播路径
                        core_taint.record_taint_path("FUNC_CALL", pc, 
                                                   target_name="strcat",
                                                   target_addr=self.state.addr,
                                                   tainted_params=tainted_param_indices)
                        
                        print(f"[STRCAT HOOK] 污点输出写入目标缓冲区: {safe_hex(dst_addr)}")
                        
                        # 返回目标指针
                        return dst_ptr
                    else:
                        print(f"[STRCAT HOOK] 目标地址是符号值，无法处理")
                        return dst_ptr
                except Exception as e:
                    print(f"[STRCAT HOOK] 处理污点输出时出错: {e}")
                    return dst_ptr
            else:
                print(f"[STRCAT HOOK] 源和目标参数都未发现污点，执行标准连接")
                
                # 执行标准的字符串连接（非污点情况）
                try:
                    if (not self.state.solver.symbolic(src_ptr) and 
                        not self.state.solver.symbolic(dst_ptr)):
                        
                        src_addr = self.state.solver.eval(src_ptr)
                        dst_addr = self.state.solver.eval(dst_ptr)
                        
                        # 读取目标字符串现有内容
                        dst_content = self.state.memory.load(dst_addr, 256)
                        
                        # 读取源字符串内容
                        src_content = self.state.memory.load(src_addr, 256)
                        
                        # 简化处理：将源内容追加到目标内容后
                        # 实际的strcat需要找到目标字符串的末尾，这里简化处理
                        combined_content = claripy.Concat(dst_content, src_content)
                        self.state.memory.store(dst_addr, combined_content)
                        
                        print(f"[STRCAT HOOK] 标准连接完成")
                        return dst_ptr
                    else:
                        return dst_ptr
                except Exception as e:
                    print(f"[STRCAT HOOK] 标准连接时出错: {e}")
                    return dst_ptr
            
        except Exception as e:
            print(f"[ERROR] strcat hook 出错: {e}")
            import traceback
            traceback.print_exc()
            return dst_ptr
        
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
    def is_library_function(addr, project):
        """判断一个函数是否是库函数"""
        if not project or not project.loader.main_object.contains_addr(addr):
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
            # 获取CoreTaint对象和项目对象
            core_taint = state.globals.get('core_taint')
            project = state.globals.get('project')
            remove_functions = state.globals.get('remove_functions', [])
            
            if core_taint is None or project is None:
                return
            
            # 获取函数调用地址和目标
            pc = state.addr
            history = state.history.addr if hasattr(state, 'history') and hasattr(state.history, 'addr') else pc
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
               
            # 检查是否是跳过的函数
            if target_name in remove_functions:
                print(f"[DEBUG] 即将调用被跳过的函数: {target_name} ({safe_hex(target_addr)})")
                return
            if target_name =="sprintf":
                print(f"[DEBUG] 即将调用 sprintf 函数，使用 EnhancedSprintfHook 处理")
                return
            if target_name =="snprintf":
                print(f"[DEBUG] 即将调用 snprintf 函数，使用 EnhancedSnprintfHook 处理")
                return
            print(f"[函数调用] {safe_hex(pc)}: 即将调用 {target_name} ({safe_hex(target_addr)})")
            # if target_name=="_system":
            #     print(f"[DEBUG] 检测到 特殊 调用，可能需要特殊处理")
            # 检查参数寄存器
            arch_name = project.arch.name
            if arch_name not in func_params_regs:
                print(f"[警告] 不支持的架构 {arch_name} 的参数寄存器检查")
                return
                
            reg_names = func_params_regs[arch_name]
            tainted_params = []
            call_reg_num = get_arity(project, history)
            print(f"[DEBUG] 检查 {min(call_reg_num, len(reg_names))} 个参数寄存器")
            
            # 检查每个参数寄存器
            for i, reg_name in enumerate(reg_names):
                if i >= call_reg_num:
                    break
                try:
                    reg_val = state.registers.load(reg_name)
                    print(f"[DEBUG] 检查寄存器 {reg_name}: {safe_hex(reg_val) if hasattr(reg_val, 'args') else reg_val}")
                    
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
                print(f"[污点传播] 发现 {len(tainted_params)} 个被污染的参数")
                
                # 记录到污点传播路径
                core_taint.record_taint_path("FUNC_CALL", pc, target_name=target_name, 
                                           target_addr=target_addr, tainted_params=tainted_params)
                
                # 判断是否需要求解约束
                is_lib_func = CallParamCheckHooks.is_library_function(target_addr, project)
                is_danger_func = CallParamCheckHooks.is_dangerous_function(target_name)
                
                print(f"[DEBUG] 函数 {target_name}: 是库函数={is_lib_func}, 是危险函数={is_danger_func}")
                
                if not is_lib_func or is_danger_func:
                    print(f"\n[路径约束求解] 为函数 {target_name} 求解约束")
                    
                    for i, reg_name, varname in tainted_params:
                        core_taint.add_critical_variable(varname)
                    
                    # 求解约束
                    core_taint.solve_constraints(state)
            else:
                print(f"[DEBUG] 调用 {target_name} 时未发现污点参数")

        except Exception as e:
            print(f"[ERROR] 函数调用钩子出错: {e}")
            import traceback
            traceback.print_exc()

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
            func_params_count=func.get("parameter_count",0)
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
                "parameter_count": func_params_count,
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

def analyze_target_function(binary_path, target_func, output_dir, IO_funcs, remove_functions):
    """单个函数的分析逻辑，单线程版本"""
    func_name = target_func.get("name")
    func_addr = target_func.get("address")
    
    print(f"\n[INFO] 开始分析函数: {func_name} ({hex(func_addr)})")
    
    try:
        # 加载二进制文件
        project = angr.Project(binary_path, auto_load_libs=False, use_sim_procedures=True)
        
        # **提前设置所有需要跳过的函数的Hook**
        print(f"[INFO] 设置跳过函数的Hook...")
        skipped_count = 0
        for remove_name in remove_functions:
            try:
                sym=project.loader.find_symbol(remove_name)
                project.hook(sym.rebased_addr, EnhancedSkipFunction())
                print(f"[INFO] 已Hook跳过函数: {remove_name} at {hex(sym.rebased_addr)}")
                skipped_count += 1
            except Exception as e:
                print(f"[WARNING] Hook函数 {sym} 失败: {e}")
        
        print(f"[INFO] 已设置 {skipped_count} 个跳过函数的Hook")
        blocking_functions = ['fgets', 'fread', 'read', 'scanf', 'getchar', 'gets']
        for block_func_name in blocking_functions:
            try:
                project.hook_symbol(block_func_name, SmartBlockingHandler())
                print(f"[INFO] 已Hook阻塞函数: {block_func_name}")
            except:
                pass  # 如果函数不存在就忽略
        
        try:
            project.hook_symbol("sprintf", EnhancedSprintfHook())
            print("[INFO] 已Hook sprintf函数")
        except Exception as e:
            print(f"[WARNING] Hook sprintf函数失败: {e}")
        
        try:
            project.hook_symbol("snprintf", EnhancedSnprintfHook())
            print("[INFO] 已Hook snprintf函数")
        except Exception as e:
            print(f"[WARNING] Hook snprintf函数失败: {e}")
            
        # 创建CoreTaint对象
        core_taint = CoreTaint(project)
        
        # 设置IO函数钩子
        for hook_func_name, hook_func_info in IO_funcs.items():
            hook_func_addr = hook_func_info.get("address")
            param_count = hook_func_info.get("parameter_count", 1)
            hook_class = get_hook_class_by_param_count(param_count)
            project.hook(hook_func_addr, hook_class())
            print(f"[INFO] 为函数 {hook_func_name} 设置钩子, 地址: {hex(hook_func_addr)}, 参数数量: {param_count}")
        
        # # 设置常见的IO函数Hook
        # try:
        #     project.hook_symbol("nvram_safe_get", HookWebsGetVar())
        #     project.hook_symbol("nvram_get", HookWebsGetVar())
        #     #project.hook_symbol("websGetVar", HookWebsGetVar())
        #     print("[INFO] 设置常见IO函数Hook完成")
        # except Exception as e:
        #     print(f"[WARNING] 设置常见IO函数Hook时出错: {e}")
        cfg = project.analyses.CFGFast()
        print(f"[INFO] [进程 {os.getpid()}] 分析函数 {func_name} 的参数...")
        try:
            func_obj= project.kb.functions.get(func_addr)
            if func_obj and hasattr(func_obj, 'prototype') and func_obj.prototype:
                param_count=len(func_obj.prototype.args) if func_obj.prototype.args else 0
                print(f"[INFO] 函数 {func_name} 的参数数量: {param_count}")
            else:
                param_count = 0
                print(f"[WARNING] 无法获取函数 {func_name} 的参数信息，默认参数数量为0")
        except Exception as e:
            print(f"[ERROR] 获取函数 {func_name} 的参数信息时出错: {e}")
            param_count = 0  
        # 创建调用状态
        state = project.factory.call_state(func_addr)
        
        # 将对象存储到状态中
        state.globals['core_taint'] = core_taint
        state.globals['project'] = project
        state.globals['remove_functions'] = remove_functions
        
        # 设置函数调用钩子
        state.inspect.b('call', when=angr.BP_BEFORE, action=CallParamCheckHooks.hook_function_call)
        
        simgr = project.factory.simgr(state)
        simgr.use_technique(angr.exploration_techniques.Timeout(30))
        step_count = 0
        max_steps = 50
        
        print(f"[INFO] 开始符号执行，最大步数: {max_steps}")
        
        while simgr.active and step_count < max_steps:
            try:
                simgr.step()
                step_count += 1
                print(f"[STEP {step_count}] Active: {len(simgr.active)}, Deadended: {len(simgr.deadended)}, Errored: {len(simgr.errored)}")      
                
                # 打印一些调试信息
                if step_count % 10 == 0:
                    print(f"[DEBUG] 当前污点变量: {list(core_taint.global_var_symbols.keys())}")
                    print(f"[DEBUG] 关键变量: {list(core_taint.critical_variables)}")
                    
            except Exception as e:
                print(f"[ERROR] 符号执行步骤出错: {e}")
                import traceback
                traceback.print_exc()
                break
        
        # 收集所有状态
        all_states = simgr.active[:]
        if hasattr(simgr, 'timeout'):
            all_states.extend(simgr.timeout)
        if hasattr(simgr, 'deadended'):
            all_states.extend(simgr.deadended)
        
        print(f"[INFO] 符号执行完成，共收集到 {len(all_states)} 个状态")
                    
        # 如果没有找到任何关键变量，但有符号变量，尝试从最后状态求解
        if core_taint.global_var_symbols and all_states:
            print(f"[INFO]从最终状态计算约束解...")
            
            # 从不同状态获取约束解
            if len(all_states) >= 3:
                sorted_states = sorted(all_states, key=lambda s: len(s.history.bbl_addrs) if hasattr(s, 'history') else 0)
                
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
                    (f"路径 {i}", state) for i, state in enumerate(all_states)
                ]
            
            # 从每个选定的状态中获取求解结果
            for path_desc, state in states_to_analyze:
                print(f"[INFO] 从{path_desc}计算约束解...")
                core_taint.solve_constraints(state)
        
        # 打印分析结果
        core_taint.print_results()
        
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
        print(f"[ERROR] 分析函数 {func_name} 时发生错误: {e}")
        import traceback
        traceback.print_exc()
        return {
            "func_name": func_name,
            "func_addr": func_addr,
            "error": str(e)
        }

def parse_args():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="污点分析工具 (单线程调试版)")
    parser.add_argument("json_file", help="提取结果的JSON文件路径")
    parser.add_argument("-o", "--output-dir", default="output_debug", help="输出目录，默认为'output_debug'")
    parser.add_argument("-f", "--function", help="指定要分析的函数名称（用于单独调试）")
    return parser.parse_args()

def main():
    """主函数，执行污点分析流程"""
    args = parse_args()
    json_file = args.json_file
    output_dir = args.output_dir
    target_function = args.function

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
    
    print("[INFO] 开始污点分析 (单线程调试版)...")
    print(f"[INFO] 加载二进制文件: {binary_path}")
    
    remove_functions = info.get("remove_functions", [])   
    if remove_functions:
        print(f"[INFO] 将跳过以下函数的深入分析: {', '.join(remove_functions)}")
        
    IO_funcs = {}
    for function in info.get("functions", []):
        func_name = function.get("name", "")
        addr_str = function.get("address", "")
        param_count= function.get("parameter_count", 0)
        if addr_str:
            if addr_str.startswith("0x"):
                func_addr = int(addr_str, 16)
            else:
                func_addr = int(addr_str)
                
            IO_funcs[func_name] = {
                "address": func_addr,
                "parameter_count": param_count
            }
            print(f"[INFO] 从JSON中获取 IO函数 {func_name} 地址: {hex(func_addr)}, 参数数量: {param_count}")
    
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
            
            # 如果指定了特定函数，只分析该函数
            if target_function and caller_name != target_function:
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
        if target_function:
            print(f"[ERROR] 未找到指定的函数 {target_function}")
        else:
            print("[ERROR] 未找到任何调用IO的函数，退出分析")
        return
    
    print(f"[INFO] 将分析 {len(target_funcs)} 个函数:")
    for func in target_funcs:
        print(f"  - {func['name']} ({hex(func['address'])})")
    
    # 单线程分析每个函数
    results = []
    for func in target_funcs:
        print(f"\n{'='*60}")
        result = analyze_target_function(binary_path, func, output_dir, IO_funcs, remove_functions)
        results.append(result)
        print(f"{'='*60}")
    
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

if __name__ == "__main__":
    main()