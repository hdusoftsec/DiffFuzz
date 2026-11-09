# @category: FHFuzz
# @author: FHFuzz
# @description: 获取注册的handler函数

from ghidra.app.decompiler import DecompInterface,DecompileOptions
from ghidra.util.task import ConsoleTaskMonitor
import os
import json

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

def collect_function_info(function_manager, reference_manager, addr_factory, func_name):
    """
    收集函数的详细信息，包括函数名、地址和内部子调用函数列表
    
    :param function_manager: Ghidra函数管理器
    :param reference_manager: Ghidra引用管理器
    :param addr_factory: Ghidra地址工厂
    :param func_name: 函数名
    :return: 函数信息字典
    """
    try:
        # 通过函数名查找函数
        func = None
        for f in function_manager.getFunctions(True):
            if f.getName() == func_name:
                func = f
                break
        
        if func is None:
            return {
                'name': func_name,
                'address': 'UNKNOWN',
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
        print(f"收集函数信息时出错 ({func_name}): {str(e)}")
        return {
            'name': func_name,
            'address': 'ERROR',
            'subcalls': [],
            'is_valid': False,
            'error': str(e)
        }

def collect_handler_functions_info(filtered_functions, function_manager, reference_manager, addr_factory):
    """
    从filtered_functions中收集所有handler函数的详细信息
    
    :param filtered_functions: analyze_top_functions返回的过滤函数字典
    :param function_manager: Ghidra函数管理器
    :param reference_manager: Ghidra引用管理器
    :param addr_factory: Ghidra地址工厂
    :return: handler函数详细信息列表
    """
    all_handler_functions = {}
    
    print(f"开始从 {len(filtered_functions)} 个注册函数中收集handler函数信息...")
    
    # 遍历所有过滤出的注册函数
    for register_func_name, register_func_info in filtered_functions.items():
        print(f"\n处理注册函数: {register_func_name}")
        
        # 获取该注册函数中的所有handler函数指针
        second_param_functions = register_func_info.get("second_param_functions", {})
        
        if not second_param_functions:
            print(f"  - 注册函数 {register_func_name} 中没有发现handler函数指针")
            continue
            
        print(f"  - 发现 {len(second_param_functions)} 个handler函数指针")
        
        # 遍历每个handler函数指针
        for handler_name, handler_basic_info in second_param_functions.items():
            print(f"    分析handler函数: {handler_name}")
            
            # 如果已经收集过这个函数，跳过
            if handler_name in all_handler_functions:
                print(f"      - 函数 {handler_name} 已经分析过，跳过")
                continue
            
            # 收集handler函数的详细信息
            handler_detail = collect_function_info(
                function_manager,
                reference_manager,
                addr_factory,
                handler_name
            )
            
            if handler_detail and handler_detail['is_valid']:
                all_handler_functions[handler_name] = handler_detail
                print(f"      - 地址: {handler_detail['address']}")
                print(f"      - 子调用数: {len(handler_detail['subcalls'])}")
            else:
                print(f"      - 函数无效或分析失败")
    
    print(f"\nhandler函数信息收集完成，共 {len(all_handler_functions)} 个有效handler函数")
    return all_handler_functions

def save_handler_functions_to_json(handler_functions_dict, output_file):
    """
    将handler函数信息保存为JSON格式
    
    :param handler_functions_dict: handler函数信息字典
    :param output_file: 输出JSON文件路径
    """
    print("保存handler函数信息到JSON文件...")
    
    # 转换为列表格式，只保留需要的字段
    handler_functions_list = []
    
    for handler_name, handler_info in handler_functions_dict.items():
        handler_functions_list.append({
            'name': handler_info['name'],
            'address': handler_info['address'],
            'subcalls': handler_info['subcalls']
        })
    
    # 按函数名排序
    handler_functions_list.sort(key=lambda x: x['name'])
    
    # 保存为JSON文件
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(handler_functions_list, f, indent=2, ensure_ascii=False)
        
        print(f"handler函数信息已保存为JSON格式: {output_file}")
        print(f"统计摘要:")
        print(f"  - 总handler函数数: {len(handler_functions_list)}")
        
        # 统计有子调用的函数
        functions_with_subcalls = [f for f in handler_functions_list if f['subcalls']]
        total_subcalls = sum(len(f['subcalls']) for f in handler_functions_list)
        
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
        is_handler_register_func = False
        all_second_params = []  # 所有发现的第二个参数
        second_param_functions = {}  # 存储第二个参数到函数映射
        function_ptr_count = 0  # 记录识别到的函数指针数量
        
        # 分析每个调用函数的伪代码
        for caller_name, caller_info in caller_funcs.items():
            caller_func = caller_info["func"]
            call_addrs = caller_info["calls"]
            
            # 反编译调用者函数
            caller_code = decompiled_code(caller_func, decompiler)
            if not caller_code:
                print(f"  无法反编译调用函数 {caller_name}")
                continue
                
            print(f"  分析调用函数: {caller_name}")
            
            # 对该调用函数中的参数进行统计
            param_values = []  # 这个调用者函数中的所有第二参数
            found_function_ptr = False  # 标记本函数中是否找到函数指针
            
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
                        # print(f"  调用点发现第二个参数: {second_param}")
                        
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
                                    print(f"  ✅ 识别到函数指针: {second_param} -> {f.getEntryPoint()}")
                                    found_function_ptr = True
                                    function_ptr_count += 1
                                    break
            
            # 调用函数分析完毕后，判断是否找到函数指针
            if found_function_ptr:
                print(f"  ✅ 调用函数 {caller_name} 中发现函数指针作为第二个参数")
                all_second_params.extend(param_values)
                is_handler_register_func = True
            else:
                print(f"  ⚠️ 调用函数 {caller_name} 中未识别到函数指针")
        
        # 如果是处理程序注册函数，保存结果
        if is_handler_register_func and function_ptr_count > 0:
            # 去重
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
    
    print(f"\n分析完成，从 {int(len(matched_functions))} 个顶级函数中筛选出 {len(filtered_functions)} 个可能的处理程序注册函数")
    return filtered_functions

def main():
    try:
        # 获取当前程序
        program = getCurrentProgram()
        function_manager = program.getFunctionManager()
        reference_manager = program.getReferenceManager()
        addr_factory = program.getAddressFactory()
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
        handler_json_file = os.path.join(output_dir, "handler_functions.json")
        # 分析函数参数
        matched_functions = analyze_function_params(program, decompiler)
        filtered_functions = analyze_top_functions(matched_functions, program, decompiler)
        
        # 从filtered_functions中收集handler函数信息
        if filtered_functions:
            print(f"\n开始统计handler函数...")
            handler_functions = collect_handler_functions_info(
                filtered_functions,
                function_manager,
                reference_manager,
                addr_factory
            )
            
            # 保存handler函数信息为JSON格式
            if handler_functions:
                save_handler_functions_to_json(handler_functions, handler_json_file)
            else:
                print("未发现任何有效的handler函数")
        else:
            print("未发现任何注册函数，无法提取handler函数")
        # 保存详细分析结果
        with open(output_file, "w") as f:
            f.write("# 详细分析结果\n\n")
            f.write("以下是可能的处理程序注册函数：\n\n")
            
            for func_name, func_info in filtered_functions.items():
                name = func_info["name"]
                address = func_info["address"]
                call_count = func_info["call_count"]
                return_type = func_info["return_type"]
                param_count = func_info.get("param_count", 0)
                
                f.write(f"## 函数: {name}\n")
                f.write(f"- 地址: {address}\n")
                f.write(f"- 参数: {', '.join(func_info['params'])}\n")
                f.write(f"- 被调用次数: {call_count}\n")
                f.write(f"- 返回类型: {return_type}\n")
                f.write(f"- 处理程序参数数量: {param_count}\n\n")
                
                # 添加第二个参数函数指针信息
                f.write("### 第二个参数函数指针:\n")
                if "second_params" in func_info:
                    all_params = func_info["second_params"]
                    f.write(f"- 所有第二个参数值: {', '.join(all_params)}\n\n")
                    
                    # 添加函数指针详细信息
                    if "second_param_functions" in func_info and func_info["second_param_functions"]:
                        f.write("#### 识别的函数指针:\n")
                        for param_name, func_ptr in func_info["second_param_functions"].items():
                            f.write(f"- {param_name}: {func_ptr['address']}\n")
                    else:
                        f.write("未识别到函数指针\n")
                else:
                    f.write("无法识别第二个参数\n")
                
                f.write("\n---\n\n")
        print(f"结果已保存到: {output_file}")
        
    except Exception as e:
        print(f"错误: {str(e)}")

# 执行主函数
if __name__ == "__main__":
    main()
else:
    main()