1、解包binwalk

2、提取固件关键二进制信息、共享关键字信息

```shell
python3 ./static_analysis/static_analysis.py /root/FHFuzz/experiment/satc_exp/firmware_SaTC/TOTOLink/T10 ./experiment/satc_exp/firmware_SaTC/TOTOLink/T10
```

3、根据关键字信息提取候选IO函数列表

```
../ghidra_11.1.2_PUBLIC/support/analyzeHeadless /root/ghidra_11.1.2_PUBLIC/result handler -process A702R_boa -postScript ./static_analysis/func_IO/ghidra_string_to_func.py ./experiment/TOTOLINK/A702R/ ./experiment/TOTOLINK/A702R boa > ./experiment/TOTOLINK/A702R/log_string_to_func
```

4、提取handler函数列表

```
../ghidra_11.1.2_PUBLIC/support/analyzeHeadless /root/ghidra_11.1.2_PUBLIC/result handler -process A702R_boa -postScript ./static_analysis/func_IO/handler_extract_latest.py ./experiment/TOTOLINK/A702R/  > ./experiment/TOTOLINK/A702R/log_handler_extract
```

5、综合3、4两步结合ai筛选IO函数

```
python3 ./static_analysis/func_IO/filter_io_func.py ./experiment/TOTOLINK/A702R ./experiment/TOTOLINK/A702R --ai_flag > ./experiment/TOTOLINK/A702R/log_filter_io_func
```

6、构建extract.json进行提取

```json
{
    "program_path":"/root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root/bin/httpd",
    "extract_func":["websGetVar","websGetVarWithValidate"],
    "remove_func":[
        {
            "name":"websWrite",
            "return_value":0
        },
        {
            "name":"websTransfer",
            "return_value":0
        },
        {
            "name":"websHeader",
            "return_value":0
        },
        {
            "name":"websMsgStart",
            "return_value":0
        },
        {
            "name":"websMsgEnd",
            "return_value":0
        },
        {
            "name":"websFooter",
            "return_value":0
        },
        {
            "name":"websDone",
            "return_value":0
        },
        {
            "name":"websRedirect",
            "return_value":0
        }
    ]
}

```

7、提取函数信息

```
../ghidra_11.1.2_PUBLIC/support/analyzeHeadless /root/FHFuzz/experiment/satc_exp/ghidra_project satc -process DIR878_prog.cgi -postScript ./static_analysis/func_IO/extract.py ./experiment/satc_exp/firmware_SaTC/D-Link/D-Link\ 878/extract_DIR878_progcgi.json ./experiment/satc_exp/firmware_SaTC/D-Link/D-Link\ 878/combined_handler_functions.json ./experiment/satc_exp/firmware_SaTC/D-Link/D-Link\ 878/
```

8、差异化分析

```
python3 ./static_analysis/diff/my_auto_bindiff.py --binexport_dir=./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff --output_dir=./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff

export GHIDRA_INSTALL_DIR="/root/ghidra_11.1.2_PUBLIC/"
ghidriff ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC6_httpd ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC9_httpd ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC12_httpd -o ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/ --summary=True

#要先把提取信息转移到/root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/json综合起来
python3 ./static_analysis/diff/ghidriff_parser_nosymbol.py AC6_httpd AC9_httpd AC12_httpd --json_dir=/root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/json --output=/root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC6_9_12_test_plan.json
```

9、符号执行分析

```
python3.11 ./static_analysis/taint_analysis/taint_core.py ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/json/extract_AC6_httpd_results.json -o ./experiment/satc_exp/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root/afl_test -t 8 -p ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC6_9_12_test_plan.json -b AC6_httpd > log_taint_diff
```

10、生成hook库

```
python3 ./func_hook/generated.py /root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/AC6/extract_AC6_httpd_results.json /root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root/afl_test
```

11、执行模糊测试

```
python3 ./start_fuzz/start_fuzz.py /root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/AC6/extract_AC6_httpd_results.json /root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root --test_plan /root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC6_9_12_test_plan.json --test_target AC6_httpd --handler_folder afl_test --binary httpd --parallel 10 --interval 5 --inactive 300 --report /root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/AC6/AC6_report.md
```

