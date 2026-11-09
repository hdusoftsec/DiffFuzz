'''
date created: 12 April 2021
notes: this script will extract function information and create a bindiff from a binary using ghidra, 
the output is a .csv with address information for each function, and the *.bindiff format
'''

import csv
import os
from ghidra.app.script import GhidraScript
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.app.util import Option
from ghidra.app.util.exporter import Exporter
from com.google.security.binexport import BinExportExporter
from java.io import File
from java.util import ArrayList

function_list = []
monitor = getMonitor()
currentProgram = getCurrentProgram()
program_name = currentProgram.getName()
path = currentProgram.getExecutablePath()
listing = currentProgram.getListing()
func_manager = currentProgram.getFunctionManager()
internal_fcn_objs = func_manager.getFunctions(True)

# 创建导出目录
export_path='/root/FHFuzz/diff/ghidraheadless_binexport/ghidra_binary_binexport/'
os.makedirs(export_path, exist_ok=True)
f = File(export_path+program_name + '.BinExport')

# 创建BinExport导出器
exporter = BinExportExporter() # Binary BinExport (v2) for BinDiff

# 根据BinExportExporter.java文件，需要创建Option对象列表
options = ArrayList()
#options.add(Option("IDA Pro Compatibility", "Subtract Imagebase", True))
#options.add(Option("IDA Pro Compatibility", "Remap mnemonics", True))
options.add(Option("IDA Pro Compatibility", "Prepend Namespace to Function Names", True))

# 设置选项
exporter.setOptions(options)

# 执行导出
print(f"正在导出 {program_name} 到 {export_path + program_name}.BinExport...")
addr_set = currentProgram.getMemory()
exporter.export(f, currentProgram, addr_set, monitor)
print("导出完成")

# 收集函数信息
print("收集函数信息...")
for fun_obj in internal_fcn_objs:
    fun_name = fun_obj.getName()
    min_addr = fun_obj.getBody().getMinAddress().getOffset()
    function_list.append([path, fun_name, min_addr])

# 确保函数数据目录存在
function_data_dir = '/root/FHFuzz/diff/ghidraheadless_binexport/ghidra_function_data/'
os.makedirs(function_data_dir, exist_ok=True)

# 保存函数信息
with open(function_data_dir + 'sample_functions_addresses.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(function_list)
print(f"保存了 {len(function_list)} 个函数信息")