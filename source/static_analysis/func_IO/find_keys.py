#@category Analysis
#ghidra实现的用于识别websgetvar的name脚本，不用理会
import sys
import os
from ghidra.app.plugin.core.analysis import ConstantPropagationAnalyzer
from ghidra.program.util import SymbolicPropogator
from ghidra.util.exception import CancelledException
from ghidra.util.task import TaskMonitor
from ghidra.util.classfinder import ClassSearcher
from ghidra.program.model.pcode import PcodeOp
from collections import defaultdict

# 设置输出文件路径
output_file_path = os.path.join(os.getcwd(), "result.txt")

# 记录标准输出流
original_stdout = sys.stdout

# 打开文件进行写入，并重定向输出
with open(output_file_path, "w", encoding="utf-8") as f:
    sys.stdout = f  # 重定向标准输出到文件

    monitor = getMonitor()
    currentProgram = getCurrentProgram()
    analyzer = None
    syms = {}
    
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
    def find_websGetVar_calls():
        """
        查找所有调用 `websGetVar` 的位置，并返回调用点信息
        """
        funcs = getGlobalFunctions("websGetVar")
        if not funcs:
            print("未找到函数 websGetVar。")
            return []

        websGetVarFunc = funcs[0]
        entry = websGetVarFunc.getEntryPoint()
        print("函数 websGetVar 位于地址: " + str(entry))

        ref_manager = currentProgram.getReferenceManager()
        refs = list(ref_manager.getReferencesTo(entry))

        print("共找到 {} 个调用点：".format(len(refs)))
        call_sites = []
        for ref in refs:
            from_addr = ref.getFromAddress()
            call_inst = getInstructionAt(from_addr)
            caller_func = getFunctionContaining(from_addr)
            if caller_func:
                print("调用自函数：{}，调用地址：{}，指令：{}".format(caller_func.getName(), from_addr, call_inst))
                call_sites.append((caller_func, from_addr, call_inst))

        return call_sites

    def get_return_store_instruction(call_inst):
        """
        找到 `websGetVar` 调用后的存储返回值的指令 (`sw v0, local_xxx(s8)`)
        """
        if call_inst is None:
            return None

        caller_func = getFunctionContaining(call_inst.getAddress())
        if caller_func is None:
            return None

        next_addr = call_inst.getFallThrough()
        if next_addr is None:
            return None

        current_inst = getInstructionAt(next_addr)
        while current_inst is not None and caller_func.getBody().contains(current_inst.getAddress()):
            inst_str = current_inst.toString()
            if "sw" in inst_str and "v0" in inst_str:
                print("找到存储 `websGetVar` 返回值的指令: {} -> {}".format(current_inst.getAddress(), inst_str))
                return current_inst
            current_inst = current_inst.getNext()

        return None

    def parse_local_variable(store_inst):
        """
        解析 `sw v0, local_390(s8)` 的存储变量
        """
        if store_inst is None:
            return None

        local_var = store_inst.getDefaultOperandRepresentation(1)
        print("解析出的局部变量: {}".format(local_var))
        
        return local_var

    def track_symbolic_execution(var_name, func):
        """
        符号执行：追踪局部变量的流向
        """
        if func is None:
            return

        symEval = SymbolicPropogator(currentProgram)
        symEval.setParamRefCheck(True)
        symEval.setReturnRefCheck(True)
        symEval.setStoredRefCheck(True)

        analyzer = ConstantPropagationAnalyzer()
        analyzer.flowConstants(currentProgram, func.getEntryPoint(), func.getBody(), symEval, monitor)

        print("开始符号执行: 追踪变量 `{}` 在函数 `{}` 内的传播".format(var_name, func.getName()))
        parmsregs = ["a0", "a1", "a2", "a3"]
        inst = getInstructionAt(func.getEntryPoint())
        while inst is not None and func.getBody().contains(inst.getAddress()):
            inst_str = inst.toString()
            if var_name in inst_str:
                print("变量 `{}` 在 {} 处被使用: {}".format(var_name, inst.getAddress(), inst_str))
                if f"lw" in inst_str:
                    # 继续扫描，查找最近的 `jal` 或 `jalr` 调用
                    reg = inst.getDefaultOperandRepresentation(0)
                    if reg in parmsregs:
                        next_inst = inst.getNext()
                        while next_inst is not None and func.getBody().contains(next_inst.getAddress()):
                            next_inst_str = next_inst.toString()
                            if "jal " in next_inst_str or "jalr " in next_inst_str:
                                target_func = getCallee(next_inst)
                                if target_func:
                                    print("变量 `{}` 作为参数 `{}` 传递给函数 `{}` (调用地址: {})".format(
                                        var_name, reg,target_func.getName(), next_inst.getAddress()))
                                break
                            next_inst = next_inst.getNext()
            inst = inst.getNext()

    def analyze_call_graph(var_name, func):
        """
        遍历调用图，查找变量是否流入 `sink` 函数
        """
        #构建函数调用图
        callMap = defaultdict(dict)
        pending = [func]
        def build_call_map(func):
            while pending:
                current_func = pending.pop()
                if current_func in callMap:
                    continue
                callMap[current_func] = {}

                inst = getInstructionAt(current_func.getEntryPoint())
                while inst is not None and current_func.getBody().contains(inst.getAddress()):
                    callee = getCallee(inst)
                    if callee is not None:
                        callMap[current_func][inst.getAddress()] = callee
                        if callee not in callMap:
                            pending.append(callee)

                    inst = inst.getNext()
                    
    # **分析 `formSetCfm` 调用的所有函数**
    def analyze_function_calls(target_func):
        if not target_func:
            print("[ERROR] 找不到函数: formSetCfm")
            return

        print(f"[INFO] 分析函数: {target_func.getName()} @ {target_func.getEntryPoint()}")

        # 获取函数中的所有指令
        instruction = getInstructionAt(target_func.getEntryPoint())

        called_functions = set()

        while instruction and instruction.getAddress() < target_func.getBody().getMaxAddress():
            # **检查是否是 CALL 指令**
            callee_func = getCallee(instruction)

            if callee_func:
                print(f"  - 调用 @ {instruction.getAddress()} -> {callee_func.getName()} ({callee_func.getEntryPoint()})")
                called_functions.add((callee_func.getName(), callee_func.getEntryPoint()))

            # **继续下一条指令**
            instruction = instruction.getNext()

        print("\n[分析完成] 解析出的调用目标:")
        for func_name, addr in called_functions:
            print(f"  -> {func_name} @ {addr}")

    def main():
        call_sites = find_websGetVar_calls()
        func_child_call_map = {}
        for (caller_func, from_addr, call_inst) in call_sites:
            store_inst = get_return_store_instruction(call_inst)
            if store_inst is None:
                continue

            local_var = parse_local_variable(store_inst)
            if local_var is None:
                continue

            track_symbolic_execution(local_var, caller_func)
            analyze_call_graph(local_var, caller_func)

    if __name__ == '__main__':
        main()

# 还原标准输出
sys.stdout = original_stdout

print(f"分析完成，结果已保存至 {output_file_path}")
