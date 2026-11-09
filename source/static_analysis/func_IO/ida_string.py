from headless_ida import HeadlessIda
IDAT_PATH = "D:\CTFtools\IDA 7.7\IDA_Pro_7.7\idat.exe"

class IDA:
    def __init__(self, binary_path):
        self.headless_ida = HeadlessIda(IDAT_PATH, binary_path)
        self.idautils = self.headless_ida.import_module("idautils")
        self.ida_funcs = self.headless_ida.import_module("ida_funcs")
        self.ida_hexrays = self.headless_ida.import_module("ida_hexrays")

    def get_function_by_name(self, name):
        for ea in self.idautils.Functions():
            if self.ida_funcs.get_func_name(ea) == name:
                return ea
        return None

    def decompile_function(self, ea):
        cfunc = self.ida_hexrays.decompile(ea)
        if cfunc is None:
            return None
        return str(cfunc)
    def search_string(self, search):
        result = {}
        for string in self.idautils.Strings():
            if search in str(string):
                result[string.ea] = str(string)
        return result
    def get_string_references(self, ea):
        result = []
        for ref in self.idautils.DataRefsTo(ea):
            result.append(ref)
        return result
    
    def analyze_string_usage(self, ea, str_value):
        # 获取字符串的引用
        refs = self.get_string_references(ea)
        usages = []
        
        for ref in refs:
            # 获取包含该引用的函数
            func = self.ida_funcs.get_func(ref)
            if not func:
                continue
                
            function_ea = func.start_ea
            function_name = self.ida_funcs.get_func_name(function_ea)
            
            # 反编译函数获取ctree
            cfunc = self.ida_hexrays.decompile(function_ea)
            if not cfunc:
                continue
                
            # 导入必要的模块
            ida_hexrays = self.ida_hexrays
            # 获取ida_funcs引用，以便在访问者类中使用
            ida_funcs = self.ida_funcs
            
            # 创建一个访问者类来查找字符串的使用
            class StringUsageVisitor(ida_hexrays.ctree_visitor_t):
                def __init__(self, str_ea, str_value):
                    ida_hexrays.ctree_visitor_t.__init__(self, ida_hexrays.CV_FAST)
                    self.str_ea = str_ea
                    self.str_value = str_value
                    self.usages = []
                    
                def visit_expr(self, expr):
                    # 检查是否是对目标字符串的引用
                    if expr.op == ida_hexrays.cot_obj and expr.obj_ea == self.str_ea:
                        # 向上查找父节点，找到调用表达式
                        parent = self.parents.back() if self.parents else None
                        if parent and parent.op == ida_hexrays.cot_call:
                            # 获取函数调用名称
                            call_expr = parent.x
                            if call_expr.op == ida_hexrays.cot_obj:
                                call_name = "UNKNOWN"
                                try:
                                    # 使用外部传入的ida_funcs
                                    call_name = ida_funcs.get_func_name(call_expr.obj_ea)
                                except:
                                    pass
                                if not call_name:
                                    call_name = f"func_{call_expr.obj_ea:x}"
                                    
                                # 记录使用情况
                                self.usages.append({
                                    "function_name": function_name,
                                    "called_function": call_name,
                                    "string_value": self.str_value
                                })
                    return 0
            
            # 创建并应用访问者
            visitor = StringUsageVisitor(ea, str_value)
            visitor.apply_to(cfunc.body, None)
            usages.extend(visitor.usages)
        
        return usages
    
prog_cgi=IDA("D:\CTFtools\IDA 7.7\IDA_Pro_7.7\script\prog.cgi")
string = prog_cgi.search_string("ScheduleDate")
all_usages = []

for ea, str_value in string.items():
    usages = prog_cgi.analyze_string_usage(ea, str_value)
    all_usages.extend(usages)
    
# 打印分析结果
print("\n=== 字符串用法分析 ===")
for usage in all_usages:
    print(f"字符串 '{usage['string_value']}' 在函数 {usage['function_name']} 中被用于调用 {usage['called_function']}")