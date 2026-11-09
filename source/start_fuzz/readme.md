export QEMU_LD_PREFIX="/root/FHFuzz/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root"
export QEMU_SET_ENV="LD_PRELOAD=/lib/libdl.so.0:/lib/formWifiWpsStart_hooks.so"
export AFL_TAINT_CONFIG_FILE="/root/FHFuzz/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root/result_test/formSetCfm/config/taint.txt"
export AFL_CUSTOM_MUTATOR_LIBRARY="/root/AFLplusplus/custom_mutators/key_value_mutator/key_value_mutator.so"
export AFL_DISABLE_TRIM=1
export AFL_CUSTOM_MUTATOR_ONLY=1
BINARY=/root/FHFuzz/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root/result_test/formWifiWpsStart/httpd

/root/AFLplusplus/afl-fuzz -i ./result_test/formWifiWpsStart/input -o ./result_new/formWifiWpsStart/output -m none -Q $BINARY @@

python3 /root/FHFuzz/fuzz/start_fuzz.py /root/FHFuzz/static_analysis/func_IO/extract_ac6_results.json /root/FHFuzz/firmware_SaTC/Tenda/AC6/_US_AC6V2.0RTL_V15.03.06.23_multi_TD01.bin.extracted/squashfs-root --handler_folder result_test  --parallel 10 --interval 5 --inactive 300 --report ./ac6_report.md