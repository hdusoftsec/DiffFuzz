 /root/ghidra_11.3.2_PUBLIC/support/analyzeHeadless /root/FHFuzz/ghidra_project Tenda -import ./static_analysis/diff/Tenda_httpd/AC9_httpd -postScript ./static_analysis/func_IO/extract.py /root/FHFuzz/static_analysis/func_IO/extract_ac9.json /root/FHFuzz/static_analysis/diff/Tenda_httpd

 字符串提取
首先satc提取前后端关键字信息
python3 ./SaTC/satc_front/satc.py -d /root/FHFuzz/firmware_SaTC/D-Link/DIR-825/_DIR825B1_FW206WWB05.bin.extracted/squashfs-root -o ./SaTC/satc_front/result/DIR825 --ghidra_script=all

解析提取satc分析结果，生成prar_statistics.json
python3 ./static_analysis/func_IO/front_prar.py ./SaTC/satc_front/result/DIR825 ./dir825_analyis

根据关键字信息找出使用关键字的函数
../ghidra_11.1.2_PUBLIC/support/analyzeHeadless /root/ghidra_11.1.2_PUBLIC/result handler -process DIR825_httpd -postScript ./static_analysis/func_IO/ghidra_string_to_func.py ./dir825_analyis ./dir825_analyis httpd > log_string_to_func

提取固件中存在的handler函数
../ghidra_11.1.2_PUBLIC/support/analyzeHeadless /root/ghidra_11.1.2_PUBLIC/result handler -process DIR825_httpd -postScript ./static_analysis/func_IO/handler_extract_latest.py ./analysis_output > log_handler

根据前面两个的结果分析出可能的IO函数
python3 ./static_analysis/func_IO/filter_io_func.py ./dir825_analyis ./dir825_analyis --ai_flag > log_filter_io_func