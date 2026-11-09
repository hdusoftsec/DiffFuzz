import angr
import claripy
import logging
import archinfo
import summary_func
# 配置日志级别
logging.getLogger('angr').setLevel(logging.ERROR)

# **存储 `websGetVar` 获取的变量及其污点信息**
global_var_symbols = {}
critical_variables = set()  # 存储关键变量
tainted_addresses = set()  # 存储已被污染的内存地址
taint_propagation_paths = []  # 存储污点传播路径
global_constraint_solutions = []
memory_offset_counter = 0
arch_mips32 = archinfo.ArchMIPS32()  # 创建MIPS32架构实例
arch_armel = archinfo.ArchARMEL()    # 创建ARMEL架构实例
global taint_flag,tmp_state
# **加载二进制程序**
project = angr.Project("/root/func_fuzz/auto_hook/Tenda/AC6/squashfs-root/bin/httpd", arch='mipsel', auto_load_libs=False,use_sim_procedures=True)

# **自动获取 websGetVar 和 formSetCfm 地址**
websGetVar_symbol = project.loader.find_symbol("websGetVar")
formSetCfm_symbol = project.loader.find_symbol("GetParentControlInfo")
websGetVarWithValidate_symbol = project.loader.find_symbol("websGetVarWithValidate")

if websGetVar_symbol:
    websGetVar_addr = websGetVar_symbol.rebased_addr
    print(f"[INFO] Found websGetVar at {hex(websGetVar_addr)}")
else:
    print("[ERROR] Could not find websGetVar symbol!")
    exit()

if formSetCfm_symbol:
    formSetCfm_addr = formSetCfm_symbol.rebased_addr
    print(f"[INFO] Found formSetCfm at {hex(formSetCfm_addr)}")
else:
    print("[ERROR] Could not find formSetCfm symbol!")
    exit()

if websGetVarWithValidate_symbol:
    websGetVarWithValidate_addr = websGetVarWithValidate_symbol.rebased_addr
    print(f"[INFO] Found websGetVarWithValidate at {hex(websGetVarWithValidate_addr)}")
else:
    print("[ERROR] Could not find websGetVarWithValidate symbol!")
    exit()

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
            
    def _get_sym_val(self, name='x_', bits=None, inc=True, explicit=False):
        if bits is None:
            bits = self._p.arch.bits

        if explicit:
            var = claripy.BVS(name=name, size=bits, explicit_name=True)
        else:
            var = claripy.BVS(name=(name + '_' + str(self._count_var) + '_' + str(self._p.arch.bits)), 
                            size=bits, explicit_name=True)
            if inc:
                self._count_var += 1
        return var
        
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
                
# **检查值是否被污染**
def check_taint(state, value, context=""):
    try:
        # 检查具体值
        if isinstance(value, (int, claripy.ast.BV)) and not state.solver.symbolic(value):
            concrete_val = state.solver.eval(value)
            mem_content_tmp=state.memory.load(concrete_val, 4)
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
            global taint_flag,tmp_state
            tmp_state=state.copy()
            taint_flag=False
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
            
            print(f"[函数调用] {safe_hex(pc)}: 即将调用 {target_name} ({safe_hex(target_addr)})")
            if target_name =="cJSON_CreateString":
                print(f"[DEBUG] 函数调用目标: {target_name} ({safe_hex(target_addr)})")
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
                taint_flag=True
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
                                concrete_solution_str = concrete_solution.decode('utf-8', 'ignore').rstrip('\x00')
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
    @staticmethod
    def hook_function_return(state):
        try:
            global taint_flag,tmp_state
            #if not taint_flag:
            #    return
            arch_name = project.arch.name
            reg_names = func_params_regs[arch_name]
            tainted_params = []
            call_reg_num=get_arity(project, tmp_state.history.addr)
            pc = tmp_state.addr
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
                except Exception as reg_error:
                    # 如果寄存器不存在，会捕获到异常
                    print(f"[DEBUG] 无法读取寄存器 {reg_name}: {reg_error}")
                    continue
            
            ret_value = state.solver.eval(state.regs.v0)
            is_tainted, varname = check_taint(state, ret_value, f"{safe_hex(state.addr)}: 函数返回")
            if is_tainted:
                print(f"[污点传播] {safe_hex(state.addr)}: 函数返回值 {safe_hex(ret_value)} 被 {varname} 污染")
        except Exception as e:
            print(f"[ERROR] 函数返回钩子出错: {e}")
# **创建符号执行状态**
print("[INFO] 开始符号执行...")
project.hook(websGetVar_addr, HookWebsGetVar())
project.hook(websGetVarWithValidate_addr, HookwebsGetVarWithValidate())
state = project.factory.call_state(formSetCfm_addr)
# 添加内存读写钩子
#state.inspect.b('mem_read', when=angr.BP_AFTER, action=MemoryReadWriteHooks.hook_memory_read)
#state.inspect.b('mem_write', when=angr.BP_AFTER, action=MemoryReadWriteHooks.hook_memory_write)
state.inspect.b('call', when=angr.BP_BEFORE, action=CallParamCheckHooks.hook_function_call)
#state.inspect.b('return', when=angr.BP_BEFORE, action=CallParamCheckHooks.hook_function_return)
simgr = project.factory.simgr(state)
#simgr.use_technique(angr.exploration_techniques.Threading(10))
simgr.use_technique(angr.exploration_techniques.Timeout(60))
# **逐步执行**
step_count = 0
max_steps = 200  # 增加步数上限以获得更完整的覆盖
max_active=100
concrete_values = {}
while simgr.active and step_count < max_steps:
    try:
        simgr.step()
        step_count += 1
        print(f"[STEP {step_count}] Active Paths: {len(simgr.active)}, Deadended: {len(simgr.deadended)}")
    except Exception as e:
        print(f"[ERROR] 符号执行步骤出错: {e}")
        break
tmp_active=simgr.active[:]
if hasattr(simgr, 'timeout'):
    # 将所有超时状态添加到列表中
    tmp_active.extend(simgr.timeout)
print("\n[INFO] 污点分析完成。")
# 使用最活跃的路径状态进行求解
final_state = tmp_active[0]
current_solution = {}

# 对所有符号变量进行约束求解
for varname, sym_var in global_var_symbols.items():
    try:
        if final_state.solver.satisfiable():
            concrete_solution = final_state.solver.eval(sym_var, cast_to=bytes)
            concrete_solution_str = concrete_solution.decode('utf-8', 'ignore').rstrip('\x00')
            current_solution[varname] = concrete_solution_str
            print(f"[约束解] 变量 {varname} = '{concrete_solution_str}'")
    except Exception as e:
        print(f"[错误] 求解变量 {varname} 时出错: {e}")
if current_solution and not any(s == current_solution for s in global_constraint_solutions):
    global_constraint_solutions.append(current_solution)
    print(f"[路径约束] 已保存新的完整约束解决方案 #{len(global_constraint_solutions)}")
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
