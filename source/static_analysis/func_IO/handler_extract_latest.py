# @category: FHFuzz
# @author: FHFuzz
# @description: 综合提取handler函数 - 从注册函数和数据段中识别handler函数

from ghidra.app.decompiler import DecompInterface, DecompileOptions
from ghidra.util.task import ConsoleTaskMonitor
import os
import traceback
import json

def setup_decompiler():
    """设置并返回反编译器接口"""
    decompiler = DecompInterface()
    decompiler.openProgram(getCurrentProgram())
    decompileOptions = DecompileOptions()
    decompileOptions.setProtoEvalModel("__stdcall")
    decompiler.setOptions(decompileOptions)
    return decompiler

def collect_function_info(function_manager, reference_manager, addr_factory, func_identifier):
    """
    收集函数的详细信息，包括函数名、地址和内部子调用函数列表
    
    :param function_manager: Ghidra函数管理器
    :param reference_manager: Ghidra引用管理器
    :param addr_factory: Ghidra地址工厂
    :param func_identifier: 函数标识符（可以是函数名或地址字符串）
    :return: 函数信息字典
    """
    try:
        func = None
        
        # 尝试按函数名查找
        if isinstance(func_identifier, str) and not func_identifier.startswith('0x'):
            for f in function_manager.getFunctions(True):
                if f.getName() == func_identifier:
                    func = f
                    break
        
        # 如果没找到，尝试按地址查找
        if func is None:
            try:
                if isinstance(func_identifier, str):
                    func_addr = addr_factory.getAddress(func_identifier.replace("0x", ""))
                else:
                    func_addr = func_identifier
                    
                if func_addr is not None:
                    func = function_manager.getFunctionAt(func_addr)
                    if func is None:
                        func = function_manager.getFunctionContaining(func_addr)
            except:
                pass
        
        if func is None:
            return {
                'name': f"UNKNOWN_FUNC_{func_identifier}",
                'address': str(func_identifier),
                'subcalls': [],
                'is_valid': False
            }
        
        # 基本函数信息
        func_info = {
            'name': func.getName(),
            'address': func.getEntryPoint().toString(),
            'subcalls': [],
            'is_valid': True
        }
        
        # 收集函数内部的子调用
        subcalls = []
        
        # 获取函数体范围
        func_body = func.getBody()
        
        # 遍历函数体中的所有引用
        for addr_range in func_body:
            current_addr = addr_range.getMinAddress()
            while current_addr.compareTo(addr_range.getMaxAddress()) <= 0:
                # 获取从当前地址发出的所有引用
                refs_from = reference_manager.getReferencesFrom(current_addr)
                
                for ref in refs_from:
                    ref_type = ref.getReferenceType()
                    
                    # 只关注函数调用引用
                    if ref_type.isCall():
                        target_addr = ref.getToAddress()
                        target_func = function_manager.getFunctionAt(target_addr)
                        
                        if target_func:
                            subcall_info = {
                                'name': target_func.getName(),
                                'address': target_addr.toString()
                            }
                            
                            # 避免重复添加同一个函数
                            if not any(sc['address'] == subcall_info['address'] for sc in subcalls):
                                subcalls.append(subcall_info)
                
                # 移动到下一个地址
                try:
                    current_addr = current_addr.next()
                except:
                    break
        
        func_info['subcalls'] = subcalls
        
        return func_info
        
    except Exception as e:
        print(f"收集函数信息时出错 ({func_identifier}): {str(e)}")
        return {
            'name': f"ERROR_FUNC_{func_identifier}",
            'address': str(func_identifier),
            'subcalls': [],
            'is_valid': False,
            'error': str(e)
        }

# ========== 注册函数相关代码 ==========

def parse_function_params(param_str):
    """解析函数调用中的参数，处理嵌套括号的情况"""
    params = []
    current_param = ""
    bracket_count = 0
    
    for char in param_str:
        if char == ',' and bracket_count == 0:
            processed_param = process_param_value(current_param.strip())
            params.append(processed_param)
            current_param = ""
        else:
            if char == '(':
                bracket_count += 1
            elif char == ')':
                bracket_count -= 1
            current_param += char
    
    if current_param:
        processed_param = process_param_value(current_param.strip())
        params.append(processed_param)
    
    return params

def process_param_value(param):
    """处理参数值，提取真实函数名"""
    if ')' in param:
        parts = param.split(')')
        if len(parts) > 1:
            return parts[-1].strip()
    return param

def decompiled_code(func, decompiler):
    """使用反编译器获取函数的C代码"""
    results = decompiler.decompileFunction(func, 30, ConsoleTaskMonitor())
    if results is None or not results.decompileCompleted():
        return None
    return results.getDecompiledFunction().getC()

def extract_params(c_code):
    """从反编译代码中提取函数参数"""
    if not c_code:
        return []

    lines = c_code.splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("/*"):
            continue
        
        if '(' in line and ')' in line:
            start = line.find('(') + 1
            end = line.find(')', start)
            if start <= 0 or end <= 0:
                continue
                
            param_str = line[start:end]
            if param_str.strip() == "void" or not param_str.strip():
                return []
                
            params = param_str.split(',')
            return [param.strip() for param in params]
    
    return []

def get_retype(c_code):
    """从反编译代码中提取函数返回值类型"""
    if not c_code:
        return None

    lines = c_code.splitlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("/* WARNING"):
            continue
        if '(' in line and ')' in line:
            func_def = line.split('(')[0].strip()
            if not func_def:
                continue
            parts = func_def.split()
            if len(parts) > 1:
                return " ".join(parts[:-1])
            elif len(parts) == 1:
                return parts[0]
    return None

def count_calls(func, program):
    """统计函数的被调用次数"""
    func_addr = func.getEntryPoint()
    ref_manager = program.getReferenceManager()
    ref_to_func = ref_manager.getReferencesTo(func_addr)

    call_count = 0
    for ref in ref_to_func:
        ref_type = ref.getReferenceType()
        if ref_type.isCall():
            call_count += 1

    return call_count

def check_params_pattern(params):
    """检查参数是否符合要求"""
    if len(params) != 2:
        return False
    
    flag = 0
    if 'char *' in params[0] or 'undefined4' in params[0].lower():
        flag += 1
    if 'int' in params[1].lower() or 'void' in params[1].lower() or 'undefined4' in params[1].lower() or 'char *' in params[1].lower():
        flag += 1
    return (flag == 2)

def analyze_function_params(program, decompiler):
    """分析所有函数的参数信息，筛选符合条件的函数"""
    listing = program.getListing()
    functions = listing.getFunctions(True)
    
    matched_functions = []
    
    function_count = 0
    matched_count = 0
    for func in functions:
        function_count += 1
        name = func.getName()
        address = func.getEntryPoint()
        
        try:
            code = decompiled_code(func, decompiler)
            params = extract_params(code)
            
            is_matched = check_params_pattern(params)
            if is_matched:
                matched_count += 1
                
                call_count = count_calls(func, program)
                return_type = get_retype(code)
                if return_type is None:
                    return_type = "unknown"
                
                matched_functions.append({
                    "name": name,
                    "address": address,
                    "params": params,
                    "call_count": call_count,
                    "return_type": return_type
                })
            
        except Exception as e:
            print(f"处理函数 {name} 时出错: {str(e)}")
        
        if function_count % 100 == 0:
            print(f"已处理 {function_count} 个函数，找到 {matched_count} 个匹配函数...")
    
    matched_functions.sort(key=lambda x: x["call_count"], reverse=True)
    print(f"分析完成，共处理了 {function_count} 个函数，找到 {matched_count} 个匹配函数")
    return matched_functions

def get_caller_func(func_addr, program):
    """获取调用指定函数的所有调用者函数"""
    ref_manager = program.getReferenceManager()
    refs = ref_manager.getReferencesTo(func_addr)
    
    caller_funcs = {}
    
    for ref in refs:
        if not ref.getReferenceType().isCall():
            continue
            
        call_addr = ref.getFromAddress()
        caller_func = program.getFunctionManager().getFunctionContaining(call_addr)
        if not caller_func:
            continue
            
        caller_name = caller_func.getName()
        
        if caller_name not in caller_funcs:
            caller_funcs[caller_name] = {
                "func": caller_func,
                "calls": []
            }
        
        caller_funcs[caller_name]["calls"].append(call_addr)
    return caller_funcs

def analyze_top_functions(matched_functions, program, decompiler):
    """分析排名靠前的函数，提取handler函数"""
    filtered_functions = {}
    save_flag=False
    for idx, func_info in enumerate(matched_functions):
        func_name = func_info["name"]
        func_addr = func_info["address"]
        print(f"\n[{idx+1}/{len(matched_functions)}] 分析函数: {func_name} ({func_addr})")
        
        caller_funcs = get_caller_func(func_addr, program)
        print(f"  共有 {len(caller_funcs)} 个唯一调用函数")
        
        is_handler_register_func = False
        all_second_params = []
        second_param_functions = {}
        function_ptr_count = 0
        
        for caller_name, caller_info in caller_funcs.items():
            caller_func = caller_info["func"]
            caller_code = decompiled_code(caller_func, decompiler)
            if not caller_code:
                print(f"  无法反编译调用函数 {caller_name}")
                continue
                
            print(f"  分析调用函数: {caller_name}")
            
            param_values = []
            found_function_ptr = False
            
            for line in caller_code.splitlines():
                line = line.strip()
                if func_name in line and '(' in line and ');' in line:
                    func_index = line.find(func_name)
                    start_idx = line.find('(', func_index)
                    if start_idx == -1:
                        continue
                        
                    end_idx = line.find(');', start_idx)
                    if end_idx == -1:
                        continue
                        
                    params_str = line[start_idx + 1:end_idx]
                    params = parse_function_params(params_str)
                        
                    if len(params) >= 2:
                        second_param_raw = params[1]
                        param_values.append(second_param_raw)
                        
                        # 规范化参数名，去除可能的'&'前缀和空格
                        second_param = second_param_raw.lstrip('&').strip()
                        
                        # 使用规范化后的名字作为初步检查的键
                        if second_param not in second_param_functions:
                            func_mgr = program.getFunctionManager()
                            addr_factory = program.getAddressFactory()
                            target_func = None
                            
                            # 1. 优先按函数名称查找
                            for f in func_mgr.getFunctions(True):
                                if f.getName() == second_param:
                                    target_func = f
                                    break
                            
                            # 如果按名称未找到，则尝试将其作为地址处理
                            if target_func is None:
                                addr_str = None
                                # 2. 检查是否为LAB_或FUN_格式
                                if second_param.startswith("LAB_") or second_param.startswith("FUN_"):
                                    addr_str = second_param.split('_')[-1]
                                # 3. 检查是否为十六进制地址字面量 (e.g., "0x428204")
                                elif second_param.startswith("0x"):
                                    addr_str = second_param[2:]
                                
                                if addr_str:
                                    try:
                                        func_addr = addr_factory.getAddress(addr_str)
                                        if func_addr:
                                            # 尝试获取函数，如果不存在...
                                            target_func = func_mgr.getFunctionAt(func_addr)
                                            if target_func is None:
                                                # ...则尝试在该地址创建函数
                                                print(f"  ℹ️ 地址 {func_addr} 处无函数，尝试创建...")
                                                from ghidra.app.cmd.function import CreateFunctionCmd
                                                create_cmd = CreateFunctionCmd(func_addr)
                                                if create_cmd.applyTo(program):
                                                    target_func = func_mgr.getFunctionAt(func_addr)
                                                    if target_func:
                                                        print(f"  ✓ 成功创建函数: {target_func.getName()} @ {func_addr}")
                                                        # 保存程序状态
                                                        save_flag=True
                                                    else:
                                                        print(f"  ✗ 创建函数后无法获取对象")
                                                else:
                                                    print(f"  ✗ 创建函数命令执行失败")
                                    except Exception as e:
                                        print(f"  解析或创建函数时出错 ({second_param}): {e}")

                            if target_func:
                                handler_name = target_func.getName()
                                handler_addr_str = target_func.getEntryPoint().toString()
                                
                                # 使用函数地址作为唯一的键，防止因命名不同导致重复
                                if handler_addr_str not in second_param_functions:
                                    second_param_functions[handler_addr_str] = {
                                        "name": handler_name,
                                        "address": target_func.getEntryPoint() # 存储地址对象
                                    }
                                    print(f"  ✅ 识别到函数指针: {handler_name} -> {handler_addr_str} (来自 '{second_param_raw}')")
                                    found_function_ptr = True
                                    function_ptr_count += 1
            
            if found_function_ptr:
                print(f"  ✅ 调用函数 {caller_name} 中发现函数指针作为第二个参数")
                all_second_params.extend(param_values)
                is_handler_register_func = True
            else:
                print(f"  ⚠️ 调用函数 {caller_name} 中未识别到函数指针")
        
        if is_handler_register_func and function_ptr_count > 0:
            unique_second_params = list(set(all_second_params))
            print(f"  总共找到 {function_ptr_count} 个作为第二参数的函数指针")
            
            filtered_functions[func_name] = {
                "name": func_name,
                "address": func_addr,
                "params": func_info["params"],
                "call_count": func_info["call_count"],
                "return_type": func_info["return_type"],
                "second_params": unique_second_params,
                "second_param_functions": second_param_functions,
                "function_ptr_count": function_ptr_count
            }
        else:
            print(f"  函数 {func_name} 未发现函数指针作为第二个参数，跳过")
    if save_flag:
        print("\n检测到程序数据库已更改，正在保存...")
        try:
            program.saveToOriginalDatabase(ConsoleTaskMonitor())
            print("✓ 程序状态已成功保存。")
        except Exception as e:
            print(f"⚠️ 保存程序状态时出错: {str(e)}")
    print(f"\n分析完成，从 {len(matched_functions)} 个顶级函数中筛选出 {len(filtered_functions)} 个可能的处理程序注册函数")
    return filtered_functions

def extract_handler_functions_from_registration(program, decompiler, function_manager, reference_manager, addr_factory):
    """从注册函数中提取handler函数"""
    print("\n=== 第一阶段：从注册函数中提取handler函数 ===")
    
    # 分析函数参数
    matched_functions = analyze_function_params(program, decompiler)
    filtered_functions = analyze_top_functions(matched_functions, program, decompiler)
    
    # 收集handler函数信息
    handler_functions = {}
    
    if filtered_functions:
        print(f"\n开始收集从注册函数中识别的handler函数...")
        
        for register_func_name, register_func_info in filtered_functions.items():
            print(f"\n处理注册函数: {register_func_name}")
            
            second_param_functions = register_func_info.get("second_param_functions", {})
            
            if not second_param_functions:
                print(f"  - 注册函数 {register_func_name} 中没有发现handler函数指针")
                continue
                
            print(f"  - 发现 {len(second_param_functions)} 个handler函数指针")
            
            for handler_name, handler_basic_info in second_param_functions.items():
                print(f"    分析handler函数: {handler_name}")
                
                if handler_name in handler_functions:
                    print(f"      - 函数 {handler_name} 已经分析过，跳过")
                    continue
                
                handler_detail = collect_function_info(
                    function_manager,
                    reference_manager,
                    addr_factory,
                    handler_name
                )
                
                if handler_detail and handler_detail['is_valid']:
                    handler_functions[handler_name] = handler_detail
                    print(f"      - 地址: {handler_detail['address']}")
                    print(f"      - 子调用数: {len(handler_detail['subcalls'])}")
                else:
                    print(f"      - 函数无效或分析失败")
    
    print(f"\n从注册函数中收集完成，共 {len(handler_functions)} 个有效handler函数")
    return handler_functions

# ========== 数据段相关代码 ==========

def detect_handler_tables(program, start_addr_str=None, end_addr_str=None):
    """识别数据段中的函数指针表"""
    print("\n=== 第二阶段：识别数据段中的函数指针表 ===")
    
    memory_manager = program.getMemory()
    function_manager = program.getFunctionManager()
    symbol_table = program.getSymbolTable()
    listing = program.getListing()
    addr_factory = program.getAddressFactory()
    reference_manager = program.getReferenceManager()
    
    # 获取地址范围
    if start_addr_str and end_addr_str:
        start_addr = addr_factory.getAddress(start_addr_str)
        end_addr = addr_factory.getAddress(end_addr_str)
        
        if start_addr is None or end_addr is None:
            print("无效的地址范围")
            return []
            
        if start_addr.compareTo(end_addr) >= 0:
            print("开始地址必须小于结束地址")
            return []
        
        print(f"分析指定地址范围: {start_addr} - {end_addr}")
    else:
        # 查找.data段
        data_block = None
        for block in memory_manager.getBlocks():
            if block.getName() == ".data":
                data_block = block
                start_addr = data_block.getStart()
                end_addr = data_block.getEnd()
                print(f"分析.data段: {start_addr} - {end_addr}")
                break
        
        if data_block is None:
            print("未找到.data段，跳过分析")
            print("未找到.data段，尝试分析所有段")
            # 分析所有段
            all_blocks = list(memory_manager.getBlocks())
            if not all_blocks:
                print("未找到任何内存段，跳过分析")
                return []
            # 取所有段的最小起始地址和最大结束地址
            start_addr = min((block.getStart() for block in all_blocks), key=lambda a: a.getOffset())
            end_addr = max((block.getEnd() for block in all_blocks), key=lambda a: a.getOffset())
            print(f"分析所有段: {start_addr} - {end_addr}")
        if data_block is not None:
            start_addr = data_block.getStart()
            end_addr = data_block.getEnd()
            print(f"分析.data段: {start_addr} - {end_addr}")
    
    # 使用指针大小作为基本步长
    ptr_size = program.getDefaultPointerSize()
    
    # 算法参数
    initial_window_size = 24
    min_pattern_len = 2
    max_pattern_len = 8
    min_repeats = 3
    min_func_ptrs = 1
    window_overlap = 8
    # 创建函数的辅助函数
    def create_function_at_address(addr):
        """在指定地址创建函数"""
        try:
            # 检查地址是否在可执行内存块中
            mem_block = memory_manager.getBlock(addr)
            if not mem_block or not mem_block.isExecute():
                print(f"    地址 {addr} 不在可执行内存中，无法创建函数")
                return None
            
            # 检查地址是否有指令
            code_unit = listing.getCodeUnitAt(addr)
            if not code_unit or not code_unit.isInstruction():
                print(f"    地址 {addr} 处没有指令，尝试反汇编")
                # 尝试在该地址进行反汇编
                from ghidra.app.cmd.disassemble import DisassembleCommand
                disassemble_cmd = DisassembleCommand(addr, None, True)
                if disassemble_cmd.applyTo(program):
                    print(f"    成功在地址 {addr} 进行反汇编")
                else:
                    print(f"    在地址 {addr} 反汇编失败")
                    return None
            
            # 创建函数
            from ghidra.app.cmd.function import CreateFunctionCmd
            create_func_cmd = CreateFunctionCmd(addr)
            if create_func_cmd.applyTo(program):
                new_func = function_manager.getFunctionAt(addr)
                if new_func:
                    print(f"    ✓ 成功创建函数: {new_func.getName()} @ {addr}")
                    
                    # 保存程序状态
                    try:
                        program.saveToOriginalDatabase(ConsoleTaskMonitor())
                        print(f"    ✓ 已保存程序状态")
                    except Exception as save_e:
                        print(f"    ⚠️ 保存程序状态时出错: {str(save_e)}")
                         
                    return new_func
                else:
                    print(f"    创建函数后无法获取函数对象")
                    return None
            else:
                print(f"    创建函数命令执行失败")
                return None
                
        except Exception as e:
            print(f"    创建函数时出错: {str(e)}")
            return None
        
    # 函数指针检测函数
    def is_function_pointer(value):
        if value == 0:
            return False
        
        try:
            addr = addr_factory.getAddress(f"0x{value:08x}")
            
            # 1. 检查是否有正式的函数定义
            existing_func = function_manager.getFunctionAt(addr)
            if existing_func is not None:
                return True
            # 2. 检查是否在某个函数内部    
            if function_manager.getFunctionContaining(addr) is not None:
                return True
            
            # 3. 检查符号表中的LAB、FUN、SUB标签
            symbols = symbol_table.getSymbols(addr)
            lab_symbol = None
            for symbol in symbols:
                name = symbol.getName()
                if (name.startswith("LAB_") or 
                    name.startswith("FUN_") or 
                    name.startswith("SUB_")):
                    lab_symbol = symbol
                    print(f"    发现符号标签: {name} @ {addr}")
                    
                    # 如果是LAB标签但没有函数，尝试创建函数
                    if name.startswith("LAB_") and existing_func is None:
                        print(f"    LAB标签 {name} 处无函数定义，尝试创建函数...")
                        created_func = create_function_at_address(addr)
                        if created_func:
                            return True
                        else:
                            # 即使创建函数失败，LAB标签仍然表示这是一个代码位置
                            print(f"    函数创建失败，但LAB标签仍视为有效代码地址")
                            return True
                    else:
                        return True
                   
            # 4. 检查是否在可执行内存段中且有代码
            mem_block = memory_manager.getBlock(addr)
            if mem_block and mem_block.isExecute():
                code_unit = listing.getCodeUnitAt(addr)
                if code_unit:
                    if code_unit.isInstruction():
                        # 如果有指令但没有函数，也尝试创建函数
                        if existing_func is None:
                            print(f"    地址 {addr} 有指令但无函数定义，尝试创建函数...")
                            created_func = create_function_at_address(addr)
                            if created_func:
                                return True
                        return True
                    
                    # 检查是否有到该地址的引用
                    refs_to = reference_manager.getReferencesTo(addr)
                    if refs_to.hasNext():
                        for ref in refs_to:
                            ref_type = ref.getReferenceType()
                            if (ref_type.isJump() or 
                                ref_type.isCall() or 
                                ref_type.isComputed()):
                                # 有引用到该地址，尝试创建函数
                                if existing_func is None:
                                    print(f"    地址 {addr} 有调用/跳转引用但无函数定义，尝试创建函数...")
                                    created_func = create_function_at_address(addr)
                                    if created_func:
                                        return True
                                return True
            
            # 5. 检查是否有引用指向该地址（可能是代码标签）
            references = reference_manager.getReferencesTo(addr)
            if references.hasNext():
                for reference in references:
                    ref_type = reference.getReferenceType()
                    if ref_type.isJump() or ref_type.isCall():
                        # 有调用或跳转引用，尝试创建函数
                        if existing_func is None:
                            print(f"    地址 {addr} 有调用/跳转引用但无函数定义，尝试创建函数...")
                            created_func = create_function_at_address(addr)
                            if created_func:
                                return True
                        return True
                        
        except Exception as e:
            print(f"函数指针检查错误: {str(e)}")
        
        return False
    
    # 字符串指针检测函数
    def is_string_pointer(value):
        if value == 0:
            return False
        try:
            ptr_addr = addr_factory.getAddress(f"0x{value:08x}")
            data = listing.getDataAt(ptr_addr)
            if data and data.hasStringValue():
                return True
            
            symbols = symbol_table.getSymbols(ptr_addr)
            for symbol in symbols:
                symbol_name = symbol.getName()
                if symbol_name.startswith("s_") or "str" in symbol_name.lower():
                    return True
                
            try:
                printable_count = 0
                for i in range(30):
                    byte_val = memory_manager.getByte(ptr_addr.add(i)) & 0xFF
                    if byte_val == 0:
                        if printable_count >= 4:
                            return True
                        break
                    
                    if 32 <= byte_val <= 126:
                        printable_count += 1
                    else:
                        break
                
                if printable_count >= 8:
                    return True
            except:
                pass
        except:
            pass
        return False
    
    # 读取内存区域
    def read_memory_region(start_addr, length):
        values = []
        types = []
        current_addr = start_addr
        
        for _ in range(length):
            if current_addr.compareTo(end_addr) >= 0:
                break
                
            try:
                value = memory_manager.getInt(current_addr)
                
                if value == 0:
                    type_code = 'Z'
                elif is_function_pointer(value):
                    type_code = 'F'
                elif is_string_pointer(value):
                    type_code = 'S'
                else:
                    type_code = 'D'
                
                values.append(value)
                types.append(type_code)
            except Exception as e:
                print(f"读取地址 {current_addr} 出错: {str(e)}")
                values.append(0)
                types.append('Z')
                
            current_addr = current_addr.add(ptr_size)
            
        return values, types, current_addr

    # 在给定的类型序列窗口中检测模式
    def detect_pattern_in_window(values, types, start_offset):
        detected_patterns = []
        processed_positions = set()
        
        for pattern_len in range(min_pattern_len, min(max_pattern_len, len(types) // 2) + 1):
            max_start = len(types) - pattern_len * min_repeats
            for start in range(max_start + 1):
                if start in processed_positions:
                    continue
                    
                candidate_pattern = types[start:start+pattern_len]
                
                func_ptr_count = candidate_pattern.count('F')
                if func_ptr_count < min_func_ptrs:
                    continue
                
                # 检查是否为更短模式的重复
                is_sub_pattern = False
                for shorter_len in range(1, pattern_len):
                    if pattern_len % shorter_len == 0:
                        repetitions = pattern_len // shorter_len
                        base_pattern = candidate_pattern[:shorter_len]
                        
                        is_repeat = True
                        for i in range(repetitions):
                            segment = candidate_pattern[i*shorter_len:(i+1)*shorter_len]
                            if segment != base_pattern:
                                is_repeat = False
                                break
                        
                        if is_repeat:
                            is_sub_pattern = True
                            break
                
                if is_sub_pattern:
                    continue
                    
                # 计算模式重复次数
                repeats = 1
                offset = start + pattern_len
                exact_matches = 1
                fuzzy_matches = 0
                
                while offset + pattern_len <= len(types):
                    next_segment = types[offset:offset+pattern_len]
                    
                    matches = True
                    segment_exact_match = True
                    
                    for i in range(pattern_len):
                        if i >= len(next_segment) or i >= len(candidate_pattern):
                            matches = False
                            break
                        
                        if next_segment[i] == candidate_pattern[i]:
                            continue
                        elif (next_segment[i] == 'Z' and candidate_pattern[i] in ['F', 'S']) or \
                            (candidate_pattern[i] == 'Z' and next_segment[i] in ['F', 'S']):
                            segment_exact_match = False
                            continue
                        else:
                            matches = False
                            break
                    
                    if matches:
                        repeats += 1
                        offset += pattern_len
                        if segment_exact_match:
                            exact_matches += 1
                        else:
                            fuzzy_matches += 1
                    else:
                        break
                
                if repeats >= min_repeats:
                    match_quality = float(exact_matches) / (exact_matches + fuzzy_matches) if repeats > 0 else 0
                    
                    if match_quality >= 0.6:
                        pattern_addr = addr_factory.getAddress(f"0x{(start_offset + start * ptr_size):08x}")
                        
                        detected_patterns.append({
                            'pattern_type': ''.join(candidate_pattern),
                            'length': pattern_len,
                            'start_index': start,
                            'start_addr': pattern_addr,
                            'repeats': repeats,
                            'match_quality': match_quality,
                            'exact_matches': exact_matches,
                            'fuzzy_matches': fuzzy_matches,
                            'func_ptr_positions': [i for i, t in enumerate(candidate_pattern) if t == 'F'],
                            'string_ptr_positions': [i for i, t in enumerate(candidate_pattern) if t == 'S'],
                            'values': values[start:start+pattern_len*repeats]
                        })
                        
                        for pos in range(start, start + pattern_len * repeats):
                            processed_positions.add(pos)
                        
                        print(f"识别到最小模式: {''.join(candidate_pattern)} (长度={pattern_len}, 重复={repeats}次)")
                        break
        
        if detected_patterns:
            detected_patterns.sort(key=lambda p: (p['length'], -p['match_quality'], -p['repeats']))
            
        return detected_patterns
    
    def extract_complete_table(pattern_info, start_addr):
        """根据识别的模式提取完整的表"""
        pattern_type = pattern_info['pattern_type']
        pattern_len = pattern_info['length']
        func_indices = pattern_info['func_ptr_positions']
        string_indices = pattern_info['string_ptr_positions']
        
        print(f"提取表: 起始地址={start_addr}, 模式={pattern_type}, 长度={pattern_len}")
        
        table_structure = {
            'entry_size': pattern_len,
            'func_positions': func_indices,
            'string_positions': string_indices,
            'pattern': pattern_type
        }
        
        table_entries = []
        entry_count = 0
        max_entries = 500
        
        current_addr = start_addr
        
        while entry_count < max_entries:
            try:
                entry_data = []
                entry_types = []
                valid_entry = True
                
                for i in range(pattern_len):
                    item_addr = current_addr.add(i * ptr_size)
                    if item_addr.compareTo(end_addr) >= 0:
                        valid_entry = False
                        break
                    
                    value = memory_manager.getInt(item_addr)
                    entry_data.append(value)
                    
                    if value == 0:
                        entry_types.append('Z')
                    elif is_function_pointer(value):
                        entry_types.append('F')
                    elif is_string_pointer(value):
                        entry_types.append('S')
                    else:
                        entry_types.append('D')
                
                if valid_entry:
                    for idx in func_indices:
                        if idx >= len(entry_types) or (entry_types[idx] != 'F' and entry_types[idx] != 'Z'):
                            valid_entry = False
                            break
                
                if not valid_entry:
                    break
                
                entry_funcs = []
                entry_strings = []
                
                for idx in func_indices:
                    if idx < len(entry_data):
                        func_value = entry_data[idx]
                        if func_value != 0:
                            func_addr = addr_factory.getAddress(f"0x{func_value:08x}")
                            
                            # 获取函数名称，优先使用符号表中的名称
                            func_name = None
                            
                            # 首先检查是否存在函数
                            func_obj = function_manager.getFunctionAt(func_addr)
                            
                            # 如果没有函数但有符号，尝试创建函数
                            if func_obj is None:
                                symbols = symbol_table.getSymbols(func_addr)
                                for symbol in symbols:
                                    symbol_name = symbol.getName()
                                    if (symbol_name.startswith("LAB_") or 
                                        symbol_name.startswith("FUN_") or 
                                        symbol_name.startswith("SUB_")):
                                        print(f"    发现符号 {symbol_name} 但无函数，尝试创建函数...")
                                        
                                        # 尝试创建函数
                                        try:
                                            mem_block = memory_manager.getBlock(func_addr)
                                            if mem_block and mem_block.isExecute():
                                                from ghidra.app.cmd.function import CreateFunctionCmd
                                                create_func_cmd = CreateFunctionCmd(func_addr)
                                                if create_func_cmd.applyTo(program):
                                                    func_obj = function_manager.getFunctionAt(func_addr)
                                                    if func_obj:
                                                        print(f"    ✓ 成功创建函数: {symbol_name}")
                                                        # 保存程序状态
                                                        try:
                                                            program.saveToOriginalDatabase(ConsoleTaskMonitor())
                                                        except:
                                                            pass
                                                    break
                                        except Exception as e:
                                            print(f"    创建函数失败: {str(e)}")
                                        break
                            
                            # 获取函数名称
                            if func_obj:
                                func_name = func_obj.getName()
                            else:
                                # 如果仍然没有函数对象，从符号表获取名称
                                symbols = symbol_table.getSymbols(func_addr)
                                for symbol in symbols:
                                    symbol_name = symbol.getName()
                                    if (symbol_name.startswith("FUN_") or 
                                        symbol_name.startswith("LAB_") or 
                                        symbol_name.startswith("SUB_")):
                                        func_name = symbol_name
                                        break
                                
                                # 如果还是没有名称，生成默认名称
                                if func_name is None:
                                    func_name = f"FUNC_{func_addr}"
                            
                            entry_funcs.append({
                                'address': f"0x{func_value:08x}",
                                'name': func_name
                            })
                
                for idx in string_indices:
                    if idx < len(entry_data):
                        str_value = entry_data[idx]
                        if str_value != 0:
                            str_addr = addr_factory.getAddress(f"0x{str_value:08x}")
                            data = listing.getDataAt(str_addr)
                            if data and data.hasStringValue():
                                entry_strings.append({
                                    'value': str(data.getValue()),
                                    'address': str_addr.toString()
                                })
                            else:
                                memory_bytes = bytearray()
                                for i in range(30):
                                    byte_val = memory_manager.getByte(str_addr.add(i)) & 0xFF
                                    memory_bytes.append(byte_val)
                                    if byte_val == 0:
                                        break
                                if memory_bytes:
                                    printable = ""
                                    for i in range(len(memory_bytes)):
                                        b = memory_bytes[i] & 0xFF
                                        if b == 0:
                                            break
                                        if 32 <= b <= 126:
                                            printable += chr(b)
                                    if len(printable) >= 2:
                                        entry_strings.append({
                                            'value': printable,
                                            'address': str_addr.toString()
                                        })
                
                entry = {
                    'address': current_addr.toString(),
                    'types': ''.join(entry_types),
                    'data': [f"0x{v:08x}" for v in entry_data],
                    'functions': entry_funcs,
                    'strings': entry_strings
                }
                table_entries.append(entry)
                
                current_addr = current_addr.add(pattern_len * ptr_size)
                entry_count += 1
                
            except Exception as e:
                print(f"提取表时出错: {str(e)}")
                break
        
        print(f"表提取完成，共 {entry_count} 个条目")
        
        return {
            'start_address': start_addr.toString(),
            'end_address': current_addr.toString(),
            'entry_count': entry_count,
            'structure': table_structure,
            'entries': table_entries
        }
    
    # 开始扫描
    discovered_tables = []
    processed_addrs = set()
    
    print("\n开始扫描数据段...")
    
    current_addr = start_addr
    
    while current_addr.compareTo(end_addr) < 0:
        window_values, window_types, _ = read_memory_region(current_addr, initial_window_size*2)
        
        if len(window_values) < min_pattern_len * min_repeats:
            break
            
        current_offset = current_addr.getOffset()
        patterns = detect_pattern_in_window(window_values, window_types, current_offset)
        
        found_pattern = False
        
        for pattern in patterns:
            if len(pattern['pattern_type']) < min_pattern_len:
                continue
            if pattern['pattern_type'].count('F') < min_func_ptrs:
                continue
            
            pattern_addr = pattern['start_addr']
            addr_str = pattern_addr.toString()
            
            if addr_str in processed_addrs:
                continue
                
            found_pattern = True
            processed_addrs.add(addr_str)
            
            table = extract_complete_table(pattern, pattern_addr)
            
            if table['entry_count'] >= min_repeats:
                print(f"发现函数指针表: {table['start_address']} - {table['end_address']}")
                print(f"  模式: {pattern['pattern_type']}, 条目数: {table['entry_count']}")
                
                # 生成表描述
                description = ""
                if pattern['pattern_type'] == "SF" or pattern['pattern_type'] == "FS":
                    description = "字符串-函数指针交替表"
                elif "F" in pattern['pattern_type'] and "S" in pattern['pattern_type']:
                    description = f"{len(pattern['pattern_type'])}元组结构表(含字符串和函数指针)"
                elif pattern['pattern_type'].count("F") > 1:
                    description = f"多函数指针表({pattern['pattern_type'].count('F')}个函数指针/条目)"
                else:
                    description = f"函数指针表(模式:{pattern['pattern_type']})"
                
                table['description'] = description
                discovered_tables.append(table)
                
                try:
                    end_addr_str = table['end_address']
                    next_addr = addr_factory.getAddress(end_addr_str)
                    if next_addr.compareTo(current_addr) > 0:
                        current_addr = next_addr
                        break
                except:
                    pass
        
        if not found_pattern:
            step_size = max(1, initial_window_size - window_overlap)
            current_addr = current_addr.add(step_size * ptr_size)
    
    if discovered_tables:
        print(f"\n在扫描范围内共发现 {len(discovered_tables)} 个候选表")
        
    return discovered_tables

def extract_handler_functions_from_data_segment(program, function_manager, reference_manager, addr_factory):
    """从数据段中提取handler函数"""
    print("\n开始从数据段中提取handler函数...")
    
    # 识别函数指针表
    all_tables = detect_handler_tables(program)
    
    if not all_tables:
        print("未在数据段中发现函数指针表")
        return {}
    
    # 收集所有唯一的函数地址
    unique_func_addresses = set()
    func_address_sources = {}  # 记录每个地址来源于哪些表
    for table_idx, table in enumerate(all_tables):
        print(f"\n扫描表 {table_idx + 1}: {table.get('description', '未命名表')}")
        print(f"  - 起始地址: {table.get('start_address', 'N/A')}")
        print(f"  - 条目数: {table.get('entry_count', 0)}")
        print(f"  - 模式: {table.get('structure', {}).get('pattern', 'N/A')}")
        
        func_count_in_table = 0
        valid_func_count = 0
        for entry_idx, entry in enumerate(table.get('entries', [])):
            entry_func_count = 0
            for func_info in entry.get('functions', []):
                func_addr = func_info['address']
                func_name = func_info['name']
                entry_func_count += 1
                func_count_in_table += 1
                
                # 验证函数是否真实存在
                try:
                    addr_obj = addr_factory.getAddress(func_addr.replace('0x', ''))
                    if addr_obj:
                        actual_func = function_manager.getFunctionAt(addr_obj)
                        if actual_func:
                            unique_func_addresses.add(func_addr)
                            valid_func_count += 1
                            
                            # 记录来源
                            if func_addr not in func_address_sources:
                                func_address_sources[func_addr] = []
                            func_address_sources[func_addr].append(f"表{table_idx + 1}条目{entry_idx + 1}")
                            
                            print(f"    ✓ 有效函数: {func_name} @ {func_addr}")
                        else:
                            print(f"    ✗ 无效函数: {func_name} @ {func_addr} (函数不存在)")
                    else:
                        print(f"    ✗ 无效地址: {func_addr}")
                except Exception as e:
                    print(f"    ✗ 地址解析错误: {func_addr} - {str(e)}")
            
            if entry_func_count > 0:
                print(f"  条目 {entry_idx + 1}: 发现 {entry_func_count} 个函数指针")
        
        print(f"  表 {table_idx + 1} 总计: {func_count_in_table} 个函数指针，{valid_func_count} 个有效")
    
    print(f"发现 {len(unique_func_addresses)} 个唯一函数地址")
    
    # 为每个唯一函数收集详细信息
    data_segment_functions = {}
    
    for i, func_addr in enumerate(unique_func_addresses):
        print(f"分析函数 {i+1}/{len(unique_func_addresses)}: {func_addr}")
        
        detailed_info = collect_function_info(
            function_manager,
            reference_manager,
            addr_factory,
            func_addr
        )
        
        if detailed_info and detailed_info['is_valid']:
            data_segment_functions[func_addr] = detailed_info
            print(f"  - 函数: {detailed_info['name']}")
            print(f"  - 子调用数: {len(detailed_info['subcalls'])}")
        else:
            print(f"  - 函数无效或分析失败")
    
    print(f"数据段函数信息收集完成，共 {len(data_segment_functions)} 个有效函数")
    return data_segment_functions

# ========== 合并和输出相关代码 ==========

def merge_handler_functions(registration_handlers, data_segment_handlers):
    """合并来自注册函数和数据段的handler函数"""
    print("\n=== 第三阶段：合并handler函数 ===")
    
    merged_functions = {}
    
    # 添加注册函数中的handler
    for func_name, func_info in registration_handlers.items():
        # 始终使用 func_info['address'] 作为键
        addr_key = func_info['address']
        merged_functions[addr_key] = {
            'name': func_info['name'],
            'address': func_info['address'],
            'subcalls': func_info['subcalls'],
            'source': 'registration'
        }
    
    # 添加数据段中的handler
    for func_addr, func_info in data_segment_handlers.items():
        # 同样，始终使用 func_info['address'] 作为键
        addr_key = func_info['address']
        if addr_key not in merged_functions:
            merged_functions[addr_key] = {
                'name': func_info['name'],
                'address': func_info['address'],
                'subcalls': func_info['subcalls'],
                'source': 'data_segment'
            }
        else:
            # 函数已存在，使用正确的键来更新来源信息
            merged_functions[addr_key]['source'] = 'both'
    
    print(f"合并完成:")
    print(f"  - 仅来自注册函数: {len([f for f in merged_functions.values() if f['source'] == 'registration'])}")
    print(f"  - 仅来自数据段: {len([f for f in merged_functions.values() if f['source'] == 'data_segment'])}")
    print(f"  - 同时来自两个来源: {len([f for f in merged_functions.values() if f['source'] == 'both'])}")
    print(f"  - 总计: {len(merged_functions)}")
    
    return merged_functions

def save_merged_functions_to_json(merged_functions, output_file):
    """将合并后的handler函数信息保存为JSON格式"""
    print("保存合并后的handler函数信息到JSON文件...")
    
    # 转换为列表格式，只保留需要的字段
    functions_list = []
    
    for func_addr, func_info in merged_functions.items():
        functions_list.append({
            'name': func_info['name'],
            'address': func_info['address'],
            'subcalls': func_info['subcalls']
        })
    
    # 按函数名排序
    functions_list.sort(key=lambda x: x['name'])
    
    # 保存为JSON文件
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(functions_list, f, indent=2, ensure_ascii=False)
        
        print(f"合并后的handler函数信息已保存为JSON格式: {output_file}")
        print(f"统计摘要:")
        print(f"  - 总handler函数数: {len(functions_list)}")
        
        # 统计有子调用的函数
        functions_with_subcalls = [f for f in functions_list if f['subcalls']]
        total_subcalls = sum(len(f['subcalls']) for f in functions_list)
        
        print(f"  - 有子调用的函数数: {len(functions_with_subcalls)}")
        print(f"  - 总子调用数: {total_subcalls}")
        
        # 打印子调用最多的前5个函数
        if functions_with_subcalls:
            functions_with_subcalls.sort(key=lambda x: len(x['subcalls']), reverse=True)
            print(f"\n子调用最多的前5个handler函数:")
            for i, func in enumerate(functions_with_subcalls[:5]):
                print(f"  {i+1}. {func['name']} - {len(func['subcalls'])} 个子调用")
        
    except Exception as e:
        print(f"保存JSON文件时出错: {str(e)}")

def save_detailed_analysis(registration_handlers, data_segment_handlers, merged_functions, output_file):
    """保存详细的分析结果"""
    try:
        with open(output_file, "w", encoding='utf-8') as f:
            f.write("# 综合Handler函数分析结果\n\n")
            
            # 统计信息
            f.write("## 统计摘要\n\n")
            f.write(f"- 从注册函数中识别的handler函数: {len(registration_handlers)}\n")
            f.write(f"- 从数据段中识别的handler函数: {len(data_segment_handlers)}\n")
            f.write(f"- 合并后的总handler函数数: {len(merged_functions)}\n")
            
            # 来源分析
            sources = {}
            for func_info in merged_functions.values():
                source = func_info['source']
                if source not in sources:
                    sources[source] = []
                sources[source].append(func_info['name'])
            
            f.write("\n## 来源分析\n\n")
            for source, funcs in sources.items():
                source_name = {
                    'registration': '仅来自注册函数',
                    'data_segment': '仅来自数据段',
                    'both': '同时来自两个来源'
                }.get(source, source)
                f.write(f"### {source_name} ({len(funcs)}个)\n\n")
                for func_name in sorted(funcs):
                    f.write(f"- {func_name}\n")
                f.write("\n")
            
            # 详细函数信息
            f.write("## 详细函数信息\n\n")
            
            sorted_functions = sorted(merged_functions.values(), key=lambda x: x['name'])
            for func_info in sorted_functions:
                f.write(f"### {func_info['name']}\n\n")
                f.write(f"- **地址**: {func_info['address']}\n")
                f.write(f"- **来源**: {func_info['source']}\n")
                f.write(f"- **子调用数**: {len(func_info['subcalls'])}\n")
                
                if func_info['subcalls']:
                    f.write(f"- **子调用函数**:\n")
                    for subcall in func_info['subcalls']:
                        f.write(f"  - `{subcall['name']}` @ {subcall['address']}\n")
                else:
                    f.write(f"- **子调用函数**: 无\n")
                
                f.write("\n")
        
        print(f"详细分析结果已保存到: {output_file}")
        
    except Exception as e:
        print(f"保存详细分析结果时出错: {str(e)}")

def main():
    try:
        # 获取当前程序
        program = getCurrentProgram()
        function_manager = program.getFunctionManager()
        reference_manager = program.getReferenceManager()
        addr_factory = program.getAddressFactory()
        
        # 设置反编译器
        decompiler = setup_decompiler()
        
        # 设置输出目录
        output_dir = os.getcwd()
        if getScriptArgs():
            args = getScriptArgs()
            if len(args) > 0:
                output_dir = args[0]
                print(f"从命令行获取输出目录: {output_dir}")
        
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        
        # 定义输出文件
        combined_json_file = os.path.join(output_dir, "combined_handler_functions.json")
        detailed_analysis_file = os.path.join(output_dir, "detailed_handler_analysis.md")
        
        print("=== 开始综合Handler函数提取 ===")
        
        # 第一阶段：从注册函数中提取handler函数
        registration_handlers = extract_handler_functions_from_registration(
            program, decompiler, function_manager, reference_manager, addr_factory
        )
        
        # 第二阶段：从数据段中提取handler函数
        data_segment_handlers = extract_handler_functions_from_data_segment(
            program, function_manager, reference_manager, addr_factory
        )
        
        # 第三阶段：合并结果
        merged_handlers = merge_handler_functions(registration_handlers, data_segment_handlers)
        
        # 保存结果
        if merged_handlers:
            save_merged_functions_to_json(merged_handlers, combined_json_file)
            save_detailed_analysis(registration_handlers, data_segment_handlers, merged_handlers, detailed_analysis_file)
        else:
            print("未发现任何handler函数")
        
        print("\n=== 综合Handler函数提取完成 ===")
        
    except Exception as e:
        print(f"错误: {str(e)}")
        traceback.print_exc()

# 执行主函数
if __name__ == "__main__":
    main()