#@category Analysis
import sys
import os
import json
from ghidra.app.plugin.core.analysis import ConstantPropagationAnalyzer
from ghidra.program.util import SymbolicPropogator
from ghidra.util.exception import CancelledException
from ghidra.util.task import TaskMonitor
from ghidra.util.classfinder import ClassSearcher
from ghidra.program.model.pcode import PcodeOp
from ghidra.app.decompiler import DecompInterface, DecompileOptions
from collections import defaultdict

def log(message):
    """将日志消息打印到控制台"""
    print(message)
monitor = getMonitor()
currentProgram = getCurrentProgram()
analyzer = None
syms = {}
decompiler=None

def setup_decompiler():
    """设置反编译器"""
    global decompiler
    if decompiler is None:
        decompiler = DecompInterface()
        options = DecompileOptions()
        decompiler.setOptions(options)
        decompiler.openProgram(currentProgram)
        log("反编译器初始化完成")
    return decompiler


def getAnalyzer():
    global analyzer
    for a in ClassSearcher.getInstances(ConstantPropagationAnalyzer):
        if a.canAnalyze(currentProgram):
            analyzer = a
            break
    else:
        assert 0
        
def getRegister(addr, reg):
    if analyzer is None:
        getAnalyzer()

    func = getFunctionContaining(addr)
    if func is None:
        return

    if func in syms:
        symEval = syms[func]
    else:
        symEval = SymbolicPropogator(currentProgram)
        symEval.setParamRefCheck(True)
        symEval.setReturnRefCheck(True)
        symEval.setStoredRefCheck(True)
        analyzer.flowConstants(currentProgram, func.getEntryPoint(), func.getBody(), symEval, monitor)
        syms[func] = symEval

    return symEval.getRegisterValue(addr, reg)

def getCallingArgs(addr, pos):
    if not 0 <= pos <= 3:
        return
    arch = str(currentProgram.language.processor)
    if arch == 'ARM':
        reg = currentProgram.getRegister('r%d' % pos)
    elif arch == 'MIPS':
        nextInst = getInstructionAt(addr).next
        if len(nextInst.pcode):  # not NOP
            addr = addr.add(8)
        reg = currentProgram.getRegister('a%d' % pos)
    else:
        return
    return getRegister(addr, reg)

def getCallee(inst):
    """
    获取调用指令的目标函数（适用于 CALL 和 CALLIND）
    """
    if inst is None or not inst.getPcode():
        return None

    last_pcode = inst.getPcode()[-1]  # 获取最后一个 PCode 操作

    # 直接调用 CALL func()
    if last_pcode.getMnemonic() == 'CALL':
        return getFunctionAt(inst.getOpObjects(0)[0])

    # 间接调用 CALLIND (如 MIPS `jalr t9`)
    elif last_pcode.getMnemonic() == 'CALLIND':
        regval = getRegister(inst.getAddress(), inst.getOpObjects(0)[0])
        if regval is not None:
            try:
                callee_addr = regval.getValue()  # 尝试获取值
            except AttributeError:
                callee_addr = regval.getScalar().getValue()  # 备用方法
            return getFunctionAt(toAddr(callee_addr))

    return None


def find_function_references(func_name):
    """
    查找所有调用指定函数的位置，并返回调用点信息
    """
    funcs = getGlobalFunctions(func_name)
    if not funcs:
        log(f"未找到函数 {func_name}。")
        return [], None
    
    target_func = funcs[0]
    entry = target_func.getEntryPoint()
    log(f"函数 {func_name} 位于地址: {entry}")
    
    ref_manager = currentProgram.getReferenceManager()
    refs = list(ref_manager.getReferencesTo(entry))
    
    log(f"共找到 {len(refs)} 个调用点")
    
    # 使用字典来整合同一函数内的多次调用
    caller_dict = {}
    
    for ref in refs:
        from_addr = ref.getFromAddress()
        call_inst = getInstructionAt(from_addr)
        caller_func = getFunctionContaining(from_addr)
        if caller_func:
            #log(f"调用自函数：{caller_func.getName()}，调用地址：{from_addr}，指令：{call_inst}")
            
            # 获取函数名作为键
            func_name = caller_func.getName()
            func_addr = caller_func.getEntryPoint()
            
            # 如果这个函数已经在字典中，追加调用地址
            if func_name in caller_dict:
                caller_dict[func_name]["call_sites"].append("0x"+str(from_addr))
            else:
                caller_dict[func_name] = {
                    "func": caller_func,
                    "call_sites": ["0x"+str(from_addr)]
                }
    
    # 将字典转换回列表格式
    call_sites = []
    for func_name, info in caller_dict.items():
        call_sites.append((info["func"], info["call_sites"]))
    
    return call_sites, target_func

def get_function_address(func_name):
    """
    获取函数的入口地址
    """
    funcs = getGlobalFunctions(func_name)
    if not funcs:
        log(f"未找到函数 {func_name}。")
        return None
    
    target_func = funcs[0]
    entry = target_func.getEntryPoint()
    return str(entry), target_func
def analyze_signature_for_param_count(signature_string):
    """
    分析 Ghidra 风格的函数签名字符串，返回参数的数量。

    例如:
    "undefined4 get_cgi(ACTION param_1);" -> 1
    "void my_func(int a, char* b, long c);" -> 3
    "int no_param_func(void);" -> 0
    "int empty_param_func();" -> 0

    Args:
        signature_string (str): Ghidra 函数签名字符串。

    Returns:
        int: 参数的数量。如果解析失败或格式不正确，则返回 -1。
    """
    if not isinstance(signature_string, str) or not signature_string:
        print("错误: 输入的签名不是有效的字符串。")
        return -1

    # 找到第一个开括号和最后一个闭括号
    start_paren = signature_string.find('(')
    end_paren = signature_string.rfind(')')

    if start_paren == -1 or end_paren == -1 or start_paren >= end_paren:
        print(f"错误: 签名 '{signature_string}' 格式不正确，未找到有效的括号对。")
        return -1

    # 提取括号内的参数部分
    params_part = signature_string[start_paren + 1:end_paren].strip()

    if not params_part:
        # 括号内为空，例如 "func();"
        return 0
    
    # 检查是否是 'void' 参数，例如 "func(void);"
    if params_part.lower() == "void":
        return 0

    # 按逗号分割参数
    parameters = params_part.split(',')

    # 过滤掉空的字符串（例如，如果有额外的逗号或空格）
    valid_params = [param.strip() for param in parameters if param.strip()]
    
    return len(valid_params)
def get_function_parameter_count(func):
    """
    获取函数的参数数量
    
    Args:
        func: Ghidra函数对象
    
    Returns:
        int: 参数数量，如果无法确定则返回-1
    """
    if func is None:
        return -1
    
    try:
        decompiler = setup_decompiler()
        result = decompiler.decompileFunction(func, 30, monitor)
        if result.decompileCompleted():
            decomp_func = result.getDecompiledFunction()
            signature = decomp_func.getSignature()
            print(f"分析函数 {func.getName()} 的签名: {signature}")
            param_count = analyze_signature_for_param_count(signature)
            return param_count
        else:
            param_count=func.getAutoParameterCount()
            print(f"  函数 {func.getName()} 的参数数量: {param_count}")
            return param_count
        
    except Exception as e:
        log(f"  获取函数参数数量时出错: {str(e)}")
        return -1

def read_combined_handler_functions(filename):
    """
    读取combined_handler_functions.json文件
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        log(f"读取combined_handler_functions.json失败: {str(e)}")
        return []

def read_extract_config(filename="extract_ac6.json"):
    """
    从配置文件中读取需要提取的函数
    """
    try:
        if os.path.isfile(filename):
            config_path = filename
        log(f"尝试读取配置文件: {config_path}")
        
        with open(config_path, "r") as f:
            config = json.load(f)
        
        # 兼容键名不同的情况
        if "extract_func" in config and "extract_funcs" not in config:
            config["extract_funcs"] = config["extract_func"]
        
        if "const_value_func" in config and "const_value_funcs" not in config:
            config["const_value_funcs"] = config["const_value_func"]
            
        if "remove_func" in config and "remove_funcs" not in config:
            config["remove_funcs"] = config["remove_func"]
            
        return config
    except Exception as e:
        log(f"读取配置文件失败: {str(e)}")
        # 默认配置
        return {"extract_funcs": ["websGetVar"], "remove_funcs": []}

def get_function_subcalls(func_name):
    """
    使用Ghidra获取函数的所有子调用
    """
    try:
        # 获取函数对象
        funcs = getGlobalFunctions(func_name)
        if not funcs:
            return []
        
        target_func = funcs[0]
        subcalls = []
        
        # 遍历函数体中的所有指令
        func_body = target_func.getBody()
        inst_iter = currentProgram.getListing().getInstructions(func_body, True)
        
        for inst in inst_iter:
            if monitor.isCancelled():
                break
                
            # 获取指令的所有引用
            refs = inst.getOperandReferences(0)
            for ref in refs:
                if ref.getReferenceType().isCall():
                    # 获取被调用的函数
                    called_addr = ref.getToAddress()
                    called_func = getFunctionAt(called_addr)
                    if called_func:
                        called_name = called_func.getName()
                        if called_name not in subcalls:
                            subcalls.append(called_name)
        
        return subcalls
        
    except Exception as e:
        log(f"获取函数 {func_name} 的子调用时出错: {str(e)}")
        return []


def build_call_tree(handler_data, max_depth=2):
    """
    构建调用树，向下查询指定深度的子函数
    第一层从handler_data获取，第二层使用Ghidra动态提取
    返回: {handler_name: {level1: [func_names], level2: [func_names]}}
    """
    call_tree = {}
    
    for handler in handler_data:
        handler_name = handler["name"]
        call_tree[handler_name] = {"level1": [], "level2": []}
        
        # 第一层：从handler_data中获取直接子函数
        level1_subcalls = []
        for subcall in handler.get("subcalls", []):
            # 检查subcall是否有name字段，如果没有则跳过
            if isinstance(subcall, dict) and "name" in subcall:
                subcall_name = subcall["name"]
                level1_subcalls.append(subcall_name)
            elif isinstance(subcall, dict) and "address" in subcall:
                # 如果只有地址，尝试通过地址获取函数名
                try:
                    addr = toAddr(subcall["address"])
                    func = getFunctionAt(addr)
                    if func:
                        subcall_name = func.getName()
                        level1_subcalls.append(subcall_name)
                except:
                    log(f"无法解析地址 {subcall.get('address', 'unknown')}")
                    continue
        
        call_tree[handler_name]["level1"] = level1_subcalls
        
        # 第二层：使用Ghidra动态提取子函数的子函数
        level2_subcalls = []
        for level1_func_name in level1_subcalls:
            if monitor.isCancelled():
                break
                
            # 使用Ghidra获取这个函数的子调用
            subcalls = get_function_subcalls(level1_func_name)
            for subcall_name in subcalls:
                if subcall_name not in level2_subcalls:
                    level2_subcalls.append(subcall_name)
        
        call_tree[handler_name]["level2"] = level2_subcalls
        
        log(f"Handler {handler_name}: 第1层 {len(level1_subcalls)} 个函数, 第2层 {len(level2_subcalls)} 个函数")
    
    return call_tree

def check_handler_needs_extraction(handler_name, call_tree, extract_funcs):
    """
    检查handler函数是否需要保留
    """
    if handler_name not in call_tree:
        return False
    
    # 检查第一层调用
    for func in call_tree[handler_name]["level1"]:
        if func in extract_funcs:
            return True
    
    # 检查第二层调用
    for func in call_tree[handler_name]["level2"]:
        if func in extract_funcs:
            return True
    
    return False

def find_handlers_with_extract_funcs(handler_data, extract_funcs):
    """
    找到需要保留的handler函数，无论在哪一层发现extract_func，都使用最顶层的handler
    返回按extract_func分组的结果
    """
    call_tree = build_call_tree(handler_data)
    log(f"构建了 {len(call_tree)} 个handler的调用树")
    
    # 按extract_func分组的结果
    extract_func_handlers = {}
    
    # 初始化每个extract_func的handler列表
    for extract_func in extract_funcs:
        extract_func_handlers[extract_func] = []
    
    # 找出所有涉及extract_func的handler，无论在哪一层都使用顶层handler
    for handler_name in call_tree:
        handler_extract_funcs = set()  # 该handler涉及的extract_func
        
        # 检查第一层调用
        for func in call_tree[handler_name]["level1"]:
            if func in extract_funcs:
                handler_extract_funcs.add(func)
        
        # 检查第二层调用
        for func in call_tree[handler_name]["level2"]:
            if func in extract_funcs:
                handler_extract_funcs.add(func)
        
        # 将该handler添加到所有相关的extract_func中
        for extract_func in handler_extract_funcs:
            extract_func_handlers[extract_func].append({
                "handler": handler_name,
                "call_tree": call_tree[handler_name]
            })
            log(f"Handler {handler_name} 涉及 extract_func: {extract_func}")
    
    return extract_func_handlers
            
def main():
    # 尝试获取Ghidra脚本参数
    output_dir = os.getcwd()
    if getScriptArgs():
        args = getScriptArgs()
        if len(args) > 0:
            config_filename = args[0]
            log(f"从命令行获取extract配置文件名: {config_filename}")
        if len(args) > 1:
            combined_handler_filename = args[1]
            log(f"从命令行获取handler函数文件名: {combined_handler_filename}")
        if len(args) > 2:
            output_dir = args[2]
            log(f"从命令行获取输出目录: {output_dir}")
    
    # 读取配置文件
    config = read_extract_config(config_filename)
    extract_funcs = config.get("extract_funcs", ["websGetVar"])
    const_value_funcs = config.get("const_value_funcs", [])
    remove_funcs = config.get("remove_funcs", [])
    
    handler_data = read_combined_handler_functions(combined_handler_filename)
    if not handler_data:
        log("未找到有效的handler函数数据，退出")
        return
    
    program_path=config.get("program_path", currentProgram.getExecutablePath())
    program_arch = str(currentProgram.getLanguage().getProcessor())
    language_id = str(currentProgram.getLanguageID())
    print(f"当前程序: {currentProgram.getName()}, 路径: {program_path}, 架构: {program_arch}, 语言ID: {language_id}")
    endianness = "unknown"
    if "BE" in language_id.upper() or "BIG" in language_id.upper():
        endianness = "big"
    elif "LE" in language_id.upper() or "LITTLE" in language_id.upper():
        endianness = "little"
    else:
        # 尝试从程序的字节序获取
        if currentProgram.getMemory().isBigEndian():
            endianness = "big"
        else:
            endianness = "little"
    
    # 构建完整的架构描述
    if program_arch == "MIPS":
        if endianness == "little":
            arch_name = "MIPSEL"  # MIPS Little Endian
        else:
            arch_name = "MIPSEB"  # MIPS Big Endian
    elif program_arch == "ARM":
        if endianness == "little":
            arch_name = "ARMEL"   # ARM Little Endian
        else:
            arch_name = "ARMEB"   # ARM Big Endian
    else:
        # 其他架构，保持原有格式
        arch_name = program_arch
        if endianness != "unknown":
            arch_name += "_" + endianness.upper()
    result = {
        "program_name": currentProgram.getName(),
        "program_path": program_path,
        "program_arch": arch_name,
        "extract_functions": [],
        "const_value_functions": [],
        "remove_functions": []
    }
    # 分析handler函数，按extract_func分组
    extract_func_handlers = find_handlers_with_extract_funcs(handler_data, extract_funcs)
    
    total_handlers = 0
    for extract_func, handlers in extract_func_handlers.items():
        total_handlers += len(handlers)
    log(f"总共找到 {total_handlers} 个handler函数")
    
    # 为每个extract_func构建结果
    for extract_func in extract_funcs:
        # 获取extract_func的地址和参数信息
        address, target_func = get_function_address(extract_func)
        if not target_func:
            log(f"未找到extract函数 {extract_func}")
            # 即使未找到函数，也要创建条目以保持一致性
            func_info = {
                "name": extract_func,
                "address": "unknown",
                "parameter_count": -1,
                "callers": []
            }
            result["extract_functions"].append(func_info)
            continue
            
        param_count = get_function_parameter_count(target_func)
        log(f"Extract函数 {extract_func} 的参数数量: {param_count}")
        
        # 构建该extract_func的调用者列表
        callers = []
        handlers = extract_func_handlers.get(extract_func, [])
        
        for handler_info in handlers:
            handler_name = handler_info["handler"]
            
            # 获取handler函数的地址
            handler_address, handler_func = get_function_address(handler_name)
            if handler_func:
                caller_info = {
                    "name": handler_name,
                    "address": "0x" + handler_address if handler_address else "unknown"
                }
                callers.append(caller_info)
                log(f"  添加调用者: {handler_name}")
        
        func_info = {
            "name": extract_func,
            "address": "0x" + address if address else "unknown",
            "parameter_count": param_count,
            "callers": callers
        }
        
        result["extract_functions"].append(func_info)
        log(f"Extract函数 {extract_func}: 找到 {len(callers)} 个调用者")
    
    # 处理需要提取常量值的函数
    for const_func_item in const_value_funcs:
        # 兼容老格式字符串和新格式字典
        if isinstance(const_func_item, dict):
            const_func_name = const_func_item.get("name")
        else:
            const_func_name = const_func_item

        log(f"查找常量值函数: {const_func_name}")
        result_tuple = get_function_address(const_func_name)
        
        if result_tuple:
            address, func = result_tuple
            const_info = {
                "name": const_func_name,
                "address": "0x" + address,
            }
            result["const_value_functions"].append(const_info)
        else:
            # 未找到函数，可能是库函数export的，不标明地址
            log(f"未找到函数 {const_func_name}，可能是库函数")
            const_info = {
                "name": const_func_name,
                "address": "unknown",
            }
            result["const_value_functions"].append(const_info)
            
    # 处理需要移除的函数
    for remove_func_item in remove_funcs:
        # 兼容老格式字符串和新格式字典
        if isinstance(remove_func_item, dict):
            remove_func_name = remove_func_item.get("name")
            return_value = remove_func_item.get("return_value", 0)
        else:
            remove_func_name = remove_func_item
            return_value = 0

        log(f"查找移除函数: {remove_func_name}")
        address, func = get_function_address(remove_func_name)
        
        if address:
            remove_info = {
                "name": remove_func_name,
                "address": "0x"+address,
                "return_value": return_value
            }
            result["remove_functions"].append(remove_info)
        else:
            log(f"警告: 未找到移除函数 {remove_func_name}")
    # 确保输出目录存在
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            log(f"创建输出目录: {output_dir}")
    except Exception as e:
        log(f"创建输出目录失败: {str(e)}")
        output_dir = os.getcwd()
        log(f"回退使用当前工作目录: {output_dir}")
    # 生成输出文件名，基于输入配置文件名
    output_basename = os.path.splitext(os.path.basename(config_filename))[0]
    output_file_path = os.path.join(output_dir, f"{output_basename}_results.json")
    # 将结果写入JSON文件
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    
    log(f"分析完成，结果已保存至 {output_file_path}")
    total_callers = sum(len(func['callers']) for func in result['extract_functions'])
    log(f"共保留 {total_callers} 个handler函数")
    log(f"共移除 {len(result['remove_functions'])} 个函数")
    log(f"共找到 {len(result['const_value_functions'])} 个常量值函数")
    
if __name__ == '__main__':
    main()

