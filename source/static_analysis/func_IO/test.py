# @category: FHFuzz
# @author: FHFuzz
# @description: 获取具有特定参数模式的函数信息

from ghidra.app.decompiler import DecompInterface,DecompileOptions
from ghidra.util.task import ConsoleTaskMonitor
import os

def setup_decompiler():
    """
    设置并返回反编译器接口
    """
    decompiler = DecompInterface()
    decompiler.openProgram(getCurrentProgram())
    decompileOptions = DecompileOptions()
    decompileOptions.setProtoEvalModel("__stdcall")
    decompiler.setOptions(decompileOptions)
    return decompiler
def parse_function_params(param_str):
    """
    解析函数调用中的参数，处理嵌套括号的情况
    
    :param param_str: 参数字符串，如 "a, (void (*)(webs_t, char_t *, char_t *))func"
    :return: 参数列表 ["a", "func"]
    """
    params = []
    current_param = ""
    bracket_count = 0
    
    for char in param_str:
        if char == ',' and bracket_count == 0:
            # 找到一个顶层参数分隔符
            processed_param = process_param_value(current_param.strip())
            params.append(processed_param)
            current_param = ""
        else:
            # 处理括号嵌套
            if char == '(':
                bracket_count += 1
            elif char == ')':
                bracket_count -= 1
            current_param += char
    
    # 添加最后一个参数
    if current_param:
        processed_param = process_param_value(current_param.strip())
        params.append(processed_param)
    
    return params

def process_param_value(param):
    """
    处理参数值，提取真实函数名
    
    :param param: 原始参数字符串
    :return: 处理后的参数值
    """
    # 如果参数包含类型转换(有右括号)，则只保留最后一个右括号后的内容
    if ')' in param:
        parts = param.split(')')
        if len(parts) > 1:  # 确保有右括号后的内容
            return parts[-1].strip()
    
    return param

def decompiled_code(func, decompiler):
    """
    使用反编译器获取函数的C代码
    """
    results = decompiler.decompileFunction(func, 30, ConsoleTaskMonitor())
    if results is None or not results.decompileCompleted():
        return None
    return results.getDecompiledFunction().getC()

def extract_params(c_code):
    """
    从反编译代码中提取函数参数
    """
    if not c_code:
        return []

    # 获取函数定义行
    lines = c_code.splitlines()
    for line in lines:
        line = line.strip()
        # 跳过空行和警告
        if not line or line.startswith("/*"):
            continue
        
        # 查找包含左括号和右括号的行（函数定义行）
        if '(' in line and ')' in line:
            # 提取参数部分
            start = line.find('(') + 1
            end = line.find(')', start)
            if start <= 0 or end <= 0:
                continue
                
            param_str = line[start:end]
            # 对于空参数的情况
            if param_str.strip() == "void" or not param_str.strip():
                return []
                
            # 分割参数并清理
            params = param_str.split(',')
            return [param.strip() for param in params]
    
    return []

def get_retype(c_code):
    """
    从反编译代码中提取函数返回值类型
    """
    if not c_code:
        return None

    lines = c_code.splitlines()
    for line in lines:
        line = line.strip()
        # 可能会存在有WARNING，跳过就好了
        if not line or line.startswith("/* WARNING"):
            continue
        # 查找包含括号的有效函数定义行
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
    """
    统计函数的被调用次数
    """
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
    """
    检查参数是否符合要求：
    1. 有两个参数
    2. 同时包含字符串类型和函数指针(int)
    
    返回: (是否符合, 参数分类数组['string', 'function_ptr'])
    """
    if len(params) != 2:
        return False
    
    flag=0
    
    if 'char *' in params[0] or 'undefined4' in params[0].lower():
        flag+=1
    if 'int' in params[1].lower() or 'void' in params[1].lower() or 'undefined4' in params[1].lower():
        flag+=1
    return (flag == 2)
    
def analyze_function_params(program, decompiler):
    """
    分析所有函数的参数信息，筛选符合条件的函数
    
    :param program: 当前程序
    :param decompiler: 反编译器接口
    :return: 匹配的函数列表，每个函数包含名称、地址、参数、调用次数和返回值类型
    """
    listing = program.getListing()
    functions = listing.getFunctions(True)
    
    # 用于存储匹配的函数信息
    matched_functions = []
    
        
    # 遍历所有函数
    function_count = 0
    matched_count = 0
    for func in functions:
        function_count += 1
        name = func.getName()
        address = func.getEntryPoint()
        
        try:
            # 反编译函数
            code = decompiled_code(func, decompiler)
            params = extract_params(code)
            print(f"分析函数: {name} ({address})")
            if params:
                print(f"  函数参数: {params}")
            # 检查参数模式
            is_matched= check_params_pattern(params)
            if is_matched:
                matched_count += 1
                
                # 获取函数被调用次数
                call_count = count_calls(func, program)
                
                # 获取函数返回值类型
                return_type = get_retype(code)
                if return_type is None:
                    return_type = "unknown"
                
                
                # 添加到匹配函数列表
                matched_functions.append({
                    "name": name,
                    "address": address,
                    "params": params,
                    "call_count": call_count,
                    "return_type": return_type
                })
            
        except Exception as e:
            print(f"处理函数 {name} 时出错: {str(e)}")
        
        # 每处理100个函数打印一次进度
        if function_count % 100 == 0:
            print(f"已处理 {function_count} 个函数，找到 {matched_count} 个匹配函数...")
    # 处理完所有函数后，按调用次数排序        
    matched_functions.sort(key=lambda x: x["call_count"], reverse=True)
    print(f"分析完成，共处理了 {function_count} 个函数，找到 {matched_count} 个匹配函数")
    return matched_functions
def get_caller_func(func_addr, program):
    ref_manager = program.getReferenceManager()
    refs = ref_manager.getReferencesTo(func_addr)
    
    # 用于存储调用点和第二个参数值
    caller_funcs = {}
    
    # 遍历所有调用点
    for ref in refs:
        if not ref.getReferenceType().isCall():
            continue
            
        # 获取调用地址
        call_addr = ref.getFromAddress()
        
        # 获取调用者函数
        caller_func = program.getFunctionManager().getFunctionContaining(call_addr)
        if not caller_func:
            continue
            
        caller_name = caller_func.getName()
        
        # 去重调用函数
        if caller_name not in caller_funcs:
            caller_funcs[caller_name] = {
                "func": caller_func,
                "calls": []
            }
        
        caller_funcs[caller_name]["calls"].append(call_addr)
    return caller_funcs
def analyze_top_functions(matched_functions, program, decompiler):
    """
    分析排名靠前的函数
    
    :param matched_functions: 匹配的函数列表
    :param program: 当前程序
    :param decompiler: 反编译器接口
    :return: 筛选后的函数列表，每个函数包含被调用信息和第二个参数函数指针列表
    """    
    # 用于存储分析结果
    filtered_functions = {}
    
    for idx, func_info in enumerate(matched_functions):
        func_name = func_info["name"]
        func_addr = func_info["address"]
        print(f"\n[{idx+1}/{int(len(matched_functions))}] 分析函数: {func_name} ({func_addr})")
        
        # 获取调用该函数的所有调用点

        caller_funcs = get_caller_func(func_addr, program)                
        print(f"  共有 {len(caller_funcs)} 个唯一调用函数")
        
        # 标记该函数是否可能是处理程序注册函数
        is_handler_register_func = True
        all_second_params = []  # 所有发现的第二个参数
        second_param_functions = {}  # 存储第二个参数到函数映射
        has_duplicate_param = False  # 标记是否在同一个调用函数中发现重复参数
        # 分析每个调用函数的伪代码
        for caller_name, caller_info in caller_funcs.items():
            caller_func = caller_info["func"]
            call_addrs = caller_info["calls"]
            
            if has_duplicate_param :
                break
            # 反编译调用者函数
            caller_code = decompiled_code(caller_func, decompiler)
            if not caller_code:
                print(f"  无法反编译调用函数 {caller_name}")
                continue
                
            print(f"  分析调用函数: {caller_name}")
            
            # 对该调用函数中的参数进行统计
            param_values = []  # 这个调用者函数中的所有第二参数
            
            # 遍历该调用者函数中的所有调用点
            for line in caller_code.splitlines():
                line = line.strip()
                # 查找包含函数名的调用行
                if func_name in line and '(' in line and ');' in line:
                    # 找到函数名的位置
                    func_index = line.find(func_name)
                    # 找到调用开始的位置
                    start_idx = line.find('(', func_index)
                    if start_idx == -1:
                        continue
                        
                    # 找到调用结束的位置
                    end_idx = line.find(');', start_idx)
                    if end_idx == -1:
                        continue
                        
                    # 提取参数字符串
                    params_str = line[start_idx + 1:end_idx]
                    
                    # 解析参数
                    params = parse_function_params(params_str)
                        
                    # 获取第二个参数(如果存在)
                    if len(params) >= 2:
                        second_param = params[1]
                        print(f"  调用点发现第二个参数: {second_param}")
                        
                        # 检查在当前调用函数中是否已经有相同的参数
                        if second_param in param_values:
                            print(f"  ⚠️ 警告: 在同一个调用函数中发现重复的参数")
                            has_duplicate_param = True
                            is_handler_register_func = False
                            break
                        # 添加到参数列表
                        param_values.append(second_param)
                        
                        # 尝试识别函数指针
                        if second_param not in second_param_functions:
                            # 检查是否是已知函数名
                            func_mgr = program.getFunctionManager()
                            for f in func_mgr.getFunctions(True):
                                if f.getName() == second_param:
                                    second_param_functions[second_param] = {
                                        "name": second_param,
                                        "address": f.getEntryPoint()
                                    }
                                    print(f"  识别到函数指针: {second_param} -> {f.getEntryPoint()}")
                                    break
            
            # 调用函数分析完毕后，判断是否符合处理程序注册模式
            if param_values and not has_duplicate_param:
                print(f"  ✅ 调用函数 {caller_name} 中{func_name}第二个参数均不重复，可能是处理程序注册")
                all_second_params.extend(param_values)
            else:
                print(f"  ⚠️ 调用函数 {caller_name} 中{func_name}未找到有效参数")
        
        # 如果是处理程序注册函数，保存结果
        if is_handler_register_func and all_second_params:
            # 去重
            unique_second_params = list(set(all_second_params))
            print(f"  总共找到 {len(unique_second_params)} 个唯一的第二参数")
            
            filtered_functions[func_name] = {
                "name": func_name,
                "address": func_addr,
                "params": func_info["params"],
                "call_count": func_info["call_count"],
                "return_type": func_info["return_type"],
                "second_params": unique_second_params,
                "second_param_functions": second_param_functions,
                "param_count": len(unique_second_params)
            }
        else:
            print(f"  函数 {func_name} 不符合处理程序注册模式，跳过")
    
    print(f"\n分析完成，从 {int(len(matched_functions))} 个顶级函数中筛选出 {len(filtered_functions)} 个可能的处理程序注册函数")
    return filtered_functions
def analyze_data_section_pattern(program, start_addr_str=None, end_addr_str=None):
    """
    使用自适应滑动窗口算法分析.data段中的函数指针模式
    能够自动检测多种模式:
    1. 固定间隔模式(如每个指针间隔4字节)
    2. 复杂组合模式(如每组包含多个固定偏移的函数指针)
    
    :param program: 当前程序
    :param start_addr_str: 开始地址字符串，如'005785E8'，如果为None则分析整个.data段
    :param end_addr_str: 结束地址字符串，如'00578A3C'
    :return: 发现的模式列表
    """
    print("\n开始分析数据段中的函数指针模式...")
    
    # 获取程序管理器
    memory_manager = program.getMemory()
    function_manager = program.getFunctionManager()
    symbol_table = program.getSymbolTable()
    listing = program.getListing()
    
    # 获取地址范围
    addr_factory = program.getAddressFactory()
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
                break
        
        if data_block is None:
            print("未找到.data段，跳过分析")
            return []
        
        start_addr = data_block.getStart()
        end_addr = data_block.getEnd()
        print(f"分析.data段: {start_addr} - {end_addr}")
    
    # 使用指针大小作为基本步长
    ptr_size = program.getDefaultPointerSize()
    
    # 配置模式检测参数
    min_pattern_repeat = 2     # 模式至少重复次数
    max_sequence_len = 10      # 最大序列长度考虑
    min_function_pointers = 3  # 最小函数指针数量才考虑为有效模式
    
    # 存储发现的模式
    discovered_patterns = []
    
    # 存储当前扫描到的值序列
    addr_value_sequence = []
    func_ptr_sequence = []   # 存储函数指针位置
    string_ptr_sequence = [] # 存储字符串指针位置
    
    # 检查是否是函数指针
    def is_function_pointer(addr_value):
        if addr_value == 0:
            return False
            
        try:
            ptr_addr = addr_factory.getAddress(f"0x{addr_value:08x}")
            func = function_manager.getFunctionAt(ptr_addr)
            return func is not None
        except:
            return False
    
    # 检查是否是字符串指针
    def is_string_pointer(addr_value):
        if addr_value == 0:
            return False
            
        try:
            ptr_addr = addr_factory.getAddress(f"0x{addr_value:08x}")
            data = listing.getDataAt(ptr_addr)
            if data and data.hasStringValue():
                return True
                
            # 检查内存中是否含有字符串特征
            memory_bytes = memory_manager.getBytes(ptr_addr, 30)
            if memory_bytes:
                byte_str = "".join([chr(b & 0xFF) for b in memory_bytes if 32 <= (b & 0xFF) <= 126])
                if len(byte_str) >= 4:
                    return True
        except:
            pass
            
        return False
    
    # 分析序列中的模式
    def analyze_sequence_pattern(sequence, offset_start):
        if len(sequence) < min_function_pointers:
            return None
            
        # 存储发现的模式
        patterns = []
        
        # 分析函数指针间的偏移规律
        for pattern_len in range(1, min(max_sequence_len, len(sequence) // 2 + 1)):
            # 尝试不同的模式长度
            matches = []
            
            # 将序列分组检查
            for i in range(0, len(sequence) - pattern_len, pattern_len):
                group1 = sequence[i:i+pattern_len]
                group2 = sequence[i+pattern_len:i+2*pattern_len]
                
                if len(group2) < pattern_len:
                    break
                
                # 比较两组间的偏移是否一致
                offsets1 = [group1[j+1] - group1[j] for j in range(len(group1)-1)]
                offsets2 = [group2[j+1] - group2[j] for j in range(len(group2)-1)]
                
                if offsets1 == offsets2:
                    matches.append((i, pattern_len))
            
            # 如果发现了足够的匹配，记录该模式
            if matches:
                base_offset = offset_start + ptr_size * sequence[0]
                pattern_offsets = [sequence[i+1] - sequence[i] for i in range(pattern_len-1)]
                
                # 计算模式重复次数
                repeat_count = len(sequence) // pattern_len
                # 修复：创建Address对象而不是整数
                addresses = []
                for i in sequence[:pattern_len*min(3, repeat_count)]:
                    addr_val = offset_start + ptr_size * i
                    addr_obj = addr_factory.getAddress(f"0x{addr_val:08x}")
                    addresses.append(addr_obj)
                patterns.append({
                    "pattern_len": pattern_len,
                    "base_offset": base_offset,
                    "pattern_offsets": pattern_offsets,
                    "repeat_count": repeat_count,
                    "addresses": addresses
                })
        
        # 如果发现多个模式，选择最长和重复最多的
        if patterns:
            # 按模式长度和重复次数排序
            patterns.sort(key=lambda x: (x["pattern_len"], x["repeat_count"]), reverse=True)
            return patterns[0]
        
        return None
    
    # 检测多元组模式
    def detect_multi_tuple_pattern():
        # 分析值序列中重复的模式
        if len(addr_value_sequence) < 8:  # 至少需要两组完整数据
            return None
            
        # 寻找模式长度
        for tuple_size in range(2, 8):  # 尝试2到8元组模式
            # 检查模式是否重复
            is_pattern = True
            pattern_values = []
            has_function_ptr = False
            # 检查首个模式
            for i in range(tuple_size):
                if i >= len(addr_value_sequence):
                    is_pattern = False
                    break
                    
                value = addr_value_sequence[i]
                if is_function_pointer(value):
                    pattern_values.append("F")  # 函数
                    has_function_ptr = True
                elif is_string_pointer(value):
                    pattern_values.append("S")  # 字符串
                else:
                    pattern_values.append("O")  # 其他
            
            if not is_pattern or not has_function_ptr:
                continue
                
            # 检查该模式是否在后续重复
            repeats = 0
            for j in range(1, len(addr_value_sequence) // tuple_size):
                curr_pattern = []
                has_function_ptr = False
                for i in range(tuple_size):
                    idx = j * tuple_size + i
                    if idx >= len(addr_value_sequence):
                        break
                        
                    value = addr_value_sequence[idx]
                    if is_function_pointer(value):
                        curr_pattern.append("F")
                        has_function_ptr = True
                    elif is_string_pointer(value):
                        curr_pattern.append("S")
                    else:
                        curr_pattern.append("O")
                
                if len(curr_pattern) == tuple_size and curr_pattern == pattern_values and has_function_ptr:
                    repeats += 1
                else:
                    break
            
            # 如果找到重复的模式
            if repeats >= 1:
                # 计算基础地址和模式细节
                base_addr = offset_start
                
                # 返回模式信息
                return {
                    "type": "multi_tuple",
                    "tuple_size": tuple_size,
                    "pattern": "".join(pattern_values),
                    "repeats": repeats + 1,
                    "base_address": base_addr
                }
                
        return None
    # 检测函数指针规律模式
    def detect_function_pointer_pattern():
        """
        专门检测函数指针出现的规律，忽略字符串指针
        能够识别固定间隔的函数指针模式，包括连续的函数指针和空值
        
        :return: 识别到的函数指针规律模式信息，如未识别到则返回None
        """
        if len(addr_value_sequence) < 6:  # 需要足够的数据来检测规律
            return None
        
        # 标记每个位置是否是函数指针或可能等价的空值
        is_func_ptr = []
        for value in addr_value_sequence:
            if is_function_pointer(value) or value == 0:  # 函数指针或空值
                is_func_ptr.append(1)
            else:
                is_func_ptr.append(0)
        
        # 查找可能的规律
        patterns = []
        
        # 尝试不同大小的元组（1-8个指针为一组）
        for group_size in range(1, 9):
            if len(is_func_ptr) < group_size * 2:  # 至少需要两组完整数据
                continue
                
            # 尝试不同的偏移起点
            for start_offset in range(group_size):
                # 检查是否在特定位置上总是出现函数指针
                position_patterns = []  # 记录每个位置是否总是函数指针
                
                # 检查每个位置
                for pos in range(group_size):
                    # 统计该位置上有多少函数指针
                    func_ptr_count = 0
                    sample_count = 0
                    
                    # 从起点开始，按组大小间隔检查
                    for i in range(start_offset + pos, len(is_func_ptr), group_size):
                        sample_count += 1
                        if is_func_ptr[i] == 1:
                            func_ptr_count += 1
                    
                    # 如果该位置上50%以上是函数指针，认为该位置是函数指针模式
                    if sample_count > 0 and func_ptr_count / sample_count >= 0.5:
                        position_patterns.append(1)
                    else:
                        position_patterns.append(0)
                
                # 如果存在函数指针模式
                if sum(position_patterns) > 0:
                    # 计算函数指针模式匹配的可靠性
                    reliability = 0
                    samples = 0
                    
                    # 检查每个组
                    for group_idx in range((len(is_func_ptr) - start_offset) // group_size):
                        group_start = start_offset + group_idx * group_size
                        group_end = min(group_start + group_size, len(is_func_ptr))
                        
                        # 检查该组中每个位置
                        for pos in range(group_size):
                            if group_start + pos >= group_end:
                                break
                                
                            samples += 1
                            # 如果该位置应该是函数指针，且实际是函数指针
                            if position_patterns[pos] == 1 and is_func_ptr[group_start + pos] == 1:
                                reliability += 1
                    
                    # 计算可靠性百分比
                    if samples > 0:
                        reliability_pct = reliability / samples * 100
                        
                        # 如果可靠性足够高且有足够的样本
                        if reliability_pct >= 70 and samples >= group_size * 2:
                            # 获取函数指针在组中的位置
                            func_positions = [i for i, val in enumerate(position_patterns) if val == 1]
                            
                            # 收集这些位置上的实际函数指针
                            func_ptrs = []
                            for group_idx in range(min(5, (len(is_func_ptr) - start_offset) // group_size)):
                                group_start = start_offset + group_idx * group_size
                                
                                for pos in func_positions:
                                    if group_start + pos < len(addr_value_sequence):
                                        value = addr_value_sequence[group_start + pos]
                                        if is_function_pointer(value):  # 只收集实际的函数指针，不包括空值
                                            try:
                                                ptr_addr = addr_factory.getAddress(f"0x{value:08x}")
                                                func = function_manager.getFunctionAt(ptr_addr)
                                                if func:
                                                    func_ptrs.append({
                                                        "group": group_idx,
                                                        "position": pos,
                                                        "value": value,
                                                        "address": ptr_addr,
                                                        "name": func.getName()
                                                    })
                                            except Exception as e:
                                                print(f"获取函数信息错误: {str(e)}")
                            
                            # 添加到候选模式
                            patterns.append({
                                "start_offset": start_offset,
                                "group_size": group_size,
                                "func_positions": func_positions,
                                "pattern_array": position_patterns,
                                "reliability": reliability_pct,
                                "samples": samples,
                                "function_pointers": func_ptrs
                            })
        
        # 如果找到了候选模式，选择最佳的一个
        if patterns:
            # 按组大小、可靠性和函数指针位置数排序
            patterns.sort(key=lambda x: (x["reliability"], len(x["func_positions"]), x["group_size"]), reverse=True)
            
            best_pattern = patterns[0]
            
            # 计算地址和输出格式
            base_address = offset_start + best_pattern["start_offset"] * ptr_size
            
            # 生成模式描述
            pattern_desc = ""
            for i, is_fp in enumerate(best_pattern["pattern_array"]):
                if is_fp:
                    pattern_desc += "F"
                else:
                    pattern_desc += "."
            
            return {
                "type": "function_pointer_rhythm",
                "group_size": best_pattern["group_size"],
                "group_bytes": best_pattern["group_size"] * ptr_size,
                "func_positions": best_pattern["func_positions"],
                "pattern_desc": pattern_desc,
                "base_address": base_address,
                "reliability": best_pattern["reliability"],
                "function_pointers": best_pattern["function_pointers"]
            }
        
        return None
    
    # 开始遍历地址范围
    addr = start_addr
    offset_start = addr.getOffset()
    
    # 存储模式识别的上下文
    window_size = 20  # 滑动窗口大小
    addr_value_sequence = []  # 存储连续读取的值
    func_ptr_indices = []     # 存储函数指针在序列中的索引
    string_ptr_indices = []   # 存储字符串指针在序列中的索引
    
    print("\n开始扫描地址...")
    while addr.compareTo(end_addr) < 0:
        try:
            # 读取当前地址的值
            value = memory_manager.getInt(addr)
            current_offset = (addr.getOffset() - offset_start) // ptr_size
            
            # 添加到序列
            addr_value_sequence.append(value)
            
            # 检查是否是函数指针
            if is_function_pointer(value):
                func_ptr_sequence.append(current_offset)
            
            # 检查是否是字符串指针
            if is_string_pointer(value):
                string_ptr_sequence.append(current_offset)
            
            # 如果窗口已满，进行模式分析
            if len(addr_value_sequence) >= window_size:
                # 分析函数指针序列中的模式
                print(f"\n函数指针序列: {func_ptr_sequence}")
                # func_pattern = analyze_sequence_pattern(func_ptr_sequence, offset_start)
                # if func_pattern:
                #     print(f"\n发现函数指针模式:")
                #     print(f"  基地址: {hex(func_pattern['base_offset'])}")
                #     print(f"  模式长度: {func_pattern['pattern_len']}")
                #     print(f"  偏移: {func_pattern['pattern_offsets']}")
                #     print(f"  重复次数: {func_pattern['repeat_count']}")
                #     print(f"  地址示例: {[hex(a.getOffset()) for a in func_pattern['addresses']]}")
                    
                #     discovered_patterns.append({
                #         "type": "function_pointer_pattern",
                #         "details": func_pattern,
                #         "start_addr": addr_factory.getAddress(hex(func_pattern['base_offset'])),
                #         "pattern_description": f"每组{func_pattern['pattern_len']}个函数指针，偏移模式: {func_pattern['pattern_offsets']}"
                #     })
                                
                # 分析多元组模式
                # multi_tuple_pattern = detect_multi_tuple_pattern()
                # if multi_tuple_pattern:
                #     print(f"\n发现多元组模式:")
                #     print(f"  类型: {multi_tuple_pattern['pattern']}")
                #     print(f"  元组大小: {multi_tuple_pattern['tuple_size']}")
                #     print(f"  重复次数: {multi_tuple_pattern['repeats']}")
                #     print(f"  基地址: {multi_tuple_pattern['base_address']}")
                    
                #     discovered_patterns.append({
                #         "type": "multi_tuple_pattern",
                #         "details": multi_tuple_pattern,
                #         "start_addr": addr_factory.getAddress(hex(multi_tuple_pattern['base_address'])),
                #         "pattern_description": f"{multi_tuple_pattern['tuple_size']}元组模式: {multi_tuple_pattern['pattern']}，重复{multi_tuple_pattern['repeats']}次"
                #     })
                # 新增：分析函数指针规律模式
                fp_rhythm_pattern = detect_function_pointer_pattern()
                if fp_rhythm_pattern:
                    print(f"\n发现函数指针规律模式:")
                    print(f"  组大小: {fp_rhythm_pattern['group_size']} 个指针 ({fp_rhythm_pattern['group_bytes']} 字节)")
                    print(f"  模式描述: {fp_rhythm_pattern['pattern_desc']}")
                    print(f"  函数指针位置: {fp_rhythm_pattern['func_positions']}")
                    print(f"  基地址: {hex(fp_rhythm_pattern['base_address'])}")
                    print(f"  可靠性: {fp_rhythm_pattern['reliability']:.1f}%")
                    
                    # 打印函数指针详情
                    if fp_rhythm_pattern.get("function_pointers"):
                        print("\n  函数指针详情:")
                        for i, func_ptr in enumerate(fp_rhythm_pattern["function_pointers"][:10]):  # 显示前10个
                            print(f"    #{i+1}: 组 {func_ptr['group']+1} 位置 {func_ptr['position']}: {func_ptr['name']} (地址: {func_ptr['address']})")
                        
                        if len(fp_rhythm_pattern["function_pointers"]) > 10:
                            print(f"    ...省略其余 {len(fp_rhythm_pattern['function_pointers']) - 10} 个函数指针...")
                    
                    discovered_patterns.append({
                        "type": "function_pointer_rhythm_pattern",
                        "details": fp_rhythm_pattern,
                        "start_addr": addr_factory.getAddress(hex(fp_rhythm_pattern['base_address'])),
                        "pattern_description": f"函数指针规律: 每组{fp_rhythm_pattern['group_size']}个指针，模式:{fp_rhythm_pattern['pattern_desc']}"
                    })
                # 保留最新的half_window_size个元素，滑动窗口
                half_window = window_size // 2
                addr_value_sequence = addr_value_sequence[half_window:]
                
                # 调整函数和字符串指针索引
                func_ptr_sequence = [i - half_window for i in func_ptr_sequence if i >= half_window]
                string_ptr_sequence = [i - half_window for i in string_ptr_sequence if i >= half_window]
                
                # 更新偏移起点
                offset_start += half_window * ptr_size
        except Exception as e:
            print(f"地址 {addr} 处理错误: {str(e)}")
        
        # 移动到下一个地址
        addr = addr.add(ptr_size)
    
    # 最后一个窗口的处理
    if addr_value_sequence:
        # 分析函数指针序列中的模式
        func_pattern = analyze_sequence_pattern(func_ptr_sequence, offset_start)
        if func_pattern:
            print(f"\n发现函数指针模式:")
            print(f"  基地址: {func_pattern['base_offset']}")
            print(f"  模式长度: {func_pattern['pattern_len']}")
            print(f"  偏移: {func_pattern['pattern_offsets']}")
            print(f"  重复次数: {func_pattern['repeat_count']}")
            
            discovered_patterns.append({
                "type": "function_pointer_pattern",
                "details": func_pattern,
                "start_addr": addr_factory.getAddress(hex(func_pattern['base_offset'])),
                "pattern_description": f"每组{func_pattern['pattern_len']}个函数指针，偏移模式: {func_pattern['pattern_offsets']}"
            })
    
    print(f"\n分析完成，发现 {len(discovered_patterns)} 个模式")
    
    # 合并重叠的模式
    if discovered_patterns:
        print("\n合并重叠模式...")
        merged_patterns = []
        discovered_patterns.sort(key=lambda x: x["start_addr"].getOffset())
        
        current = discovered_patterns[0]
        for i in range(1, len(discovered_patterns)):
            next_pattern = discovered_patterns[i]
            
            # 如果两个模式地址接近，合并它们
            if (next_pattern["start_addr"].getOffset() - 
                current["start_addr"].getOffset()) < window_size * ptr_size:
                # 保留更复杂的模式描述
                if "multi_tuple_pattern" in next_pattern["type"]:
                    current = next_pattern
                elif "string_function_alternating" in next_pattern["type"] and "function_pointer_pattern" in current["type"]:
                    current = next_pattern
            else:
                merged_patterns.append(current)
                current = next_pattern
        
        merged_patterns.append(current)
        
        print(f"合并后剩余 {len(merged_patterns)} 个独立模式")
        return merged_patterns
    
    return discovered_patterns
def print_data_range_formatted(program, start_addr_str, end_addr_str):
    """
    按Ghidra GUI格式打印指定地址范围内的数据内容
    
    :param program: 当前程序
    :param start_addr_str: 开始地址字符串，如'005785E8'
    :param end_addr_str: 结束地址字符串，如'00578A3C'
    """
    print(f"\n以Ghidra GUI格式打印地址范围 {start_addr_str}-{end_addr_str} 的内容...\n")
    
    # 获取程序管理器
    memory_manager = program.getMemory()
    function_manager = program.getFunctionManager()
    symbol_table = program.getSymbolTable()
    listing = program.getListing()
    reference_manager = program.getReferenceManager()
    
    # 创建地址对象
    addr_factory = program.getAddressFactory()
    start_addr = addr_factory.getAddress(start_addr_str)
    end_addr = addr_factory.getAddress(end_addr_str)
    
    if start_addr is None or end_addr is None:
        print("无效的地址范围")
        return
    
    # 确认地址范围是有效的
    if start_addr.compareTo(end_addr) >= 0:
        print("开始地址必须小于结束地址")
        return
    
    # 使用指针大小作为步长
    ptr_size = program.getDefaultPointerSize()
    
    # 逐地址读取
    addr = start_addr
    while addr.compareTo(end_addr) < 0:
        try:
            # 读取值
            value = memory_manager.getInt(addr)
            value_addr_str = f"0x{value:08x}"
            value_addr = addr_factory.getAddress(value_addr_str)
            
            # 获取指向该地址的引用
            refs_to = reference_manager.getReferencesTo(addr)
            xrefs = []
            for ref in refs_to:
                from_addr = ref.getFromAddress()
                # 检查是否来自函数
                func_containing = function_manager.getFunctionContaining(from_addr)
                if func_containing:
                    xrefs.append(f"{func_containing.getName()}:{from_addr}({ref.getReferenceType().getName()[0]})")
                else:
                    xrefs.append(f"{from_addr}(*)")
            
            # 获取该地址的符号
            symbols = symbol_table.getSymbols(addr)
            symbol_names = []
            for symbol in symbols:
                symbol_names.append(symbol.getName())
            
            # 获取该值指向的函数或符号
            target_func = function_manager.getFunctionAt(value_addr)
            target_symbols = symbol_table.getSymbols(value_addr)
            target_symbol_names = []
            for symbol in target_symbols:
                target_symbol_names.append(symbol.getName())
            
            # 打印地址、符号和XREF信息
            if symbol_names:
                for i, symbol_name in enumerate(symbol_names):
                    if i == 0:
                        print(f"{'':12} {symbol_name:45} XREF[{len(xrefs)}]: ", end="")
                        if xrefs:
                            print(f"{', '.join(xrefs[:3])}")
                            for j in range(3, len(xrefs), 3):
                                print(f"{'':61} {', '.join(xrefs[j:j+3])}")
                        else:
                            print()
                    else:
                        print(f"{'':12} {symbol_name:45}")
            
            # 打印地址和数据内容
            hex_bytes = " ".join([f"{memory_manager.getByte(addr.add(i)) & 0xff:02x}" for i in range(4)])
            
            # 确定数据类型描述
            data_type = "undefined4"
            if target_func:
                data_type = "addr"
            elif target_symbol_names:
                data_type = "addr"
            
            # 打印格式化的数据行
            print(f"{addr} {hex_bytes:12} {data_type:10} {value_addr_str:10}", end="")
            
            # 打印该地址指向的内容
            if target_func:
                print(f"{' ':27} = {target_func.getName()}")
            elif target_symbol_names:
                symbol_value = listing.getDataAt(value_addr)
                if symbol_value and symbol_value.getValue():
                    str_value = str(symbol_value.getValue())
                    print(f"{' ':27} = {str_value}")
                else:
                    print(f"{' ':27} -> {target_symbol_names[0]}")
            else:
                print()
                
        except Exception as e:
            print(f"{addr}: 读取错误 - {str(e)}")
        
        # 移动到下一个地址
        addr = addr.add(ptr_size)
def main():
    try:
        # 获取当前程序
        program = getCurrentProgram()
        
        # 设置反编译器
        decompiler = setup_decompiler()
        
        output_dir = os.getcwd()
        if getScriptArgs():
            args = getScriptArgs()
            if len(args) > 0:
                output_dir = args[0]
                print(f"从命令行获取输出目录: {output_dir}")
        # 创建输出目录
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, "filtered_functions.txt")
        os.makedirs(output_dir, exist_ok=True)
        pattern_file = os.path.join(output_dir, "pointer_patterns.txt")
        
        # 分析指针模式
        patterns = analyze_data_section_pattern(program, "00062cf0", "0006379f")
        # print_data_range_formatted(program, "005785E8", "00578A3C")
        # 分析函数参数
        # 保存处理程序表分析结果
        with open(pattern_file, "w") as f:
            f.write("# 数据段指针模式分析结果\n\n")
            
            for i, pattern in enumerate(patterns):
                f.write(f"## 模式 {i+1}\n")
                f.write(f"- 类型: {pattern['type']}\n")
                f.write(f"- 起始地址: {pattern['start_addr']}\n")
                f.write(f"- 描述: {pattern['pattern_description']}\n\n")
                
                # 根据不同模式类型输出详细信息
                if pattern['type'] == 'function_pointer_pattern':
                    details = pattern['details']
                    f.write(f"- 模式长度: {details['pattern_len']}\n")
                    f.write(f"- 偏移序列: {details['pattern_offsets']}\n")
                    f.write(f"- 重复次数: {details['repeat_count']}\n")
                    f.write(f"- 地址示例: {[hex(a.getOffset()) for a in details['addresses']]}\n")
                elif pattern['type'] == 'string_function_alternating':
                    details = pattern['details']
                    f.write(f"- 交替类型: {details['type']}\n")
                    f.write(f"- 条目对数: {details['pairs']}\n")
                elif pattern['type'] == 'multi_tuple_pattern':
                    details = pattern['details']
                    f.write(f"- 元组大小: {details['tuple_size']}\n")
                    f.write(f"- 模式组成: {details['pattern']}\n")
                    f.write(f"- 重复次数: {details['repeats']}\n")
                
                f.write("\n---\n\n")
                
        print(f"指针模式分析结果已保存到: {pattern_file}")
        
        # 也可以指定特定地址范围进行分析
        # specific_patterns = analyze_data_section_pattern(program, "005785E8", "00578A3C")
        # print(f"\n在指定范围内发现 {len(specific_patterns)} 个模式")

        
    except Exception as e:
        print(f"错误: {str(e)}")

# 执行主函数
if __name__ == "__main__":
    main()
else:
    main()