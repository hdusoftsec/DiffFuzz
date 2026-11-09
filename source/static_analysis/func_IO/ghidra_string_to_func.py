# @category: FHFuzz
# @author: FHFuzz 
# @description: 通过字符串引用地址分析参数使用频率，统计函数调用次数

import json
import os
import sys
from ghidra.util.classfinder import ClassSearcher
from ghidra.app.plugin.core.analysis import ConstantPropagationAnalyzer
from ghidra.program.util import SymbolicPropogator, DefinedDataIterator
from ghidra.program.model.mem import MemoryAccessException
from ghidra.app.decompiler import DecompInterface, DecompileOptions
from collections import defaultdict, Counter
import re

# 全局变量
syms = {}
analyzer = None
decompiler = None

def setup_decompiler():
    """设置反编译器"""
    global decompiler
    if decompiler is None:
        decompiler = DecompInterface()
        options = DecompileOptions()
        decompiler.setOptions(options)
        decompiler.openProgram(getCurrentProgram())
    return decompiler

def find_prar_statistics_file(input_dir):
    """
    在输入目录中查找prar_statistics.json文件
    
    Args:
        input_dir: 输入目录路径
    
    Returns:
        prar_statistics.json文件的完整路径，如果找不到则返回None
    """
    # 首先在输入目录根目录查找
    expected_path = os.path.join(input_dir, "prar_statistics.json")
    
    if os.path.exists(expected_path):
        print(f"找到prar_statistics.json文件: {expected_path}")
        return expected_path
    else:
        print(f"未在根目录找到prar_statistics.json文件: {expected_path}")
        
        # 尝试递归搜索
        print("尝试在输入目录中递归搜索prar_statistics.json文件...")
        for root, dirs, files in os.walk(input_dir):
            if "prar_statistics.json" in files:
                found_path = os.path.join(root, "prar_statistics.json")
                print(f"在以下位置找到文件: {found_path}")
                return found_path
        
        return None
    
def load_prar_statistics(input_dir, target_program_name):
    """
    从输入目录中的JSON文件加载指定程序的参数统计信息
    
    Args:
        input_dir: 输入目录路径
        target_program_name: 目标程序名（如 httpd, rc, cli 等）
    
    Returns:
        tuple: (file_name, prar_names, bin_paths) 或 (None, [], [])
    """
    # 查找JSON文件
    json_file_path = find_prar_statistics_file(input_dir)
    
    if json_file_path is None:
        print(f"错误: 在输入目录 {input_dir} 中未找到 prar_statistics.json 文件")
        return None, [], []
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'bin_files' not in data:
            print("JSON文件中没有找到bin_files数据")
            return None, [], []
        
        # 查找指定的程序
        target_file_info = None
        for bin_file in data['bin_files']:
            file_name = bin_file.get('file_name', '')
            if file_name == target_program_name:
                target_file_info = bin_file
                break
        
        if target_file_info is None:
            print(f"错误: 在JSON文件中未找到程序 '{target_program_name}'")
            print("可用的程序名:")
            for bin_file in data['bin_files']:
                print(f"  - {bin_file.get('file_name', 'unknown')}")
            return None, [], []
        
        # 提取目标程序的信息
        file_name = target_file_info.get('file_name', 'unknown')
        prar_names = target_file_info.get('prar_names', [])
        bin_paths = target_file_info.get('bin_paths', [])
        
        print(f"成功加载程序信息:")
        print(f"  - 程序名: {file_name}")
        print(f"  - 二进制路径: {bin_paths}")
        print(f"  - 参数名数量: {len(prar_names)}")
        
        # 显示前10个参数名作为预览
        if prar_names:
            print(f"  - 参数名预览: {', '.join(prar_names[:10])}")
            if len(prar_names) > 10:
                print(f"    ... 还有 {len(prar_names) - 10} 个参数名")
        
        return file_name, prar_names, bin_paths
            
    except Exception as e:
        print(f"加载JSON文件失败: {e}")
        return None, [], []

def get_analyzer():
    """获取常量传播分析器"""
    global analyzer
    if analyzer is None:
        for a in ClassSearcher.getInstances(ConstantPropagationAnalyzer):
            if a.canAnalyze(getCurrentProgram()):
                analyzer = a
                break
    return analyzer

def get_calling_args(addr, pos):
    """获取函数调用的第pos个参数值 (参考ref2share的getCallingArgs)"""
    if not 0 <= pos <= 3:
        return None
        
    program = getCurrentProgram()
    arch = str(program.getLanguageID())
    
    if 'ARM' in arch:
        reg = program.getRegister('r%d' % pos)
    elif 'MIPS' in arch:
        # MIPS延迟槽处理
        next_inst = getInstructionAt(addr).getNext()
        if next_inst and len(next_inst.getPcode()):  # not NOP
            addr = addr.add(8)
        reg = program.getRegister('a%d' % pos)
    else:
        return None
    
    if reg is None:
        return None
    
    result = get_register(addr, reg)
    return result

def get_register(addr, reg):
    """获取寄存器值 (参考ref2share的getRegister)"""
    global analyzer, syms
    
    if analyzer is None:
        get_analyzer()
    
    if analyzer is None:
        return None

    program = getCurrentProgram()
    func = getFunctionContaining(addr)
    if func is None:
        return None

    # 使用缓存
    if func in syms:
        sym_eval = syms[func]
    else:
        sym_eval = SymbolicPropogator(program)
        sym_eval.setParamRefCheck(True)
        sym_eval.setReturnRefCheck(True)
        sym_eval.setStoredRefCheck(True)
        
        try:
            analyzer.flowConstants(program, func.getEntryPoint(), func.getBody(), sym_eval, getMonitor())
            syms[func] = sym_eval
        except Exception as e:
            print(f"符号传播分析失败: {e}")
            return None

    return sym_eval.getRegisterValue(addr, reg)

def get_str(addr):
    """从地址读取字符串 (参考ref2share的getStr)"""
    if addr is None:
        return None
        
    try:
        current_addr = addr
        result = ''
        
        while True:
            byte_val = getByte(current_addr) & 0xFF
            if byte_val == 0:  # 字符串结束
                break
            result += chr(byte_val)
            current_addr = current_addr.add(1)
            
            # 防止读取过长的字符串
            if len(result) > 1000:
                break
                
        return result if result else None
        
    except MemoryAccessException:
        return None

def get_str_arg(addr, arg_pos=0):
    """获取函数调用指定位置的字符串参数 (参考ref2share的getStrArg)"""
    reg_value = get_calling_args(addr, arg_pos)
    if reg_value is None:
        return None
    
    try:
        string_addr = toAddr(reg_value.getValue())
        result = get_str(string_addr)
        return result
    except Exception as e:
        return None

def get_callee(inst):
    """获取指令调用的目标函数 (参考ref2share的getCallee)"""
    callee = None
    
    if inst and len(inst.getPcode()):
        pcode_ops = inst.getPcode()
        
        if len(pcode_ops) > 0:
            last_pcode = pcode_ops[-1]
            
            if last_pcode.getMnemonic() == 'CALL':
                try:
                    # 获取调用目标
                    op_objects = inst.getOpObjects(0)
                    if len(op_objects) > 0:
                        target_addr = op_objects[0]
                        callee = getFunctionAt(target_addr)
                except Exception as e:
                    pass
                    
            elif last_pcode.getMnemonic() == 'CALLIND':
                try:
                    # 获取寄存器
                    op_objects = inst.getOpObjects(0)
                    if len(op_objects) > 0:
                        reg = op_objects[0]
                        reg_val = get_register(inst.getAddress(), reg)
                        if reg_val is not None:
                            target_addr = toAddr(reg_val.getValue())
                            callee = getFunctionAt(target_addr)
                except Exception as e:
                    pass
    
    return callee

def get_function_pseudocode(func, max_lines=None):
    """获取函数的伪代码（反编译结果）"""
    if func is None:
        return ""
    if is_external_function(func):
        return f"// 函数 {func.getName()} 是外部函数，无法反编译"
    try:
        decompiler = setup_decompiler()
        
        # 反编译函数
        result = decompiler.decompileFunction(func, 30, getMonitor())
        
        if result.decompileCompleted():
            c_code = result.getDecompiledFunction().getC()
            
            # 限制行数
            lines = c_code.split('\n')
            if len(lines) > max_lines:
                lines = lines[:max_lines]
                lines.append("... (代码被截断)")
            
            return '\n'.join(lines)
        else:
            return f"// 反编译失败: {result.getErrorMessage()}"
            
    except Exception as e:
        return f"// 反编译错误: {str(e)}"

def get_call_context_pseudocode(call_addr, context_lines=None):
    """获取函数调用上下文的伪代码"""
    try:
        call_inst = getInstructionAt(toAddr(call_addr))
        if call_inst is None:
            return ""
        
        # 获取包含此调用的函数
        containing_func = getFunctionContaining(call_inst.getAddress())
        if containing_func is None:
            return ""
        
        # 反编译整个函数
        decompiler = setup_decompiler()
        result = decompiler.decompileFunction(containing_func, 30, getMonitor())
        
        if result.decompileCompleted():
            c_code = result.getDecompiledFunction().getC()
            lines = c_code.split('\n')
            
            # 查找调用指令附近的代码
            # 这里简化处理，返回函数的一部分代码作为上下文
            if len(lines) > context_lines * 2:
                start_line = max(0, len(lines) // 2 - context_lines)
                end_line = min(len(lines), start_line + context_lines * 2)
                context_lines_list = lines[start_line:end_line]
                
                return f"// 调用地址: {call_addr}\n// 包含函数: {containing_func.getName()}\n" + '\n'.join(context_lines_list)
            else:
                return f"// 调用地址: {call_addr}\n// 包含函数: {containing_func.getName()}\n" + c_code
        else:
            return f"// 反编译失败: {result.getErrorMessage()}"
            
    except Exception as e:
        return f"// 获取调用上下文时出错: {str(e)}"

def is_external_function(func_obj):
    """
    判断函数是否为外部函数的更准确方法
    """
    if func_obj is None:
        return False
    
    try:
        # 方法1: 检查函数符号是否为外部
        symbol = func_obj.getSymbol()
        if symbol is not None and symbol.isExternal():
            return True
        
        # 方法2: 检查函数是否为外部函数
        if func_obj.isExternal():
            return True
            
        # 方法3: 检查函数是否在EXTERNAL内存块中
        program = func_obj.getProgram()
        memory = program.getMemory()
        func_addr = func_obj.getEntryPoint()
        
        # 获取函数所在的内存块
        memory_block = memory.getBlock(func_addr)
        if memory_block is not None:
            block_name = memory_block.getName().upper()
            # 检查是否在外部相关的内存块中
            if any(ext_name in block_name for ext_name in ['EXTERNAL', 'IMPORT', 'PLT', 'GOT']):
                return True
        
        # 方法4: 检查函数体是否为空或只包含跳转指令
        func_body = func_obj.getBody()
        if func_body is None or func_body.isEmpty():
            return True
            
        # 方法5: 检查是否为thunk函数（通常是对外部函数的包装）
        if func_obj.isThunk():
            return True
            
        return False
        
    except Exception as e:
        print(f"判断外部函数时出错: {e}")
        return False
    
def build_string_map(program):
    """构建程序中所有已定义字符串的映射"""
    print("正在构建字符串映射...")
    string_map = {}
    
    string_iterator = DefinedDataIterator.definedStrings(program)
    
    string_count = 0
    while string_iterator.hasNext():
        string_data = string_iterator.next()
        
        try:
            string_value = str(string_data.getValue())
            string_addr = string_data.getAddress()
            
            if string_value not in string_map:
                string_map[string_value] = []
            
            string_map[string_value].append({
                'address': string_addr,
                'data': string_data
            })
            
            string_count += 1
            
            if string_count % 1000 == 0:
                print(f"已处理 {string_count} 个字符串...")
                
        except Exception as e:
            continue
    
    print(f"字符串映射构建完成，共找到 {len(string_map)} 个不同的字符串")
    return string_map

def search_from_string_reference(ref_addr, target_string, max_search_distance=30):
    """从字符串引用地址开始搜索函数调用 (参考ref2share的searchParam方式)"""
    results = []
    
    # 获取包含引用地址的函数
    containing_func = getFunctionContaining(ref_addr)
    if containing_func is None:
        return results
    
    func_start = containing_func.getEntryPoint()
    func_end = containing_func.getBody().getMaxAddress()
    
    # 从引用地址开始向前搜索函数调用
    current_addr = ref_addr
    search_count = 0
    
    while current_addr is not None and current_addr.compareTo(func_end) <= 0 and search_count < max_search_distance:
        inst = getInstructionAt(current_addr)
        if inst is None:
            break
        
        callee = get_callee(inst)
        if callee is not None:
            # 找到函数调用，检查所有参数位置
            for pos in range(4):  # 检查前4个参数
                str_arg = get_str_arg(inst.getAddress(), pos)
                
                if str_arg:
                    # 检查精确匹配
                    if str_arg == target_string:
                        results.append({
                            'match_type': 'exact',
                            'target_string': target_string,
                            'callee_name': callee.getName(),
                            'callee_function': callee,
                            'call_addr': str(inst.getAddress()),
                            'reference_addr': str(ref_addr),
                            'argument_position': pos,
                            'containing_function': containing_func.getName(),
                            'search_distance': search_count
                        })
                        # 找到精确匹配就可以返回
                        return results
                    
                    # 检查部分匹配
                    elif len(target_string) >= 3 and target_string in str_arg:
                        results.append({
                            'match_type': 'partial',
                            'target_string': target_string,
                            'full_string': str_arg,
                            'callee_name': callee.getName(),
                            'callee_function': callee,
                            'call_addr': str(inst.getAddress()),
                            'reference_addr': str(ref_addr),
                            'argument_position': pos,
                            'containing_function': containing_func.getName(),
                            'search_distance': search_count
                        })
        
        # 移动到下一条指令
        try:
            next_inst = inst.getNext()
            if next_inst is not None:
                current_addr = next_inst.getAddress()
            else:
                break
        except Exception as e:
            break
            
        search_count += 1
    
    return results

def find_string_references_and_analyze(target_strings, string_map, program):
    """查找字符串引用并分析使用模式 (参考ref2share的searchParam)"""
    reference_manager = program.getReferenceManager()
    
    # 全局函数使用统计
    global_function_counter = Counter()
    global_detailed_usage = defaultdict(list)
    
    processed_strings = 0
    total_matches = 0
    
    for target_string in target_strings:
        processed_strings += 1
        print(f"正在处理字符串: {target_string[:30]}... ({processed_strings}/{len(target_strings)})")
        
        # 跳过过短的字符串
        if len(target_string) < 3:
            continue
        
        string_matches = 0
        processed_refs = set()  # 避免重复处理相同的引用地址
        
        # 1. 查找精确匹配的字符串
        if target_string in string_map:
            for string_info in string_map[target_string]:
                str_addr = string_info['address']
                refs_to_string = reference_manager.getReferencesTo(str_addr)
                
                for ref in refs_to_string:
                    ref_addr = ref.getFromAddress()
                    
                    # 避免重复处理相同的引用地址
                    if ref_addr in processed_refs:
                        continue
                    processed_refs.add(ref_addr)
                    
                    print(f"  分析字符串 '{target_string}' 的引用地址: {ref_addr}")
                    
                    # 从引用地址开始搜索函数调用
                    usage_results = search_from_string_reference(ref_addr, target_string)
                    
                    for usage in usage_results:
                        callee_name = usage['callee_name']
                        global_function_counter[callee_name] += 1
                        global_detailed_usage[callee_name].append(usage)
                        string_matches += 1
                        total_matches += 1
        
        # 2. 查找部分匹配的字符串 (包含目标字符串的其他字符串)
        for string_value, string_infos in string_map.items():
            if target_string in string_value and target_string != string_value:
                for string_info in string_infos:
                    str_addr = string_info['address']
                    refs_to_string = reference_manager.getReferencesTo(str_addr)
                    
                    for ref in refs_to_string:
                        ref_addr = ref.getFromAddress()
                        
                        # 避免重复处理相同的引用地址
                        if ref_addr in processed_refs:
                            continue
                        processed_refs.add(ref_addr)
                        
                        print(f"  分析包含 '{target_string}' 的字符串 '{string_value[:30]}...' 的引用地址: {ref_addr}")
                        
                        # 从引用地址开始搜索函数调用
                        usage_results = search_from_string_reference(ref_addr, target_string)
                        
                        for usage in usage_results:
                            callee_name = usage['callee_name']
                            global_function_counter[callee_name] += 1
                            global_detailed_usage[callee_name].append(usage)
                            string_matches += 1
                            total_matches += 1
        
        print(f"  字符串 '{target_string}' 找到 {string_matches} 个匹配")
    
    print(f"\n总共找到 {total_matches} 个字符串使用实例")
    return global_function_counter, global_detailed_usage

def main():
    args = getScriptArgs()
    if len(args) < 3:
        print("用法: python ghidra_string_to_func.py <输入目录> <输出目录> <程序名>")
        print("例如: python ghidra_string_to_func.py /root/FHFuzz/dir825_analysis /root/output httpd")
        print("程序名可以是: httpd, rc, cli, hostapd, dcc, miniupnpd 等")
        return
    input_dir = args[0]
    output_dir = args[1] 
    target_program_name = args[2]
    # 输出目录
    print(f"输入目录: {input_dir}")
    print(f"输出目录: {output_dir}")
    print(f"目标程序: {target_program_name}")
    
    # 验证输入目录是否存在
    if not os.path.exists(input_dir):
        print(f"错误: 输入目录不存在: {input_dir}")
        return
    
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建输出目录: {output_dir}")
    
    # 设置输出文件路径
    output_file = os.path.join(output_dir, f"function_usage_statistics.md")
    json_output_file = os.path.join(output_dir, f"function_usage_analysis.json")
    
    # 获取当前程序
    program = getCurrentProgram()
    binary_name = program.getName()
    
    print(f"当前分析的二进制文件: {binary_name}")
    
    # 加载指定程序的参数统计信息
    file_name, prar_names, bin_paths = load_prar_statistics(input_dir, target_program_name)
    
    if not prar_names:
        print("没有找到参数名列表")
        return
    
    # 设置反编译器
    print("正在初始化反编译器...")
    setup_decompiler()
    
    # 构建字符串映射
    string_map = build_string_map(program)
    
    print(f"开始分析 {len(prar_names)} 个参数名的函数使用情况...")
    
    # 分析字符串使用模式
    function_counter, detailed_usage = find_string_references_and_analyze(
        prar_names, string_map, program
    )
    
    # 按使用频率排序
    sorted_functions = function_counter.most_common()
    
    # 构建JSON数据结构
    json_data = {
        "binary_name": binary_name,
        "analysis_summary": {
            "total_param_names": len(prar_names),
            "total_string_count": len(string_map),
            "functions_using_strings": len(sorted_functions),
            "total_string_usages": sum(function_counter.values())
        },
        "function_statistics": []
    }
    
    # 为每个统计到的函数添加详细信息
    for rank, (func_name, count) in enumerate(sorted_functions, 1):
        print(f"正在处理函数 {rank}/{len(sorted_functions)}: {func_name}")
        
        # 获取函数对象
        func_obj = None
        sample_usage = None
        
        if func_name in detailed_usage and detailed_usage[func_name]:
            # 获取第一个使用实例来获取函数对象
            sample_usage = detailed_usage[func_name][0]
            if 'callee_function' in sample_usage:
                func_obj = sample_usage['callee_function']
        
        # 如果没有找到函数对象，尝试通过名称查找
        if func_obj is None:
            func_manager = program.getFunctionManager()
            functions = func_manager.getFunctions(True)  # 获取所有函数
            for f in functions:
                if f.getName() == func_name:
                    func_obj = f
                    break
        
        # 获取函数伪代码
        function_pseudocode = ""
        if func_obj is not None:
            if is_external_function(func_obj):
                print(f"  函数 {func_name} 是外部函数，无法反编译")
                function_pseudocode = f"// 函数 {func_name} 是外部函数，无法反编译"
            else:
                print(f"  正在反编译函数: {func_name}")
                function_pseudocode = get_function_pseudocode(func_obj, max_lines=50)
        
        # 获取调用场景伪代码
        call_context_pseudocode = ""
        if sample_usage and 'call_addr' in sample_usage:
            print(f"  正在获取调用上下文伪代码")
            call_context_pseudocode = get_call_context_pseudocode(
                sample_usage['call_addr'], context_lines=15
            )
        
        # 统计精确和部分匹配
        exact_count = 0
        partial_count = 0
        usage_examples = []
        
        if func_name in detailed_usage:
            details = detailed_usage[func_name]
            exact_count = len([d for d in details if d['match_type'] == 'exact'])
            partial_count = len([d for d in details if d['match_type'] == 'partial'])
            
            # 取前5个使用实例作为例子
            for detail in details[:5]:
                usage_example = {
                    "match_type": detail['match_type'],
                    "target_string": detail['target_string'],
                    "call_address": detail['call_addr'],
                    "reference_address": detail['reference_addr'],
                    "argument_position": detail['argument_position'],
                    "containing_function": detail['containing_function'],
                    "search_distance": detail['search_distance']
                }
                
                if detail['match_type'] == 'partial':
                    usage_example["full_string"] = detail.get('full_string', '')
                
                usage_examples.append(usage_example)
        
        function_info = {
            "rank": rank,
            "function_name": func_name,
            "usage_count": count,
            "exact_matches": exact_count,
            "partial_matches": partial_count,
            "function_address": str(func_obj.getEntryPoint()) if func_obj else "unknown",
            "is_external": is_external_function(func_obj) if func_obj else False,
            "function_pseudocode": function_pseudocode,
            "sample_call_context_pseudocode": call_context_pseudocode,
            "usage_examples": usage_examples
        }
        
        json_data["function_statistics"].append(function_info)
    
    # 保存JSON文件
    with open(json_output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    
    # 保存分析结果 (原有的Markdown文件)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# 函数字符串参数使用统计报告\n\n")
        f.write(f"## 分析目标\n")
        f.write(f"- 二进制文件: {binary_name}\n")
        f.write(f"- 原始文件名: {file_name}\n")
        f.write(f"- 二进制路径: {', '.join(bin_paths)}\n")
        f.write(f"- 总参数名数量: {len(prar_names)}\n")
        f.write(f"- 程序中总字符串数量: {len(string_map)}\n")
        f.write(f"- 发现的使用函数数量: {len(sorted_functions)}\n\n")
        
        f.write(f"## 函数使用频率统计 (按使用次数降序排列)\n\n")
        f.write("| 排名 | 函数名 | 使用次数 | 精确匹配数 | 部分匹配数 |\n")
        f.write("|------|--------|----------|------------|------------|\n")
        
        for rank, (func_name, count) in enumerate(sorted_functions, 1):
            if func_name in detailed_usage:
                exact_count = len([d for d in detailed_usage[func_name] if d['match_type'] == 'exact'])
                partial_count = len([d for d in detailed_usage[func_name] if d['match_type'] == 'partial'])
            else:
                exact_count = partial_count = 0
            
            f.write(f"| {rank} | `{func_name}` | {count} | {exact_count} | {partial_count} |\n")
        
        f.write(f"\n## 详细使用信息 (Top 15)\n\n")
        
        # 显示前15个最常用的函数的详细信息
        for rank, (func_name, count) in enumerate(sorted_functions[:15], 1):
            f.write(f"### {rank}. 函数: `{func_name}` (使用次数: {count})\n\n")
            
            if func_name in detailed_usage:
                details = detailed_usage[func_name]
                
                # 按匹配类型分组
                exact_matches = [d for d in details if d['match_type'] == 'exact']
                partial_matches = [d for d in details if d['match_type'] == 'partial']
                
                if exact_matches:
                    f.write(f"#### 精确匹配 ({len(exact_matches)} 次)\n\n")
                    for detail in exact_matches[:5]:  # 最多显示5个实例
                        f.write(f"**字符串**: `{detail['target_string']}`\n")
                        f.write(f"- 调用地址: `{detail['call_addr']}`\n")
                        f.write(f"- 引用地址: `{detail['reference_addr']}`\n")
                        f.write(f"- 参数位置: {detail['argument_position']}\n")
                        f.write(f"- 包含函数: `{detail['containing_function']}`\n")
                        f.write(f"- 搜索距离: {detail['search_distance']} 条指令\n\n")
                
                if partial_matches:
                    f.write(f"#### 部分匹配 ({len(partial_matches)} 次)\n\n")
                    for detail in partial_matches[:5]:  # 最多显示5个实例
                        f.write(f"**目标子串**: `{detail['target_string']}`\n")
                        f.write(f"- 完整字符串: `{detail['full_string']}`\n")
                        f.write(f"- 调用地址: `{detail['call_addr']}`\n")
                        f.write(f"- 引用地址: `{detail['reference_addr']}`\n")
                        f.write(f"- 参数位置: {detail['argument_position']}\n")
                        f.write(f"- 包含函数: `{detail['containing_function']}`\n")
                        f.write(f"- 搜索距离: {detail['search_distance']} 条指令\n\n")
            
            f.write("---\n\n")
    
    # 控制台输出统计结果
    print(f"\n分析完成！")
    print(f"Markdown结果已保存到: {output_file}")
    print(f"JSON结果已保存到: {json_output_file}")
    print(f"\n=== 函数使用频率统计 (Top 20) ===")
    print(f"{'排名':<4} {'函数名':<30} {'使用次数':<8} {'精确匹配':<8} {'部分匹配':<8}")
    print("-" * 70)
    
    for rank, (func_name, count) in enumerate(sorted_functions[:20], 1):
        if func_name in detailed_usage:
            exact_count = len([d for d in detailed_usage[func_name] if d['match_type'] == 'exact'])
            partial_count = len([d for d in detailed_usage[func_name] if d['match_type'] == 'partial'])
        else:
            exact_count = partial_count = 0
        
        print(f"{rank:<4} {func_name:<30} {count:<8} {exact_count:<8} {partial_count:<8}")
    
    print(f"\n总统计:")
    print(f"- 二进制文件: {binary_name}")
    print(f"- 发现 {len(sorted_functions)} 个使用字符串参数的函数")
    print(f"- 总字符串使用数: {sum(function_counter.values())}")

if __name__ == "__main__":
    main()