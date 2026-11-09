#将目标固件的二进制程序导出binexport文件后，进行bindff初步对比分组
python3 ./static_analysis/diff/my_auto_bindiff.py --binexport_dir=./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff --output_dir=./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff

export GHIDRA_INSTALL_DIR="/root/ghidra_11.1.2_PUBLIC/"
ghidriff ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC6_httpd ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC9_httpd ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC12_httpd -o ./experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/ --summary=True

#要先把提取信息转移到/root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/json综合起来
python3 ./static_analysis/diff/ghidriff_parser_nosymbol.py AC6_httpd AC9_httpd AC12_httpd --json_dir=/root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/json --output=/root/FHFuzz/experiment/satc_exp/firmware_SaTC/Tenda/binary_diff/AC6_9_12_test_plan.json