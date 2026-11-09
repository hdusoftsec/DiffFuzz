# AC6_httpd-AC9_httpd Diff

# TOC

* [Visual Chart Diff](#visual-chart-diff)
* [Metadata](#metadata)
	* [Ghidra Diff Engine](#ghidra-diff-engine)
		* [Command Line](#command-line)
	* [Binary Metadata Diff](#binary-metadata-diff)
	* [Program Options](#program-options)
	* [Diff Stats](#diff-stats)
	* [Strings](#strings)
* [Deleted](#deleted)
* [Added](#added)
	* [get_usb_device_num](#get_usb_device_num)
	* [Usb_Up](#usb_up)
	* [check_if_dir_empty](#check_if_dir_empty)
	* [formSetUsbPrint](#formsetusbprint)
	* [formGetUsbPrint](#formgetusbprint)
	* [formSetSambaConf](#formsetsambaconf)
	* [formGetSambaConf](#formgetsambaconf)
	* [fill_smbpasswd_input_file](#fill_smbpasswd_input_file)
	* [writePasswd](#writepasswd)
	* [SpecChConv](#specchconv)
	* [formGetUSBStatus](#formgetusbstatus)
	* [formsetUsbUnload](#formsetusbunload)
	* [formGetUsbCfg](#formgetusbcfg)
	* [<EXTERNAL>::closedir](#externalclosedir)
	* [<EXTERNAL>::readdir](#externalreaddir)
	* [<EXTERNAL>::opendir](#externalopendir)
	* [<EXTERNAL>::atof](#externalatof)
* [Modified](#modified)
	* [fromSetWirelessRepeat](#fromsetwirelessrepeat)
	* [formGetRouterStatus](#formgetrouterstatus)
	* [formDefineTendDa](#formdefinetendda)
	* [ate_Tenda_mfg_check_wpsbutton](#ate_tenda_mfg_check_wpsbutton)
	* [ate_nvram_set_maxpower](#ate_nvram_set_maxpower)
	* [fromGetSysTime](#fromgetsystime)
	* [formGetOnlineList](#formgetonlinelist)
	* [ate_nvram_set_maxpower_2G](#ate_nvram_set_maxpower_2g)
	* [ate_nvram_set_maxpower_5G](#ate_nvram_set_maxpower_5g)
	* [wan_lan_same_deal](#wan_lan_same_deal)
	* [formWifiApScan](#formwifiapscan)
	* [form_fast_setting_get](#form_fast_setting_get)
	* [aspGetModeShow](#aspgetmodeshow)
* [Modified (No Code Changes)](#modified-no-code-changes)
	* [cJSON_CreateObject](#cjson_createobject)
	* [websTransfer](#webstransfer)
	* [cJSON_AddItemToArray](#cjson_additemtoarray)
	* [websFormDefine](#websformdefine)
	* [__ledf2](#__ledf2)
	* [set_cfm_mib](#set_cfm_mib)
	* [cJSON_CreateArray](#cjson_createarray)
	* [cJSON_Object_2String](#cjson_object_2string)
	* [cJSON_AddItemToObject](#cjson_additemtoobject)
	* [cJSON_Print](#cjson_print)
	* [cJSON_CreateString](#cjson_createstring)
	* [websGetVar](#websgetvar)
	* [cJSON_Delete](#cjson_delete)
	* [websDone](#websdone)
	* [websWrite](#webswrite)

# Visual Chart Diff



```mermaid

flowchart LR

fromSetWirelessRepeat-4-old<--Match 99%-->fromSetWirelessRepeat-4-new
formGetRouterStatus-5-old<--Match 88%-->formGetRouterStatus-5-new
formDefineTendDa-0-old<--Match 98%-->formDefineTendDa-0-new
ate_Tenda_mfg_check_wpsbutton-2-old<--Match 99%-->ate_Tenda_mfg_check_wpsbutton-2-new
ate_nvram_set_maxpower-1-old<--Match 83%-->ate_nvram_set_maxpower-1-new
fromGetSysTime-2-old<--Match 79%-->fromGetSysTime-2-new
formGetOnlineList-5-old<--Match 99%-->formGetOnlineList-5-new
ate_nvram_set_maxpower_2G-1-old<--Match 83%-->ate_nvram_set_maxpower_2G-1-new
ate_nvram_set_maxpower_5G-1-old<--Match 84%-->ate_nvram_set_maxpower_5G-1-new
wan_lan_same_deal-2-old<--Match 93%-->wan_lan_same_deal-2-new
formWifiApScan-5-old<--Match 50%-->formWifiApScan-5-new
form_fast_setting_get-2-old<--Match 84%-->form_fast_setting_get-2-new
aspGetModeShow-4-old<--Match 96%-->aspGetModeShow-4-new

subgraph AC9_httpd
    fromSetWirelessRepeat-4-new
formGetRouterStatus-5-new
formDefineTendDa-0-new
ate_Tenda_mfg_check_wpsbutton-2-new
ate_nvram_set_maxpower-1-new
fromGetSysTime-2-new
formGetOnlineList-5-new
ate_nvram_set_maxpower_2G-1-new
ate_nvram_set_maxpower_5G-1-new
wan_lan_same_deal-2-new
formWifiApScan-5-new
form_fast_setting_get-2-new
aspGetModeShow-4-new
    subgraph Added
direction LR
get_usb_device_num
    Usb_Up
    check_if_dir_empty
    formSetUsbPrint
    formGetUsbPrint
    formSetSambaConf
    formGetSambaConf
    fill_smbpasswd_input_file
    writePasswd
    SpecChConv
    formGetUSBStatus
    formsetUsbUnload
    formGetUsbCfg
    EXTERNAL-closedir
    EXTERNAL-readdir
    EXTERNAL-opendir
    EXTERNAL-atof
end
end

subgraph AC6_httpd
    fromSetWirelessRepeat-4-old
formGetRouterStatus-5-old
formDefineTendDa-0-old
ate_Tenda_mfg_check_wpsbutton-2-old
ate_nvram_set_maxpower-1-old
fromGetSysTime-2-old
formGetOnlineList-5-old
ate_nvram_set_maxpower_2G-1-old
ate_nvram_set_maxpower_5G-1-old
wan_lan_same_deal-2-old
formWifiApScan-5-old
form_fast_setting_get-2-old
aspGetModeShow-4-old
    
end

```


```mermaid
pie showData
    title Function Matches - 99.5699%
"unmatched_funcs_len" : 17
"matched_funcs_len" : 3936
```



```mermaid
pie showData
    title Matched Function Similarity - 99.2886%
"matched_funcs_with_code_changes_len" : 13
"matched_funcs_with_non_code_changes_len" : 15
"matched_funcs_no_changes_len" : 3908
```

# Metadata

## Ghidra Diff Engine

### Command Line

#### Captured Command Line


```
ghidriff --project-location ghidra_projects --project-name ghidriff --symbols-path symbols --threaded --log-level INFO --file-log-level INFO --log-path ghidriff.log --min-func-len 10 --gdt [] --bsim --max-ram-percent 60.0 --max-section-funcs 200 AC6_httpd AC9_httpd
```


#### Verbose Args


<details>

```
--old ['./Tenda_httpd/AC6_httpd'] --new [['./Tenda_httpd/AC9_httpd', './Tenda_httpd/AC12_httpd']] --engine VersionTrackingDiff --output-path ./Tenda_httpd/112ghidra --summary Treu --project-location ghidra_projects --project-name ghidriff --symbols-path symbols --threaded True --force-analysis False --force-diff False --no-symbols False --log-level INFO --file-log-level INFO --log-path ghidriff.log --va False --min-func-len 10 --use-calling-counts False --gdt [] --bsim True --bsim-full False --max-ram-percent 60.0 --print-flags False --jvm-args None --side-by-side False --max-section-funcs 200 --md-title None
```


</details>

## Binary Metadata Diff


```diff
--- AC6_httpd Meta
+++ AC9_httpd Meta
@@ -1,177 +1,178 @@
-Program Name: AC6_httpd
+Program Name: AC9_httpd
 Language ID: MIPS:LE:32:default (1.8)
 Compiler ID: default
 Processor: MIPS
 Endian: Little
 Address Size: 32
-Minimum Address: 003ff000
+Minimum Address: 00400000
 Maximum Address: _elfSectionHeaders::00000757
-# of Bytes: 2129469
-# of Memory Blocks: 50
-# of Instructions: 254926
-# of Defined Data: 17472
-# of Functions: 1966
-# of Symbols: 24878
-# of Data Types: 930
-# of Data Type Categories: 118
+# of Bytes: 2148436
+# of Memory Blocks: 48
+# of Instructions: 257313
+# of Defined Data: 17677
+# of Functions: 1987
+# of Symbols: 25124
+# of Data Types: 940
+# of Data Type Categories: 120
 Analyzed: true
 Created With Ghidra Version: 11.1.2
 DWARF Loaded: true
-Date Created: Tue May 13 16:43:25 CST 2025
+Date Created: Tue May 13 16:43:26 CST 2025
 ELF File Type: executable
-ELF Original Image Base: 0x3ff000
+ELF Original Image Base: 0x400000
 ELF Prelinked: false
 ELF Source File [   0]: initfini.c
 ELF Source File [   1]: crtstuff.c
 ELF Source File [   2]: crtstuff.c
 ELF Source File [   3]: initfini.c
 ELF Source File [   4]: asp.c
 ELF Source File [   5]: balloc.c
 ELF Source File [   6]: base64.c
 ELF Source File [   7]: cgi.c
 ELF Source File [   8]: default.c
 ELF Source File [   9]: ejlex.c
 ELF Source File [  10]: ejparse.c
 ELF Source File [  11]: form.c
 ELF Source File [  12]: h.c
 ELF Source File [  13]: handler.c
 ELF Source File [  14]: uemf.h
 ELF Source File [  15]: misc.c
 ELF Source File [  16]: page.c
 ELF Source File [  17]: ringq.c
 ELF Source File [  18]: sock.c
 ELF Source File [  19]: sockGen.c
 ELF Source File [  20]: sslSocket.c
 ELF Source File [  21]: matrix_ssl.c
 ELF Source File [  22]: security.c
 ELF Source File [  23]: sym.c
 ELF Source File [  24]: uemf.c
 ELF Source File [  25]: url.c
 ELF Source File [  26]: value.c
 ELF Source File [  27]: md5c.c
 ELF Source File [  28]: um.c
 ELF Source File [  29]: umui.c
 ELF Source File [  30]: websda.c
 ELF Source File [  31]: emfdb.c
 ELF Source File [  32]: webs.c
 ELF Source File [  33]: websuemf.c
 ELF Source File [  34]: main.c
 ELF Source File [  35]: ../../../../infra/pal/list.h
 ELF Source File [  36]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/sysCurrentInfor.c
 ELF Source File [  37]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/controlCfm.c
 ELF Source File [  38]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/networkCfm.c
 ELF Source File [  39]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/sysSafe.c
 ELF Source File [  40]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/Dhcp.c
 ELF Source File [  41]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/upload.c
 ELF Source File [  42]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cJSON.c
 ELF Source File [  43]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/Form_define.c
 ELF Source File [  44]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/system_reboot.c
 ELF Source File [  45]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/mtenda.c
 ELF Source File [  46]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/Form_public.c
 ELF Source File [  47]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/index.c
 ELF Source File [  48]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/wizard.c
 ELF Source File [  49]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/lan.c
 ELF Source File [  50]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/../../../../infra/pal/list.h
 ELF Source File [  51]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/fast_setting.c
 ELF Source File [  52]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/usb_cgi.c
 ELF Source File [  53]: /home/work/workspace/AC6V2.0/infra/pal/list.h
 ELF Source File [  54]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/webip_lan.c
 ELF Source File [  55]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/wan_policy.c
 ELF Source File [  56]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/multiWan_setting.c
 ELF Source File [  57]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/webip_wan.c
 ELF Source File [  58]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/nat_dmz.c
 ELF Source File [  59]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/arp.c
 ELF Source File [  60]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/nat_virtualser.c
 ELF Source File [  61]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/nat_static.c
 ELF Source File [  62]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/nat_set.c
 ELF Source File [  63]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/ddns_config.c
 ELF Source File [  64]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/routing_table.c
 ELF Source File [  65]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/routing_static.c
 ELF Source File [  66]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/system_log.c
 ELF Source File [  67]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/log_addsetting.c
 ELF Source File [  68]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/system_restore.c
 ELF Source File [  69]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/system_password.c
 ELF Source File [  70]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/system_baseuser.c
 ELF Source File [  71]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/system_upgrade.c
 ELF Source File [  72]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cmd.c
 ELF Source File [  73]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/utf_gbl_encode.c
 ELF Source File [  74]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/qos_rule.c
 ELF Source File [  75]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/auto_qos_cgi.c
 ELF Source File [  76]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_utils.c
 ELF Source File [  77]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/pacontrol.c
 ELF Source File [  78]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/upnp_config.c
 ELF Source File [  79]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/lan_dhcps.c
 ELF Source File [  80]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/lan_dhcp_clients.c
 ELF Source File [  81]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/system_hostname.c
 ELF Source File [  82]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/dns_safesecond.c
 ELF Source File [  83]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/sched_wifi_check.c
 ELF Source File [  84]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/sched_led_check.c
 ELF Source File [  85]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/electronic_bulletin.c
 ELF Source File [  86]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/switch_portVLAN.c
 ELF Source File [  87]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/wifi.c
-ELF Source File [  88]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/behaviormanager_demo.c
-ELF Source File [  89]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/safe_demo.c
-ELF Source File [  90]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/ucloud_v2.c
-ELF Source File [  91]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/alischedule.c
-ELF Source File [  92]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/apclient.c
-ELF Source File [  93]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/iptv.c
-ELF Source File [  94]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/reboot_timer.c
-ELF Source File [  95]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/smart_power_management_cgi.c
-ELF Source File [  96]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/guest_ip_confilct.c
-ELF Source File [  97]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/vpn.c
-ELF Source File [  98]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/wan_err_info.c
-ELF Source File [  99]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_common.c
-ELF Source File [ 100]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_mac_filter.c
-ELF Source File [ 101]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_advertisement.c
-ELF Source File [ 102]: matrixSsl.c
-ELF Source File [ 103]: sslDecode.c
-ELF Source File [ 104]: sslEncode.c
-ELF Source File [ 105]: sslv3.c
-ELF Source File [ 106]: linux.c
-ELF Source File [ 107]: md5.c
-ELF Source File [ 108]: mpi.c
-ELF Source File [ 109]: sha1.c
-ELF Source File [ 110]: rsaPki.c
-ELF Source File [ 111]: x509.c
-ELF Source File [ 112]: cipherSuite.c
-ELF Source File [ 113]: arc4.c
-ELF Source File [ 114]: base64.c
-ELF Source File [ 115]: des3.c
-ELF Source File [ 116]: rsa.c
-ELF Source File [ 117]: asn1.c
-ELF Source File [ 118]: libgcc2.c
-ELF Source File [ 119]: adddf3.c
-ELF Source File [ 120]: divdf3.c
-ELF Source File [ 121]: gedf2.c
-ELF Source File [ 122]: ledf2.c
-ELF Source File [ 123]: muldf3.c
-ELF Source File [ 124]: subdf3.c
-ELF Source File [ 125]: fixdfsi.c
-ELF Source File [ 126]: floatsidf.c
-ELF Source File [ 127]: floatunsidf.c
-ELF Source File [ 128]: extendsfdf2.c
-ELF Source File [ 129]: 
+ELF Source File [  88]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/usb.c
+ELF Source File [  89]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/behaviormanager_demo.c
+ELF Source File [  90]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/safe_demo.c
+ELF Source File [  91]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/ucloud_v2.c
+ELF Source File [  92]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/alischedule.c
+ELF Source File [  93]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/apclient.c
+ELF Source File [  94]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/iptv.c
+ELF Source File [  95]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/reboot_timer.c
+ELF Source File [  96]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/smart_power_management_cgi.c
+ELF Source File [  97]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/guest_ip_confilct.c
+ELF Source File [  98]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/vpn.c
+ELF Source File [  99]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/wan_err_info.c
+ELF Source File [ 100]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_common.c
+ELF Source File [ 101]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_mac_filter.c
+ELF Source File [ 102]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_advertisement.c
+ELF Source File [ 103]: matrixSsl.c
+ELF Source File [ 104]: sslDecode.c
+ELF Source File [ 105]: sslEncode.c
+ELF Source File [ 106]: sslv3.c
+ELF Source File [ 107]: linux.c
+ELF Source File [ 108]: md5.c
+ELF Source File [ 109]: mpi.c
+ELF Source File [ 110]: sha1.c
+ELF Source File [ 111]: rsaPki.c
+ELF Source File [ 112]: x509.c
+ELF Source File [ 113]: cipherSuite.c
+ELF Source File [ 114]: arc4.c
+ELF Source File [ 115]: base64.c
+ELF Source File [ 116]: des3.c
+ELF Source File [ 117]: rsa.c
+ELF Source File [ 118]: asn1.c
+ELF Source File [ 119]: libgcc2.c
+ELF Source File [ 120]: adddf3.c
+ELF Source File [ 121]: divdf3.c
+ELF Source File [ 122]: gedf2.c
+ELF Source File [ 123]: ledf2.c
+ELF Source File [ 124]: muldf3.c
+ELF Source File [ 125]: subdf3.c
+ELF Source File [ 126]: fixdfsi.c
+ELF Source File [ 127]: floatsidf.c
+ELF Source File [ 128]: floatunsidf.c
+ELF Source File [ 129]: extendsfdf2.c
+ELF Source File [ 130]: 
 Elf Comment[0]: GCC: (GNU) 3.3.2
 Elf Comment[1]: GCC: (Realtek MSDK-4.4.7 Build 2001) 4.4.7
 Executable Format: Executable and Linking Format (ELF)
-Executable Location: /root/FHFuzz/static_analysis/diff/Tenda_httpd/AC6_httpd
-Executable MD5: 6bbbe9d79eed77c2b21108d6bc60e46a
-Executable SHA256: 2b6bbc43b4a718af5533ea75e177ee6f9f8fb265beabaa95973faf474b3ce869
-FSRL: file:///root/FHFuzz/static_analysis/diff/Tenda_httpd/AC6_httpd?MD5=6bbbe9d79eed77c2b21108d6bc60e46a
+Executable Location: /root/FHFuzz/static_analysis/diff/Tenda_httpd/AC9_httpd
+Executable MD5: 8bcc3eee1768591e050db8ff4eff7da1
+Executable SHA256: 329d918f05c1a76bf41074eba35553b2517f2054c1c10ab8c41ac2e037e12c6f
+FSRL: file:///root/FHFuzz/static_analysis/diff/Tenda_httpd/AC9_httpd?MD5=8bcc3eee1768591e050db8ff4eff7da1
 GNU DebugLink: httpd.debug
 Preferred Root Namespace Category: 
 Relocatable: false
 Required Library [    0]: libCfm.so
 Required Library [    1]: libcommon.so
 Required Library [    2]: libChipApi.so
 Required Library [    3]: libvos_util.so
 Required Library [    4]: libz.so
 Required Library [    5]: libpthread.so.0
 Required Library [    6]: libapmib.so
 Required Library [    7]: librtlWifiSrc.so
 Required Library [    8]: libtpi.so
 Required Library [    9]: libm.so.0
 Required Library [   10]: libucapi.so
 Required Library [   11]: libgcc_s.so.1
 Required Library [   12]: libc.so.0
 Should Ask To Analyze: false

```


## Program Options


<details>
<summary>Ghidra AC6_httpd Decompiler Options</summary>


|Decompiler Option|Value|
| :---: | :---: |
|Prototype Evaluation|__stdcall|

</details>


<details>
<summary>Ghidra AC6_httpd Specification extensions Options</summary>


|Specification extensions Option|Value|
| :---: | :---: |
|FormatVersion|0|
|VersionCounter|0|

</details>


<details>
<summary>Ghidra AC6_httpd Analyzers Options</summary>


|Analyzers Option|Value|
| :---: | :---: |
|ASCII Strings|true|
|ASCII Strings.Create Strings Containing Existing Strings|true|
|ASCII Strings.Create Strings Containing References|true|
|ASCII Strings.Force Model Reload|false|
|ASCII Strings.Minimum String Length|LEN_5|
|ASCII Strings.Model File|StringModel.sng|
|ASCII Strings.Require Null Termination for String|true|
|ASCII Strings.Search Only in Accessible Memory Blocks|true|
|ASCII Strings.String Start Alignment|ALIGN_1|
|ASCII Strings.String end alignment|4|
|Aggressive Instruction Finder|false|
|Aggressive Instruction Finder.Create Analysis Bookmarks|true|
|Apply Data Archives|true|
|Apply Data Archives.Archive Chooser|[Auto-Detect]|
|Apply Data Archives.Create Analysis Bookmarks|true|
|Apply Data Archives.GDT User File Archive Path|None|
|Apply Data Archives.User Project Archive Path|None|
|Call Convention ID|true|
|Call Convention ID.Analysis Decompiler Timeout (sec)|60|
|Call-Fixup Installer|true|
|Condense Filler Bytes|false|
|Condense Filler Bytes.Filler Value|Auto|
|Condense Filler Bytes.Minimum number of sequential bytes|1|
|Create Address Tables|true|
|Create Address Tables.Allow Offcut References|false|
|Create Address Tables.Auto Label Table|false|
|Create Address Tables.Create Analysis Bookmarks|true|
|Create Address Tables.Maxmimum Pointer Distance|16777215|
|Create Address Tables.Minimum Pointer Address|4132|
|Create Address Tables.Minimum Table Size|3|
|Create Address Tables.Pointer Alignment|1|
|Create Address Tables.Relocation Table Guide|true|
|Create Address Tables.Table Alignment|4|
|DWARF|true|
|DWARF.Add Inlined Functions Comments|false|
|DWARF.Add Lexical Block Comments|false|
|DWARF.Create Function Signatures|true|
|DWARF.Import Data Types|true|
|DWARF.Import Functions|true|
|DWARF.Import Local Variable Info|true|
|DWARF.Output DWARF DIE Info|false|
|DWARF.Output Source Info|false|
|DWARF.Output Source Line Info|false|
|DWARF.Try To Pack Structs|true|
|Data Reference|true|
|Data Reference.Address Table Alignment|1|
|Data Reference.Address Table Minimum Size|3|
|Data Reference.Align End of Strings|false|
|Data Reference.Ascii String References|true|
|Data Reference.Create Address Tables|false|
|Data Reference.Minimum String Length|5|
|Data Reference.References to Pointers|true|
|Data Reference.Relocation Table Guide|true|
|Data Reference.Respect Execute Flag|true|
|Data Reference.Subroutine References|true|
|Data Reference.Switch Table References|false|
|Data Reference.Unicode String References|true|
|Decompiler Parameter ID|true|
|Decompiler Parameter ID.Analysis Clear Level|ANALYSIS|
|Decompiler Parameter ID.Analysis Decompiler Timeout (sec)|60|
|Decompiler Parameter ID.Commit Data Types|true|
|Decompiler Parameter ID.Commit Void Return Values|false|
|Decompiler Parameter ID.Prototype Evaluation|__stdcall|
|Decompiler Switch Analysis|true|
|Decompiler Switch Analysis.Analysis Decompiler Timeout (sec)|60|
|Demangler GNU|true|
|Demangler GNU.Apply Function Calling Conventions|true|
|Demangler GNU.Apply Function Signatures|true|
|Demangler GNU.Demangle Only Known Mangled Symbols|false|
|Demangler GNU.Demangler Format|AUTO|
|Demangler GNU.Use Deprecated Demangler|false|
|Disassemble Entry Points|true|
|Disassemble Entry Points.Respect Execute Flag|true|
|ELF Scalar Operand References|false|
|ELF Scalar Operand References.Relocation Table Guide|true|
|Embedded Media|true|
|Embedded Media.Create Analysis Bookmarks|true|
|External Entry References|true|
|External Symbol Resolver|true|
|Function Start Search|true|
|Function Start Search.Bookmark Functions|false|
|Function Start Search.Search Data Blocks|false|
|GCC Exception Handlers|true|
|GCC Exception Handlers.Create Try Catch Comments|true|
|MIPS Constant Reference Analyzer|true|
|MIPS Constant Reference Analyzer.Assume T9 set to Function entry|true|
|MIPS Constant Reference Analyzer.Attempt to recover switch tables|false|
|MIPS Constant Reference Analyzer.Create Data from pointer|false|
|MIPS Constant Reference Analyzer.Function parameter/return Pointer analysis|true|
|MIPS Constant Reference Analyzer.Mark dual instruction references|false|
|MIPS Constant Reference Analyzer.Max Threads|2|
|MIPS Constant Reference Analyzer.Min absolute reference|4|
|MIPS Constant Reference Analyzer.Recover global GP register writes|true|
|MIPS Constant Reference Analyzer.Require pointer param data type|false|
|MIPS Constant Reference Analyzer.Speculative reference max|256|
|MIPS Constant Reference Analyzer.Speculative reference min|512|
|MIPS Constant Reference Analyzer.Stored Value Pointer analysis|true|
|MIPS Constant Reference Analyzer.Trust values read from writable memory|true|
|MIPS Symbol|true|
|MIPS UnAlligned Instruction Fix|true|
|Non-Returning Functions - Discovered|true|
|Non-Returning Functions - Discovered.Create Analysis Bookmarks|true|
|Non-Returning Functions - Discovered.Function Non-return Threshold|3|
|Non-Returning Functions - Discovered.Repair Flow Damage|true|
|Non-Returning Functions - Known|true|
|Non-Returning Functions - Known.Create Analysis Bookmarks|true|
|Reference|true|
|Reference.Address Table Alignment|1|
|Reference.Address Table Minimum Size|3|
|Reference.Align End of Strings|false|
|Reference.Ascii String References|true|
|Reference.Create Address Tables|false|
|Reference.Minimum String Length|5|
|Reference.References to Pointers|true|
|Reference.Relocation Table Guide|true|
|Reference.Respect Execute Flag|true|
|Reference.Subroutine References|true|
|Reference.Switch Table References|false|
|Reference.Unicode String References|true|
|Shared Return Calls|true|
|Shared Return Calls.Allow Conditional Jumps|false|
|Shared Return Calls.Assume Contiguous Functions Only|false|
|Stack|true|
|Stack.Create Local Variables|true|
|Stack.Create Param Variables|true|
|Stack.useNewFunctionStackAnalysis|true|
|Subroutine References|true|
|Subroutine References.Create Thunks Early|true|
|Variadic Function Signature Override|false|
|Variadic Function Signature Override.Create Analysis Bookmarks|false|

</details>


<details>
<summary>Ghidra AC9_httpd Decompiler Options</summary>


|Decompiler Option|Value|
| :---: | :---: |
|Prototype Evaluation|__stdcall|

</details>


<details>
<summary>Ghidra AC9_httpd Specification extensions Options</summary>


|Specification extensions Option|Value|
| :---: | :---: |
|FormatVersion|0|
|VersionCounter|0|

</details>


<details>
<summary>Ghidra AC9_httpd Analyzers Options</summary>


|Analyzers Option|Value|
| :---: | :---: |
|ASCII Strings|true|
|ASCII Strings.Create Strings Containing Existing Strings|true|
|ASCII Strings.Create Strings Containing References|true|
|ASCII Strings.Force Model Reload|false|
|ASCII Strings.Minimum String Length|LEN_5|
|ASCII Strings.Model File|StringModel.sng|
|ASCII Strings.Require Null Termination for String|true|
|ASCII Strings.Search Only in Accessible Memory Blocks|true|
|ASCII Strings.String Start Alignment|ALIGN_1|
|ASCII Strings.String end alignment|4|
|Aggressive Instruction Finder|false|
|Aggressive Instruction Finder.Create Analysis Bookmarks|true|
|Apply Data Archives|true|
|Apply Data Archives.Archive Chooser|[Auto-Detect]|
|Apply Data Archives.Create Analysis Bookmarks|true|
|Apply Data Archives.GDT User File Archive Path|None|
|Apply Data Archives.User Project Archive Path|None|
|Call Convention ID|true|
|Call Convention ID.Analysis Decompiler Timeout (sec)|60|
|Call-Fixup Installer|true|
|Condense Filler Bytes|false|
|Condense Filler Bytes.Filler Value|Auto|
|Condense Filler Bytes.Minimum number of sequential bytes|1|
|Create Address Tables|true|
|Create Address Tables.Allow Offcut References|false|
|Create Address Tables.Auto Label Table|false|
|Create Address Tables.Create Analysis Bookmarks|true|
|Create Address Tables.Maxmimum Pointer Distance|16777215|
|Create Address Tables.Minimum Pointer Address|4132|
|Create Address Tables.Minimum Table Size|3|
|Create Address Tables.Pointer Alignment|1|
|Create Address Tables.Relocation Table Guide|true|
|Create Address Tables.Table Alignment|4|
|DWARF|true|
|DWARF.Add Inlined Functions Comments|false|
|DWARF.Add Lexical Block Comments|false|
|DWARF.Create Function Signatures|true|
|DWARF.Import Data Types|true|
|DWARF.Import Functions|true|
|DWARF.Import Local Variable Info|true|
|DWARF.Output DWARF DIE Info|false|
|DWARF.Output Source Info|false|
|DWARF.Output Source Line Info|false|
|DWARF.Try To Pack Structs|true|
|Data Reference|true|
|Data Reference.Address Table Alignment|1|
|Data Reference.Address Table Minimum Size|3|
|Data Reference.Align End of Strings|false|
|Data Reference.Ascii String References|true|
|Data Reference.Create Address Tables|false|
|Data Reference.Minimum String Length|5|
|Data Reference.References to Pointers|true|
|Data Reference.Relocation Table Guide|true|
|Data Reference.Respect Execute Flag|true|
|Data Reference.Subroutine References|true|
|Data Reference.Switch Table References|false|
|Data Reference.Unicode String References|true|
|Decompiler Parameter ID|true|
|Decompiler Parameter ID.Analysis Clear Level|ANALYSIS|
|Decompiler Parameter ID.Analysis Decompiler Timeout (sec)|60|
|Decompiler Parameter ID.Commit Data Types|true|
|Decompiler Parameter ID.Commit Void Return Values|false|
|Decompiler Parameter ID.Prototype Evaluation|__stdcall|
|Decompiler Switch Analysis|true|
|Decompiler Switch Analysis.Analysis Decompiler Timeout (sec)|60|
|Demangler GNU|true|
|Demangler GNU.Apply Function Calling Conventions|true|
|Demangler GNU.Apply Function Signatures|true|
|Demangler GNU.Demangle Only Known Mangled Symbols|false|
|Demangler GNU.Demangler Format|AUTO|
|Demangler GNU.Use Deprecated Demangler|false|
|Disassemble Entry Points|true|
|Disassemble Entry Points.Respect Execute Flag|true|
|ELF Scalar Operand References|false|
|ELF Scalar Operand References.Relocation Table Guide|true|
|Embedded Media|true|
|Embedded Media.Create Analysis Bookmarks|true|
|External Entry References|true|
|External Symbol Resolver|true|
|Function Start Search|true|
|Function Start Search.Bookmark Functions|false|
|Function Start Search.Search Data Blocks|false|
|GCC Exception Handlers|true|
|GCC Exception Handlers.Create Try Catch Comments|true|
|MIPS Constant Reference Analyzer|true|
|MIPS Constant Reference Analyzer.Assume T9 set to Function entry|true|
|MIPS Constant Reference Analyzer.Attempt to recover switch tables|false|
|MIPS Constant Reference Analyzer.Create Data from pointer|false|
|MIPS Constant Reference Analyzer.Function parameter/return Pointer analysis|true|
|MIPS Constant Reference Analyzer.Mark dual instruction references|false|
|MIPS Constant Reference Analyzer.Max Threads|2|
|MIPS Constant Reference Analyzer.Min absolute reference|4|
|MIPS Constant Reference Analyzer.Recover global GP register writes|true|
|MIPS Constant Reference Analyzer.Require pointer param data type|false|
|MIPS Constant Reference Analyzer.Speculative reference max|256|
|MIPS Constant Reference Analyzer.Speculative reference min|512|
|MIPS Constant Reference Analyzer.Stored Value Pointer analysis|true|
|MIPS Constant Reference Analyzer.Trust values read from writable memory|true|
|MIPS Symbol|true|
|MIPS UnAlligned Instruction Fix|true|
|Non-Returning Functions - Discovered|true|
|Non-Returning Functions - Discovered.Create Analysis Bookmarks|true|
|Non-Returning Functions - Discovered.Function Non-return Threshold|3|
|Non-Returning Functions - Discovered.Repair Flow Damage|true|
|Non-Returning Functions - Known|true|
|Non-Returning Functions - Known.Create Analysis Bookmarks|true|
|Reference|true|
|Reference.Address Table Alignment|1|
|Reference.Address Table Minimum Size|3|
|Reference.Align End of Strings|false|
|Reference.Ascii String References|true|
|Reference.Create Address Tables|false|
|Reference.Minimum String Length|5|
|Reference.References to Pointers|true|
|Reference.Relocation Table Guide|true|
|Reference.Respect Execute Flag|true|
|Reference.Subroutine References|true|
|Reference.Switch Table References|false|
|Reference.Unicode String References|true|
|Shared Return Calls|true|
|Shared Return Calls.Allow Conditional Jumps|false|
|Shared Return Calls.Assume Contiguous Functions Only|false|
|Stack|true|
|Stack.Create Local Variables|true|
|Stack.Create Param Variables|true|
|Stack.useNewFunctionStackAnalysis|true|
|Subroutine References|true|
|Subroutine References.Create Thunks Early|true|
|Variadic Function Signature Override|false|
|Variadic Function Signature Override.Create Analysis Bookmarks|false|

</details>

## Diff Stats



|Stat|Value|
| :---: | :---: |
|added_funcs_len|17|
|deleted_funcs_len|0|
|modified_funcs_len|28|
|added_symbols_len|64|
|deleted_symbols_len|64|
|diff_time|39.78942942619324|
|deleted_strings_len|154|
|added_strings_len|212|
|match_types|Counter({'SymbolsHash': 1672, 'ExternalsName': 280, 'StructuralGraphHash': 14, 'ExactInstructionsFunctionHasher': 4, 'StrUniqueFuncRefsHasher': 2})|
|items_to_process|173|
|diff_types|Counter({'address': 28, 'refcount': 15, 'calling': 14, 'code': 13, 'length': 13, 'called': 8})|
|unmatched_funcs_len|17|
|total_funcs_len|3953|
|matched_funcs_len|3936|
|matched_funcs_with_code_changes_len|13|
|matched_funcs_with_non_code_changes_len|15|
|matched_funcs_no_changes_len|3908|
|match_func_similarity_percent|99.2886%|
|func_match_overall_percent|99.5699%|
|first_matches|Counter({'SymbolsHash': 1672, 'StructuralGraphHash': 14, 'ExactInstructionsFunctionHasher': 4, 'StrUniqueFuncRefsHasher': 2})|



```mermaid
pie showData
    title All Matches
"SymbolsHash" : 1672
"ExternalsName" : 280
"ExactInstructionsFunctionHasher" : 4
"StrUniqueFuncRefsHasher" : 2
"StructuralGraphHash" : 14
```



```mermaid
pie showData
    title First Matches
"SymbolsHash" : 1672
"ExactInstructionsFunctionHasher" : 4
"StrUniqueFuncRefsHasher" : 2
"StructuralGraphHash" : 14
```



```mermaid
pie showData
    title Diff Stats
"added_funcs_len" : 17
"deleted_funcs_len" : 0
"modified_funcs_len" : 28
```



```mermaid
pie showData
    title Symbols
"added_symbols_len" : 64
"deleted_symbols_len" : 64
```

## Strings



```mermaid
pie showData
    title Strings
"deleted_strings_len" : 154
"added_strings_len" : 212
```

### Strings Diff


```diff
--- deleted strings
+++ added strings
@@ -1,154 +1,212 @@
-__FUNCTION__.10180
-__FUNCTION__.12612
-__FUNCTION__.4005
-__FUNCTION__.4055
-__FUNCTION__.4125
-__FUNCTION__.4510
-__FUNCTION__.4621
-__FUNCTION__.4670
-__FUNCTION__.4834
-__FUNCTION__.6454
-__FUNCTION__.6515
-__FUNCTION__.6541
-__FUNCTION__.6633
-__FUNCTION__.6665
-__FUNCTION__.6722
-__FUNCTION__.6740
-__FUNCTION__.6748
-__FUNCTION__.7081
-__FUNCTION__.7207
-__FUNCTION__.7217
-__FUNCTION__.7280
-__FUNCTION__.7287
-__FUNCTION__.7492
-__FUNCTION__.7657
-__FUNCTION__.7712
-__FUNCTION__.7731
-__FUNCTION__.7793
-__FUNCTION__.8100
-__FUNCTION__.8144
-__FUNCTION__.8225
-__FUNCTION__.8231
-__FUNCTION__.8345
-__FUNCTION__.8430
-__FUNCTION__.8490
-__FUNCTION__.8544
-__FUNCTION__.8597
-__FUNCTION__.8642
-__FUNCTION__.8672
-__FUNCTION__.9836
-__FUNCTION__.9860
-__PRETTY_FUNCTION__.4274
-__PRETTY_FUNCTION__.4298
-__PRETTY_FUNCTION__.4316
-__PRETTY_FUNCTION__.4337
-__PRETTY_FUNCTION__.4370
-__PRETTY_FUNCTION__.4402
-__PRETTY_FUNCTION__.4444
-__PRETTY_FUNCTION__.4746
-__PRETTY_FUNCTION__.4797
-__PRETTY_FUNCTION__.4833
-__func__.10026
-__func__.10075
-__func__.10113
-__func__.10179
-__func__.10188
-__func__.10229
-__func__.10273
-__func__.10274
-__func__.10379
-__func__.10421
-__func__.10483
-__func__.10568
-__func__.10636
-__func__.10658
-__func__.10703
-__func__.10732
-__func__.10823
-__func__.10874
-__func__.10891
-__func__.10980
-__func__.11096
-__func__.11151
-__func__.11174
-__func__.11219
-__func__.11286
-__func__.11363
-__func__.11424
-__func__.11451
-__func__.11484
-__func__.11486
-__func__.11545
-__func__.11672
-__func__.11683
-__func__.11724
-__func__.11744
-__func__.11789
-__func__.11809
-__func__.11890
-__func__.12013
-__func__.12040
-__func__.12088
-__func__.12110
-__func__.12221
-__func__.12234
-__func__.12253
-__func__.12296
-__func__.12398
-__func__.12477
-__func__.12501
-__func__.12536
-__func__.12624
-__func__.12667
-__func__.12754
-__func__.12811
-__func__.12860
-__func__.12918
-__func__.12956
-__func__.13003
-__func__.13123
-__func__.13349
-__func__.13418
-__func__.2596
-__func__.2657
-__func__.6207
-__func__.6253
-__func__.6348
-__func__.6892
-__func__.6972
-__func__.7734
-__func__.7781
-__func__.7838
-__func__.7843
-__func__.7877
-__func__.7911
-__func__.8003
-__func__.8031
-__func__.8047
-__func__.8048
-__func__.8112
-__func__.8283
-__func__.8407
-__func__.8423
-__func__.8490
-__func__.8552
-__func__.8710
-__func__.8745
-__func__.9132
-__func__.9140
-__func__.9296
-__func__.9359
-__func__.9417
-__func__.9529
-__func__.9754
-__func__.9771
-__func__.9840
-__func__.9867
-__func__.9925
-__func__.9927
-__func__.9985
-s_11:10:31
-s_Aug
-s_V15.03.06.23
-s_countryCode
-s_nextzone_=_%s
+__FUNCTION__.10290
+__FUNCTION__.12722
+__FUNCTION__.4017
+__FUNCTION__.4067
+__FUNCTION__.4137
+__FUNCTION__.4522
+__FUNCTION__.4633
+__FUNCTION__.4682
+__FUNCTION__.4846
+__FUNCTION__.6478
+__FUNCTION__.6527
+__FUNCTION__.6553
+__FUNCTION__.6627
+__FUNCTION__.6655
+__FUNCTION__.6709
+__FUNCTION__.6727
+__FUNCTION__.6735
+__FUNCTION__.7093
+__FUNCTION__.7194
+__FUNCTION__.7204
+__FUNCTION__.7266
+__FUNCTION__.7273
+__FUNCTION__.7478
+__FUNCTION__.7698
+__FUNCTION__.7717
+__FUNCTION__.7767
+__FUNCTION__.7903
+__FUNCTION__.8210
+__FUNCTION__.8254
+__FUNCTION__.8334
+__FUNCTION__.8341
+__FUNCTION__.8456
+__FUNCTION__.8540
+__FUNCTION__.8600
+__FUNCTION__.8654
+__FUNCTION__.8707
+__FUNCTION__.8752
+__FUNCTION__.8782
+__FUNCTION__.9946
+__FUNCTION__.9970
+__PRETTY_FUNCTION__.4286
+__PRETTY_FUNCTION__.4310
+__PRETTY_FUNCTION__.4328
+__PRETTY_FUNCTION__.4349
+__PRETTY_FUNCTION__.4382
+__PRETTY_FUNCTION__.4414
+__PRETTY_FUNCTION__.4456
+__PRETTY_FUNCTION__.4758
+__PRETTY_FUNCTION__.4809
+__PRETTY_FUNCTION__.4845
+__func__.10035
+__func__.10037
+__func__.10095
+__func__.10136
+__func__.10185
+__func__.10223
+__func__.10289
+__func__.10298
+__func__.10339
+__func__.10383
+__func__.10384
+__func__.10490
+__func__.10531
+__func__.10593
+__func__.10678
+__func__.10746
+__func__.10768
+__func__.10813
+__func__.10843
+__func__.10933
+__func__.11001
+__func__.11090
+__func__.11094
+__func__.11206
+__func__.11261
+__func__.11284
+__func__.11329
+__func__.11396
+__func__.11473
+__func__.11535
+__func__.11561
+__func__.11595
+__func__.11596
+__func__.11655
+__func__.11793
+__func__.11805
+__func__.11834
+__func__.11877
+__func__.11899
+__func__.11941
+__func__.12000
+__func__.12123
+__func__.12150
+__func__.12198
+__func__.12236
+__func__.12331
+__func__.12344
+__func__.12363
+__func__.12406
+__func__.12508
+__func__.12587
+__func__.12611
+__func__.12646
+__func__.12864
+__func__.12921
+__func__.12954
+__func__.12978
+__func__.12997
+__func__.13028
+__func__.13066
+__func__.13113
+__func__.13241
+__func__.13467
+__func__.13536
+__func__.2608
+__func__.2669
+__func__.6219
+__func__.6265
+__func__.6360
+__func__.6879
+__func__.6959
+__func__.7767
+__func__.7829
+__func__.7844
+__func__.7948
+__func__.7987
+__func__.8021
+__func__.8034
+__func__.8113
+__func__.8141
+__func__.8157
+__func__.8222
+__func__.8393
+__func__.8517
+__func__.8533
+__func__.8600
+__func__.8662
+__func__.8820
+__func__.8855
+__func__.9242
+__func__.9250
+__func__.9369
+__func__.9406
+__func__.9469
+__func__.9527
+__func__.9639
+__func__.9864
+__func__.9881
+__func__.9950
+__func__.9977
+s_%[^:]:%[^*]*%s
+s_%[^;];%[^;];%[^_]
+s_%s_%d:_getWanIfName_return_NULL
+s_*******_unlink_/tmp/smbpasswd_is
+s_/tmp/UDiskname
+s_/tmp/smbpasswd
+s_/tmp/usb/PrinterName
+s_/tmp/usb/UsbVolumeInfo
+s_/var/etc/upan
+s_10:27:30
+s_Feb
+s_GetPrinterCfg
+s_GetSambaCfg
+s_GetUSBStatus
+s_GetUsbCfg
+s_SetPrinterCfg
+s_SetSambaCfg
+s_V15.03.06.42
+s_admin
+s_busybox_deluser_%s
+s_cfm_post_netctrl_%d?op=%d,string
+s_devId
+s_diskList
+s_diskName
+s_dlna.en
+s_fileCode
+s_fileshare
+s_ftpLink
+s_guestaccess
+s_guestpwd
+s_guestuser
+s_hasusb
+s_insmod_/lib/modules/2.6.36.4brcm
+s_internetLink
+s_internetPort
+s_memoryTotal
+s_memoryUnUse
+s_premitEn
+s_printer
+s_printerEn
+s_setUsbUnload
+s_smbpasswd_-a_%s_-s_<_/tmp/smbpas
+s_usb.ftp.charset
+s_usb.ftp.guest.acess
+s_usb.ftp.guest.pwd
+s_usb.ftp.guest.user
+s_usb.ftp.port
+s_usb.ftp.pwd
+s_usb.ftp.remote.acess
+s_usb.ftp.remote.port
+s_usb.ippd.enable
+s_usb.samba.enable
+s_usb.samba.guest.acess
+s_usb.samba.guest.pwd
+s_usb.samba.guest.user
+s_usb.samba.pwd
+s_usb.samba.user
+s_usbList
+s_usbName
+s_usbNum
+s_usb_total=%s,usb_usable=%s
+s_{"printerEn":"%d","printerName":

```


### String References

#### Old



|String|Ref Count|Ref Func|
| :---: | :---: | :---: |
|__func__.7843|1|ate_iwpriv_set|
|__FUNCTION__.7207|1|ate_Tenda_mfg_check_usb|
|__func__.9529|10|get_online_dev_list|
|__FUNCTION__.7492|1|ate_Tenda_mfg_LanWanInfo|
|__func__.11486|1|formWifiStatistic|
|__FUNCTION__.7280|1|ate_Tenda_mfg_reboot|
|__func__.12667|1|parse_ssid_from_file|
|__func__.11545|1|formWifiDhcpGuestGet|
|__func__.7877|11|fromAdvSetLanip|
|__func__.12860|1|formSetQosBand|
|__func__.11744|1|formsetNotUpgrade|
|__FUNCTION__.8144|6|_query_upgrade_|
|s_countryCode_0050ec18|1|form_fast_setting_get|
|__func__.12624|1|set_cn_ssid_ori_encode|
|__PRETTY_FUNCTION__.4370|2|check_number_range|
|__func__.6253|1|CreateDhcpsConfigFile|
|__FUNCTION__.7217|1|ate_Tenda_mfg_check_usb3|
|__func__.7838|4|get_idle_rule_id|
|__func__.11683|1|formWifiStatus|
|__func__.10188|2|parse_macfilter_rule|
|__FUNCTION__.8672|2|send_login_sta_update|
|__func__.9985|2|set_macfilter_rules|
|__func__.11363|4|get_delete_pos|
|__FUNCTION__.8597|1|cloudv2_manage|
|__func__.10568|4|get_macfilter_rule_index|
|__FUNCTION__.8490|1|setbasic|
|s_11:10:31_0050813c|1|get_compile_date_time|
|__func__.12040|2|formWifiWpsOOB|
|__func__.10891|5|delete_id_from_rule_list_id|
|__func__.11151|3|get_device_name|
|__FUNCTION__.6454|1|formSetIptv|
|__FUNCTION__.7793|1|formSetRebootTimer|
|__FUNCTION__.6541|3|ali_get_statistic_info|
|__func__.7911|5|set_wl_guest_iplist|
|__func__.10732|9|formGetSystemStatus|
|__func__.9296|4|get_local_host_info|
|__func__.9840|5|formSetMacFilterCfg|
|__FUNCTION__.12612|1|set_value_by_def|
|__func__.11424|2|get_black_num|
|__func__.11724|2|formWifiWpsGet|
|__func__.8048|1|ate_rtl_cmd_process_check|
|__func__.11219|3|is_mac_existed_in_rule_list|
|s_V15.03.06.23_0050c058|1|aspTendaGetStatus|
|__func__.11451|1|formWifiPowerGet|
|__FUNCTION__.4621|1|get_str_after_delimiter|
|__FUNCTION__.7287|1|ate_Tenda_mfg_default|
|__func__.9927|3|set_macfilter_mode|
|__func__.10636|1|set_macfilter_rule_to_list|
|__func__.11096|3|set_device_name|
|__func__.13418|1|formGetHomeLink|
|__func__.12088|2|formWifiWpsSet|
|__FUNCTION__.4125|1|bm_alloc_buff|
|__func__.13003|1|volidate_wds_maclist|
|__func__.9359|3|get_macfilter_mode|
|__FUNCTION__.6722|1|ate_nvram_set_country|
|__func__.12754|1|volidate_range|
|__func__.11484|3|check_mac_in_blacklist|
|__func__.10273|9|reload_macfilter_rules_to_wireless|
|__func__.10421|9|formAddMacfilterRule|
|__func__.8283|1|webCgiGetUploadFile|
|__FUNCTION__.6740|1|ate_nvram_set_profile|
|__func__.6348|1|CreateDhcps2ConfigFile|
|__FUNCTION__.4005|1|bm_get_id_list|
|__FUNCTION__.8544|2|setaccount|
|__func__.8710|2|get_panic_file|
|__func__.12398|4|get_wifi_ifname|
|__PRETTY_FUNCTION__.4316|2|save_value|
|__func__.12477|1|get_ssid_num_by_mode|
|__func__.10075|2|unset_macfilter_rules|
|s_nextzone_=_%s_0051a5f8|1|fromGetSysTime|
|__func__.8552|1|uploadPolicy|
|__func__.11890|3|wps_restore_mib_default_value|
|__func__.7734|4|setQosMiblist|
|__FUNCTION__.6665|1|ate_nvram_set_maxpower_5G|
|__func__.8423|5|upgrade|
|__func__.10823|3|delete_macfilter_rule_by_mac|
|__func__.12501|1|get_all_ssid_on_off|
|__func__.12536|1|set_all_ssid_on_off|
|__PRETTY_FUNCTION__.4833|4|ip_pool_check|
|__PRETTY_FUNCTION__.4402|1|ip_addr_is_valid|
|__PRETTY_FUNCTION__.4298|2|get_value_f|
|__func__.10113|5|unset_wireless_macfilter_rules|
|__func__.11789|2|formWifiWpsStart|
|__func__.10179|1|formWifiBasicSet|
|__func__.11672|1|check_mac_in_parentctrl_list|
|__FUNCTION__.10180|1|exchange_wan_action|
|__func__.10229|2|set_macfilter_list_id|
|__func__.6207|1|initWebs|
|__FUNCTION__.6633|1|ate_nvram_set_maxpower_2G|
|__FUNCTION__.6515|1|get_online_ip_count|
|__func__.12221|1|init_global_wifi_buf|
|__func__.9867|3|formWifiMultiSsid|
|__func__.8003|7|unset_wl_guest_list|
|__FUNCTION__.7731|1|ate_wlctrl_get|
|__PRETTY_FUNCTION__.4746|2|check_reserve_network|
|__func__.10874|1|check_param_changed|
|__func__.9132|8|formGetMacFilterCfg|
|__PRETTY_FUNCTION__.4337|1|save_value_array|
|__func__.10658|2|add_id_to_rule_list_id|
|__func__.11174|1|formWifiRadioGet|
|__func__.8407|1|have_enough_mem|
|__func__.10379|1|formGetWanStatistic|
|__FUNCTION__.8225|1|form_fast_setting_wifi_set|
|__FUNCTION__.9860|1|saveParentControlInfo|
|__func__.7781|1|iwpriv_wlan_set|
|__func__.10483|1|formWanInfoGet|
|__func__.9417|5|get_macfilter_rule|
|__FUNCTION__.8231|1|prod_new_ack|
|__func__.12956|1|validate_hwaddr|
|__func__.8031|1|fromSetIpMacBind|
|__FUNCTION__.7657|1|get_online_ip_info|
|__func__.13349|3|check_vendor_from_offline_list|
|__FUNCTION__.8345|1|check_pptp_user_if_login|
|__func__.12811|2|volidate_wep_key|
|__func__.9140|1|UploadWebsite|
|__func__.6892|8|ate_rtl_set_prod_arg|
|__func__.2657|4|parse_response_string|
|__func__.2596|5|get_advertise_url_from_cloud|
|__func__.12296|1|set_idx_to_mib|
|__func__.10026|3|set_macfilter_rules_by_one|
|__func__.10274|1|formSetParentControlEnable|
|__func__.12918|1|volidate_wpa_key|
|__func__.12234|1|get_mib_2cJSONString|
|__func__.8745|1|get_log_file|
|__func__.8112|1|formAdvGetLanIp|
|__func__.12013|1|wps_restore_nvram_default_value|
|__FUNCTION__.7712|1|ate_wlctrl_set|
|__PRETTY_FUNCTION__.4797|2|validate_ip_mask|
|__FUNCTION__.6748|1|ate_nvram_set_test|
|__func__.9925|1|formWifiBasicGet|
|__FUNCTION__.8642|1|ucloud_v2_init|
|__FUNCTION__.4670|1|get_netmask_by_num|
|__func__.13123|5|formGetParentCtrlList|
|__func__.9754|4|is_lan_host|
|__func__.10980|4|formWifiMacFilterGet|
|__func__.11809|5|formGetRouterStatus|
|__FUNCTION__.8100|3|_query_version_|
|__FUNCTION__.9836|1|do_wifi_handle|
|__func__.10703|7|formDelMacfilterRule|
|__FUNCTION__.4510|2|cgi_del_much_rule|
|__PRETTY_FUNCTION__.4444|3|cgi_detect_field_sameness|
|__PRETTY_FUNCTION__.4274|1|cgi_request_str2num|
|__FUNCTION__.8430|1|_cgi_query_uc_account_|
|__FUNCTION__.7081|1|wan_lan_same_deal|
|s_Aug_9_2018_0050c11c|1|aspTendaGetStatus|
|__func__.12110|5|formGetOnlineList|
|__FUNCTION__.4055|1|mac_str2num|
|__func__.8047|2|is_wan_onlined|
|__func__.6972|8|ate_rtl_set_hw_wlan|
|__func__.11286|5|update_mac_filter_enable_flag|
|__func__.8490|1|UploadCfg|
|__FUNCTION__.4834|1|ip_pool_check|
|__func__.12253|1|get_index_mib_2cJSONString|
|__func__.9771|1|string_replace|

#### New



|String|Ref Count|Ref Func|
| :---: | :---: | :---: |
|__func__.12997|2|volidate_ip|
|__func__.9639|10|get_online_dev_list|
|__FUNCTION__.7698|1|ate_wlctrl_set|
|__func__.10843|9|formGetSystemStatus|
|s_usb.samba.guest.acess_005203d4|2|formSetSambaConf,formGetSambaConf|
|__func__.10035|1|formWifiBasicGet|
|__func__.7844|4|setQosMiblist|
|__FUNCTION__.8210|3|_query_version_|
|s_GetSambaCfg_0050d2dc|1|formDefineTendDa|
|s_usb.ftp.port_005204a4|1|formGetSambaConf|
|__FUNCTION__.8782|2|send_login_sta_update|
|__func__.12611|1|get_all_ssid_on_off|
|__func__.10339|2|set_macfilter_list_id|
|__func__.7767|1|iwpriv_wlan_set|
|__func__.11261|3|get_device_name|
|__func__.10223|5|unset_wireless_macfilter_rules|
|s_guestaccess_0052033c|2|formSetSambaConf,formGetSambaConf|
|__func__.11805|1|check_mac_in_parentctrl_list|
|__FUNCTION__.7093|1|wan_lan_same_deal|
|s_%s_%d:_getWanIfName_return_NULL_005204e4|1|formGetSambaConf|
|__func__.10037|3|set_macfilter_mode|
|__func__.10298|2|parse_macfilter_rule|
|s_GetUsbCfg_0050d2f8|1|formDefineTendDa|
|__FUNCTION__.8334|1|form_fast_setting_wifi_set|
|s_SetPrinterCfg_0050d2b0|1|formDefineTendDa|
|s_Feb_6_2018_0050e8bc|1|aspTendaGetStatus|
|s_fileshare_00520628|2|formGetUSBStatus|
|__func__.8820|2|get_panic_file|
|__FUNCTION__.8600|1|setbasic|
|s_busybox_deluser_%s_0052039c|1|formSetSambaConf|
|__func__.10531|9|formAddMacfilterRule|
|__func__.11899|2|formWifiWpsStart|
|s_usb.ftp.pwd_005203ec|1|formSetSambaConf|
|__FUNCTION__.8456|1|check_pptp_user_if_login|
|s_insmod_/lib/modules/2.6.36.4brcm_0051fde4|1|fromSetWirelessRepeat|
|__func__.12864|1|volidate_range|
|__func__.9864|4|is_lan_host|
|__PRETTY_FUNCTION__.4414|1|ip_addr_is_valid|
|__func__.9527|5|get_macfilter_rule|
|__PRETTY_FUNCTION__.4328|2|save_value|
|__FUNCTION__.10290|1|exchange_wan_action|
|__PRETTY_FUNCTION__.4382|2|check_number_range|
|__FUNCTION__.4633|1|get_str_after_delimiter|
|__FUNCTION__.9970|1|saveParentControlInfo|
|__func__.6879|8|ate_rtl_set_prod_arg|
|s_%[^;];%[^;];%[^_]_00520680|1|formGetUsbCfg|
|s_/tmp/usb/PrinterName_00520298|1|formGetUsbPrint|
|__func__.12000|3|wps_restore_mib_default_value|
|s_usb.ftp.guest.acess_00520420|1|formSetSambaConf|
|__func__.7829|1|ate_iwpriv_set|
|__func__.8662|1|uploadPolicy|
|__FUNCTION__.6553|3|ali_get_statistic_info|
|__FUNCTION__.6735|1|ate_nvram_set_test|
|__FUNCTION__.4137|1|bm_alloc_buff|
|__func__.11595|3|check_mac_in_blacklist|
|__FUNCTION__.7717|1|ate_wlctrl_get|
|s_premitEn_005202f0|2|formSetSambaConf,formGetSambaConf|
|__func__.10768|2|add_id_to_rule_list_id|
|s_diskName_005206e4|1|formGetUsbCfg|
|__FUNCTION__.8254|6|_query_upgrade_|
|s_usb.ftp.remote.acess_00520434|3|formGetUSBStatus,formSetSambaConf,formGetSambaConf|
|s_V15.03.06.42_0050e7f8|1|aspTendaGetStatus|
|__FUNCTION__.6627|1|ate_nvram_set_maxpower_2G|
|__FUNCTION__.8707|1|cloudv2_manage|
|s_*******_unlink_/tmp/smbpasswd_is_00520550|1|fill_smbpasswd_input_file|
|__func__.11396|5|update_mac_filter_enable_flag|
|__FUNCTION__.4522|2|cgi_del_much_rule|
|__func__.6959|8|ate_rtl_set_hw_wlan|
|__func__.12198|2|formWifiWpsSet|
|__func__.11094|6|formGetMacfilterRuleList|
|__func__.9369|1|formGetSambaConf|
|__PRETTY_FUNCTION__.4349|1|save_value_array|
|__PRETTY_FUNCTION__.4286|1|cgi_request_str2num|
|__func__.13241|5|formGetParentCtrlList|
|__FUNCTION__.6655|1|ate_nvram_set_maxpower_5G|
|__func__.11793|1|formWifiStatus|
|__func__.9406|4|get_local_host_info|
|__FUNCTION__.7478|1|ate_Tenda_mfg_LanWanInfo|
|__PRETTY_FUNCTION__.4809|2|validate_ip_mask|
|s_memoryTotal_005206fc|1|formGetUsbCfg|
|__FUNCTION__.7903|1|formSetRebootTimer|
|__func__.11206|3|set_device_name|
|s_usb.ftp.guest.user_005203f8|1|formSetSambaConf|
|s_{"printerEn":"%d","printerName":_005202b4|1|formGetUsbPrint|
|__func__.10095|2|set_macfilter_rules|
|s_diskList_005206a4|1|formGetUsbCfg|
|__func__.10746|1|set_macfilter_rule_to_list|
|s_usb.samba.enable_00520470|1|formSetSambaConf|
|__func__.12921|2|volidate_wep_key|
|__func__.10678|4|get_macfilter_rule_index|
|__FUNCTION__.7767|1|get_online_ip_info|
|__func__.12406|1|set_idx_to_mib|
|__FUNCTION__.4017|1|bm_get_id_list|
|__func__.13066|1|validate_hwaddr|
|s_%[^:]:%[^*]*%s_005206b0|1|formGetUsbCfg|
|s_/tmp/UDiskname_0051fad8|1|Usb_Up|
|__func__.6219|1|initWebs|
|__func__.10593|1|formWanInfoGet|
|s_devId_0052069c|1|formGetUsbCfg|
|__FUNCTION__.7266|1|ate_Tenda_mfg_reboot|
|__func__.12123|1|wps_restore_nvram_default_value|
|s_usb.ftp.remote.port_0052044c|2|formSetSambaConf,formGetSambaConf|
|__func__.9977|3|formWifiMultiSsid|
|__func__.8855|1|get_log_file|
|__func__.10813|7|formDelMacfilterRule|
|__func__.7948|4|get_idle_rule_id|
|__func__.10289|1|formWifiBasicSet|
|__func__.12344|1|get_mib_2cJSONString|
|s_/var/etc/upan_00520634|1|formGetUSBStatus|
|__FUNCTION__.6478|3|ali_talking_with_kernel|
|__func__.11090|4|formWifiMacFilterGet|
|s_internetPort_005202fc|2|formSetSambaConf,formGetSambaConf|
|__func__.13028|1|volidate_wpa_key|
|__func__.8533|5|upgrade|
|__func__.10384|1|formSetParentControlEnable|
|__func__.8222|1|formAdvGetLanIp|
|__FUNCTION__.9946|1|do_wifi_handle|
|__func__.9469|3|get_macfilter_mode|
|__func__.8600|1|UploadCfg|
|__FUNCTION__.7194|1|ate_Tenda_mfg_check_usb|
|__func__.13536|1|formGetHomeLink|
|__func__.10490|1|formGetWanStatistic|
|__func__.10136|3|set_macfilter_rules_by_one|
|__PRETTY_FUNCTION__.4845|4|ip_pool_check|
|__func__.9881|1|string_replace|
|__func__.8113|7|unset_wl_guest_list|
|__func__.12150|2|formWifiWpsOOB|
|s_SetSambaCfg_0050d2d0|1|formDefineTendDa|
|__func__.12508|4|get_wifi_ifname|
|s_usb.samba.user_0052057c|1|writePasswd|
|__func__.11596|1|formWifiStatistic|
|__FUNCTION__.6727|1|ate_nvram_set_profile|
|__FUNCTION__.7204|1|ate_Tenda_mfg_check_usb3|
|__func__.12236|5|formGetOnlineList|
|__func__.11834|2|formWifiWpsGet|
|__FUNCTION__.6527|1|get_online_ip_count|
|__func__.12363|1|get_index_mib_2cJSONString|
|s_usbList_00520660|1|formGetUsbCfg|
|s_usbName_0052031c|1|formSetSambaConf|
|s_GetUSBStatus_0050d2a0|1|formDefineTendDa|
|__FUNCTION__.8341|1|prod_new_ack|
|__FUNCTION__.8540|1|_cgi_query_uc_account_|
|s_usb.samba.pwd_005203b0|3|writePasswd,formSetSambaConf,formGetSambaConf|
|__func__.13467|3|check_vendor_from_offline_list|
|__func__.12954|2|volidate_wpapsk_key|
|s_guestuser_00520330|2|formSetSambaConf,formGetSambaConf|
|s_cfm_post_netctrl_%d?op=%d,string_00520358|2|formSetSambaConf,formsetUsbUnload|
|s_dlna.en_00520614|1|formGetUSBStatus|
|__PRETTY_FUNCTION__.4310|2|get_value_f|
|__func__.8517|1|have_enough_mem|
|__FUNCTION__.4846|1|ip_pool_check|
|s_memoryUnUse_005206f0|1|formGetUsbCfg|
|s_printer_00520620|2|formGetUSBStatus|
|s_guestpwd_00520324|2|formSetSambaConf,formGetSambaConf|
|s_usb_total=%s,usb_usable=%s_005206c8|1|formGetUsbCfg|
|__func__.7987|11|fromAdvSetLanip|
|s_usb.ippd.enable_00520248|3|formGetUsbPrint,formGetUSBStatus,formSetUsbPrint|
|s_/tmp/smbpasswd_00520540|2|fill_smbpasswd_input_file|
|__func__.8021|5|set_wl_guest_iplist|
|__func__.9950|5|formSetMacFilterCfg|
|__func__.11877|1|formsetNotUpgrade|
|s_setUsbUnload_0050d2e8|1|formDefineTendDa|
|__FUNCTION__.6709|1|ate_nvram_set_country|
|s_/tmp/usb/UsbVolumeInfo_00520668|1|formGetUsbCfg|
|s_usbNum_00510808|1|formGetRouterStatus|
|__func__.11655|1|formWifiDhcpGuestGet|
|__func__.2669|4|parse_response_string|
|s_hasusb_00520644|2|formGetUSBStatus|
|__func__.12978|1|formSetQosBand|
|s_smbpasswd_-a_%s_-s_<_/tmp/smbpas_0052058c|1|writePasswd|
|s_printerEn_00520238|1|formSetUsbPrint|
|__func__.12646|1|set_all_ssid_on_off|
|__func__.11001|5|delete_id_from_rule_list_id|
|__func__.6360|1|CreateDhcps2ConfigFile|
|__func__.9242|8|formGetMacFilterCfg|
|__func__.12331|1|init_global_wifi_buf|
|__PRETTY_FUNCTION__.4456|3|cgi_detect_field_sameness|
|s_usb.samba.guest.user_00520384|3|formSetSambaConf,formGetSambaConf|
|s_ftpLink_00520514|1|formGetSambaConf|
|s_GetPrinterCfg_0050d2c0|1|formDefineTendDa|
|__func__.13113|1|volidate_wds_maclist|
|__func__.8393|1|webCgiGetUploadFile|
|__FUNCTION__.7273|1|ate_Tenda_mfg_default|
|__func__.8141|1|fromSetIpMacBind|
|__func__.11561|1|formWifiPowerGet|
|__FUNCTION__.8752|1|ucloud_v2_init|
|__func__.11329|3|is_mac_existed_in_rule_list|
|__func__.11284|1|formWifiRadioGet|
|__func__.8157|2|is_wan_onlined|
|__func__.9250|1|UploadWebsite|
|__func__.11941|5|formGetRouterStatus|
|__FUNCTION__.12722|1|set_value_by_def|
|s_admin_005202e8|3|writePasswd,formSetSambaConf|
|__func__.10383|9|reload_macfilter_rules_to_wireless|
|s_usb.ftp.guest.pwd_0052040c|1|formSetSambaConf|
|s_internetLink_0052051c|1|formGetSambaConf|
|__FUNCTION__.4682|1|get_netmask_by_num|
|s_usb.samba.guest.pwd_005203c0|2|formSetSambaConf,formGetSambaConf|
|s_fileCode_00520348|2|formSetSambaConf,formGetSambaConf|
|__func__.8034|1|ate_rtl_cmd_process_check|
|__func__.10933|3|delete_macfilter_rule_by_mac|
|__func__.12587|1|get_ssid_num_by_mode|
|__PRETTY_FUNCTION__.4758|2|check_reserve_network|
|__func__.11535|2|get_black_num|
|__func__.10185|2|unset_macfilter_rules|
|s_usb.ftp.charset_00520460|2|formSetSambaConf,formGetSambaConf|
|__func__.2608|5|get_advertise_url_from_cloud|
|__FUNCTION__.8654|2|setaccount|
|__func__.6265|1|CreateDhcpsConfigFile|
|s_10:27:30_0050a87c|1|get_compile_date_time|
|__FUNCTION__.4067|1|mac_str2num|
|__func__.11473|4|get_delete_pos|

# Deleted

# Added

## get_usb_device_num

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|get_usb_device_num|
|fullname|get_usb_device_num|
|refcount|4|
|length|336|
|called|<EXTERNAL>::fclose<br><EXTERNAL>::feof<br><EXTERNAL>::fgets<br><EXTERNAL>::fopen<br><EXTERNAL>::memset|
|calling|formGetRouterStatus|
|paramcount|0|
|address|0046c51c|
|sig|int __stdcall get_usb_device_num(void)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- get_usb_device_num
+++ get_usb_device_num
@@ -0,0 +1,28 @@
+
+int get_usb_device_num(void)
+
+{
+  FILE *__stream;
+  int iVar1;
+  char *pcVar2;
+  int local_110;
+  char acStack_108 [256];
+  
+  local_110 = 0;
+  memset(acStack_108,0,0x100);
+  __stream = fopen("/tmp/usb/UsbVolumeInfo","r");
+  if (__stream != (FILE *)0x0) {
+    while ((iVar1 = feof(__stream), iVar1 == 0 &&
+           (pcVar2 = fgets(acStack_108,0x100,__stream), pcVar2 != (char *)0x0))) {
+      local_110 = local_110 + 1;
+    }
+  }
+  if (__stream != (FILE *)0x0) {
+    fclose(__stream);
+  }
+  if (2 < local_110) {
+    local_110 = 2;
+  }
+  return local_110;
+}
+

```


## Usb_Up

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|Usb_Up|
|fullname|Usb_Up|
|refcount|2|
|length|312|
|called|<EXTERNAL>::doSystemCmd<br><EXTERNAL>::fclose<br><EXTERNAL>::feof<br><EXTERNAL>::fgets<br><EXTERNAL>::fopen|
|calling|fromSetWirelessRepeat|
|paramcount|0|
|address|004c203c|
|sig|undefined __stdcall Usb_Up(void)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- Usb_Up
+++ Usb_Up
@@ -0,0 +1,24 @@
+
+void Usb_Up(void)
+
+{
+  FILE *__stream;
+  int iVar1;
+  undefined4 local_14;
+  undefined4 local_10;
+  
+  local_14 = 0;
+  local_10 = 0;
+  __stream = fopen("/tmp/UDiskname","r+");
+  if (__stream != (FILE *)0x0) {
+    while (iVar1 = feof(__stream), iVar1 == 0) {
+      fgets((char *)&local_14,8,__stream);
+      if ((char)local_14 != '\0') {
+        doSystemCmd("cfm post netctrl %d?op=%d,string_info=%s",0x33,1,&local_14);
+      }
+    }
+    fclose(__stream);
+  }
+  return;
+}
+

```


## check_if_dir_empty

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|check_if_dir_empty|
|fullname|check_if_dir_empty|
|refcount|4|
|length|292|
|called|<EXTERNAL>::closedir<br><EXTERNAL>::opendir<br><EXTERNAL>::readdir<br><EXTERNAL>::strcmp|
|calling|formGetUSBStatus|
|paramcount|1|
|address|004c7b10|
|sig|undefined4 __stdcall check_if_dir_empty(char * param_1)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- check_if_dir_empty
+++ check_if_dir_empty
@@ -0,0 +1,24 @@
+
+undefined4 check_if_dir_empty(char *param_1)
+
+{
+  DIR *__dirp;
+  int iVar1;
+  dirent *pdVar2;
+  undefined4 local_18;
+  
+  local_18 = 0;
+  __dirp = opendir(param_1);
+  if (__dirp != (DIR *)0x0) {
+    do {
+      pdVar2 = readdir(__dirp);
+      if (pdVar2 == (dirent *)0x0) goto LAB_004c7c00;
+      iVar1 = strcmp(pdVar2->d_name,".");
+    } while ((iVar1 == 0) || (iVar1 = strcmp(pdVar2->d_name,".."), iVar1 == 0));
+    local_18 = 1;
+LAB_004c7c00:
+    closedir(__dirp);
+  }
+  return local_18;
+}
+

```


## formSetUsbPrint

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formSetUsbPrint|
|fullname|formSetUsbPrint|
|refcount|4|
|length|456|
|called|<EXTERNAL>::CommitCfm<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memset<br>websDone<br>websGetVar<br>websWrite|
|calling|formDefineTendDa|
|paramcount|4|
|address|004c7c34|
|sig|undefined __stdcall formSetUsbPrint(int * param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formSetUsbPrint
+++ formSetUsbPrint
@@ -0,0 +1,30 @@
+
+void formSetUsbPrint(int *param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)
+
+{
+  char *__nptr;
+  int iVar1;
+  size_t *psVar2;
+  undefined auStack_8c [64];
+  undefined auStack_4c [68];
+  
+  memset(auStack_8c,0,0x40);
+  memset(auStack_4c,0,0x40);
+  __nptr = websGetVar((int)param_1,"printerEn",&DAT_00520244);
+  SetValue("usb.ippd.enable",__nptr);
+  iVar1 = atoi(__nptr);
+  if (iVar1 == 1) {
+    psVar2 = (size_t *)0x1;
+    doSystemCmd("cfm post netctrl %d?op=%d",0x30);
+  }
+  else {
+    psVar2 = (size_t *)0x2;
+    doSystemCmd("cfm post netctrl %d?op=%d",0x30);
+  }
+  CommitCfm();
+  websWrite((int)param_1,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar2,param_4);
+  websWrite((int)param_1,(size_t *)"{\"errCode\":0}",psVar2,param_4);
+  websDone(param_1,200);
+  return;
+}
+

```


## formGetUsbPrint

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetUsbPrint|
|fullname|formGetUsbPrint|
|refcount|4|
|length|548|
|called|<EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::fclose<br><EXTERNAL>::fgets<br><EXTERNAL>::fopen<br><EXTERNAL>::memset<br><EXTERNAL>::strlen<br>websDone<br>websWrite|
|calling|formDefineTendDa|
|paramcount|4|
|address|004c7dfc|
|sig|undefined __stdcall formGetUsbPrint(int * param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetUsbPrint
+++ formGetUsbPrint
@@ -0,0 +1,34 @@
+
+void formGetUsbPrint(int *param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)
+
+{
+  FILE *__stream;
+  size_t sVar1;
+  char *pcVar2;
+  size_t *psVar3;
+  FILE *pFVar4;
+  char acStack_c8 [63];
+  char acStack_89 [129];
+  
+  memset(acStack_c8,0,0x40);
+  pFVar4 = (FILE *)0x80;
+  memset(acStack_89 + 1,0,0x80);
+  __stream = fopen("/tmp/usb/PrinterName","r");
+  if (__stream != (FILE *)0x0) {
+    while (pFVar4 = __stream, pcVar2 = fgets(acStack_89 + 1,0x80,__stream), pcVar2 != (char *)0x0) {
+      sVar1 = strlen(acStack_89 + 1);
+      if (acStack_89[sVar1] == '\n') {
+        acStack_89[sVar1] = '\0';
+      }
+    }
+    fclose(__stream);
+  }
+  GetValue("usb.ippd.enable",acStack_c8);
+  websWrite((int)param_1,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",(size_t *)pFVar4,param_4);
+  psVar3 = (size_t *)atoi(acStack_c8);
+  websWrite((int)param_1,(size_t *)"{\"printerEn\":\"%d\",\"printerName\":\"%s\"}",psVar3,
+            acStack_89 + 1);
+  websDone(param_1,200);
+  return;
+}
+

```


## formSetSambaConf

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formSetSambaConf|
|fullname|formSetSambaConf|
|refcount|4|
|length|1308|
|called|<EXTERNAL>::CommitCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memset<br><EXTERNAL>::strcmp<br>websDone<br>websGetVar<br>websWrite|
|calling|formDefineTendDa|
|paramcount|4|
|address|004c8020|
|sig|undefined __stdcall formSetSambaConf(int * param_1, undefined4 param_2, undefined4 param_3, undefined4 param_4)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formSetSambaConf
+++ formSetSambaConf
@@ -0,0 +1,62 @@
+
+void formSetSambaConf(int *param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4)
+
+{
+  undefined1 *puVar1;
+  undefined1 *puVar2;
+  undefined1 *puVar3;
+  char *__s1;
+  undefined1 *puVar4;
+  undefined1 *puVar5;
+  undefined1 *puVar6;
+  undefined1 *puVar7;
+  undefined1 *puVar8;
+  int iVar9;
+  size_t *psVar10;
+  char local_4c [68];
+  
+  memset(local_4c,0,0x40);
+  puVar1 = websGetVar((int)param_1,"password","admin");
+  puVar2 = websGetVar((int)param_1,"premitEn",&DAT_00520244);
+  puVar3 = websGetVar((int)param_1,"internetPort",&DAT_0052030c);
+  __s1 = websGetVar((int)param_1,"action",&DAT_00520318);
+  puVar4 = websGetVar((int)param_1,"usbName",&DAT_00520318);
+  puVar5 = websGetVar((int)param_1,"guestpwd",&DAT_00520318);
+  puVar6 = websGetVar((int)param_1,"guestuser",&DAT_00520318);
+  puVar7 = websGetVar((int)param_1,"guestaccess",&DAT_00520318);
+  puVar8 = websGetVar((int)param_1,"fileCode",&DAT_00520318);
+  iVar9 = strcmp(__s1,"del");
+  if (iVar9 == 0) {
+    psVar10 = (size_t *)0x3;
+    doSystemCmd("cfm post netctrl %d?op=%d,string_info=%s",0x33);
+    websWrite((int)param_1,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar10,puVar4);
+    websWrite((int)param_1,(size_t *)"{\"errCode\":0}",psVar10,puVar4);
+    websDone(param_1,200);
+  }
+  else {
+    GetValue("usb.samba.guest.user",local_4c);
+    if (local_4c[0] != '\0') {
+      doSystemCmd("busybox deluser %s",local_4c);
+    }
+    SetValue("usb.samba.pwd",puVar1);
+    SetValue("usb.samba.guest.user",puVar6);
+    SetValue("usb.samba.guest.pwd",puVar5);
+    SetValue("usb.samba.guest.acess",puVar7);
+    SetValue("usb.ftp.pwd",puVar1);
+    SetValue("usb.ftp.guest.user",puVar6);
+    SetValue("usb.ftp.guest.pwd",puVar5);
+    SetValue("usb.ftp.guest.acess",puVar7);
+    SetValue("usb.ftp.remote.acess",puVar2);
+    SetValue("usb.ftp.remote.port",puVar3);
+    SetValue("usb.ftp.charset",puVar8);
+    GetValue("usb.samba.enable",local_4c);
+    psVar10 = (size_t *)0x5;
+    doSystemCmd("cfm post netctrl %d?op=%d",0x33);
+    CommitCfm();
+    websWrite((int)param_1,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar10,param_4);
+    websWrite((int)param_1,(size_t *)"{\"errCode\":0}",psVar10,param_4);
+    websDone(param_1,200);
+  }
+  return;
+}
+

```


## formGetSambaConf

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetSambaConf|
|fullname|formGetSambaConf|
|refcount|4|
|length|2468|
|called|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::free<br><EXTERNAL>::getIfIp<br><EXTERNAL>::getLanIfName<br><EXTERNAL>::getWanIfName<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::strcmp<br><EXTERNAL>::tpi_wifi_get_ifname<br>cJSON_AddItemToObject</summary>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Object_2String<br>websDone<br>websWrite</details>|
|calling|formDefineTendDa|
|paramcount|5|
|address|004c853c|
|sig|undefined __stdcall formGetSambaConf(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetSambaConf
+++ formGetSambaConf
@@ -0,0 +1,189 @@
+
+void formGetSambaConf(double param_1,int *param_2,undefined4 param_3,undefined4 param_4,
+                     undefined4 param_5)
+
+{
+  int iVar1;
+  int iVar2;
+  undefined4 uVar3;
+  undefined4 *puVar4;
+  void *pvVar5;
+  size_t *psVar6;
+  size_t *__ptr;
+  char acStack_240 [64];
+  char acStack_200 [64];
+  undefined4 local_1c0;
+  undefined4 local_1bc;
+  undefined4 local_1b8;
+  undefined4 local_1b4;
+  char acStack_1b0 [64];
+  char acStack_170 [64];
+  char acStack_130 [64];
+  undefined4 local_f0;
+  undefined4 local_ec;
+  undefined4 local_e8;
+  undefined4 local_e4;
+  undefined4 local_e0;
+  undefined4 local_dc;
+  undefined4 local_d8;
+  undefined4 local_d4;
+  undefined4 local_d0;
+  undefined4 local_cc;
+  undefined4 local_c8;
+  undefined4 local_c4;
+  undefined4 local_c0;
+  undefined4 local_bc;
+  undefined4 local_b8;
+  undefined4 local_b4;
+  undefined4 local_b0;
+  undefined4 local_ac;
+  undefined4 local_a8;
+  undefined4 local_a4;
+  undefined4 local_a0;
+  undefined4 local_9c;
+  undefined4 local_98;
+  undefined4 local_94;
+  undefined4 local_90;
+  undefined4 local_8c;
+  undefined4 local_88;
+  undefined4 local_84;
+  undefined4 local_80;
+  undefined4 local_7c;
+  undefined4 local_78;
+  undefined4 local_74;
+  undefined4 local_70;
+  undefined4 local_6c;
+  undefined4 local_68;
+  undefined4 local_64;
+  undefined4 local_60;
+  undefined4 local_5c;
+  undefined4 local_58;
+  undefined4 local_54;
+  undefined auStack_50 [68];
+  
+  memset(acStack_240,0,0x40);
+  memset(acStack_200,0,0x40);
+  local_1c0 = 0;
+  local_1bc = 0;
+  local_1b8 = 0;
+  local_1b4 = 0;
+  memset(acStack_1b0,0,0x40);
+  memset(acStack_170,0,0x40);
+  memset(acStack_130,0,0x40);
+  local_f0 = 0;
+  local_ec = 0;
+  local_e8 = 0;
+  local_e4 = 0;
+  local_e0 = 0;
+  local_dc = 0;
+  local_d8 = 0;
+  local_d4 = 0;
+  local_d0 = 0;
+  local_cc = 0;
+  local_c8 = 0;
+  local_c4 = 0;
+  local_c0 = 0;
+  local_bc = 0;
+  local_b8 = 0;
+  local_b4 = 0;
+  local_b0 = 0;
+  local_ac = 0;
+  local_a8 = 0;
+  local_a4 = 0;
+  local_a0 = 0;
+  local_9c = 0;
+  local_98 = 0;
+  local_94 = 0;
+  local_90 = 0;
+  local_8c = 0;
+  local_88 = 0;
+  local_84 = 0;
+  local_80 = 0;
+  local_7c = 0;
+  local_78 = 0;
+  local_74 = 0;
+  local_70 = 0;
+  local_6c = 0;
+  local_68 = 0;
+  local_64 = 0;
+  local_60 = 0;
+  local_5c = 0;
+  local_58 = 0;
+  local_54 = 0;
+  memset(auStack_50,0,0x40);
+  GetValue("wan1.connecttype",&local_80);
+  GetValue("sys.mode",&local_d0);
+  GetValue("usb.ftp.port",&local_c0);
+  GetValue("usb.ftp.remote.acess",&local_1c0);
+  GetValue("usb.ftp.remote.port",&local_b0);
+  GetValue("usb.ftp.charset",&local_e0);
+  GetValue("wl2g.public.mode",&local_a0);
+  GetValue("wl5g.public.mode",&local_90);
+  iVar1 = strcmp((char *)&local_a0,"wisp");
+  if (iVar1 == 0) {
+    tpi_wifi_get_ifname(0x18,4,auStack_50);
+    getIfIp(auStack_50,acStack_200);
+  }
+  else {
+    iVar1 = strcmp((char *)&local_90,"wisp");
+    if (iVar1 == 0) {
+      tpi_wifi_get_ifname(5,4,auStack_50);
+      getIfIp(auStack_50,acStack_200);
+    }
+    else {
+      iVar1 = atoi((char *)&local_d0);
+      iVar2 = atoi((char *)&local_80);
+      iVar1 = getWanIfName(1,iVar1,iVar2);
+      if (iVar1 == 0) {
+        printf("%s %d: getWanIfName return NULL\n","formGetSambaConf",0xfd);
+      }
+      else {
+        getIfIp(iVar1,acStack_200);
+      }
+    }
+  }
+  GetValue("extra_chkHz",&local_70);
+  iVar1 = atoi((char *)&local_70);
+  if (iVar1 == 0) {
+    GetValue("wl2g.public.mode",&local_60);
+  }
+  else {
+    GetValue("wl5g.public.mode",&local_60);
+  }
+  uVar3 = getLanIfName();
+  getIfIp(uVar3,acStack_240);
+  puVar4 = (undefined4 *)cJSON_CreateObject();
+  GetValue("usb.samba.pwd",acStack_1b0);
+  GetValue("usb.samba.guest.user",acStack_170);
+  GetValue("usb.samba.guest.pwd",acStack_130);
+  GetValue("usb.samba.guest.acess",&local_f0);
+  pvVar5 = cJSON_CreateString(acStack_1b0);
+  cJSON_AddItemToObject((int)puVar4,"password",(int)pvVar5);
+  pvVar5 = cJSON_CreateString(acStack_240);
+  cJSON_AddItemToObject((int)puVar4,"ftpLink",(int)pvVar5);
+  pvVar5 = cJSON_CreateString((char *)&local_1c0);
+  cJSON_AddItemToObject((int)puVar4,"premitEn",(int)pvVar5);
+  pvVar5 = cJSON_CreateString(acStack_200);
+  cJSON_AddItemToObject((int)puVar4,"internetLink",(int)pvVar5);
+  pvVar5 = cJSON_CreateString((char *)&local_c0);
+  cJSON_AddItemToObject((int)puVar4,"outPort",(int)pvVar5);
+  pvVar5 = cJSON_CreateString((char *)&local_60);
+  cJSON_AddItemToObject((int)puVar4,"wl_mode",(int)pvVar5);
+  pvVar5 = cJSON_CreateString((char *)&local_b0);
+  cJSON_AddItemToObject((int)puVar4,"internetPort",(int)pvVar5);
+  pvVar5 = cJSON_CreateString((char *)&local_e0);
+  cJSON_AddItemToObject((int)puVar4,"fileCode",(int)pvVar5);
+  pvVar5 = cJSON_CreateString(acStack_170);
+  cJSON_AddItemToObject((int)puVar4,"guestuser",(int)pvVar5);
+  pvVar5 = cJSON_CreateString(acStack_130);
+  cJSON_AddItemToObject((int)puVar4,"guestpwd",(int)pvVar5);
+  psVar6 = (size_t *)cJSON_CreateString((char *)&local_f0);
+  cJSON_AddItemToObject((int)puVar4,"guestaccess",(int)psVar6);
+  __ptr = (size_t *)cJSON_Object_2String(param_1,puVar4);
+  websWrite((int)param_2,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar6,param_5);
+  websWrite((int)param_2,(size_t *)&DAT_0052053c,__ptr,param_5);
+  free(__ptr);
+  websDone(param_2,200);
+  return;
+}
+

```


## fill_smbpasswd_input_file

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|fill_smbpasswd_input_file|
|fullname|fill_smbpasswd_input_file|
|refcount|4|
|length|420|
|called|<EXTERNAL>::close<br><EXTERNAL>::open<br><EXTERNAL>::puts<br><EXTERNAL>::strlen<br><EXTERNAL>::unlink<br><EXTERNAL>::write|
|calling|writePasswd|
|paramcount|1|
|address|004c8ee0|
|sig|undefined4 __stdcall fill_smbpasswd_input_file(char * param_1)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- fill_smbpasswd_input_file
+++ fill_smbpasswd_input_file
@@ -0,0 +1,31 @@
+
+undefined4 fill_smbpasswd_input_file(char *param_1)
+
+{
+  int iVar1;
+  size_t sVar2;
+  undefined4 uVar3;
+  
+  iVar1 = unlink("/tmp/smbpasswd");
+  if (iVar1 == -1) {
+    puts("******* unlink /tmp/smbpasswd is fail ");
+  }
+  iVar1 = open("/tmp/smbpasswd",0x312);
+  if ((iVar1 < 1) || (param_1 == (char *)0x0)) {
+    if (iVar1 == 0) {
+      close(0);
+    }
+    uVar3 = 0;
+  }
+  else {
+    sVar2 = strlen(param_1);
+    write(iVar1,param_1,sVar2);
+    write(iVar1,&DAT_00520578,1);
+    sVar2 = strlen(param_1);
+    write(iVar1,param_1,sVar2);
+    close(iVar1);
+    uVar3 = 1;
+  }
+  return uVar3;
+}
+

```


## writePasswd

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|writePasswd|
|fullname|writePasswd|
|refcount|2|
|length|596|
|called|<EXTERNAL>::GetValue<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strlen<br><EXTERNAL>::strncpy<br><EXTERNAL>::system<br>fill_smbpasswd_input_file|
|calling||
|paramcount|0|
|address|004c9084|
|sig|undefined4 __stdcall writePasswd(void)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- writePasswd
+++ writePasswd
@@ -0,0 +1,32 @@
+
+undefined4 writePasswd(void)
+
+{
+  size_t __n;
+  char local_414 [256];
+  char local_314 [256];
+  char acStack_214 [256];
+  char acStack_114 [264];
+  
+  memset(local_414,0,0x100);
+  memset(local_314,0,0x100);
+  memset(acStack_214,0,0x100);
+  memset(acStack_114,0,0x100);
+  GetValue("usb.samba.user",local_414);
+  GetValue("usb.samba.pwd",local_314);
+  if (local_414[0] == '\0') {
+    memcpy(local_414,"admin",5);
+  }
+  if (local_314[0] == '\0') {
+    memcpy(acStack_214,"admin",5);
+  }
+  else {
+    __n = strlen(local_314);
+    strncpy(acStack_214,local_314,__n);
+  }
+  fill_smbpasswd_input_file(acStack_214);
+  sprintf(acStack_114,"smbpasswd -a %s -s < /tmp/smbpasswd",local_414);
+  system(acStack_114);
+  return 0;
+}
+

```


## SpecChConv

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|SpecChConv|
|fullname|SpecChConv|
|refcount|2|
|length|580|
|called|<EXTERNAL>::memset<br><EXTERNAL>::strchr<br><EXTERNAL>::strcpy<br><EXTERNAL>::strlen|
|calling||
|paramcount|1|
|address|004c92d8|
|sig|undefined4 __stdcall SpecChConv(char * param_1)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- SpecChConv
+++ SpecChConv
@@ -0,0 +1,39 @@
+
+undefined4 SpecChConv(char *param_1)
+
+{
+  char *pcVar1;
+  size_t sVar2;
+  uint local_878;
+  char acStack_874 [1024];
+  undefined2 local_474;
+  undefined local_472;
+  undefined auStack_471 [97];
+  char acStack_410 [1028];
+  
+  local_878 = 0;
+  memset(acStack_874,0,0x400);
+  local_474 = 0x6027;
+  local_472 = 0;
+  memset(auStack_471,0,0x61);
+  memset(acStack_410,0,0x400);
+  strcpy(acStack_410,param_1);
+  while( true ) {
+    sVar2 = strlen(param_1);
+    if (sVar2 <= local_878) break;
+    pcVar1 = strchr((char *)&local_474,(int)acStack_410[local_878]);
+    if (pcVar1 == (char *)0x0) {
+      sVar2 = strlen(acStack_874);
+      acStack_874[sVar2] = acStack_410[local_878];
+    }
+    else {
+      sVar2 = strlen(acStack_874);
+      acStack_874[sVar2] = '\\';
+      acStack_874[sVar2 + 1] = acStack_410[local_878];
+    }
+    local_878 = local_878 + 1;
+  }
+  strcpy(param_1,acStack_874);
+  return 0;
+}
+

```


## formGetUSBStatus

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetUSBStatus|
|fullname|formGetUSBStatus|
|refcount|4|
|length|996|
|called|<EXTERNAL>::GetValue<br><EXTERNAL>::strcmp<br>cJSON_AddItemToObject<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Object_2String<br>check_if_dir_empty<br>websTransfer|
|calling|formDefineTendDa|
|paramcount|5|
|address|004c951c|
|sig|undefined __stdcall formGetUSBStatus(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetUSBStatus
+++ formGetUSBStatus
@@ -0,0 +1,68 @@
+
+void formGetUSBStatus(double param_1,int *param_2,undefined4 param_3,undefined4 param_4,
+                     undefined4 param_5)
+
+{
+  undefined4 *puVar1;
+  int iVar2;
+  void *pvVar3;
+  size_t *psVar4;
+  size_t *psVar5;
+  undefined4 local_20;
+  undefined4 local_1c;
+  undefined4 local_18;
+  undefined4 local_14;
+  undefined4 local_10;
+  undefined4 local_c;
+  
+  local_20 = 0;
+  local_1c = 0;
+  local_18 = 0;
+  local_14 = 0;
+  local_10 = 0;
+  local_c = 0;
+  puVar1 = (undefined4 *)cJSON_CreateObject();
+  GetValue("usb.ippd.enable",&local_20);
+  GetValue("usb.ftp.remote.acess",&local_18);
+  GetValue("dlna.en",&local_10);
+  iVar2 = strcmp((char *)&local_20,"1");
+  if (iVar2 == 0) {
+    pvVar3 = cJSON_CreateString("1");
+    cJSON_AddItemToObject((int)puVar1,"printer",(int)pvVar3);
+  }
+  else {
+    pvVar3 = cJSON_CreateString("0");
+    cJSON_AddItemToObject((int)puVar1,"printer",(int)pvVar3);
+  }
+  iVar2 = strcmp((char *)&local_18,"1");
+  if (iVar2 == 0) {
+    pvVar3 = cJSON_CreateString("1");
+    cJSON_AddItemToObject((int)puVar1,"fileshare",(int)pvVar3);
+  }
+  else {
+    pvVar3 = cJSON_CreateString("0");
+    cJSON_AddItemToObject((int)puVar1,"fileshare",(int)pvVar3);
+  }
+  iVar2 = check_if_dir_empty("/var/etc/upan");
+  if (iVar2 == 0) {
+    pvVar3 = cJSON_CreateString("0");
+    cJSON_AddItemToObject((int)puVar1,"hasusb",(int)pvVar3);
+  }
+  else {
+    pvVar3 = cJSON_CreateString("1");
+    cJSON_AddItemToObject((int)puVar1,"hasusb",(int)pvVar3);
+  }
+  iVar2 = strcmp((char *)&local_10,"1");
+  if (iVar2 == 0) {
+    psVar4 = (size_t *)cJSON_CreateString("1");
+    cJSON_AddItemToObject((int)puVar1,"dlna",(int)psVar4);
+  }
+  else {
+    psVar4 = (size_t *)cJSON_CreateString("0");
+    cJSON_AddItemToObject((int)puVar1,"dlna",(int)psVar4);
+  }
+  psVar5 = (size_t *)cJSON_Object_2String(param_1,puVar1);
+  websTransfer(param_2,psVar5,psVar4,param_5);
+  return;
+}
+

```


## formsetUsbUnload

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formsetUsbUnload|
|fullname|formsetUsbUnload|
|refcount|4|
|length|248|
|called|<EXTERNAL>::doSystemCmd<br>websDone<br>websGetVar<br>websWrite|
|calling|formDefineTendDa|
|paramcount|1|
|address|004c9900|
|sig|undefined __stdcall formsetUsbUnload(int * param_1)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formsetUsbUnload
+++ formsetUsbUnload
@@ -0,0 +1,16 @@
+
+void formsetUsbUnload(int *param_1)
+
+{
+  undefined1 *puVar1;
+  size_t *psVar2;
+  
+  puVar1 = websGetVar((int)param_1,"deviceName",&DAT_00520318);
+  psVar2 = (size_t *)0x3;
+  doSystemCmd("cfm post netctrl %d?op=%d,string_info=%s",0x33);
+  websWrite((int)param_1,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar2,puVar1);
+  websWrite((int)param_1,(size_t *)"{\"errCode\":0}",psVar2,puVar1);
+  websDone(param_1,200);
+  return;
+}
+

```


## formGetUsbCfg

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetUsbCfg|
|fullname|formGetUsbCfg|
|refcount|4|
|length|1876|
|called|<details><summary>Expand for full list:<br><EXTERNAL>::atof<br><EXTERNAL>::fclose<br><EXTERNAL>::feof<br><EXTERNAL>::fgets<br><EXTERNAL>::fopen<br><EXTERNAL>::free<br><EXTERNAL>::memset<br><EXTERNAL>::perror<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf<br><EXTERNAL>::sscanf</summary><EXTERNAL>::strchr<br>__ledf2<br>cJSON_AddItemToArray<br>cJSON_AddItemToObject<br>cJSON_CreateArray<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>websDone<br>websWrite</details>|
|calling|formDefineTendDa|
|paramcount|5|
|address|004c99f8|
|sig|undefined __stdcall formGetUsbCfg(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined4 * param_5)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetUsbCfg
+++ formGetUsbCfg
@@ -0,0 +1,127 @@
+
+void formGetUsbCfg(double param_1,int *param_2,undefined4 param_3,undefined4 param_4,
+                  undefined4 *param_5)
+
+{
+  undefined4 *puVar1;
+  FILE *pFVar2;
+  FILE *__stream;
+  void *pvVar3;
+  void *pvVar4;
+  FILE *pFVar5;
+  code *pcVar6;
+  int iVar7;
+  char *pcVar8;
+  size_t *__ptr;
+  undefined4 *puVar9;
+  FILE *pFVar10;
+  char *local_a70;
+  char *local_a68;
+  int local_a64;
+  int local_a60;
+  char acStack_a40 [1024];
+  char acStack_640 [256];
+  undefined4 local_540;
+  undefined4 local_53c;
+  undefined4 local_538;
+  undefined4 local_534;
+  char acStack_530 [1024];
+  undefined4 auStack_130 [64];
+  undefined4 local_30;
+  undefined4 local_2c;
+  undefined4 local_28;
+  undefined4 local_24;
+  undefined4 local_20;
+  undefined4 local_1c;
+  undefined4 local_18;
+  undefined4 local_14;
+  
+  local_a60 = 0;
+  local_a64 = 0;
+  memset(acStack_a40,0,0x400);
+  memset(acStack_640,0,0x100);
+  local_540 = 0;
+  local_53c = 0;
+  local_538 = 0;
+  local_534 = 0;
+  memset(acStack_530,0,0x400);
+  memset(auStack_130,0,0x100);
+  local_30 = 0;
+  local_2c = 0;
+  local_28 = 0;
+  local_24 = 0;
+  local_20 = 0;
+  local_1c = 0;
+  local_18 = 0;
+  local_14 = 0;
+  puVar1 = (undefined4 *)cJSON_CreateObject();
+  pFVar2 = (FILE *)cJSON_CreateArray();
+  pFVar10 = pFVar2;
+  cJSON_AddItemToObject((int)puVar1,"usbList",(int)pFVar2);
+  __stream = fopen("/tmp/usb/UsbVolumeInfo","r");
+  if (__stream == (FILE *)0x0) {
+    perror((char *)fopen);
+  }
+  else {
+    for (; ((iVar7 = feof(__stream), iVar7 == 0 &&
+            (pFVar10 = __stream, pcVar8 = fgets(acStack_a40,0x400,__stream), pcVar8 != (char *)0x0))
+           && (local_a60 < 2)); local_a60 = local_a60 + 1) {
+      param_5 = &local_540;
+      sscanf(acStack_a40,"%[^;];%[^;];%[^\n]\n",acStack_640,param_5,acStack_530);
+      pvVar3 = cJSON_CreateObject();
+      cJSON_AddItemToArray((int)pFVar2,(int)pvVar3);
+      pvVar4 = cJSON_CreateString(acStack_640);
+      cJSON_AddItemToObject((int)pvVar3,"devName",(int)pvVar4);
+      pvVar4 = cJSON_CreateString((char *)&local_540);
+      cJSON_AddItemToObject((int)pvVar3,"devId",(int)pvVar4);
+      pFVar5 = (FILE *)cJSON_CreateArray();
+      pFVar10 = pFVar5;
+      cJSON_AddItemToObject((int)pvVar3,"diskList",(int)pFVar5);
+      local_a70 = strchr(acStack_530,0x7e);
+      local_a68 = acStack_530;
+      while ((local_a70 != (char *)0x0 && (local_a64 < 8))) {
+        *local_a70 = '\0';
+        pcVar8 = local_a70 + 1;
+        puVar9 = auStack_130;
+        sscanf(local_a68,"%[^:]:%[^*]*%s",puVar9,&local_30,&local_20);
+        local_a70 = strchr(pcVar8,0x7e);
+        pcVar6 = atof;
+        atof((char *)&local_30);
+        param_5 = (undefined4 *)0x3ee4f8b5;
+        pFVar10 = (FILE *)0x88e368f1;
+        iVar7 = __ledf2((uint)pcVar6,(uint)puVar9,0x88e368f1,0x3ee4f8b5);
+        local_a68 = pcVar8;
+        if (-1 < iVar7) {
+          pcVar6 = atof;
+          atof((char *)&local_20);
+          sprintf((char *)&local_20,"%.6f",pcVar6,puVar9);
+          pcVar6 = atof;
+          atof((char *)&local_30);
+          sprintf((char *)&local_30,"%.6f",pcVar6);
+          printf("usb_total=%s,usb_usable=%s\n",&local_30,&local_20);
+          pvVar3 = cJSON_CreateObject();
+          cJSON_AddItemToArray((int)pFVar5,(int)pvVar3);
+          pvVar4 = cJSON_CreateString((char *)auStack_130);
+          cJSON_AddItemToObject((int)pvVar3,"diskName",(int)pvVar4);
+          pvVar4 = cJSON_CreateString((char *)&local_20);
+          cJSON_AddItemToObject((int)pvVar3,"memoryUnUse",(int)pvVar4);
+          pFVar10 = (FILE *)cJSON_CreateString((char *)&local_30);
+          cJSON_AddItemToObject((int)pvVar3,"memoryTotal",(int)pFVar10);
+          local_a64 = local_a64 + 1;
+          param_5 = puVar9;
+        }
+      }
+    }
+  }
+  __ptr = (size_t *)cJSON_Print(param_1,(int)puVar1);
+  cJSON_Delete(puVar1);
+  websWrite((int)param_2,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",(size_t *)pFVar10,param_5);
+  websWrite((int)param_2,(size_t *)&DAT_0052053c,__ptr,param_5);
+  free(__ptr);
+  websDone(param_2,200);
+  if (__stream != (FILE *)0x0) {
+    fclose(__stream);
+  }
+  return;
+}
+

```


## <EXTERNAL>::closedir

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|closedir|
|fullname|<EXTERNAL>::closedir|
|refcount|1|
|length|0|
|called||
|calling||
|paramcount|1|
|address|EXTERNAL:000000cd|
|sig|int closedir(DIR * __dirp)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|True|


*No code available for <EXTERNAL>::closedir*
## <EXTERNAL>::readdir

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|readdir|
|fullname|<EXTERNAL>::readdir|
|refcount|1|
|length|0|
|called||
|calling||
|paramcount|1|
|address|EXTERNAL:000000f2|
|sig|dirent * readdir(DIR * __dirp)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|True|


*No code available for <EXTERNAL>::readdir*
## <EXTERNAL>::opendir

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|opendir|
|fullname|<EXTERNAL>::opendir|
|refcount|1|
|length|0|
|called||
|calling||
|paramcount|1|
|address|EXTERNAL:0000011c|
|sig|DIR * opendir(char * __name)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|True|


*No code available for <EXTERNAL>::opendir*
## <EXTERNAL>::atof

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|atof|
|fullname|<EXTERNAL>::atof|
|refcount|1|
|length|0|
|called||
|calling||
|paramcount|1|
|address|EXTERNAL:00000044|
|sig|double atof(char * __nptr)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|True|


*No code available for <EXTERNAL>::atof*
# Modified


*Modified functions contain code changes*
## fromSetWirelessRepeat

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.98|
|i_ratio|0.39|
|m_ratio|0.99|
|b_ratio|0.99|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|fromSetWirelessRepeat|fromSetWirelessRepeat|
|fullname|fromSetWirelessRepeat|fromSetWirelessRepeat|
|refcount|4|4|
|`length`|9920|10028|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::CommitSyncCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memcmp<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp</summary><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::sys_pktc_disable<br><EXTERNAL>::tpi_systool_reboot<br><EXTERNAL>::tpi_wifi_get_ifname<br>set_cn_ssid_ori_encode<br>set_idx_to_mib<br>websGetVar<br>websGetVarWithValidate<br>websTransfer</details>|<details><summary>Expand for full list:<br><EXTERNAL>::CommitSyncCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memcmp<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp</summary><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::sys_pktc_disable<br><EXTERNAL>::tpi_systool_reboot<br><EXTERNAL>::tpi_wifi_get_ifname<br>Usb_Up<br>set_cn_ssid_ori_encode<br>set_idx_to_mib<br>websGetVar<br>websGetVarWithValidate<br>websTransfer</details>|
|calling|formDefineTendDa|formDefineTendDa|
|paramcount|4|4|
|`address`|004c28c4|004c293c|
|sig|undefined __stdcall fromSetWirelessRepeat(int * param_1, undefined4 param_2, undefined4 param_3, undefined * param_4)|undefined __stdcall fromSetWirelessRepeat(int * param_1, undefined4 param_2, undefined4 param_3, undefined * param_4)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### fromSetWirelessRepeat Called Diff


```diff
--- fromSetWirelessRepeat called
+++ fromSetWirelessRepeat called
@@ -16,0 +17 @@
+Usb_Up
```


### fromSetWirelessRepeat Diff


```diff
--- fromSetWirelessRepeat
+++ fromSetWirelessRepeat
@@ -1,523 +1,527 @@
 
-/* WARNING: Removing unreachable block (ram,0x004c4ea0) */
+/* WARNING: Removing unreachable block (ram,0x004c4f84) */
 
 void fromSetWirelessRepeat(int *param_1,undefined4 param_2,undefined4 param_3,undefined *param_4)
 
 {
   undefined1 *puVar1;
   char *__s2;
   undefined1 *puVar2;
   int iVar3;
   char *pcVar4;
   undefined1 *puVar5;
   undefined1 *puVar6;
   undefined1 *puVar7;
   char *pcVar8;
   char *pcVar9;
   size_t sVar10;
   size_t *psVar11;
   undefined *puVar12;
   uint local_640;
   size_t *local_63c;
   char *local_61c;
   undefined4 local_614;
   undefined4 local_610;
   undefined4 local_60c;
   undefined4 local_608;
   undefined4 local_604;
   undefined4 local_600;
   undefined4 local_5fc;
   undefined4 local_5f8;
   undefined4 local_5f4;
   undefined4 local_5f0;
   char acStack_5ec [256];
   size_t asStack_4ec [64];
   undefined4 local_3ec;
   undefined4 local_3e8;
   undefined4 local_3e4;
   undefined4 local_3e0;
   undefined4 local_3dc;
   undefined4 local_3d8;
   undefined4 local_3d4;
   undefined4 local_3d0;
   undefined4 local_3cc;
   undefined4 local_3c8;
   undefined4 local_3c4;
   undefined4 local_3c0;
   undefined4 local_3bc;
   undefined4 local_3b8;
   undefined4 local_3b4;
   undefined4 local_3b0;
   undefined auStack_3ac [512];
   undefined4 local_1ac;
   undefined4 local_1a8;
   undefined4 local_1a4;
   undefined4 local_1a0;
   undefined4 local_19c;
   undefined4 local_198;
   undefined4 local_194;
   undefined4 local_190;
   undefined4 local_18c;
   undefined4 local_188;
   undefined4 local_184;
   undefined4 local_180;
   undefined4 local_17c;
   undefined auStack_178 [8];
   undefined auStack_170 [16];
   char acStack_160 [16];
   undefined auStack_150 [8];
   undefined auStack_148 [16];
   char acStack_138 [16];
   char acStack_128 [32];
   undefined4 local_108;
   undefined4 local_104;
   undefined4 local_100;
   undefined4 local_fc;
   undefined4 local_f8;
   undefined4 local_f4;
   undefined4 local_f0;
   undefined4 local_ec;
   
   local_614 = 0;
   local_610 = 0;
   local_60c = 0;
   local_608 = 0;
   local_604 = 0;
   local_600 = 0;
   local_5fc = 0;
   local_5f8 = 0;
   local_5f4 = 0;
   local_5f0 = 0;
   memset(acStack_5ec,0,0x100);
   memset(asStack_4ec,0,0x100);
   local_3ec = 0;
   local_3e8 = 0;
   local_3e4 = 0;
   local_3e0 = 0;
   local_3dc = 0;
   local_3d8 = 0;
   local_3d4 = 0;
   local_3d0 = 0;
   local_3cc = 0;
   local_3c8 = 0;
   local_3c4 = 0;
   local_3c0 = 0;
   local_3bc = 0;
   local_3b8 = 0;
   local_3b4 = 0;
   local_3b0 = 0;
   memset(auStack_3ac,0,0x204);
   local_1ac = 0x100;
   puVar12 = auStack_3ac;
   local_63c = (size_t *)0x0;
   puVar1 = websGetVar((int)param_1,"mac",&DAT_0);
   local_61c = websGetVar((int)param_1,"wifi_chkHz",&DAT_1);
   __s2 = websGetVar((int)param_1,"wl_mode",&DAT_2);
   puVar2 = websGetVar((int)param_1,"handset",&DAT_1);
   GetValue("wl2g.public.mode",&local_614);
   GetValue("wl5g.public.mode",&local_604);
   GetValue("wl2g.ssid1.enable",&local_3ec);
   GetValue("wl5g.ssid1.enable",&local_3dc);
   iVar3 = strcmp("ap",__s2);
   if (iVar3 == 0) {
     local_108 = 0;
     local_104 = 0;
     local_100 = 0;
     local_fc = 0;
     local_f8 = 0;
     local_f4 = 0;
     local_f0 = 0;
     local_ec = 0;
     SetValue("sys.workmode",&local_108);
     GetValue("wl.bcm11ac",acStack_128);
     iVar3 = strcmp("0",acStack_128);
     if (iVar3 == 0) {
       local_61c = "0";
     }
     else {
       iVar3 = strcmp("1",acStack_128);
       if (iVar3 == 0) {
         local_61c = "1";
       }
     }
     iVar3 = strcmp((char *)&local_108,"ap");
     if (iVar3 == 0) {
       SetValue("sys.workmode",&DAT_2);
     }
     else {
       SetValue("sys.workmode","router");
     }
   }
   else {
     iVar3 = strcmp("wds",__s2);
     if (iVar3 != 0) {
       SetValue("sys.workmode",__s2);
     }
     SetValue("dhcps.en",&DAT_3);
   }
   iVar3 = strcmp((char *)&local_614,"ap");
   if (((iVar3 == 0) && (iVar3 = strcmp((char *)&local_604,"ap"), iVar3 == 0)) &&
      (iVar3 = strcmp(__s2,"ap"), iVar3 == 0)) {
     local_63c = (size_t *)0x0;
     goto LAB_4;
   }
   strcmp(__s2,"apclient");
   local_1a8 = 0;
   local_1a4 = 0;
   local_1a0 = 0;
   local_19c = 0;
   iVar3 = strcmp((char *)&local_614,"wisp");
   if ((iVar3 == 0) || (iVar3 = strcmp((char *)&local_604,"wisp"), iVar3 == 0)) {
     memcpy(&local_1a8,&DAT_5,5);
   }
   else {
     iVar3 = strcmp((char *)&local_614,"apclient");
     if ((iVar3 == 0) || (iVar3 = strcmp((char *)&local_604,"apclient"), iVar3 == 0)) {
       memcpy(&local_1a8,"apclient",9);
     }
     else {
       memcpy(&local_1a8,&DAT_2,3);
     }
   }
   iVar3 = strcmp((char *)&local_1a8,__s2);
   local_640 = (uint)(iVar3 != 0);
   iVar3 = atoi(local_61c);
   if (iVar3 == 0) {
     GetValue("wl5g.public.mode",g_work_mode_str);
     SetValue("extra_chkHz",local_61c);
     iVar3 = strcmp(__s2,"ap");
     if (iVar3 == 0) {
       SetValue("wl2g.public.mode",&DAT_2);
       SetValue("wl5g.public.mode",&DAT_2);
     }
     else {
       SetValue("wl.guest.dhcps_enable",&DAT_1);
       iVar3 = strcmp((char *)&local_3ec,"1");
       if (iVar3 != 0) {
         SetValue("wl2g.ssid1.enable",&DAT_1);
       }
       iVar3 = strcmp((char *)&local_3dc,"1");
       if (iVar3 != 0) {
         SetValue("wl5g.ssid1.enable",&DAT_1);
       }
       SetValue("wl.bcm11ac",local_61c);
       SetValue("wl2g.extra.mac",puVar1);
       SetValue("extra_hand",puVar2);
       tpi_wifi_get_ifname(0x18,4,&local_3bc);
       SetValue("wl2g.extra.ifname",&local_3bc);
       iVar3 = strcmp(__s2,"wisp");
       if (iVar3 == 0) {
         SetValue("wl.wisp.ifname",&local_3bc);
       }
       iVar3 = strcmp(__s2,"apclient");
       if (iVar3 != 0) {
         strcmp(__s2,"wisp");
       }
       iVar3 = strcmp(g_work_mode_str,"ap");
       if (iVar3 != 0) {
         SetValue("wl5g.public.mode",&DAT_2);
       }
       SetValue("wl2g.public.mode",__s2);
       memset(&local_3cc,0,0x10);
       sprintf((char *)&local_3cc,"wan%d_err_check",1);
       SetValue(&local_3cc,&DAT_1);
       memset(&local_3cc,0,0x10);
       sprintf((char *)&local_3cc,"wan%d_isonln",1);
       SetValue(&local_3cc,&DAT_1);
       memset(&local_3cc,0,0x10);
       sprintf((char *)&local_3cc,"wan%d_check",1);
       SetValue(&local_3cc,&DAT_1);
       pcVar4 = websGetVar((int)param_1,"ssid",&DAT_0);
       set_cn_ssid_ori_encode(local_61c,pcVar4);
       SetValue("wl2g.extra.ssid",pcVar4);
       iVar3 = strcmp(__s2,"wisp");
       if (iVar3 == 0) {
         SetValue("wan1.connecttype",&DAT_1);
         SetValue("wl.wisp.access_mode",&DAT_6);
         GetValue("wan1.dynamicMTU",auStack_178);
         SetValue("wl.wisp.mtu",auStack_178);
       }
       pcVar4 = websGetVarWithValidate((int)param_1,"security",9);
       if (pcVar4 == (char *)0x0) {
         local_63c = (size_t *)0x1;
         goto LAB_4;
       }
       SetValue("wl2g.extra.security",pcVar4);
       iVar3 = strcmp(pcVar4,"none");
       if (iVar3 != 0) {
         iVar3 = strcmp(pcVar4,"wep");
         if (iVar3 == 0) {
           puVar1 = websGetVar((int)param_1,"wepauth","shared");
           puVar2 = websGetVar((int)param_1,"wepkey",&DAT_3);
           pcVar4 = websGetVar((int)param_1,"wepkey1",&DAT_0);
           puVar5 = websGetVar((int)param_1,"wepkey2",&DAT_0);
           puVar6 = websGetVar((int)param_1,"wepkey3",&DAT_0);
           puVar7 = websGetVar((int)param_1,"wepkey4",&DAT_0);
           if (*pcVar4 == '\0') {
             local_63c = (size_t *)0x1;
             goto LAB_4;
           }
           SetValue("wl2g.extra.wep_type",puVar1);
           SetValue("wl2g.extra.wep_key",puVar2);
           SetValue("wl2g.extra.wep_key1",pcVar4);
           SetValue("wl2g.extra.wep_key2",puVar5);
           SetValue("wl2g.extra.wep_key3",puVar6);
           SetValue("wl2g.extra.wep_key4",puVar7);
         }
         else {
           iVar3 = strcmp(pcVar4,"wpapsk");
           if (iVar3 != 0) {
             local_63c = (size_t *)0x1;
             goto LAB_4;
           }
           pcVar4 = websGetVar((int)param_1,"wpapsk_type","wpa&wpa2");
           pcVar8 = websGetVar((int)param_1,"wpapsk_crypto",&DAT_7);
           pcVar9 = websGetVar((int)param_1,"wpapsk_key",&DAT_0);
           if ((*pcVar9 == '\0') && (sVar10 = strlen(pcVar9), sVar10 < 8)) {
             local_63c = (size_t *)0x1;
             goto LAB_4;
           }
           iVar3 = strcmp(pcVar4,"wpa");
           if (iVar3 == 0) {
             memcpy(auStack_170,&DAT_8,4);
           }
           else {
             iVar3 = strcmp(pcVar4,"wpa2");
             if (iVar3 == 0) {
               memcpy(auStack_170,&DAT_9,5);
             }
             else {
               memcpy(auStack_170,"psk psk2",9);
             }
           }
           iVar3 = strcmp(pcVar8,"tkip&aes");
           if (iVar3 == 0) {
             memcpy(acStack_160,"tkip+aes",9);
           }
           else {
             strcpy(acStack_160,pcVar8);
           }
           SetValue("wl2g.extra.wpapsk_type",auStack_170);
           SetValue("wl2g.extra.wpapsk_crypto",acStack_160);
           SetValue("wl2g.extra.wpapsk_psk",pcVar9);
         }
       }
     }
   }
   else {
     iVar3 = atoi(local_61c);
     if (iVar3 == 1) {
       GetValue("wl2g.public.mode",g_work_mode_str);
       SetValue("extra_chkHz",local_61c);
       iVar3 = strcmp(__s2,"ap");
       if (iVar3 == 0) {
         SetValue("wl2g.public.mode",&DAT_2);
         SetValue("wl5g.public.mode",&DAT_2);
       }
       else {
         SetValue("wl.guest.dhcps_enable",&DAT_1);
         iVar3 = strcmp((char *)&local_3ec,"1");
         if (iVar3 != 0) {
           SetValue("wl2g.ssid1.enable",&DAT_1);
         }
         iVar3 = strcmp((char *)&local_3dc,"1");
         if (iVar3 != 0) {
           SetValue("wl5g.ssid1.enable",&DAT_1);
         }
         SetValue("wl.bcm11ac",local_61c);
         SetValue("wl5g.extra.mac",puVar1);
         SetValue("extra_hand",puVar2);
         tpi_wifi_get_ifname(5,4,&local_3bc);
         SetValue("wl5g.extra.ifname",&local_3bc);
         iVar3 = strcmp(__s2,"wisp");
         if (iVar3 == 0) {
           SetValue("wl.wisp.ifname",&local_3bc);
         }
         iVar3 = strcmp(__s2,"apclient");
         if (iVar3 != 0) {
           strcmp(__s2,"wisp");
         }
         iVar3 = strcmp(g_work_mode_str,"ap");
         if (iVar3 != 0) {
           SetValue("wl2g.public.mode",&DAT_2);
         }
         SetValue("wl5g.public.mode",__s2);
         memset(&local_3cc,0,0x10);
         sprintf((char *)&local_3cc,"wan%d_err_check",1);
         SetValue(&local_3cc,&DAT_1);
         memset(&local_3cc,0,0x10);
         sprintf((char *)&local_3cc,"wan%d_isonln",1);
         SetValue(&local_3cc,&DAT_1);
         memset(&local_3cc,0,0x10);
         sprintf((char *)&local_3cc,"wan%d_check",1);
         SetValue(&local_3cc,&DAT_1);
         pcVar4 = websGetVar((int)param_1,"ssid",&DAT_0);
         set_cn_ssid_ori_encode(local_61c,pcVar4);
         SetValue("wl5g.extra.ssid",pcVar4);
         iVar3 = strcmp(__s2,"wisp");
         if (iVar3 == 0) {
           SetValue("wan1.connecttype",&DAT_1);
           SetValue("wl.wisp.access_mode",&DAT_6);
           GetValue("wan1.dynamicMTU",auStack_150);
           SetValue("wl.wisp.mtu",auStack_150);
         }
         pcVar4 = websGetVarWithValidate((int)param_1,"security",9);
         if (pcVar4 == (char *)0x0) {
           local_63c = (size_t *)0x1;
           goto LAB_4;
         }
         SetValue("wl5g.extra.security",pcVar4);
         iVar3 = strcmp(pcVar4,"none");
         if (iVar3 != 0) {
           iVar3 = strcmp(pcVar4,"wep");
           if (iVar3 == 0) {
             puVar1 = websGetVar((int)param_1,"wepauth","shared");
             puVar2 = websGetVar((int)param_1,"wepkey",&DAT_3);
             pcVar4 = websGetVar((int)param_1,"wepkey1",&DAT_0);
             puVar5 = websGetVar((int)param_1,"wepkey2",&DAT_0);
             puVar6 = websGetVar((int)param_1,"wepkey3",&DAT_0);
             puVar7 = websGetVar((int)param_1,"wepkey4",&DAT_0);
             if (*pcVar4 == '\0') {
               local_63c = (size_t *)0x1;
               goto LAB_4;
             }
             SetValue("wl5g.extra.wep_type",puVar1);
             SetValue("wl5g.extra.wep_key",puVar2);
             SetValue("wl5g.extra.wep_key1",pcVar4);
             SetValue("wl5g.extra.wep_key2",puVar5);
             SetValue("wl5g.extra.wep_key3",puVar6);
             SetValue("wl5g.extra.wep_key4",puVar7);
           }
           else {
             iVar3 = strcmp(pcVar4,"wpapsk");
             if (iVar3 != 0) {
               local_63c = (size_t *)0x1;
               goto LAB_4;
             }
             pcVar4 = websGetVar((int)param_1,"wpapsk_type","wpa&wpa2");
             pcVar8 = websGetVar((int)param_1,"wpapsk_crypto",&DAT_7);
             pcVar9 = websGetVar((int)param_1,"wpapsk_key",&DAT_0);
             if ((*pcVar9 == '\0') && (sVar10 = strlen(pcVar9), sVar10 < 8)) {
               local_63c = (size_t *)0x1;
               goto LAB_4;
             }
             iVar3 = strcmp(pcVar4,"wpa");
             if (iVar3 == 0) {
               memcpy(auStack_148,&DAT_8,4);
             }
             else {
               iVar3 = strcmp(pcVar4,"wpa2");
               if (iVar3 == 0) {
                 memcpy(auStack_148,&DAT_9,5);
               }
               else {
                 memcpy(auStack_148,"psk psk2",9);
               }
             }
             iVar3 = strcmp(pcVar8,"tkip&aes");
             if (iVar3 == 0) {
               memcpy(acStack_138,"tkip+aes",9);
             }
             else {
               strcpy(acStack_138,pcVar8);
             }
             SetValue("wl5g.extra.wpapsk_type",auStack_148);
             SetValue("wl5g.extra.wpapsk_crypto",acStack_138);
             SetValue("wl5g.extra.wpapsk_psk",pcVar9);
           }
         }
       }
     }
   }
   GetValue("wl2g.public.mode",acStack_5ec);
   iVar3 = strcmp(acStack_5ec,"ap");
   if (iVar3 != 0) {
-    set_idx_to_mib("wl2g.ssidxx.wps_enable",0x51ae30,0,(int)puVar12);
-    set_idx_to_mib("wl5g.ssidxx.wps_enable",0x51ae30,0,(int)puVar12);
-    set_idx_to_mib("wl2g.ssidxx.enable",0x51ae30,1,(int)puVar12);
+    set_idx_to_mib("wl2g.ssidxx.wps_enable",0x51d560,0,(int)puVar12);
+    set_idx_to_mib("wl5g.ssidxx.wps_enable",0x51d560,0,(int)puVar12);
+    set_idx_to_mib("wl2g.ssidxx.enable",0x51d560,1,(int)puVar12);
     param_4 = puVar12;
-    set_idx_to_mib("wl5g.ssidxx.enable",0x51ae30,1,(int)puVar12);
+    set_idx_to_mib("wl5g.ssidxx.enable",0x51d560,1,(int)puVar12);
     SetValue("wl.guest.dhcps_enable",&DAT_1);
   }
   GetValue("wl5g.public.mode",acStack_5ec);
   iVar3 = strcmp(acStack_5ec,"ap");
   if (iVar3 != 0) {
-    set_idx_to_mib("wl2g.ssidxx.wps_enable",0x51ae30,0,(int)puVar12);
-    set_idx_to_mib("wl5g.ssidxx.wps_enable",0x51ae30,0,(int)puVar12);
-    set_idx_to_mib("wl2g.ssidxx.enable",0x51ae30,1,(int)puVar12);
-    set_idx_to_mib("wl5g.ssidxx.enable",0x51ae30,1,(int)puVar12);
+    set_idx_to_mib("wl2g.ssidxx.wps_enable",0x51d560,0,(int)puVar12);
+    set_idx_to_mib("wl5g.ssidxx.wps_enable",0x51d560,0,(int)puVar12);
+    set_idx_to_mib("wl2g.ssidxx.enable",0x51d560,1,(int)puVar12);
+    set_idx_to_mib("wl5g.ssidxx.enable",0x51d560,1,(int)puVar12);
     SetValue("wl.guest.dhcps_enable",&DAT_1);
     param_4 = puVar12;
   }
   local_198 = 0;
   local_194 = 0;
   local_190 = 0;
   local_18c = 0;
   GetValue("sys.sched.wifi.enable",&local_198);
   iVar3 = strcmp((char *)&local_198,"1");
   if (iVar3 == 0) {
     SetValue("sys.sched.wifi.enable",&DAT_1);
     SetValue("nkgw.wlan.listnum",&DAT_1);
     memset(&local_108,0,0x100);
     sprintf((char *)&local_108,"op=%d",2);
     send_msg_to_netctrl(0x27,&local_108);
   }
   local_188 = 0;
   local_184 = 0;
   local_180 = 0;
   local_17c = 0;
   GetValue("sys.powersleep.enable",&local_188);
   iVar3 = strcmp((char *)&local_188,"1");
   if (iVar3 == 0) {
     SetValue("sys.powersleep.enable",&DAT_1);
     doSystemCmd("cfm post netctrl %d",0x27);
+    Usb_Up();
+    doSystemCmd("insmod /lib/modules/2.6.36.4brcmarm/kernel/drivers/usb/host/ohci-hcd.ko");
+    doSystemCmd("insmod /lib/modules/2.6.36.4brcmarm/kernel/drivers/usb/host/ehci-hcd.ko");
+    doSystemCmd("insmod /lib/modules/2.6.36.4brcmarm/kernel/drivers/usb/host/xhci-hcd.ko");
   }
   iVar3 = strcmp((char *)&local_1a8,"apclient");
   if ((iVar3 == 0) || (iVar3 = strcmp(__s2,"apclient"), iVar3 == 0)) {
     SetValue("dhcps.en",&DAT_3);
   }
   iVar3 = strcmp(__s2,"wisp");
   if (iVar3 == 0) {
     SetValue("wan1.ppoe.double.access",&DAT_1);
   }
   GetValue("wl2g.public.mode",&local_614);
   GetValue("wl5g.public.mode",&local_604);
   iVar3 = strcmp((char *)&local_614,"wisp");
   if ((iVar3 == 0) || (iVar3 = strcmp((char *)&local_604,"wisp"), iVar3 == 0)) {
     SetValue("vpn.ser.pptpwanid",&DAT_10);
     SetValue("vpn.cli.pptpwanid",&DAT_10);
     SetValue("vpn.cli.l2tpwanid",&DAT_10);
   }
   else {
     SetValue("vpn.ser.pptpwanid",&DAT_3);
     SetValue("vpn.cli.pptpwanid",&DAT_3);
     SetValue("vpn.cli.l2tpwanid",&DAT_3);
   }
   iVar3 = memcmp(&local_614,"apclient",8);
   if ((iVar3 == 0) || (iVar3 = memcmp(&local_604,"apclient",8), iVar3 == 0)) {
     sys_pktc_disable(1);
   }
   else {
     sys_pktc_disable(0);
   }
   SetValue("wans.flag",&DAT_3);
   SetValue("wans.location","1 0 0 0 0");
   SetValue("iptv.enable",&DAT_1);
   SetValue("iptv.stb.enable",&DAT_1);
   SetValue("igmp.enable",&DAT_1);
   iVar3 = CommitSyncCfm();
   if (iVar3 == 0) {
     local_63c = (size_t *)0x1;
   }
 LAB_4:
   doSystemCmd("echo \"0 0\" > /etc/conntime1");
   psVar11 = local_63c;
   sprintf((char *)asStack_4ec,"{\"errCode\":%d}");
   websTransfer(param_1,asStack_4ec,psVar11,param_4);
   if ((local_63c == (size_t *)0x0) && ((local_640 == 1 || (iVar3 = strcmp(__s2,"ap"), iVar3 != 0))))
   {
     tpi_systool_reboot();
   }
   return;
 }
 

```


## formGetRouterStatus

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.82|
|i_ratio|0.42|
|m_ratio|0.47|
|b_ratio|0.88|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|formGetRouterStatus|formGetRouterStatus|
|fullname|formGetRouterStatus|formGetRouterStatus|
|refcount|4|4|
|`length`|6248|6116|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::free<br><EXTERNAL>::getIfIp<br><EXTERNAL>::getLanIfName<br><EXTERNAL>::malloc<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::ntohl<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf</summary><EXTERNAL>::strcat<br><EXTERNAL>::strcmp<br><EXTERNAL>::strlen<br><EXTERNAL>::tpi_get_online_mac_info<br>__floatsidf<br>cJSON_AddItemToObject<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_all_phy_link<br>check_mac_in_blacklist<br>getIfMac<br>get_black_num<br>get_device_info<br>get_work_mode<br>is_lan_host<br>strtoupper<br>wanErrGetInfo<br>websDone<br>websTransfer<br>websWrite<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::free<br><EXTERNAL>::getIfIp<br><EXTERNAL>::getLanIfName<br><EXTERNAL>::malloc<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::ntohl<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf</summary><EXTERNAL>::strcat<br><EXTERNAL>::strcmp<br><EXTERNAL>::strlen<br><EXTERNAL>::tpi_get_online_mac_info<br>__floatsidf<br>cJSON_AddItemToObject<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_all_phy_link<br>check_mac_in_blacklist<br>getIfMac<br>get_black_num<br>get_device_info<br>get_usb_device_num<br>get_work_mode<br>is_lan_host<br>strtoupper<br>wanErrGetInfo<br>websDone<br>websTransfer<br>websWrite<br>write_online_upgrade_info<br>write_wan_infos</details>|
|calling|formDefineTendDa|formDefineTendDa|
|paramcount|5|5|
|`address`|0046ca14|0046ce44|
|sig|undefined __stdcall formGetRouterStatus(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined1 * param_5)|undefined __stdcall formGetRouterStatus(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined1 * param_5)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### formGetRouterStatus Called Diff


```diff
--- formGetRouterStatus called
+++ formGetRouterStatus called
@@ -27,0 +28 @@
+get_usb_device_num
```


### formGetRouterStatus Diff


```diff
--- formGetRouterStatus
+++ formGetRouterStatus
@@ -1,414 +1,410 @@
 
 void formGetRouterStatus(double param_1,int *param_2,undefined4 param_3,undefined4 param_4,
                         undefined1 *param_5)
 
 {
   undefined4 *puVar1;
   bool bVar2;
   void *__ptr;
   int iVar3;
   int iVar4;
   void *pvVar5;
   undefined3 extraout_var;
   uint uVar6;
   undefined4 uVar7;
   size_t sVar8;
   char *pcVar9;
   size_t *__ptr_00;
   size_t *psVar10;
   undefined8 uVar11;
-  void *local_938;
-  int local_92c;
-  uint local_910;
-  undefined4 *local_8fc;
-  undefined auStack_8f8 [128];
-  char acStack_878 [1024];
-  char acStack_478 [256];
+  void *local_838;
+  int local_82c;
+  uint local_810;
+  undefined4 *local_7fc;
+  undefined auStack_7f8 [128];
+  char acStack_778 [1024];
   uint local_378;
   int local_374;
   undefined auStack_370 [128];
   char acStack_2f0 [164];
   size_t local_24c;
   undefined4 local_248;
   undefined4 local_244;
   undefined4 local_240;
   undefined4 local_23c;
   undefined4 local_238;
   undefined4 local_234;
   undefined4 local_230;
   undefined auStack_22c [256];
   undefined4 local_12c;
   undefined4 local_128;
   undefined4 local_124;
   undefined4 local_120;
   undefined4 local_11c;
   undefined4 local_118;
   undefined4 local_114;
   undefined4 local_110;
   undefined4 local_10c;
   undefined4 local_108;
   undefined4 local_104;
   undefined4 local_100;
   undefined4 local_fc;
   undefined4 local_f8;
   undefined4 local_f4;
   undefined4 local_f0;
   undefined4 local_ec;
   undefined4 local_e8;
   undefined4 local_e4;
   undefined4 local_e0;
   undefined4 local_dc;
   undefined4 local_d8;
   undefined4 local_d4;
   undefined4 local_d0;
   undefined4 local_cc;
   undefined4 local_c8;
   undefined4 local_c4;
   undefined4 local_c0;
   undefined4 local_bc;
   undefined4 local_b8;
   undefined4 local_b4;
   undefined4 local_b0;
   undefined4 local_ac;
   uint32_t local_a8;
   undefined4 local_a4;
   undefined4 local_a0;
   undefined4 local_9c;
   undefined4 local_98;
   undefined4 local_94;
   undefined4 local_90;
   undefined4 local_8c;
   undefined4 local_88;
   undefined4 local_84;
   undefined4 local_80;
   undefined4 local_7c;
   undefined4 local_78;
   undefined4 local_74;
   undefined4 local_70;
   undefined4 local_6c;
   undefined4 local_68;
   undefined4 local_64;
   undefined4 local_60;
   undefined4 local_5c;
   undefined4 local_58;
   undefined4 local_54;
   undefined4 local_50;
   undefined4 local_4c;
   undefined4 local_48;
   undefined4 local_44;
   undefined4 local_40;
   undefined4 local_3c;
   undefined4 local_38;
   undefined4 local_34;
   undefined4 local_30;
   undefined4 local_2c;
   undefined4 local_28;
   undefined4 local_24;
   undefined4 local_20;
   undefined4 local_1c;
   undefined4 local_18;
   
-  local_8fc = (undefined4 *)0x0;
-  memset(auStack_8f8,0,0x80);
-  memset(acStack_878,0,0x400);
-  memset(acStack_478,0,0x100);
-  local_910 = 0;
+  local_7fc = (undefined4 *)0x0;
+  memset(auStack_7f8,0,0x80);
+  memset(acStack_778,0,0x400);
+  local_810 = 0;
   local_378 = 0;
   local_374 = 0;
-  local_938 = (void *)0x0;
+  local_838 = (void *)0x0;
   local_24c = 0;
   local_248 = 0;
   local_244 = 0;
   local_240 = 0;
   local_23c = 0;
   local_238 = 0;
   local_234 = 0;
   local_230 = 0;
   memset(auStack_22c,0,0x100);
   local_12c = 0;
   local_128 = 0;
   local_124 = 0;
   local_120 = 0;
   local_11c = 0;
   local_118 = 0;
   local_114 = 0;
   local_110 = 0;
   local_10c = 0;
   local_108 = 0;
   local_104 = 0;
   local_100 = 0;
   local_fc = 0;
   local_f8 = 0;
   local_f4 = 0;
   local_f0 = 0;
   local_ec = 0;
   local_e8 = 0;
   local_e4 = 0;
   local_e0 = 0;
   local_dc = 0;
   local_d8 = 0;
   local_d4 = 0;
   local_d0 = 0;
   local_cc = 0;
   local_c8 = 0;
   local_c4 = 0;
   local_c0 = 0;
   local_bc = 0;
   local_b8 = 0;
   local_b4 = 0;
   local_b0 = 0;
   local_ac = 0;
   local_a8 = 0;
   local_a4 = 0;
   local_a0 = 0;
   local_9c = 0;
   local_98 = 0;
   local_94 = 0;
   local_90 = 0;
   local_8c = 0;
   local_88 = 0;
   local_84 = 0;
   local_80 = 0;
   local_7c = 0;
   local_78 = 0;
   local_74 = 0;
   local_70 = 0;
   local_6c = 0;
   __ptr = malloc(0x5000);
   if (__ptr == (void *)0x0) {
     psVar10 = (size_t *)0x1;
     sprintf((char *)&local_24c,"{\"errCode\":%d}");
     websTransfer(param_2,&local_24c,psVar10,param_5);
   }
   else {
     tpi_get_online_mac_info(__ptr,0x5000,&local_374);
     if (0 < local_374) {
-      local_938 = __ptr;
+      local_838 = __ptr;
     }
     get_work_mode(&local_d8);
     if (local_374 != 0) {
-      for (local_92c = 0; local_92c < local_374; local_92c = local_92c + 1) {
-        local_a8 = ntohl(*(uint32_t *)((int)local_938 + local_92c * 0x161 + 0x155));
+      for (local_82c = 0; local_82c < local_374; local_82c = local_82c + 1) {
+        local_a8 = ntohl(*(uint32_t *)((int)local_838 + local_82c * 0x161 + 0x155));
         pcVar9 = (char *)(local_a8 >> 8 & 0xff);
         sprintf((char *)&local_c8,"%u.%u.%u.%u",local_a8 & 0xff,pcVar9,local_a8 >> 0x10 & 0xff,
                 local_a8 >> 0x18);
         local_64 = 0;
         local_60 = 0;
         local_5c = 0;
         local_58 = 0;
         iVar3 = GetValue("cgi_debug",&local_64);
         if ((iVar3 != 0) && (iVar3 = strcmp("on",(char *)&local_64), iVar3 == 0)) {
           pcVar9 = "formGetRouterStatus";
           printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                 "formGetRouterStatus",0x8c8,debug_color[1],&local_c8);
+                 "formGetRouterStatus",0x8c7,debug_color[1],&local_c8);
         }
-        iVar3 = is_lan_host(*(uint32_t *)((int)local_938 + local_92c * 0x161 + 0x155));
+        iVar3 = is_lan_host(*(uint32_t *)((int)local_838 + local_82c * 0x161 + 0x155));
         local_54 = 0;
         local_50 = 0;
         local_4c = 0;
         local_48 = 0;
         iVar4 = GetValue("cgi_debug",&local_54);
         if ((iVar4 != 0) && (iVar4 = strcmp("on",(char *)&local_54), iVar4 == 0)) {
           pcVar9 = "formGetRouterStatus";
           printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                 "formGetRouterStatus",0x8ca,debug_color[1],&local_c8);
+                 "formGetRouterStatus",0x8c9,debug_color[1],&local_c8);
         }
         iVar4 = strcmp((char *)&local_d8,"ap");
         if (((iVar4 != 0) || (iVar4 = strcmp((char *)(param_2 + 0xc),(char *)&local_c8), iVar4 == 0)
-            ) || (*(char *)((int)local_938 + local_92c * 0x161) == '\x02')) {
+            ) || (*(char *)((int)local_838 + local_82c * 0x161) == '\x02')) {
           local_44 = 0;
           local_40 = 0;
           local_3c = 0;
           local_38 = 0;
           iVar4 = GetValue("cgi_debug",&local_44);
           if ((iVar4 != 0) && (iVar4 = strcmp("on",(char *)&local_44), iVar4 == 0)) {
             pcVar9 = "formGetRouterStatus";
             printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                   "formGetRouterStatus",0x8d0,debug_color[1],&local_c8);
+                   "formGetRouterStatus",0x8cf,debug_color[1],&local_c8);
           }
           if ((iVar3 != 1) ||
-             (iVar4 = check_mac_in_blacklist((char *)((int)local_938 + local_92c * 0x161 + 3)),
+             (iVar4 = check_mac_in_blacklist((char *)((int)local_838 + local_82c * 0x161 + 3)),
              iVar4 == 0)) {
             local_34 = 0;
             local_30 = 0;
             local_2c = 0;
             local_28 = 0;
             iVar4 = GetValue("cgi_debug",&local_34);
             if ((iVar4 != 0) && (iVar4 = strcmp("on",(char *)&local_34), iVar4 == 0)) {
               pcVar9 = "formGetRouterStatus";
               printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                     "formGetRouterStatus",0x8d7,debug_color[1],&local_c8);
+                     "formGetRouterStatus",0x8d6,debug_color[1],&local_c8);
             }
             iVar4 = strcmp((char *)&local_d8,"ap");
             if (((iVar4 == 0) || (iVar3 != 2)) ||
-               (*(int *)((int)local_938 + local_92c * 0x161 + 0x155) == 0)) {
+               (*(int *)((int)local_838 + local_82c * 0x161 + 0x155) == 0)) {
               local_24 = 0;
               local_20 = 0;
               local_1c = 0;
               local_18 = 0;
-              iVar4 = GetValue("cgi_debug",&local_24);
-              if ((iVar4 != 0) && (iVar4 = strcmp("on",(char *)&local_24), iVar4 == 0)) {
+              iVar3 = GetValue("cgi_debug",&local_24);
+              if ((iVar3 != 0) && (iVar3 = strcmp("on",(char *)&local_24), iVar3 == 0)) {
                 pcVar9 = "formGetRouterStatus";
                 printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                       "formGetRouterStatus",0x8e0,debug_color[1],&local_c8);
+                       "formGetRouterStatus",0x8df,debug_color[1],&local_c8);
               }
-              if ((iVar3 != 0) || (*(char *)((int)local_938 + local_92c * 0x161) == '\x02')) {
-                local_910 = local_910 + 1;
-              }
+              local_810 = local_810 + 1;
             }
           }
         }
         param_5 = pcVar9;
       }
     }
-    local_8fc = (undefined4 *)cJSON_CreateObject();
+    local_7fc = (undefined4 *)cJSON_CreateObject();
     local_68 = 0;
     GetValue("wans.flag",&local_68);
     iVar3 = atoi((char *)&local_68);
     iVar3 = wanErrGetInfo(iVar3);
     GetValue("wl2g.public.enable",&local_a4);
     GetValue("wl5g.public.enable",&local_a0);
     iVar4 = atoi((char *)&local_a0);
-    puVar1 = local_8fc;
+    puVar1 = local_7fc;
     if (iVar4 == 0) {
       pvVar5 = cJSON_CreateString("0");
       cJSON_AddItemToObject((int)puVar1,"wl5gEn",(int)pvVar5);
-      puVar1 = local_8fc;
+      puVar1 = local_7fc;
       pvVar5 = cJSON_CreateString("");
       cJSON_AddItemToObject((int)puVar1,"wl5gName",(int)pvVar5);
     }
     else {
       memset(&local_9c,0,0x20);
       memset(&local_7c,0,0x10);
       GetValue("wl5g.ssid0.ssid",&local_9c);
       GetValue("wl5g.ssid0.security",&local_7c);
       iVar4 = strcmp((char *)&local_7c,"none");
       if (iVar4 == 0) {
         memcpy(&local_7c,&DAT_1,2);
       }
       else {
         memcpy(&local_7c,&DAT_2,2);
       }
-      puVar1 = local_8fc;
+      puVar1 = local_7fc;
       pvVar5 = cJSON_CreateString("1");
       cJSON_AddItemToObject((int)puVar1,"wl5gEn",(int)pvVar5);
-      puVar1 = local_8fc;
+      puVar1 = local_7fc;
       pvVar5 = cJSON_CreateString((char *)&local_9c);
       cJSON_AddItemToObject((int)puVar1,"wl5gName",(int)pvVar5);
     }
     iVar4 = atoi((char *)&local_a4);
-    puVar1 = local_8fc;
+    puVar1 = local_7fc;
     if (iVar4 == 0) {
       pvVar5 = cJSON_CreateString("0");
       cJSON_AddItemToObject((int)puVar1,"wl24gEn",(int)pvVar5);
-      puVar1 = local_8fc;
+      puVar1 = local_7fc;
       pvVar5 = cJSON_CreateString("");
       cJSON_AddItemToObject((int)puVar1,"wl24gName",(int)pvVar5);
     }
     else {
       memset(&local_9c,0,0x20);
       memset(&local_7c,0,0x10);
       GetValue("wl2g.ssid0.ssid",&local_9c);
       GetValue("wl2g.ssid0.security",&local_7c);
       iVar4 = strcmp((char *)&local_7c,"none");
       if (iVar4 == 0) {
         memcpy(&local_7c,&DAT_1,2);
       }
       else {
         memcpy(&local_7c,&DAT_2,2);
       }
-      puVar1 = local_8fc;
+      puVar1 = local_7fc;
       pvVar5 = cJSON_CreateString("1");
       cJSON_AddItemToObject((int)puVar1,"wl24gEn",(int)pvVar5);
-      puVar1 = local_8fc;
+      puVar1 = local_7fc;
       pvVar5 = cJSON_CreateString((char *)&local_9c);
       cJSON_AddItemToObject((int)puVar1,"wl24gName",(int)pvVar5);
     }
-    for (local_92c = 0; puVar1 = local_8fc, local_92c < 5; local_92c = local_92c + 1) {
-      bVar2 = check_all_phy_link(local_92c);
-      if (local_92c == 0) {
+    for (local_82c = 0; puVar1 = local_7fc, local_82c < 5; local_82c = local_82c + 1) {
+      bVar2 = check_all_phy_link(local_82c);
+      if (local_82c == 0) {
         sprintf((char *)&local_11c,"%d",CONCAT31(extraout_var,bVar2));
 LAB_3:
         strcat((char *)&local_118,(char *)&local_11c);
       }
-      else if (local_92c != 1) {
+      else if (local_82c != 1) {
         sprintf((char *)&local_11c,"|%d",CONCAT31(extraout_var,bVar2));
         goto LAB_3;
       }
     }
     pvVar5 = cJSON_CreateString((char *)&local_118);
     cJSON_AddItemToObject((int)puVar1,"lineup",(int)pvVar5);
-    puVar1 = local_8fc;
-    uVar11 = __floatsidf(local_910);
+    iVar4 = get_usb_device_num();
+    sprintf((char *)&local_6c,"%d",iVar4);
+    puVar1 = local_7fc;
+    pvVar5 = cJSON_CreateString((char *)&local_6c);
+    cJSON_AddItemToObject((int)puVar1,"usbNum",(int)pvVar5);
+    puVar1 = local_7fc;
+    uVar11 = __floatsidf(local_810);
     pvVar5 = cJSON_CreateNumber((uint)uVar11,(uint)((ulonglong)uVar11 >> 0x20));
     cJSON_AddItemToObject((int)puVar1,"clientNum",(int)pvVar5);
     uVar6 = get_black_num((int *)&local_378);
-    puVar1 = local_8fc;
+    puVar1 = local_7fc;
     uVar11 = __floatsidf(uVar6);
     pvVar5 = cJSON_CreateNumber((uint)uVar11,(uint)((ulonglong)uVar11 >> 0x20));
     cJSON_AddItemToObject((int)puVar1,"blackNum",(int)pvVar5);
-    puVar1 = local_8fc;
+    puVar1 = local_7fc;
     uVar11 = __floatsidf(local_378);
     pvVar5 = cJSON_CreateNumber((uint)uVar11,(uint)((ulonglong)uVar11 >> 0x20));
     cJSON_AddItemToObject((int)puVar1,"listNum",(int)pvVar5);
     memset(auStack_370,0,0x124);
     get_device_info(0,auStack_370);
-    puVar1 = local_8fc;
+    puVar1 = local_7fc;
     pvVar5 = cJSON_CreateString(acStack_2f0);
     cJSON_AddItemToObject((int)puVar1,"deviceName",(int)pvVar5);
-    memset(acStack_878,0,0x400);
+    memset(acStack_778,0,0x400);
     uVar7 = getLanIfName();
-    iVar4 = getIfIp(uVar7,acStack_878);
-    puVar1 = local_8fc;
+    iVar4 = getIfIp(uVar7,acStack_778);
+    puVar1 = local_7fc;
     if (iVar4 < 0) {
       pvVar5 = cJSON_CreateString("");
       cJSON_AddItemToObject((int)puVar1,"lanIP",(int)pvVar5);
     }
     else {
-      pvVar5 = cJSON_CreateString(acStack_878);
+      pvVar5 = cJSON_CreateString(acStack_778);
       cJSON_AddItemToObject((int)puVar1,"lanIP",(int)pvVar5);
     }
-    memset(acStack_878,0,0x400);
-    iVar4 = GetValue("lan.macaddr",acStack_878);
-    if ((iVar4 == 0) || (sVar8 = strlen(acStack_878), sVar8 < 6)) {
-      memset(acStack_878,0,0x400);
+    memset(acStack_778,0,0x400);
+    iVar4 = GetValue("lan.macaddr",acStack_778);
+    if ((iVar4 == 0) || (sVar8 = strlen(acStack_778), sVar8 < 6)) {
+      memset(acStack_778,0,0x400);
       pcVar9 = (char *)getLanIfName();
-      iVar4 = getIfMac(pcVar9,acStack_878);
+      iVar4 = getIfMac(pcVar9,acStack_778);
       if (iVar4 == 0) {
-        strtoupper(acStack_878,(undefined *)&local_f8);
+        strtoupper(acStack_778,(undefined *)&local_f8);
       }
       else {
         memcpy(&local_f8,"00:00:00:00:00:00",0x12);
       }
     }
     else {
-      strtoupper(acStack_878,(undefined *)&local_f8);
-    }
-    puVar1 = local_8fc;
+      strtoupper(acStack_778,(undefined *)&local_f8);
+    }
+    puVar1 = local_7fc;
     pvVar5 = cJSON_CreateString((char *)&local_f8);
     cJSON_AddItemToObject((int)puVar1,"lanMAC",(int)pvVar5);
-    puVar1 = local_8fc;
+    puVar1 = local_7fc;
     pvVar5 = cJSON_CreateString((char *)&local_d8);
     cJSON_AddItemToObject((int)puVar1,"workMode",(int)pvVar5);
     sprintf((char *)&local_12c,"%d",iVar3);
-    puVar1 = local_8fc;
-    pvVar5 = cJSON_CreateString((char *)&local_12c);
-    cJSON_AddItemToObject((int)puVar1,"apStatus",(int)pvVar5);
-    memset(acStack_478,0,0x100);
-    GetValue("wl5g.public.country",acStack_478);
-    puVar1 = local_8fc;
-    psVar10 = (size_t *)cJSON_CreateString(acStack_478);
-    cJSON_AddItemToObject((int)puVar1,"countryCode",(int)psVar10);
-    write_wan_infos((int *)&local_8fc);
-    write_online_upgrade_info((int *)&local_8fc);
-    __ptr_00 = (size_t *)cJSON_Print(param_1,(int)local_8fc);
-    cJSON_Delete(local_8fc);
+    puVar1 = local_7fc;
+    psVar10 = (size_t *)cJSON_CreateString((char *)&local_12c);
+    cJSON_AddItemToObject((int)puVar1,"apStatus",(int)psVar10);
+    write_wan_infos((int *)&local_7fc);
+    write_online_upgrade_info((int *)&local_7fc);
+    __ptr_00 = (size_t *)cJSON_Print(param_1,(int)local_7fc);
+    cJSON_Delete(local_7fc);
     websWrite((int)param_2,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar10,param_5);
     websWrite((int)param_2,(size_t *)&DAT_4,__ptr_00,param_5);
     free(__ptr_00);
     free(__ptr);
     websDone(param_2,200);
   }
   return;
 }
 

```


## formDefineTendDa

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.97|
|i_ratio|0.19|
|m_ratio|0.98|
|b_ratio|0.98|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|formDefineTendDa|formDefineTendDa|
|fullname|formDefineTendDa|formDefineTendDa|
|refcount|4|4|
|`length`|5912|6136|
|`called`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>GetProduct<br>SetWebIpAccess<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>addWifiMacFilter<br>add_white_node<br>aspGetCfm<br>aspGetCharset<br>aspGetMaxNatNum</summary>aspGetModeShow<br>aspGetPortShow<br>aspGetWanNum<br>aspGetfilterMaxNum<br>aspGetifnlist<br>aspNatSet<br>aspTendaGetDhcpClients<br>aspTendaGetLongString<br>aspTendaGetStatus<br>asp_error_message<br>asp_error_redirect_url<br>aspmGetIPRate<br>aspmGetRouteTable<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddMacfilterRule<br>formAdvGetLanIp<br>formAliScheduleStatus<br>formBulletinSet<br>formDefineUcloudv2<br>formDelMacfilterRule<br>formExit<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formGetWifiWps<br>formMfgTest<br>formNatSet<br>formNotNowUpgrade<br>formQuickIndex<br>formSetAutoQosInfo<br>formSetCfm<br>formSetClientState<br>formSetDeviceName<br>formSetFirewallCfg<br>formSetIptv<br>formSetMacFilterCfg<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetParentControlEnable<br>formSetQosBand<br>formSetRebootTimer<br>formSetSafeWanWebMan<br>formSetSchedLed<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetVirtualSer<br>formSetWifiWps<br>formStartWifiWps<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formTendaModelStatus<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiAntijamSet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBasicSet<br>formWifiBeamformingGet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiDhcpGuestSet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiPowerSet<br>formWifiRadioGet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiStatisticClear<br>formWifiStatus<br>formWifiWpsOOB<br>formWifiWpsStart<br>formWriteFacMac<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_get<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>form_usb_get<br>formgetPptpOnlineClient<br>formsetNotUpgrade<br>fromAddressNat<br>fromAdvGetMacMtuWan<br>fromAdvSetLanip<br>fromAdvSetMacMtuWan<br>fromAdvSetPortVlan<br>fromDhcpListClient<br>fromDhcpSetSer<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromLogsSetting<br>fromNatStaticSetting<br>fromSetIpMacBind<br>fromSetRouteStatic<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromSysStatusHandle<br>fromSysToolBaseUser<br>fromSysToolChangePwd<br>fromSysToolGetUpgrade<br>fromSysToolReboot<br>fromSysToolRestoreSet<br>fromSysToolSetUpgrade<br>fromSysToolSysLog<br>fromSysToolTime<br>fromWanPolicy<br>fromWizardHandle<br>fromgetApModeCfg<br>fromsetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>initWifiMacFilter<br>mDMZGetCfg<br>mDMZSetCfg<br>mNatGetStatic<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websAspDefine<br>websFormDefine</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>GetProduct<br>SetWebIpAccess<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>addWifiMacFilter<br>add_white_node<br>aspGetCfm<br>aspGetCharset<br>aspGetMaxNatNum</summary>aspGetModeShow<br>aspGetPortShow<br>aspGetWanNum<br>aspGetfilterMaxNum<br>aspGetifnlist<br>aspNatSet<br>aspTendaGetDhcpClients<br>aspTendaGetLongString<br>aspTendaGetStatus<br>asp_error_message<br>asp_error_redirect_url<br>aspmGetIPRate<br>aspmGetRouteTable<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddMacfilterRule<br>formAdvGetLanIp<br>formAliScheduleStatus<br>formBulletinSet<br>formDefineUcloudv2<br>formDelMacfilterRule<br>formExit<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetUsbPrint<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formGetWifiWps<br>formMfgTest<br>formNatSet<br>formNotNowUpgrade<br>formQuickIndex<br>formSetAutoQosInfo<br>formSetCfm<br>formSetClientState<br>formSetDeviceName<br>formSetFirewallCfg<br>formSetIptv<br>formSetMacFilterCfg<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetParentControlEnable<br>formSetQosBand<br>formSetRebootTimer<br>formSetSafeWanWebMan<br>formSetSambaConf<br>formSetSchedLed<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetUsbPrint<br>formSetVirtualSer<br>formSetWifiWps<br>formStartWifiWps<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formTendaModelStatus<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiAntijamSet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBasicSet<br>formWifiBeamformingGet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiDhcpGuestSet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiPowerSet<br>formWifiRadioGet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiStatisticClear<br>formWifiStatus<br>formWifiWpsOOB<br>formWifiWpsStart<br>formWriteFacMac<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_get<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>form_usb_get<br>formgetPptpOnlineClient<br>formsetNotUpgrade<br>formsetUsbUnload<br>fromAddressNat<br>fromAdvGetMacMtuWan<br>fromAdvSetLanip<br>fromAdvSetMacMtuWan<br>fromAdvSetPortVlan<br>fromDhcpListClient<br>fromDhcpSetSer<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromLogsSetting<br>fromNatStaticSetting<br>fromSetIpMacBind<br>fromSetRouteStatic<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromSysStatusHandle<br>fromSysToolBaseUser<br>fromSysToolChangePwd<br>fromSysToolGetUpgrade<br>fromSysToolReboot<br>fromSysToolRestoreSet<br>fromSysToolSetUpgrade<br>fromSysToolSysLog<br>fromSysToolTime<br>fromWanPolicy<br>fromWizardHandle<br>fromgetApModeCfg<br>fromsetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>initWifiMacFilter<br>mDMZGetCfg<br>mDMZSetCfg<br>mNatGetStatic<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websAspDefine<br>websFormDefine</details>|
|calling|initWebs|initWebs|
|paramcount|0|0|
|`address`|0044d790|0044d990|
|sig|undefined __stdcall formDefineTendDa(void)|undefined __stdcall formDefineTendDa(void)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### formDefineTendDa Called Diff


```diff
--- formDefineTendDa called
+++ formDefineTendDa called
@@ -55,0 +56 @@
+formGetSambaConf
@@ -62,0 +64 @@
+formGetUSBStatus
@@ -63,0 +66,2 @@
+formGetUsbCfg
+formGetUsbPrint
@@ -89,0 +94 @@
+formSetSambaConf
@@ -93,0 +99 @@
+formSetUsbPrint
@@ -135,0 +142 @@
+formsetUsbUnload
```


### formDefineTendDa Diff


```diff
--- formDefineTendDa
+++ formDefineTendDa
@@ -1,190 +1,197 @@
 
 void formDefineTendDa(void)
 
 {
-  websAspDefine((bType *)0x50a200,aspTendaGetLongString);
+  websAspDefine((bType *)0x50c940,aspTendaGetLongString);
   websAspDefine((bType *)"aspTendaGetStatus",aspTendaGetStatus);
   websFormDefine((bType *)"updateUrlLog",(int)updateUrlLog);
   websFormDefine((bType *)"SysStatusHandle",(int)fromSysStatusHandle);
   websFormDefine((bType *)"GetWanStatus",(int)formGetWanStatus);
   websFormDefine((bType *)"GetSysInfo",(int)formGetSysInfo);
   websFormDefine((bType *)"GetWanStatistic",(int)formGetWanStatistic);
   websFormDefine((bType *)"GetAllWanInfo",(int)formGetAllWanInfo);
   websFormDefine((bType *)"GetWanNum",(int)formGetWanNum);
   websAspDefine((bType *)"aspGetWanNum",aspGetWanNum);
   websFormDefine((bType *)"getPortStatus",(int)formGetPortStatus);
   websFormDefine((bType *)"GetSystemStatus",(int)formGetSystemStatus);
   websFormDefine((bType *)"GetRouterStatus",(int)formGetRouterStatus);
   websFormDefine((bType *)"setNotUpgrade",(int)formsetNotUpgrade);
   websAspDefine((bType *)"aspGetCharset",aspGetCharset);
   websFormDefine((bType *)"WizardHandle",(int)fromWizardHandle);
   websFormDefine((bType *)"fast_setting_get",(int)form_fast_setting_get);
   websFormDefine((bType *)"fast_setting_pppoe_get",(int)form_fast_setting_pppoe_get);
   websFormDefine((bType *)"fast_setting_wifi_set",(int)form_fast_setting_wifi_set);
   websFormDefine((bType *)"fast_setting_pppoe_set",(int)form_fast_setting_pppoe_set);
   websFormDefine((bType *)"getWanConnectStatus",(int)formGetWanConnectStatus);
   websFormDefine((bType *)"getProduct",(int)GetProduct);
   websFormDefine((bType *)"fast_setting_internet_set",(int)form_fast_setting_internet_set);
   websFormDefine((bType *)"getSyncAccount",(int)form_SyncAccount_get);
   websFormDefine((bType *)"usb_get",(int)form_usb_get);
   websFormDefine((bType *)"SysToolpassword",(int)SysToolpassword);
   formDefineUcloudv2();
   websFormDefine((bType *)"notNowUpgrade",(int)formNotNowUpgrade);
   websFormDefine((bType *)"getHomeLink",(int)formGetHomeLink);
   websFormDefine((bType *)"AdvGetMacMtuWan",(int)fromAdvGetMacMtuWan);
   websFormDefine((bType *)"AdvSetMacMtuWan",(int)fromAdvSetMacMtuWan);
   websFormDefine((bType *)"AdvGetLanIp",(int)formAdvGetLanIp);
   websFormDefine((bType *)"AdvSetLanip",(int)fromAdvSetLanip);
   websFormDefine((bType *)"SetWebIpAccess",(int)SetWebIpAccess);
   websFormDefine((bType *)"WanPolicy",(int)fromWanPolicy);
   websFormDefine((bType *)"SetRemoteWebCfg",(int)formSetSafeWanWebMan);
   websFormDefine((bType *)"GetRemoteWebCfg",(int)formGetSafeWanWebMan);
   websFormDefine((bType *)"WanParameterSetting",(int)formWanParameterSetting);
   websFormDefine((bType *)"getWanParameters",(int)formGetWanParameter);
   websFormDefine((bType *)"getAdvanceStatus",(int)getAdvanceStatus);
   websFormDefine((bType *)"openDnsCheck",(int)setDnsCheck);
   websFormDefine((bType *)"initDnsCheck",(int)getDnsCheck);
   websFormDefine((bType *)"InsertWhite",(int)add_white_node);
   websFormDefine((bType *)"PowerSaveGet",(int)getSmartPowerManagement);
   websFormDefine((bType *)"PowerSaveSet",(int)setSmartPowerManagement);
   websFormDefine((bType *)"initSchedWifi",(int)getSchedWifi);
   websFormDefine((bType *)"openSchedWifi",(int)setSchedWifi);
   websFormDefine((bType *)"GetLEDCfg",(int)formGetSchedLed);
   websFormDefine((bType *)"SetLEDCfg",(int)formSetSchedLed);
   websFormDefine((bType *)"GetParentControlInfo",(int)GetParentControlInfo);
   websFormDefine((bType *)"saveParentControlInfo",(int)saveParentControlInfo);
   websFormDefine((bType *)"GetDhcpServer",(int)formGetDhcpServer);
   websFormDefine((bType *)"DhcpSetSer",(int)fromDhcpSetSer);
   websAspDefine((bType *)"TendaGetDhcpClients",aspTendaGetDhcpClients);
   websFormDefine((bType *)"DhcpListClient",(int)fromDhcpListClient);
   websFormDefine((bType *)"ajaxTendaGetDhcpClients",(int)formTendaGetDhcpClients);
   websAspDefine((bType *)"TendaGetDhcpClients",aspTendaGetDhcpClients);
   websFormDefine((bType *)"getOnlineList",(int)formGetOnlineList);
   websFormDefine((bType *)"GetAdvanceStatus",(int)formGetAdvanceStatus);
   websFormDefine((bType *)"SetVirtualServerCfg",(int)formSetVirtualSer);
   websFormDefine((bType *)"GetVirtualServerCfg",(int)formGetVirtualSer);
   websFormDefine((bType *)"SetDMZCfg",(int)mDMZSetCfg);
   websFormDefine((bType *)"GetDMZCfg",(int)mDMZGetCfg);
   websFormDefine((bType *)"GetUpnpCfg",(int)formGetUpnpLists);
   websFormDefine((bType *)"SetUpnpCfg",(int)formSetUpnp);
   websFormDefine((bType *)"NatStaticSetting",(int)fromNatStaticSetting);
   websFormDefine((bType *)"SetDDNSCfg",(int)formSetSysToolDDNS);
   websFormDefine((bType *)"GetDDNSCfg",(int)formGetSysToolDDNS);
   websAspDefine((bType *)"mGetRouteTable",aspmGetRouteTable);
   websFormDefine((bType *)"GetStaticRouteCfg",(int)formGetRouteStatic);
   websFormDefine((bType *)"SetStaticRouteCfg",(int)fromSetRouteStatic);
   websFormDefine((bType *)"addressNat",(int)fromAddressNat);
   websAspDefine((bType *)"mNatGetStatic",mNatGetStatic);
   websAspDefine((bType *)"asp_error_message",asp_error_message);
   websAspDefine((bType *)"asp_error_redirect_url",asp_error_redirect_url);
   websAspDefine((bType *)"mGetIPRate",aspmGetIPRate);
   websFormDefine((bType *)"AdvSetPortVlan",(int)fromAdvSetPortVlan);
   websFormDefine((bType *)"BulletinSet",(int)formBulletinSet);
   websFormDefine((bType *)"AdvSetNat",(int)formNatSet);
   websAspDefine((bType *)"NatSet",aspNatSet);
   websFormDefine((bType *)"getMacFilterCfg",(int)formGetMacFilterCfg);
   websFormDefine((bType *)"setMacFilterCfg",(int)formSetMacFilterCfg);
   websFormDefine((bType *)"parentControlEn",(int)formSetParentControlEnable);
   websFormDefine((bType *)"GetParentCtrlList",(int)formGetParentCtrlList);
   websFormDefine((bType *)"SetNetControlList",(int)formSetQosBand);
   websFormDefine((bType *)"GetNetControlList",(int)formGetQosBand);
   websFormDefine((bType *)"GetDeviceDetail",(int)formGetDeviceDetail);
   websFormDefine((bType *)"SetClientState",(int)formSetClientState);
   websFormDefine((bType *)"SetOnlineDevName",(int)formSetDeviceName);
   websFormDefine((bType *)"GetSystemSet",(int)formGetSystemSet);
   websFormDefine((bType *)"SetSpeedWan",(int)formSetSpeedWan);
   websFormDefine((bType *)"getParentalRuleList",(int)getParentControlAllInfo);
   websFormDefine((bType *)"delParentalRule",(int)delParentControlOneInfo);
   websFormDefine((bType *)"setBlackRule",(int)formAddMacfilterRule);
   websFormDefine((bType *)"delBlackRule",(int)formDelMacfilterRule);
   websFormDefine((bType *)"getBlackRuleList",(int)formGetMacfilterRuleList);
   websFormDefine((bType *)"SetIPTVCfg",(int)formSetIptv);
   websFormDefine((bType *)"GetIPTVCfg",(int)formGetIptv);
   websFormDefine((bType *)"SetFirewallCfg",(int)formSetFirewallCfg);
   websFormDefine((bType *)"GetFirewallCfg",(int)formGetFirewallCfg);
   websFormDefine((bType *)"GetDdosDefenceList",(int)formGetDdosDefenceList);
   websFormDefine((bType *)"initAutoQos",(int)formGetAutoQosInfo);
   websFormDefine((bType *)"saveAutoQos",(int)formSetAutoQosInfo);
   websFormDefine((bType *)"getQosSpeed",(int)formGetBandWidthSpeed);
   websFormDefine((bType *)"GetSySLogCfg",(int)formGetSysLog);
   websFormDefine((bType *)"SysToolSysLog",(int)fromSysToolSysLog);
   websFormDefine((bType *)"LogsSetting",(int)fromLogsSetting);
   websFormDefine((bType *)"SysToolTime",(int)fromSysToolTime);
   websFormDefine((bType *)"SysToolReboot",(int)fromSysToolReboot);
   websFormDefine((bType *)"telnet",(int)TendaTelnet);
   websFormDefine((bType *)"SysToolRestoreSet",(int)fromSysToolRestoreSet);
   websFormDefine((bType *)"SysToolChangePwd",(int)fromSysToolChangePwd);
   websFormDefine((bType *)"SysToolBaseUser",(int)fromSysToolBaseUser);
   websFormDefine((bType *)"SysToolGetUpgrade",(int)fromSysToolGetUpgrade);
   websFormDefine((bType *)"SysToolSetUpgrade",(int)fromSysToolSetUpgrade);
   websFormDefine((bType *)"GetIpMacBind",(int)fromGetIpMacBind);
   websFormDefine((bType *)"SetIpMacBind",(int)fromSetIpMacBind);
   websFormDefine((bType *)"WifiMultiSsid",(int)formWifiMultiSsid);
   websFormDefine((bType *)"WifiBasicGet",(int)formWifiBasicGet);
   websFormDefine((bType *)"WifiBasicSet",(int)formWifiBasicSet);
   websFormDefine((bType *)"WifiApScan",(int)formWifiApScan);
   websFormDefine((bType *)"WifiBeamformingGet",(int)formWifiBeamformingGet);
   websFormDefine((bType *)"WifiBeamformingSet",(int)formWifiBeamformingSet);
   websFormDefine((bType *)"WifiAntijamGet",(int)formWifiAntijamGet);
   websFormDefine((bType *)"WifiAntijamSet",(int)formWifiAntijamSet);
   websFormDefine((bType *)"WifiClientList",(int)formWifiClientList);
   websFormDefine((bType *)"WifiClientListAll",(int)formWifiClientListAll);
   websFormDefine((bType *)"WifiMacFilterGet",(int)formWifiMacFilterGet);
   websFormDefine((bType *)"WifiMacFilterSet",(int)formWifiMacFilterSet);
   websFormDefine((bType *)"initWifiMacFilter",(int)initWifiMacFilter);
   websFormDefine((bType *)"addWifiMacFilter",(int)addWifiMacFilter);
   websFormDefine((bType *)"delWifiMacFilter",(int)delWifiMacFilter);
   websFormDefine((bType *)"WifiRadioGet",(int)formWifiRadioGet);
   websFormDefine((bType *)"WifiRadioSet",(int)formWifiRadioSet);
   websFormDefine((bType *)"WifiPowerGet",(int)formWifiPowerGet);
   websFormDefine((bType *)"WifiPowerSet",(int)formWifiPowerSet);
   websFormDefine((bType *)"WifiStatistic",(int)formWifiStatistic);
   websFormDefine((bType *)"WifiStatisticClear",(int)formWifiStatisticClear);
   websFormDefine((bType *)"WifiDhcpGuestGet",(int)formWifiDhcpGuestGet);
   websFormDefine((bType *)"WifiDhcpGuestLists",(int)formWifiDhcpGuestLists);
   websFormDefine((bType *)"WifiDhcpGuestSet",(int)formWifiDhcpGuestSet);
   websFormDefine((bType *)"WifiStatus",(int)formWifiStatus);
   websFormDefine((bType *)"getAliWifiScheduled",(int)formAliScheduleStatus);
   websFormDefine((bType *)"WifiWpsStart",(int)formWifiWpsStart);
   websFormDefine((bType *)"WifiWpsOOB",(int)formWifiWpsOOB);
   websFormDefine((bType *)"WifiConfigGet",(int)formWifiConfigGet);
   websFormDefine((bType *)"WifiWpsGet",(int)formGetWifiWps);
   websFormDefine((bType *)"WifiWpsSet",(int)formSetWifiWps);
   websFormDefine((bType *)"WifiWpsStart",(int)formStartWifiWps);
+  websFormDefine((bType *)"GetUSBStatus",(int)formGetUSBStatus);
+  websFormDefine((bType *)"SetPrinterCfg",(int)formSetUsbPrint);
+  websFormDefine((bType *)"GetPrinterCfg",(int)formGetUsbPrint);
+  websFormDefine((bType *)"SetSambaCfg",(int)formSetSambaConf);
+  websFormDefine((bType *)"GetSambaCfg",(int)formGetSambaConf);
+  websFormDefine((bType *)"setUsbUnload",(int)formsetUsbUnload);
+  websFormDefine((bType *)"GetUsbCfg",(int)formGetUsbCfg);
   websFormDefine((bType *)&DAT_0,(int)TendaAte);
   websFormDefine((bType *)"WriteFacMac",(int)formWriteFacMac);
   websFormDefine((bType *)"MfgTest",(int)formMfgTest);
   websFormDefine((bType *)"TendaModelStatus",(int)formTendaModelStatus);
   websAspDefine((bType *)"GetPortShow",aspGetPortShow);
   websAspDefine((bType *)"getcfm",aspGetCfm);
   websFormDefine((bType *)"setcfm",(int)formSetCfm);
   websAspDefine((bType *)"getfilterMaxNum",aspGetfilterMaxNum);
   websAspDefine((bType *)"getModeShow",aspGetModeShow);
   websFormDefine((bType *)"ajaxTendaGetGuestDhcpClients",(int)formTendaGetGuestDhcpClients);
   websAspDefine((bType *)"getMaxNatNum",aspGetMaxNatNum);
   websFormDefine((bType *)"QuickIndex",(int)formQuickIndex);
   websAspDefine((bType *)"getifnlist",aspGetifnlist);
   websFormDefine((bType *)"SetSysAutoRebbotCfg",(int)formSetRebootTimer);
   websFormDefine((bType *)"GetSysAutoRebbotCfg",(int)formGetRebootTimer);
   websFormDefine((bType *)"SetSysTimeCfg",(int)fromSetSysTime);
   websFormDefine((bType *)"GetSysTimeCfg",(int)fromGetSysTime);
   websFormDefine((bType *)"setApModeCfg",(int)fromsetApModeCfg);
   websFormDefine((bType *)"getApModeCfg",(int)fromgetApModeCfg);
   websFormDefine((bType *)"WifiExtraSet",(int)fromSetWirelessRepeat);
   websFormDefine((bType *)"WifiExtraGet",(int)fromGetWirelessRepeat);
   websFormDefine((bType *)"WifiGuestSet",(int)fromSetWifiGusetBasic);
   websFormDefine((bType *)"WifiGuestGet",(int)fromGetWifiGusetBasic);
   websFormDefine((bType *)"GetWrlStatus",(int)fromGetWrlStatus);
   websFormDefine((bType *)"SetPptpServerCfg",(int)formSetPPTPServer);
   websFormDefine((bType *)"GetPptpServerCfg",(int)formGetPPTPServer);
   websFormDefine((bType *)"getPptpOnlineClient",(int)formgetPptpOnlineClient);
   websFormDefine((bType *)"setPptpUserList",(int)formSetPPTPUserList);
   websFormDefine((bType *)"SetPptpClientCfg",(int)formSetPPTPClient);
   websFormDefine((bType *)"GetPptpClientCfg",(int)formGetPPTPClient);
   websFormDefine((bType *)"GetVpnStatus",(int)formGetVpnStatus);
   websFormDefine((bType *)"GetSysStatus",(int)formGetSysStatus);
-  websFormDefine((bType *)"getRebootStatus",0x4509f0);
+  websFormDefine((bType *)"getRebootStatus",0x450cd0);
   websFormDefine((bType *)&DAT_1,(int)formExit);
   return;
 }
 

```


## ate_Tenda_mfg_check_wpsbutton

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.92|
|i_ratio|0.81|
|m_ratio|0.99|
|b_ratio|0.99|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|ate_Tenda_mfg_check_wpsbutton|ate_Tenda_mfg_check_wpsbutton|
|fullname|ate_Tenda_mfg_check_wpsbutton|ate_Tenda_mfg_check_wpsbutton|
|refcount|3|3|
|`length`|180|176|
|called|<EXTERNAL>::Get_Mfg_Button_Test_Result<br><EXTERNAL>::memcpy|<EXTERNAL>::Get_Mfg_Button_Test_Result<br><EXTERNAL>::memcpy|
|calling|||
|paramcount|2|2|
|`address`|0047e7e4|0047e830|
|sig|bool __stdcall ate_Tenda_mfg_check_wpsbutton(undefined4 param_1, void * param_2)|bool __stdcall ate_Tenda_mfg_check_wpsbutton(undefined4 param_1, void * param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### ate_Tenda_mfg_check_wpsbutton Diff


```diff
--- ate_Tenda_mfg_check_wpsbutton
+++ ate_Tenda_mfg_check_wpsbutton
@@ -1,16 +1,16 @@
 
 bool ate_Tenda_mfg_check_wpsbutton(undefined4 param_1,void *param_2)
 
 {
   bool bVar1;
   uint local_c;
   
   local_c = 0;
   Get_Mfg_Button_Test_Result(&local_c);
-  bVar1 = (local_c & 1) == 0;
+  bVar1 = (local_c & 4) == 0;
   if (!bVar1) {
     memcpy(param_2,"success",8);
   }
   return bVar1;
 }
 

```


## ate_nvram_set_maxpower

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.91|
|i_ratio|0.42|
|m_ratio|0.83|
|b_ratio|0.83|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|ate_nvram_set_maxpower|ate_nvram_set_maxpower|
|fullname|ate_nvram_set_maxpower|ate_nvram_set_maxpower|
|refcount|3|3|
|`length`|872|616|
|`called`|<EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ate_envram_set_common<br>set_cfm_mib|<EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ate_envram_set_common|
|calling|||
|paramcount|1|1|
|`address`|0047b034|0047b2f4|
|sig|undefined4 __stdcall ate_nvram_set_maxpower(char * param_1)|undefined4 __stdcall ate_nvram_set_maxpower(char * param_1)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### ate_nvram_set_maxpower Called Diff


```diff
--- ate_nvram_set_maxpower called
+++ ate_nvram_set_maxpower called
@@ -1,2 +0,0 @@
-<EXTERNAL>::memcpy
-<EXTERNAL>::memset
@@ -7 +4,0 @@
-set_cfm_mib
```


### ate_nvram_set_maxpower Diff


```diff
--- ate_nvram_set_maxpower
+++ ate_nvram_set_maxpower
@@ -1,58 +1,49 @@
 
 undefined4 ate_nvram_set_maxpower(char *param_1)
 
 {
   bool bVar1;
   undefined4 uVar2;
   int iVar3;
-  undefined auStack_100c [4100];
   
   printf("%s : %d\n","ate_nvram_set_maxpower",0x315);
   bVar1 = true;
-  memset(auStack_100c,0,0x1000);
   if (*param_1 == '\0') {
     uVar2 = 0;
   }
   else {
     iVar3 = strcmp(param_1,"0");
     if (iVar3 == 0) {
-      memcpy(auStack_100c,&DAT_0,4);
       puts("low power");
     }
     else {
       iVar3 = strcmp(param_1,"1");
       if (iVar3 == 0) {
-        memcpy(auStack_100c,"middle",7);
         bVar1 = false;
         puts("middle power");
       }
       else {
         iVar3 = strcmp(param_1,"2");
         if (iVar3 != 0) {
           printf("error maxpower %s \n",param_1);
           return 1;
         }
-        memcpy(auStack_100c,&DAT_1,5);
         puts("high power");
       }
     }
     iVar3 = ate_envram_set_common("wl2g.power",param_1);
     if (iVar3 == 0) {
       if ((bVar1) && (iVar3 = ate_envram_set_common("wl5g.power",param_1), iVar3 != 0)) {
         printf("5G modified failed! [maxpower=%s]\n",param_1);
         return 1;
-      }
-      set_cfm_mib(0x50f4f8,(int)auStack_100c);
-      if (bVar1) {
-        set_cfm_mib(0x50f50c,(int)auStack_100c);
       }
       uVar2 = 0;
     }
     else {
       printf("2.4G modified failed! [maxpower=%s]\n",param_1);
       uVar2 = 1;
     }
   }
   return uVar2;
 }
 

```


## fromGetSysTime

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.73|
|i_ratio|0.61|
|m_ratio|0.85|
|b_ratio|0.79|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|fromGetSysTime|fromGetSysTime|
|fullname|fromGetSysTime|fromGetSysTime|
|refcount|4|4|
|`length`|1588|1492|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::free<br><EXTERNAL>::localtime<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::time<br>cJSON_AddItemToObject</summary>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>websDone<br>websWrite</details>|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::free<br><EXTERNAL>::localtime<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::time<br>cJSON_AddItemToObject<br>cJSON_CreateObject</summary>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>websDone<br>websWrite</details>|
|calling|formDefineTendDa|formDefineTendDa|
|paramcount|2|2|
|`address`|004a8d5c|004a8dac|
|sig|undefined __stdcall fromGetSysTime(double param_1, int * param_2)|undefined __stdcall fromGetSysTime(double param_1, int * param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### fromGetSysTime Called Diff


```diff
--- fromGetSysTime called
+++ fromGetSysTime called
@@ -6 +5,0 @@
-<EXTERNAL>::printf
```


### fromGetSysTime Diff


```diff
--- fromGetSysTime
+++ fromGetSysTime
@@ -1,119 +1,114 @@
 
 void fromGetSysTime(double param_1,int *param_2)
 
 {
-  int iVar1;
-  tm *ptVar2;
-  undefined4 *puVar3;
+  tm *ptVar1;
+  undefined4 *puVar2;
+  int iVar3;
   void *pvVar4;
   char *__src;
   size_t *psVar5;
   size_t *__ptr;
   undefined4 local_16c;
   undefined4 local_168;
   undefined4 local_164;
   undefined4 local_160;
-  int local_15c;
+  time_t tStack_15c;
   undefined4 local_158;
   undefined4 local_154;
   undefined4 local_150;
   undefined4 local_14c;
   undefined4 local_148;
   undefined4 local_144;
   undefined4 local_140;
   undefined4 local_13c;
   undefined4 local_138;
   undefined4 local_134;
   undefined4 local_130;
   undefined4 local_12c;
   char acStack_128 [256];
   undefined4 local_28;
   undefined4 local_24;
   undefined4 local_20;
   undefined4 local_1c;
   undefined4 local_18;
   undefined4 local_14;
   undefined4 local_10;
   undefined4 local_c;
   
   local_16c = 0;
   local_168 = 0;
   local_164 = 0;
   local_160 = 0;
   local_158 = 0;
   local_154 = 0;
   local_150 = 0;
   local_14c = 0;
   local_148 = 0;
   local_144 = 0;
   local_140 = 0;
   local_13c = 0;
   local_138 = 0;
   local_134 = 0;
   local_130 = 0;
   local_12c = 0;
   memset(acStack_128,0,0x100);
   local_28 = 0;
   local_24 = 0;
   local_20 = 0;
   local_1c = 0;
   local_18 = 0;
   local_14 = 0;
   local_10 = 0;
   local_c = 0;
-  GetValue("sys.timezone",&local_148);
-  GetValue("sys.timenextzone",&local_18);
-  time(&local_15c);
-  iVar1 = strcmp((char *)&local_18,"10");
-  if (iVar1 == 0) {
-    local_15c = local_15c + -600;
-    printf("nextzone = %s \n",&local_18);
-  }
-  ptVar2 = localtime(&local_15c);
+  time(&tStack_15c);
+  ptVar1 = localtime(&tStack_15c);
   GetValue("sys.timemode",&local_16c);
-  puVar3 = (undefined4 *)cJSON_CreateObject();
-  iVar1 = strcmp((char *)&local_16c,"hand");
-  if (iVar1 == 0) {
+  puVar2 = (undefined4 *)cJSON_CreateObject();
+  iVar3 = strcmp((char *)&local_16c,"hand");
+  if (iVar3 == 0) {
     pvVar4 = cJSON_CreateString("manual");
-    cJSON_AddItemToObject((int)puVar3,"timeType",(int)pvVar4);
+    cJSON_AddItemToObject((int)puVar2,"timeType",(int)pvVar4);
   }
   else {
     pvVar4 = cJSON_CreateString("sync");
-    cJSON_AddItemToObject((int)puVar3,"timeType",(int)pvVar4);
+    cJSON_AddItemToObject((int)puVar2,"timeType",(int)pvVar4);
   }
-  iVar1 = strcmp((char *)&local_18,(char *)&DAT_0);
-  if ((iVar1 == 0) || ((char)local_18 == '\0')) {
+  GetValue("sys.timezone",&local_148);
+  GetValue("sys.timenextzone",&local_18);
+  iVar3 = strcmp((char *)&local_18,(char *)&DAT_0);
+  if ((iVar3 == 0) || ((char)local_18 == '\0')) {
     memcpy(&local_18,&DAT_1,3);
   }
   sprintf((char *)&local_28,"%s:%s",&local_148,&local_18);
   pvVar4 = cJSON_CreateString((char *)&local_28);
-  cJSON_AddItemToObject((int)puVar3,"timeZone",(int)pvVar4);
+  cJSON_AddItemToObject((int)puVar2,"timeZone",(int)pvVar4);
   GetValue("sys.timefixper",&local_138);
   pvVar4 = cJSON_CreateString((char *)&local_138);
-  cJSON_AddItemToObject((int)puVar3,"timePeriod",(int)pvVar4);
+  cJSON_AddItemToObject((int)puVar2,"timePeriod",(int)pvVar4);
   GetValue("sys.timentpserver",acStack_128);
   pvVar4 = cJSON_CreateString(acStack_128);
-  cJSON_AddItemToObject((int)puVar3,"ntpServer",(int)pvVar4);
-  iVar1 = ptVar2->tm_mon + 1;
-  sprintf((char *)&local_158,"%d-%02d-%02d %02d:%02d:%02d",ptVar2->tm_year + 0x76c,iVar1,
-          ptVar2->tm_mday,ptVar2->tm_hour,ptVar2->tm_min,ptVar2->tm_sec);
+  cJSON_AddItemToObject((int)puVar2,"ntpServer",(int)pvVar4);
+  iVar3 = ptVar1->tm_mon + 1;
+  sprintf((char *)&local_158,"%d-%02d-%02d %02d:%02d:%02d",ptVar1->tm_year + 0x76c,iVar3,
+          ptVar1->tm_mday,ptVar1->tm_hour,ptVar1->tm_min,ptVar1->tm_sec);
   pvVar4 = cJSON_CreateString((char *)&local_158);
-  cJSON_AddItemToObject((int)puVar3,"time",(int)pvVar4);
-  if (ptVar2->tm_year + 0x76c < 0x7d1) {
+  cJSON_AddItemToObject((int)puVar2,"time",(int)pvVar4);
+  if (ptVar1->tm_year + 0x76c < 0x7d1) {
     __src = "false";
   }
   else {
     __src = "true";
   }
   strcpy((char *)&local_158,__src);
   psVar5 = (size_t *)cJSON_CreateString((char *)&local_158);
-  cJSON_AddItemToObject((int)puVar3,"isSyncInternetTime",(int)psVar5);
-  __ptr = (size_t *)cJSON_Print(param_1,(int)puVar3);
-  cJSON_Delete(puVar3);
-  websWrite((int)param_2,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar5,iVar1);
-  websWrite((int)param_2,(size_t *)&DAT_2,__ptr,iVar1);
+  cJSON_AddItemToObject((int)puVar2,"isSyncInternetTime",(int)psVar5);
+  __ptr = (size_t *)cJSON_Print(param_1,(int)puVar2);
+  cJSON_Delete(puVar2);
+  websWrite((int)param_2,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar5,iVar3);
+  websWrite((int)param_2,(size_t *)&DAT_2,__ptr,iVar3);
   free(__ptr);
   websDone(param_2,200);
   return;
 }
 

```


## formGetOnlineList

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.98|
|i_ratio|0.57|
|m_ratio|0.94|
|b_ratio|0.99|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|formGetOnlineList|formGetOnlineList|
|fullname|formGetOnlineList|formGetOnlineList|
|refcount|4|4|
|`length`|5792|5708|
|called|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::free<br><EXTERNAL>::get_statistic_info<br><EXTERNAL>::hw_nat_config<br><EXTERNAL>::malloc<br><EXTERNAL>::memset<br><EXTERNAL>::ntohl<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy</summary><EXTERNAL>::tpi_get_online_mac_info<br>__floatsidf<br>cJSON_AddItemToArray<br>cJSON_AddItemToObject<br>cJSON_CreateArray<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_mac_in_blacklist<br>clac_client_rate<br>find_onlineip_client<br>get_black_num<br>get_macfilter_mode<br>get_work_mode<br>is_lan_host<br>websDone<br>websTransfer<br>websWrite</details>|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::free<br><EXTERNAL>::get_statistic_info<br><EXTERNAL>::hw_nat_config<br><EXTERNAL>::malloc<br><EXTERNAL>::memset<br><EXTERNAL>::ntohl<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy</summary><EXTERNAL>::tpi_get_online_mac_info<br>__floatsidf<br>cJSON_AddItemToArray<br>cJSON_AddItemToObject<br>cJSON_CreateArray<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_mac_in_blacklist<br>clac_client_rate<br>find_onlineip_client<br>get_black_num<br>get_macfilter_mode<br>get_work_mode<br>is_lan_host<br>websDone<br>websTransfer<br>websWrite</details>|
|calling|formDefineTendDa|formDefineTendDa|
|paramcount|5|5|
|`address`|0046e27c|0046e628|
|sig|undefined __stdcall formGetOnlineList(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined1 * param_5)|undefined __stdcall formGetOnlineList(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined1 * param_5)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### formGetOnlineList Diff


```diff
--- formGetOnlineList
+++ formGetOnlineList
@@ -1,395 +1,394 @@
 
 void formGetOnlineList(double param_1,int *param_2,undefined4 param_3,undefined4 param_4,
                       undefined1 *param_5)
 
 {
   void *__ptr;
   undefined4 *puVar1;
   void *pvVar2;
   void *pvVar3;
   char *pcVar4;
   int iVar5;
   int iVar6;
   void *pvVar7;
   uint uVar8;
   size_t *__ptr_00;
   size_t *psVar9;
   undefined8 uVar10;
   void *local_ab4;
   uint local_a80;
   undefined4 local_a64;
   undefined4 local_a60;
   undefined4 local_a5c;
   undefined4 local_a58;
   undefined4 local_a54;
   undefined4 local_a50;
   undefined4 local_a4c;
   undefined4 local_a48;
   uint local_a44;
   uint local_a40;
   undefined4 local_a3c;
   undefined4 local_a38;
   undefined4 local_a34;
   undefined4 local_a30;
   undefined4 local_a2c;
   undefined4 local_a28;
   undefined4 local_a24;
   undefined4 local_a20;
   uint32_t local_a1c;
   int local_a18;
   int local_a14;
   uint local_a10;
   int local_a0c;
   uint local_a08;
   uint local_a04;
   undefined auStack_a00 [128];
   undefined auStack_980 [1024];
   undefined auStack_580 [64];
   undefined4 local_540;
   undefined4 local_53c;
   undefined4 local_538;
   undefined4 local_534;
   undefined4 local_530;
   undefined4 local_52c;
   undefined4 local_528;
   undefined4 local_524;
   undefined4 local_520;
   undefined4 local_51c;
   undefined4 local_518;
   undefined4 local_514;
   undefined auStack_510 [128];
   undefined4 local_490;
   undefined4 local_48c;
   undefined4 local_488;
   undefined4 local_484;
   undefined4 local_480;
   undefined4 local_47c;
   undefined4 local_478;
   undefined4 local_474;
   undefined4 local_470;
   undefined4 local_46c;
   undefined auStack_468 [120];
   undefined auStack_3f0 [512];
   undefined4 local_1f0;
   undefined4 local_1ec;
   undefined4 local_1e8;
   undefined4 local_1e4;
   undefined4 local_1e0;
   undefined4 local_1dc;
   undefined4 local_1d8;
   undefined4 local_1d4;
   undefined4 local_1d0;
   undefined4 local_1cc;
   undefined4 local_1c8;
   undefined4 local_1c4;
   undefined4 local_1c0;
   undefined4 local_1bc;
   undefined4 local_1b8;
   undefined4 local_1b4;
   size_t local_8c;
   undefined4 local_88;
   undefined4 local_84;
   undefined4 local_80;
   undefined4 local_7c;
   undefined4 local_78;
   undefined4 local_74;
   undefined4 local_70;
   undefined4 local_6c;
   undefined4 local_68;
   undefined4 local_64;
   undefined4 local_60;
   undefined4 local_5c;
   undefined4 local_58;
   undefined4 local_54;
   undefined4 local_50;
   undefined4 local_4c;
   undefined4 local_48;
   undefined4 local_44;
   undefined4 local_40;
   undefined4 local_3c;
   undefined4 local_38;
   undefined4 local_34;
   undefined4 local_30;
   undefined4 local_2c;
   undefined4 local_28;
   undefined4 local_24;
   undefined4 local_20;
   undefined4 local_1c;
   undefined4 local_18;
   undefined4 local_14;
   undefined4 local_10;
   
   local_a64 = 0;
   local_a60 = 0;
   local_a5c = 0;
   local_a58 = 0;
   local_a54 = 0;
   local_a50 = 0;
   local_a4c = 0;
   local_a48 = 0;
   local_a44 = 0;
   local_a40 = 0;
   local_a3c = 0;
   local_a38 = 0;
   local_a34 = 0;
   local_a30 = 0;
   local_a2c = 0;
   local_a28 = 0;
   local_a24 = 0;
   local_a20 = 0;
   local_a1c = 0;
   local_a18 = 0;
   local_a14 = 0;
   local_a10 = 0;
   local_a0c = 0;
   local_a08 = 0;
   memset(auStack_a00,0,0x80);
   memset(auStack_980,0,0x400);
   memset(auStack_580,0,0x40);
   local_540 = 0;
   local_53c = 0;
   local_538 = 0;
   local_534 = 0;
   local_530 = 0;
   local_52c = 0;
   local_528 = 0;
   local_524 = 0;
   local_520 = 0;
   local_51c = 0;
   local_518 = 0;
   local_514 = 0;
   memset(auStack_510,0,0x80);
   local_490 = 0;
   local_48c = 0;
   local_488 = 0;
   local_484 = 0;
   local_480 = 0;
   local_47c = 0;
   local_478 = 0;
   local_474 = 0;
   local_470 = 0;
   local_46c = 0;
   memset(auStack_468,0,0x78);
   memset(auStack_3f0,0,0x200);
   local_1f0 = 0;
   local_1ec = 0;
   local_1e8 = 0;
   local_1e4 = 0;
   local_1e0 = 0;
   local_1dc = 0;
   local_1d8 = 0;
   local_1d4 = 0;
   local_1d0 = 0;
   local_1cc = 0;
   local_1c8 = 0;
   local_1c4 = 0;
   local_1c0 = 0;
   local_1bc = 0;
   local_1b8 = 0;
   local_1b4 = 0;
   local_ab4 = (void *)0x0;
   local_8c = 0;
   local_88 = 0;
   local_84 = 0;
   local_80 = 0;
   local_7c = 0;
   local_78 = 0;
   local_74 = 0;
   local_70 = 0;
   local_6c = 0;
   local_68 = 0;
   local_64 = 0;
   local_60 = 0;
   hw_nat_config(0);
   __ptr = malloc(0x5000);
   if (__ptr == (void *)0x0) {
     psVar9 = (size_t *)0x1;
     sprintf((char *)&local_8c,"{\"errCode\":%d}");
     websTransfer(param_2,&local_8c,psVar9,param_5);
   }
   else {
     puVar1 = (undefined4 *)cJSON_CreateArray();
     get_black_num((int *)&local_a04);
     pvVar2 = cJSON_CreateObject();
     cJSON_AddItemToArray((int)puVar1,(int)pvVar2);
     uVar10 = __floatsidf(local_a04);
     pvVar3 = cJSON_CreateNumber((uint)uVar10,(uint)((ulonglong)uVar10 >> 0x20));
     cJSON_AddItemToObject((int)pvVar2,"blackNum",(int)pvVar3);
     get_macfilter_mode((char *)&local_6c);
     pvVar3 = cJSON_CreateString((char *)&local_6c);
     cJSON_AddItemToObject((int)pvVar2,"macFilterType",(int)pvVar3);
     pvVar3 = cJSON_CreateString((char *)(param_2 + 0xc));
     cJSON_AddItemToObject((int)pvVar2,"localhostIP",(int)pvVar3);
     tpi_get_online_mac_info(__ptr,0x5000,&local_a44);
     if (local_a44 != 0) {
       local_ab4 = __ptr;
     }
     psVar9 = &local_a40;
     get_statistic_info(&local_a18,&local_a10);
     get_work_mode(&local_540);
     if (local_a44 != 0) {
       for (local_a80 = 0; local_a80 < local_a44; local_a80 = local_a80 + 1) {
         local_a1c = ntohl(*(uint32_t *)((int)local_ab4 + local_a80 * 0x161 + 0x155));
         psVar9 = (size_t *)(local_a1c & 0xff);
         pcVar4 = (char *)(local_a1c >> 8 & 0xff);
         sprintf((char *)&local_a3c,"%u.%u.%u.%u",psVar9,pcVar4,local_a1c >> 0x10 & 0xff,
                 local_a1c >> 0x18);
         local_5c = 0;
         local_58 = 0;
         local_54 = 0;
         local_50 = 0;
         iVar5 = GetValue("cgi_debug",&local_5c);
         if ((iVar5 != 0) && (iVar5 = strcmp("on",(char *)&local_5c), iVar5 == 0)) {
           psVar9 = (size_t *)&DAT_0;
           pcVar4 = "formGetOnlineList";
           printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                 "formGetOnlineList",0x9e9,debug_color[1],&local_a3c);
+                 "formGetOnlineList",0x9df,debug_color[1],&local_a3c);
         }
         iVar5 = is_lan_host(*(uint32_t *)((int)local_ab4 + local_a80 * 0x161 + 0x155));
         local_4c = 0;
         local_48 = 0;
         local_44 = 0;
         local_40 = 0;
         iVar6 = GetValue("cgi_debug",&local_4c);
         if ((iVar6 != 0) && (iVar6 = strcmp("on",(char *)&local_4c), iVar6 == 0)) {
           psVar9 = (size_t *)&DAT_0;
           pcVar4 = "formGetOnlineList";
           printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                 "formGetOnlineList",0x9eb,debug_color[1],&local_a3c);
+                 "formGetOnlineList",0x9e1,debug_color[1],&local_a3c);
         }
         iVar6 = strcmp((char *)&local_540,"ap");
         if (((iVar6 != 0) ||
             (iVar6 = strcmp((char *)(param_2 + 0xc),(char *)&local_a3c), iVar6 == 0)) ||
            (*(char *)((int)local_ab4 + local_a80 * 0x161) == '\x02')) {
           local_3c = 0;
           local_38 = 0;
           local_34 = 0;
           local_30 = 0;
           iVar6 = GetValue("cgi_debug",&local_3c);
           if ((iVar6 != 0) && (iVar6 = strcmp("on",(char *)&local_3c), iVar6 == 0)) {
             psVar9 = (size_t *)&DAT_0;
             pcVar4 = "formGetOnlineList";
             printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                   "formGetOnlineList",0x9f1,debug_color[1],&local_a3c);
+                   "formGetOnlineList",0x9e7,debug_color[1],&local_a3c);
           }
-          if (((iVar5 != 1) ||
-              (iVar6 = check_mac_in_blacklist((char *)((int)local_ab4 + local_a80 * 0x161 + 3)),
-              iVar6 == 0)) &&
-             ((iVar5 != 0 || (*(char *)((int)local_ab4 + local_a80 * 0x161) == '\x02')))) {
+          if ((iVar5 != 1) ||
+             (iVar6 = check_mac_in_blacklist((char *)((int)local_ab4 + local_a80 * 0x161 + 3)),
+             iVar6 == 0)) {
             local_2c = 0;
             local_28 = 0;
             local_24 = 0;
             local_20 = 0;
             iVar6 = GetValue("cgi_debug",&local_2c);
             if ((iVar6 != 0) && (iVar6 = strcmp("on",(char *)&local_2c), iVar6 == 0)) {
               psVar9 = (size_t *)&DAT_0;
               pcVar4 = "formGetOnlineList";
               printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                     "formGetOnlineList",0x9fd,debug_color[1],&local_a3c);
+                     "formGetOnlineList",0x9ee,debug_color[1],&local_a3c);
             }
             iVar6 = strcmp((char *)&local_540,"ap");
             if (((iVar6 == 0) || (iVar5 != 2)) ||
                (*(int *)((int)local_ab4 + local_a80 * 0x161 + 0x155) == 0)) {
               local_1c = 0;
               local_18 = 0;
               local_14 = 0;
               local_10 = 0;
               iVar5 = GetValue("cgi_debug",&local_1c);
               if ((iVar5 != 0) && (iVar5 = strcmp("on",(char *)&local_1c), iVar5 == 0)) {
                 pcVar4 = "formGetOnlineList";
                 printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
-                       "formGetOnlineList",0xa06,debug_color[1],&local_a3c);
+                       "formGetOnlineList",0x9f7,debug_color[1],&local_a3c);
               }
               strcpy((char *)&local_a64,(char *)((int)local_ab4 + local_a80 * 0x161 + 3));
               pvVar3 = cJSON_CreateObject();
               cJSON_AddItemToArray((int)puVar1,(int)pvVar3);
               pvVar7 = cJSON_CreateString((char *)&local_a64);
               cJSON_AddItemToObject((int)pvVar3,"deviceId",(int)pvVar7);
               pvVar7 = cJSON_CreateString((char *)&local_a3c);
               cJSON_AddItemToObject((int)pvVar3,"ip",(int)pvVar7);
               iVar5 = strcmp((char *)(param_2 + 0xc),(char *)&local_a3c);
               if (iVar5 == 0) {
                 pvVar7 = cJSON_CreateString((char *)((int)local_ab4 + local_a80 * 0x161 + 0x35));
                 cJSON_AddItemToObject((int)pvVar2,"localhostName",(int)pvVar7);
                 pvVar7 = cJSON_CreateString((char *)&local_a64);
                 cJSON_AddItemToObject((int)pvVar2,"localhostMac",(int)pvVar7);
               }
               pvVar7 = cJSON_CreateString((char *)((int)local_ab4 + local_a80 * 0x161 + 0x35));
               cJSON_AddItemToObject((int)pvVar3,"devName",(int)pvVar7);
               if (*(char *)((int)local_ab4 + local_a80 * 0x161) == '\x02') {
                 pvVar7 = cJSON_CreateString("true");
                 cJSON_AddItemToObject((int)pvVar2,"isWirelessConnect",(int)pvVar7);
                 if (*(char *)((int)local_ab4 + local_a80 * 0x161 + 1) == '\x01') {
                   pvVar7 = cJSON_CreateString("1");
                   cJSON_AddItemToObject((int)pvVar3,"line",(int)pvVar7);
                 }
                 else {
                   pvVar7 = cJSON_CreateString("2");
                   cJSON_AddItemToObject((int)pvVar3,"line",(int)pvVar7);
                 }
               }
               else {
                 pvVar7 = cJSON_CreateString("false");
                 cJSON_AddItemToObject((int)pvVar2,"isWirelessConnect",(int)pvVar7);
                 pvVar7 = cJSON_CreateString("0");
                 cJSON_AddItemToObject((int)pvVar3,"line",(int)pvVar7);
               }
               iVar5 = find_onlineip_client(local_a40,(int *)&local_a08,&local_a64);
               if ((iVar5 == 0) || (local_a40 <= local_a08)) {
                 pvVar7 = cJSON_CreateString("0");
                 cJSON_AddItemToObject((int)pvVar3,"uploadSpeed",(int)pvVar7);
                 pvVar7 = cJSON_CreateString("0");
                 cJSON_AddItemToObject((int)pvVar3,"downloadSpeed",(int)pvVar7);
               }
               else {
                 pcVar4 = (char *)&local_46c;
                 clac_client_rate(&local_470,(undefined4 *)pcVar4,local_a08,pcVar4,local_a18,
                                  local_a14,local_a10,local_a0c);
                 sprintf((char *)&local_480,"%d",local_46c);
                 sprintf((char *)&local_490,"%d",local_470);
                 pvVar7 = cJSON_CreateString((char *)&local_480);
                 cJSON_AddItemToObject((int)pvVar3,"uploadSpeed",(int)pvVar7);
                 pvVar7 = cJSON_CreateString((char *)&local_490);
                 cJSON_AddItemToObject((int)pvVar3,"downloadSpeed",(int)pvVar7);
               }
               pvVar7 = cJSON_CreateString((char *)((int)local_ab4 + local_a80 * 0x161 + 0x135));
               cJSON_AddItemToObject((int)pvVar3,"linkType",(int)pvVar7);
               uVar8 = check_mac_in_blacklist((char *)&local_a64);
               uVar10 = __floatsidf(uVar8);
               pvVar7 = cJSON_CreateNumber((uint)uVar10,(uint)((ulonglong)uVar10 >> 0x20));
               cJSON_AddItemToObject((int)pvVar3,"black",(int)pvVar7);
               iVar5 = is_lan_host(*(uint32_t *)((int)local_ab4 + local_a80 * 0x161 + 0x155));
               iVar6 = strcmp((char *)&local_540,"ap");
               if ((iVar6 == 0) || (iVar6 = strcmp((char *)&local_540,"client+ap"), iVar6 == 0)) {
                 psVar9 = (size_t *)cJSON_CreateString("false");
                 cJSON_AddItemToObject((int)pvVar3,"isGuestClient",(int)psVar9);
               }
               else if (iVar5 == 0) {
                 psVar9 = (size_t *)cJSON_CreateString("true");
                 cJSON_AddItemToObject((int)pvVar3,"isGuestClient",(int)psVar9);
               }
               else {
                 psVar9 = (size_t *)cJSON_CreateString("false");
                 cJSON_AddItemToObject((int)pvVar3,"isGuestClient",(int)psVar9);
               }
             }
           }
         }
         param_5 = pcVar4;
       }
     }
     if (ip_info != (users_info *)0x0) {
       free(ip_info);
       ip_info = (users_info *)0x0;
     }
     __ptr_00 = (size_t *)cJSON_Print(param_1,(int)puVar1);
     cJSON_Delete(puVar1);
     websWrite((int)param_2,(size_t *)"HTTP/1.0 200 OK\r\n\r\n",psVar9,param_5);
     websWrite((int)param_2,(size_t *)&DAT_1,__ptr_00,param_5);
     free(__ptr_00);
     free(__ptr);
     websDone(param_2,200);
   }
   return;
 }
 

```


## ate_nvram_set_maxpower_2G

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.9|
|i_ratio|0.4|
|m_ratio|0.75|
|b_ratio|0.83|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|ate_nvram_set_maxpower_2G|ate_nvram_set_maxpower_2G|
|fullname|ate_nvram_set_maxpower_2G|ate_nvram_set_maxpower_2G|
|refcount|3|3|
|`length`|712|504|
|`called`|<EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ate_envram_set_common<br>set_cfm_mib|<EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ate_envram_set_common|
|calling|||
|paramcount|1|1|
|`address`|0047b39c|0047b55c|
|sig|undefined4 __stdcall ate_nvram_set_maxpower_2G(char * param_1)|undefined4 __stdcall ate_nvram_set_maxpower_2G(char * param_1)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### ate_nvram_set_maxpower_2G Called Diff


```diff
--- ate_nvram_set_maxpower_2G called
+++ ate_nvram_set_maxpower_2G called
@@ -1,2 +0,0 @@
-<EXTERNAL>::memcpy
-<EXTERNAL>::memset
@@ -7 +4,0 @@
-set_cfm_mib
```


### ate_nvram_set_maxpower_2G Diff


```diff
--- ate_nvram_set_maxpower_2G
+++ ate_nvram_set_maxpower_2G
@@ -1,48 +1,42 @@
 
 undefined4 ate_nvram_set_maxpower_2G(char *param_1)
 
 {
   undefined4 uVar1;
   int iVar2;
-  undefined auStack_1008 [4096];
   
-  printf("%s : %d\n","ate_nvram_set_maxpower_2G",0x34a);
-  memset(auStack_1008,0,0x1000);
+  printf("%s : %d\n","ate_nvram_set_maxpower_2G",0x341);
   if (*param_1 == '\0') {
     uVar1 = 0;
   }
   else {
     iVar2 = strcmp(param_1,"0");
     if (iVar2 == 0) {
-      memcpy(auStack_1008,&DAT_0,4);
       puts("low power");
     }
     else {
       iVar2 = strcmp(param_1,"1");
       if (iVar2 == 0) {
-        memcpy(auStack_1008,"middle",7);
         puts("middle power");
       }
       else {
         iVar2 = strcmp(param_1,"2");
         if (iVar2 != 0) {
           printf("error maxpower %s \n",param_1);
           return 1;
         }
-        memcpy(auStack_1008,&DAT_1,5);
         puts("high power");
       }
     }
     iVar2 = ate_envram_set_common("wl2g.power",param_1);
     if (iVar2 == 0) {
-      set_cfm_mib(0x50f4f8,(int)auStack_1008);
       uVar1 = 0;
     }
     else {
       printf("2.4G modified failed! [maxpower=%s]\n",param_1);
       uVar1 = 1;
     }
   }
   return uVar1;
 }
 

```


## ate_nvram_set_maxpower_5G

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.9|
|i_ratio|0.4|
|m_ratio|0.84|
|b_ratio|0.84|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|ate_nvram_set_maxpower_5G|ate_nvram_set_maxpower_5G|
|fullname|ate_nvram_set_maxpower_5G|ate_nvram_set_maxpower_5G|
|refcount|3|3|
|`length`|592|428|
|`called`|<EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ate_envram_set_common<br>set_cfm_mib|<EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ate_envram_set_common|
|calling|||
|paramcount|1|1|
|`address`|0047b664|0047b754|
|sig|undefined4 __stdcall ate_nvram_set_maxpower_5G(char * param_1)|undefined4 __stdcall ate_nvram_set_maxpower_5G(char * param_1)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### ate_nvram_set_maxpower_5G Called Diff


```diff
--- ate_nvram_set_maxpower_5G called
+++ ate_nvram_set_maxpower_5G called
@@ -1,2 +0,0 @@
-<EXTERNAL>::memcpy
-<EXTERNAL>::memset
@@ -7 +4,0 @@
-set_cfm_mib
```


### ate_nvram_set_maxpower_5G Diff


```diff
--- ate_nvram_set_maxpower_5G
+++ ate_nvram_set_maxpower_5G
@@ -1,41 +1,36 @@
 
 undefined4 ate_nvram_set_maxpower_5G(char *param_1)
 
 {
   undefined4 uVar1;
   int iVar2;
-  undefined auStack_1008 [4096];
   
-  printf("%s : %d\n","ate_nvram_set_maxpower_5G",0x374);
-  memset(auStack_1008,0,0x1000);
+  printf("%s : %d\n","ate_nvram_set_maxpower_5G",0x364);
   if (*param_1 == '\0') {
     uVar1 = 0;
   }
   else {
     iVar2 = strcmp(param_1,"0");
     if (iVar2 == 0) {
-      memcpy(auStack_1008,&DAT_0,4);
       puts("low power");
     }
     else {
       iVar2 = strcmp(param_1,"2");
       if (iVar2 != 0) {
         printf("error maxpower %s \n",param_1);
         return 1;
       }
-      memcpy(auStack_1008,&DAT_1,5);
       puts("high power");
     }
     iVar2 = ate_envram_set_common("wl5g.power",param_1);
     if (iVar2 == 0) {
-      set_cfm_mib(0x50f50c,(int)auStack_1008);
       uVar1 = 0;
     }
     else {
       printf("5G modified failed! [maxpower=%s]\n",param_1);
       uVar1 = 1;
     }
   }
   return uVar1;
 }
 

```


## wan_lan_same_deal

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|1.0|
|i_ratio|0.69|
|m_ratio|0.99|
|b_ratio|0.93|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|wan_lan_same_deal|wan_lan_same_deal|
|fullname|wan_lan_same_deal|wan_lan_same_deal|
|refcount|4|4|
|`length`|1764|1728|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::CommitCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::sprintf<br><EXTERNAL>::sscanf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy</summary>check_ip_conflict<br>set_wl_guest_qos_list</details>|<details><summary>Expand for full list:<br><EXTERNAL>::CommitCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::sprintf<br><EXTERNAL>::sscanf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br>check_ip_conflict</summary>set_wl_guest_qos_list</details>|
|calling|guest_ip_check|guest_ip_check|
|paramcount|2|2|
|`address`|004d8af0|004db210|
|sig|undefined4 __stdcall wan_lan_same_deal(uint * param_1, uint param_2)|undefined4 __stdcall wan_lan_same_deal(uint * param_1, uint param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### wan_lan_same_deal Called Diff


```diff
--- wan_lan_same_deal called
+++ wan_lan_same_deal called
@@ -4 +3,0 @@
-<EXTERNAL>::doSystemCmd
```


### wan_lan_same_deal Diff


```diff
--- wan_lan_same_deal
+++ wan_lan_same_deal
@@ -1,196 +1,195 @@
 
 undefined4 wan_lan_same_deal(uint *param_1,uint param_2)
 
 {
   bool bVar1;
   undefined4 uVar2;
   uint uVar3;
   int iVar4;
   int local_20c;
   undefined4 local_204;
   undefined4 local_200;
   undefined4 local_1fc;
   undefined4 local_1f8;
   undefined4 local_1f4;
   undefined4 local_1f0;
   undefined4 local_1ec;
   undefined4 local_1e8;
   undefined4 local_1e4;
   undefined4 local_1e0;
   undefined4 local_1dc;
   undefined4 local_1d8;
   undefined4 local_1d4;
   undefined4 local_1d0;
   undefined4 local_1cc;
   undefined4 local_1c8;
   undefined4 local_1c4;
   undefined4 local_1c0;
   undefined4 local_1bc;
   undefined4 local_1b8;
   undefined4 local_1b4;
   undefined4 local_1b0;
   undefined4 local_1ac;
   undefined4 local_1a8;
   undefined4 local_1a4;
   undefined4 local_1a0;
   undefined4 local_19c;
   undefined4 local_198;
   undefined4 local_194;
   undefined4 local_190;
   undefined4 local_18c;
   undefined4 local_188;
   undefined4 local_184;
   undefined4 local_180;
   undefined4 local_17c;
   undefined4 local_178;
   undefined4 local_174;
   undefined4 local_170;
   undefined4 local_16c;
   undefined4 local_168;
   undefined4 local_164;
   undefined4 local_160;
   undefined4 local_15c;
   undefined4 local_158;
   undefined4 local_154;
   undefined4 local_150;
   undefined4 local_14c;
   undefined4 local_148;
   undefined4 local_144;
   undefined4 local_140;
   undefined4 local_13c;
   undefined4 local_138;
   undefined4 local_134;
   undefined4 local_130;
   undefined4 local_12c;
   undefined4 local_128;
   undefined4 local_124;
   undefined4 local_120;
   undefined4 local_11c;
   undefined4 local_118;
   undefined4 local_114;
   undefined4 local_110;
   undefined4 local_10c;
   char acStack_108 [256];
   
   local_204 = 0;
   local_200 = 0;
   local_1fc = 0;
   local_1f8 = 0;
   local_1f4 = 0;
   local_1f0 = 0;
   local_1ec = 0;
   local_1e8 = 0;
   bVar1 = false;
   local_1e4 = 0;
   local_1e0 = 0;
   local_1dc = 0;
   local_1d8 = 0;
   local_1d4 = 0;
   local_1d0 = 0;
   local_1cc = 0;
   local_1c8 = 0;
   local_1c4 = 0;
   local_1c0 = 0;
   local_1bc = 0;
   local_1b8 = 0;
   local_1b4 = 0;
   local_1b0 = 0;
   local_1ac = 0;
   local_1a8 = 0;
   local_1a4 = 0;
   local_1a0 = 0;
   local_19c = 0;
   local_198 = 0;
   local_194 = 0;
   local_190 = 0;
   local_18c = 0;
   local_188 = 0;
   local_184 = 0;
   local_180 = 0;
   local_17c = 0;
   local_178 = 0;
   local_174 = 0;
   local_170 = 0;
   local_16c = 0;
   local_168 = 0;
   local_164 = 0;
   local_160 = 0;
   local_15c = 0;
   local_158 = 0;
   local_154 = 0;
   local_150 = 0;
   local_14c = 0;
   local_148 = 0;
   local_144 = 0;
   local_140 = 0;
   local_13c = 0;
   local_138 = 0;
   local_134 = 0;
   local_130 = 0;
   local_12c = 0;
   local_128 = 0;
   local_124 = 0;
   local_120 = 0;
   local_11c = 0;
   local_118 = 0;
   local_114 = 0;
   local_110 = 0;
   local_10c = 0;
   memset(acStack_108,0,0x100);
   if (((param_1 == (uint *)0x0) || ((int)param_2 < 0)) || (5 < (int)param_2)) {
     uVar2 = 0;
   }
   else {
     for (local_20c = 0; local_20c < 6; local_20c = local_20c + 1) {
       memset(&local_204,0,0x20);
       uVar3 = check_ip_conflict(param_1,(char *)&local_204,param_2);
       if (uVar3 == 2) {
         sscanf((char *)&local_204,"%[^.].%[^.].%[^.].%s",&local_164,(int)&local_160 + 1,
                (int)&local_15c + 2,(int)&local_158 + 3);
         GetValue("wl.guest.dhcps_ipstart",&local_1a4);
         sscanf((char *)&local_1a4,"%[^.].%[^.].%[^.].%s",&local_150,(int)&local_14c + 1,
                (int)&local_148 + 2,(int)&local_144 + 3);
         GetValue("wl.guest.dhcps_ipend",&local_184);
         sscanf((char *)&local_184,"%[^.].%[^.].%[^.].%s",&local_13c,(int)&local_138 + 1,
                (int)&local_134 + 2,(int)&local_130 + 3);
         sprintf((char *)&local_1e4,"%s.%s.%s.%s",&local_164,(int)&local_160 + 1,(int)&local_15c + 2,
                 (int)&local_144 + 3);
         sprintf((char *)&local_1c4,"%s.%s.%s.%s",&local_164,(int)&local_160 + 1,(int)&local_15c + 2,
                 (int)&local_130 + 3);
         SetValue("wl.guest.dhcps_ip",&local_204);
         SetValue("wl.guest.dhcps_dns1",&local_204);
         SetValue("wl.guest.dhcps_ipstart",&local_1e4);
         SetValue("wl.guest.dhcps_ipend",&local_1c4);
         GetValue("wl.guest.down_speed",&local_128);
         set_wl_guest_qos_list("128000",&local_128);
         printf("[GUEST_IP_CONFILCT_DEBUG]:%s,%d--guest_ip=%s!\n","wan_lan_same_deal",0x29a,
                &local_204);
         strcpy((char *)((int)param_1 + 0x13a),(char *)&local_204);
         iVar4 = strcmp((char *)(param_1 + 0x4e),"1");
         if (iVar4 == 0) {
-          doSystemCmd("cfm Post netctrl %d?op=%d",0xf,6);
           sprintf(acStack_108,"op=%d, wl_rate=%d",3,0x1d);
           send_msg_to_netctrl(0x13,acStack_108);
           sprintf(acStack_108,"op=%d",9);
           send_msg_to_netctrl(0x13,acStack_108);
         }
         bVar1 = true;
       }
       else if (uVar3 == 5) {
         SetValue("d.lan.ip",&local_204);
         sprintf(acStack_108,"op=%d",3);
         send_msg_to_netctrl(0x35,acStack_108);
         bVar1 = true;
       }
     }
     if (bVar1) {
       CommitCfm();
       uVar2 = 1;
     }
     else {
       uVar2 = 0;
     }
   }
   return uVar2;
 }
 

```


## formWifiApScan

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.6|
|i_ratio|0.27|
|m_ratio|0.57|
|b_ratio|0.5|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|formWifiApScan|formWifiApScan|
|fullname|formWifiApScan|formWifiApScan|
|refcount|4|4|
|`length`|3776|3600|
|called|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::free<br><EXTERNAL>::get_eth_name<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::tpi_do_scan<br>cJSON_AddItemToArray</summary>cJSON_AddItemToObject<br>cJSON_CreateArray<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Object_2String_apscan<br>is_now_channles_in_country<br>websDone<br>websLongWrite<br>websWrite</details>|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::free<br><EXTERNAL>::get_eth_name<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::tpi_do_scan<br>cJSON_AddItemToArray</summary>cJSON_AddItemToObject<br>cJSON_CreateArray<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Object_2String_apscan<br>is_now_channles_in_country<br>websDone<br>websLongWrite<br>websWrite</details>|
|calling|formDefineTendDa|formDefineTendDa|
|paramcount|5|5|
|`address`|004b1914|004b1904|
|sig|undefined __stdcall formWifiApScan(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5)|undefined __stdcall formWifiApScan(double param_1, int * param_2, undefined4 param_3, undefined4 param_4, undefined4 param_5)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### formWifiApScan Diff


```diff
--- formWifiApScan
+++ formWifiApScan
@@ -1,196 +1,196 @@
 
 void formWifiApScan(double param_1,int *param_2,undefined4 param_3,undefined4 param_4,
                    undefined4 param_5)
 
 {
   bool bVar1;
   char *pcVar2;
   int iVar3;
   undefined4 *puVar4;
   void *pvVar5;
   void *pvVar6;
   size_t *psVar7;
-  int local_ab98;
-  int local_ab8c;
-  undefined4 local_ab84;
-  undefined4 local_ab80;
-  undefined4 local_ab7c;
-  undefined4 local_ab78;
-  undefined4 local_ab74;
-  undefined4 local_ab70;
-  int local_ab6c;
-  char acStack_ab68 [49];
-  char acStack_ab37 [18];
-  char acStack_ab25 [8];
-  char acStack_ab1d [8];
-  char acStack_ab15 [8];
-  char acStack_ab0d [64];
-  char acStack_aacd [8];
-  char acStack_aac5 [21725];
-  undefined4 local_55e8;
-  undefined4 local_55e4;
-  undefined4 local_55e0;
-  undefined4 local_55dc;
-  undefined4 local_55d8;
-  undefined4 local_55d4;
-  int local_55d0;
-  char acStack_55cc [49];
-  char acStack_559b [18];
-  char acStack_5589 [8];
-  char acStack_5581 [8];
-  char acStack_5579 [8];
-  char acStack_5571 [64];
-  char acStack_5531 [8];
-  char acStack_5529 [21725];
+  int local_9b98;
+  int local_9b8c;
+  undefined4 local_9b84;
+  undefined4 local_9b80;
+  undefined4 local_9b7c;
+  undefined4 local_9b78;
+  undefined4 local_9b74;
+  undefined4 local_9b70;
+  int local_9b6c;
+  char acStack_9b68 [33];
+  char acStack_9b47 [18];
+  char acStack_9b35 [8];
+  char acStack_9b2d [8];
+  char acStack_9b25 [8];
+  char acStack_9b1d [64];
+  char acStack_9add [8];
+  char acStack_9ad5 [19693];
+  undefined4 local_4de8;
+  undefined4 local_4de4;
+  undefined4 local_4de0;
+  undefined4 local_4ddc;
+  undefined4 local_4dd8;
+  undefined4 local_4dd4;
+  int local_4dd0;
+  char acStack_4dcc [33];
+  char acStack_4dab [18];
+  char acStack_4d99 [8];
+  char acStack_4d91 [8];
+  char acStack_4d89 [8];
+  char acStack_4d81 [64];
+  char acStack_4d41 [8];
+  char acStack_4d39 [19693];
   undefined4 local_4c;
   undefined4 local_48;
   undefined4 local_44;
   undefined4 local_40;
   undefined4 local_3c;
   undefined4 local_38;
   undefined4 local_34;
   undefined4 local_30;
   undefined4 local_2c;
   undefined4 local_28;
   undefined4 local_24;
   undefined4 local_20;
   undefined4 local_1c;
   undefined4 local_18;
   undefined4 local_14;
   undefined4 local_10;
   
   bVar1 = false;
-  local_ab84 = 0;
-  local_ab80 = 0;
-  local_ab7c = 0;
-  local_ab78 = 0;
-  local_ab74 = 0;
-  local_ab70 = 0;
-  local_ab6c = 0;
-  memset(acStack_ab68,0,0x5580);
-  local_55e8 = 0;
-  local_55e4 = 0;
-  local_55e0 = 0;
-  local_55dc = 0;
-  local_55d8 = 0;
-  local_55d4 = 0;
-  local_55d0 = 0;
-  memset(acStack_55cc,0,0x5580);
+  local_9b84 = 0;
+  local_9b80 = 0;
+  local_9b7c = 0;
+  local_9b78 = 0;
+  local_9b74 = 0;
+  local_9b70 = 0;
+  local_9b6c = 0;
+  memset(acStack_9b68,0,0x4d80);
+  local_4de8 = 0;
+  local_4de4 = 0;
+  local_4de0 = 0;
+  local_4ddc = 0;
+  local_4dd8 = 0;
+  local_4dd4 = 0;
+  local_4dd0 = 0;
+  memset(acStack_4dcc,0,0x4d80);
   local_4c = 0;
   local_48 = 0;
   local_44 = 0;
   local_40 = 0;
   local_3c = 0;
   local_38 = 0;
   local_34 = 0;
   local_30 = 0;
   GetValue("wl2g.public.country",&local_4c);
   GetValue("wl5g.public.country",&local_3c);
   pcVar2 = (char *)get_eth_name(0x17);
-  strcpy((char *)&local_ab84,pcVar2);
+  strcpy((char *)&local_9b84,pcVar2);
   pcVar2 = (char *)get_eth_name(0x1b);
-  strcpy((char *)&local_55e8,pcVar2);
+  strcpy((char *)&local_4de8,pcVar2);
   local_2c = 0;
   local_28 = 0;
   local_24 = 0;
   local_20 = 0;
   local_1c = 0;
   local_18 = 0;
   local_14 = 0;
   local_10 = 0;
   GetValue("wl2g.public.enable",&local_2c);
   GetValue("wl5g.public.enable",&local_1c);
   doSystemCmd("rm %s","/var/sta_encode_ssid_cache");
   iVar3 = strcmp((char *)&local_2c,"1");
   if (iVar3 == 0) {
     param_5 = 0x80;
-    tpi_do_scan(&local_ab84,&local_ab6c,acStack_ab68);
+    tpi_do_scan(&local_9b84,&local_9b6c,acStack_9b68);
   }
   iVar3 = strcmp((char *)&local_1c,"1");
   if (iVar3 == 0) {
     param_5 = 0x80;
-    tpi_do_scan(&local_55e8,&local_55d0,acStack_55cc);
+    tpi_do_scan(&local_4de8,&local_4dd0,acStack_4dcc);
   }
   puVar4 = (undefined4 *)cJSON_CreateArray();
-  for (local_ab8c = 0; local_ab8c < local_ab6c; local_ab8c = local_ab8c + 1) {
+  for (local_9b8c = 0; local_9b8c < local_9b6c; local_9b8c = local_9b8c + 1) {
     bVar1 = true;
-    iVar3 = strcmp(acStack_ab0d + local_ab8c * 0xab,"wep");
+    iVar3 = strcmp(acStack_9b1d + local_9b8c * 0x9b,"wep");
     if (iVar3 != 0) {
-      iVar3 = strcmp(acStack_ab0d + local_ab8c * 0xab,"unkown");
+      iVar3 = strcmp(acStack_9b1d + local_9b8c * 0x9b,"unkown");
       if (iVar3 != 0) {
-        pcVar2 = is_now_channles_in_country((char *)&local_4c,0x18,acStack_ab25 + local_ab8c * 0xab)
+        pcVar2 = is_now_channles_in_country((char *)&local_4c,0x18,acStack_9b35 + local_9b8c * 0x9b)
         ;
         if (pcVar2 != (char *)0x0) {
           pvVar5 = cJSON_CreateObject();
           cJSON_AddItemToArray((int)puVar4,(int)pvVar5);
-          pvVar6 = cJSON_CreateString(acStack_ab68 + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9b68 + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"ssid",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_ab37 + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9b47 + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"mac",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_ab25 + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9b35 + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"channel",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_ab1d + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9b2d + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"nctrlsb",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_aacd + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9add + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"bandwidth",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_ab0d + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9b1d + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"security",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_ab15 + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9b25 + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"signal",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_aac5 + local_ab8c * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_9ad5 + local_9b8c * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"nettype",(int)pvVar6);
           pvVar6 = cJSON_CreateString("0");
           cJSON_AddItemToObject((int)pvVar5,"wifi_chkHz",(int)pvVar6);
         }
       }
     }
   }
-  for (local_ab98 = 0; local_ab98 < local_55d0; local_ab98 = local_ab98 + 1) {
+  for (local_9b98 = 0; local_9b98 < local_4dd0; local_9b98 = local_9b98 + 1) {
     bVar1 = true;
-    iVar3 = strcmp(acStack_5571 + local_ab98 * 0xab,"wep");
+    iVar3 = strcmp(acStack_4d81 + local_9b98 * 0x9b,"wep");
     if (iVar3 != 0) {
-      iVar3 = strcmp(acStack_5571 + local_ab98 * 0xab,"unkown");
+      iVar3 = strcmp(acStack_4d81 + local_9b98 * 0x9b,"unkown");
       if (iVar3 != 0) {
-        pcVar2 = is_now_channles_in_country((char *)&local_3c,5,acStack_5589 + local_ab98 * 0xab);
+        pcVar2 = is_now_channles_in_country((char *)&local_3c,5,acStack_4d99 + local_9b98 * 0x9b);
         if (pcVar2 != (char *)0x0) {
           pvVar5 = cJSON_CreateObject();
           cJSON_AddItemToArray((int)puVar4,(int)pvVar5);
-          pvVar6 = cJSON_CreateString(acStack_55cc + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4dcc + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"ssid",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_559b + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4dab + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"mac",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_5589 + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4d99 + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"channel",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_5581 + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4d91 + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"nctrlsb",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_5531 + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4d41 + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"bandwidth",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_5571 + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4d81 + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"security",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_5579 + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4d89 + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"signal",(int)pvVar6);
-          pvVar6 = cJSON_CreateString(acStack_5529 + local_ab98 * 0xab);
+          pvVar6 = cJSON_CreateString(acStack_4d39 + local_9b98 * 0x9b);
           cJSON_AddItemToObject((int)pvVar5,"nettype",(int)pvVar6);
           pvVar6 = cJSON_CreateString("1");
           cJSON_AddItemToObject((int)pvVar5,"wifi_chkHz",(int)pvVar6);
         }
       }
     }
   }
   pcVar2 = (char *)cJSON_Object_2String_apscan(param_1,puVar4);
   if (!bVar1) {
     memcpy(pcVar2,&DAT_0,1);
   }
   psVar7 = (size_t *)strlen(pcVar2);
   websWrite((int)param_2,
             (size_t *)
             "HTTP/1.1 200 OK\r\nContent-Length:%d\r\nContent-type: text/plain; charset=utf-8\r\nPragma: no-cache\r\nCache-Control: no-cache\r\n\r\n"
             ,psVar7,param_5);
   websLongWrite((int)param_2,pcVar2,psVar7,param_5);
   websDone(param_2,200);
   if (pcVar2 != (char *)0x0) {
     free(pcVar2);
   }
   return;
 }
 

```


## form_fast_setting_get

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.96|
|i_ratio|0.32|
|m_ratio|0.98|
|b_ratio|0.84|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|form_fast_setting_get|form_fast_setting_get|
|fullname|form_fast_setting_get|form_fast_setting_get|
|refcount|4|4|
|`length`|3740|3604|
|called|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::__GetPortLink<br><EXTERNAL>::free<br><EXTERNAL>::get_uptime<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::sleep<br><EXTERNAL>::strcmp<br><EXTERNAL>::wanid_to_sw_port<br>GetEthFacMac</summary>__floatsidf<br>cJSON_AddItemToObject<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_wan_type<br>getIpMac<br>websTransfer</details>|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::__GetPortLink<br><EXTERNAL>::free<br><EXTERNAL>::get_uptime<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::puts<br><EXTERNAL>::sleep<br><EXTERNAL>::strcmp<br><EXTERNAL>::wanid_to_sw_port<br>GetEthFacMac</summary>__floatsidf<br>cJSON_AddItemToObject<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_wan_type<br>getIpMac<br>websTransfer</details>|
|calling|formDefineTendDa|formDefineTendDa|
|paramcount|2|2|
|`address`|00475c48|00475f98|
|sig|undefined __stdcall form_fast_setting_get(double param_1, int * param_2)|undefined __stdcall form_fast_setting_get(double param_1, int * param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### form_fast_setting_get Diff


```diff
--- form_fast_setting_get
+++ form_fast_setting_get
@@ -1,196 +1,192 @@
 
 void form_fast_setting_get(double param_1,int *param_2)
 
 {
   undefined4 *puVar1;
   undefined4 uVar2;
   int iVar3;
   uint uVar4;
   void *pvVar5;
   int iVar6;
   size_t *psVar7;
   size_t *__ptr;
   undefined8 uVar8;
   int local_180;
   char acStack_170 [256];
   undefined4 local_70;
   undefined4 local_6c;
   undefined4 local_68;
   undefined4 local_64;
   undefined4 local_60;
   undefined4 local_5c;
   undefined4 local_58;
   undefined4 local_54;
   undefined4 local_50;
   undefined4 local_4c;
   undefined4 local_48;
   undefined4 local_44;
   undefined4 local_40;
   undefined4 local_3c;
   undefined4 local_38;
   undefined4 local_34;
   undefined4 local_30;
   undefined4 local_2c;
   undefined4 local_28;
   undefined4 local_24;
   undefined4 local_20;
   undefined4 local_1c;
   undefined4 local_18;
   undefined4 local_14;
   undefined4 local_10;
   undefined4 local_c;
   
   memset(acStack_170,0,0x100);
   local_70 = 0;
   local_6c = 0;
   local_68 = 0;
   local_64 = 0;
   local_60 = 0;
   local_5c = 0;
   local_58 = 0;
   local_54 = 0;
   local_50 = 0;
   local_4c = 0;
   local_48 = 0;
   local_44 = 0;
   local_40 = 0;
   local_3c = 0;
   local_38 = 0;
   local_34 = 0;
   local_30 = 0;
   local_2c = 0;
   local_28 = 0;
   local_24 = 0;
   local_20 = 0;
   local_1c = 0;
   local_18 = 0;
   local_14 = 0;
   local_10 = 0;
   local_c = 0;
   local_180 = 0;
   puVar1 = (undefined4 *)cJSON_CreateObject();
   uVar2 = wanid_to_sw_port(1);
   iVar3 = __GetPortLink(uVar2);
   if (iVar3 == 0) {
-    fistTime_7945 = 0;
+    fistTime_8055 = 0;
     sleep(1);
   }
   else {
     local_180 = get_uptime();
-    if (fistTime_7945 == 0) {
-      fistTime_7945 = local_180;
+    if (fistTime_8055 == 0) {
+      fistTime_8055 = local_180;
     }
   }
   wanType = check_wan_type();
   if (wanType != -1) {
     net = 1;
   }
   uVar2 = wanid_to_sw_port(1);
   uVar4 = __GetPortLink(uVar2);
   uVar8 = __floatsidf(uVar4);
   pvVar5 = cJSON_CreateNumber((uint)uVar8,(uint)((ulonglong)uVar8 >> 0x20));
   cJSON_AddItemToObject((int)puVar1,"line",(int)pvVar5);
   GetValue("wl2g.public.country",&local_70);
   iVar3 = net;
-  printf("sysTime:%d fistTime:%d  net:%d\n",local_180,fistTime_7945);
+  printf("sysTime:%d fistTime:%d  net:%d\n",local_180,fistTime_8055);
   iVar6 = strcmp((char *)&local_70,"RU");
   if (iVar6 == 0) {
     puts("++++++++++RU++++++++++");
     pvVar5 = cJSON_CreateNumber(0,0xc0000000);
     cJSON_AddItemToObject((int)puVar1,"wanType",(int)pvVar5);
     pvVar5 = cJSON_CreateNumber(0,0x3ff00000);
     cJSON_AddItemToObject((int)puVar1,"net",(int)pvVar5);
     pvVar5 = cJSON_CreateNumber(0,0);
     cJSON_AddItemToObject((int)puVar1,"outType",(int)pvVar5);
     pvVar5 = cJSON_CreateString("0");
     cJSON_AddItemToObject((int)puVar1,"timeout",(int)pvVar5);
   }
-  else if ((net == 1) || (local_180 - fistTime_7945 < 0x1e)) {
+  else if ((net == 1) || (local_180 - fistTime_8055 < 0x1e)) {
     puts("##########check ok or not timeout ##########");
     uVar8 = __floatsidf(wanType);
     pvVar5 = cJSON_CreateNumber((uint)uVar8,(uint)((ulonglong)uVar8 >> 0x20));
     cJSON_AddItemToObject((int)puVar1,"wanType",(int)pvVar5);
     uVar8 = __floatsidf(net);
     pvVar5 = cJSON_CreateNumber((uint)uVar8,(uint)((ulonglong)uVar8 >> 0x20));
     cJSON_AddItemToObject((int)puVar1,"net",(int)pvVar5);
     pvVar5 = cJSON_CreateNumber(0,0x3ff00000);
     cJSON_AddItemToObject((int)puVar1,"outType",(int)pvVar5);
     pvVar5 = cJSON_CreateString("0");
     cJSON_AddItemToObject((int)puVar1,"timeout",(int)pvVar5);
   }
   else {
     puts("~~~~~~~~~~ check time out ~~~~~~~~~~");
     pvVar5 = cJSON_CreateNumber(0,0xc0000000);
     cJSON_AddItemToObject((int)puVar1,"wanType",(int)pvVar5);
     pvVar5 = cJSON_CreateNumber(0,0x3ff00000);
     cJSON_AddItemToObject((int)puVar1,"net",(int)pvVar5);
     pvVar5 = cJSON_CreateNumber(0,0);
     cJSON_AddItemToObject((int)puVar1,"outType",(int)pvVar5);
     pvVar5 = cJSON_CreateString("1");
     cJSON_AddItemToObject((int)puVar1,"timeout",(int)pvVar5);
   }
   memset(acStack_170,0,0x100);
   GetValue("lan.ip",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"lanIp",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetValue("lan.mask",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"lanMask",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetValue("wan1.ppoe.userid",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"adslUser",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetValue("wan1.ppoe.pwd",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"adslPwd",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetValue("wl2g.ssid0.ssid",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"ssid",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetValue("wl2g.ssid0.wpapsk_psk",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"wrlPassword",(int)pvVar5);
   pvVar5 = cJSON_CreateString((char *)&local_70);
   cJSON_AddItemToObject((int)puVar1,"country",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetValue("wl2g.public.power",acStack_170);
   iVar6 = strcmp(acStack_170,"high");
   if (iVar6 == 0) {
     pvVar5 = cJSON_CreateString("high");
     cJSON_AddItemToObject((int)puVar1,"power",(int)pvVar5);
   }
   else {
     pvVar5 = cJSON_CreateString("low");
     cJSON_AddItemToObject((int)puVar1,"power",(int)pvVar5);
   }
   memset(acStack_170,0,0x100);
   GetValue("wan1.mac.clone.type",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"cloneType",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetValue("wan1.macaddr",acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"mac",(int)pvVar5);
   memset(acStack_170,0,0x100);
   getIpMac((char *)(param_2 + 0xc),acStack_170);
   pvVar5 = cJSON_CreateString(acStack_170);
   cJSON_AddItemToObject((int)puVar1,"deviceMac",(int)pvVar5);
   memset(acStack_170,0,0x100);
   GetEthFacMac(1,acStack_170);
-  pvVar5 = cJSON_CreateString(acStack_170);
-  cJSON_AddItemToObject((int)puVar1,"defMac",(int)pvVar5);
-  memset(acStack_170,0,0x100);
-  GetValue("wl5g.public.country",acStack_170);
   psVar7 = (size_t *)cJSON_CreateString(acStack_170);
-  cJSON_AddItemToObject((int)puVar1,"countryCode",(int)psVar7);
+  cJSON_AddItemToObject((int)puVar1,"defMac",(int)psVar7);
   __ptr = (size_t *)cJSON_Print(param_1,(int)puVar1);
   cJSON_Delete(puVar1);
   websTransfer(param_2,__ptr,psVar7,iVar3);
   printf("json string: %s \n\n",__ptr);
   free(__ptr);
   return;
 }
 

```


## aspGetModeShow

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.99|
|i_ratio|0.05|
|m_ratio|0.96|
|b_ratio|0.96|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|aspGetModeShow|aspGetModeShow|
|fullname|aspGetModeShow|aspGetModeShow|
|refcount|4|4|
|`length`|3988|3996|
|called|<EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ejArgs<br>websWrite|<EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ejArgs<br>websWrite|
|calling|formDefineTendDa|formDefineTendDa|
|paramcount|4|4|
|`address`|00450f90|00451270|
|sig|undefined __stdcall aspGetModeShow(undefined4 param_1, int param_2, undefined4 param_3, int param_4)|undefined __stdcall aspGetModeShow(undefined4 param_1, int param_2, undefined4 param_3, int param_4)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### aspGetModeShow Diff


```diff
--- aspGetModeShow
+++ aspGetModeShow
@@ -1,421 +1,421 @@
 
 void aspGetModeShow(undefined4 param_1,int param_2,undefined4 param_3,int param_4)
 
 {
   int iVar1;
   size_t *psVar2;
   char **ppcVar3;
   size_t *local_10;
   char *local_c;
   
   local_c = (char *)0x0;
   local_10 = (size_t *)0xffffffff;
   ppcVar3 = &local_c;
   psVar2 = (size_t *)&DAT_0;
   ejArgs(param_3,param_4,"%s",(int *)ppcVar3);
   if (*local_c == '\0') {
     websWrite(param_2,(size_t *)&DAT_1,psVar2,ppcVar3);
   }
   else {
     iVar1 = strcmp(local_c,"multi_wan");
     if (iVar1 == 0) {
       local_10 = (size_t *)0x1;
     }
     else {
       iVar1 = strcmp(local_c,"parent_control");
       if (iVar1 == 0) {
         local_10 = (size_t *)0x0;
       }
       else {
         iVar1 = strcmp(local_c,"ppoesv");
         if (iVar1 == 0) {
           local_10 = (size_t *)0x0;
         }
         else {
           iVar1 = strcmp(local_c,"webauth");
           if (iVar1 == 0) {
             local_10 = (size_t *)0x0;
           }
           else {
             iVar1 = strcmp(local_c,"vpn");
             if (iVar1 == 0) {
               local_10 = (size_t *)0x1;
             }
             else {
               iVar1 = strcmp(local_c,"GMAC");
               if (iVar1 == 0) {
                 local_10 = (size_t *)0x1;
               }
               else {
                 iVar1 = strcmp(local_c,"natSessionLimit");
                 if (iVar1 == 0) {
                   local_10 = (size_t *)0x0;
                 }
                 else {
                   iVar1 = strcmp(local_c,"safeAttack");
                   if (iVar1 == 0) {
                     local_10 = (size_t *)0x1;
                   }
                   else {
                     iVar1 = strcmp(local_c,"safe_arp");
                     if (iVar1 == 0) {
                       local_10 = (size_t *)0x0;
                     }
                     else {
                       iVar1 = strcmp(local_c,"ssl");
                       if (iVar1 == 0) {
                         local_10 = (size_t *)0x1;
                       }
                       else {
                         iVar1 = strcmp(local_c,"lan_access");
                         if (iVar1 == 0) {
                           local_10 = (size_t *)0x0;
                         }
                         else {
                           iVar1 = strcmp(local_c,"wan_access");
                           if (iVar1 == 0) {
                             local_10 = (size_t *)0x1;
                           }
                           else {
                             iVar1 = strcmp(local_c,"cfg_wan");
                             if (iVar1 == 0) {
                               local_10 = (size_t *)0x1;
                             }
                             else {
                               iVar1 = strcmp(local_c,"cfg_mirror");
                               if (iVar1 == 0) {
                                 local_10 = (size_t *)0x0;
                               }
                               else {
                                 iVar1 = strcmp(local_c,"cfg_port");
                                 if (iVar1 == 0) {
                                   local_10 = (size_t *)0x1;
                                 }
                                 else {
                                   iVar1 = strcmp(local_c,"url");
                                   if (iVar1 == 0) {
                                     puts("udefine\t url");
                                     local_10 = (size_t *)0x0;
                                   }
                                   else {
                                     iVar1 = strcmp(local_c,"url_class");
                                     if (iVar1 == 0) {
                                       local_10 = (size_t *)0x0;
                                     }
                                     else {
                                       iVar1 = strcmp(local_c,"filter_layer7");
                                       if (iVar1 == 0) {
                                         local_10 = (size_t *)0x0;
                                       }
                                       else {
                                         iVar1 = strcmp(local_c,"filter_im");
                                         if (iVar1 == 0) {
                                           local_10 = (size_t *)0x0;
                                         }
                                         else {
                                           iVar1 = strcmp(local_c,"turbo_qos");
                                           if (iVar1 == 0) {
                                             local_10 = (size_t *)0x0;
                                           }
                                           else {
                                             iVar1 = strcmp(local_c,"qos_priority");
                                             if (iVar1 == 0) {
                                               local_10 = (size_t *)0x0;
                                             }
                                             else {
                                               iVar1 = strcmp(local_c,"notification");
                                               if (iVar1 == 0) {
                                                 local_10 = (size_t *)0x0;
                                               }
                                               else {
                                                 iVar1 = strcmp(local_c,"p2p_NAT");
                                                 if (iVar1 == 0) {
                                                   local_10 = (size_t *)0x0;
                                                 }
                                                 else {
                                                   iVar1 = strcmp(local_c,"ddns_ddns");
                                                   if (iVar1 == 0) {
                                                     local_10 = (size_t *)0x1;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(local_c,"ddns_3322");
                                                     if (iVar1 == 0) {
                                                       local_10 = (size_t *)0x1;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(local_c,"ddns_88ip");
                                                       if (iVar1 == 0) {
                                                         local_10 = (size_t *)0x1;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(local_c,"ddns_GNWAY");
                                                         if (iVar1 == 0) {
                                                           local_10 = (size_t *)0x0;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(local_c,"ddns_oray");
                                                           if (iVar1 == 0) {
                                                             local_10 = (size_t *)0x1;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(local_c,"ddns_noip");
                                                             if (iVar1 == 0) {
                                                               local_10 = (size_t *)0x1;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(local_c,"ddns_dyn");
                                                               if (iVar1 == 0) {
                                                                 local_10 = (size_t *)0x1;
                                                               }
                                                               else {
                                                                 iVar1 = strcmp(local_c,
                                                   "update_layer7");
                                                   if (iVar1 == 0) {
                                                     local_10 = (size_t *)0x0;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(local_c,"cfg_dsl");
                                                     if (iVar1 == 0) {
                                                       local_10 = (size_t *)0x0;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(local_c,"dsl_annex_a");
                                                       if (iVar1 == 0) {
                                                         local_10 = (size_t *)0x0;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(local_c,"dsl_annex_b");
                                                         if (iVar1 == 0) {
                                                           local_10 = (size_t *)0x0;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(local_c,"cfg_wifi");
                                                           if (iVar1 == 0) {
                                                             local_10 = (size_t *)0x1;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(local_c,"wifi_auth_1x");
                                                             if (iVar1 == 0) {
                                                               local_10 = (size_t *)0x1;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(local_c,"wifi_auth_wps"
                                                                             );
                                                               if (iVar1 == 0) {
                                                                 local_10 = (size_t *)0x1;
                                                               }
                                                               else {
                                                                 iVar1 = strcmp(local_c,
                                                   "wifi_auth_wds");
                                                   if (iVar1 == 0) {
                                                     local_10 = (size_t *)0x0;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(local_c,"wifi_auth_apClient");
                                                     if (iVar1 == 0) {
                                                       local_10 = (size_t *)0x0;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(local_c,"wifi_tempNetwork");
                                                       if (iVar1 == 0) {
                                                         local_10 = (size_t *)0x0;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(local_c,"wifi_guest");
                                                         if (iVar1 == 0) {
                                                           local_10 = (size_t *)0x1;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(local_c,"cfg_tr069");
                                                           if (iVar1 == 0) {
                                                             local_10 = (size_t *)0x0;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(local_c,"cfg_ipv6");
                                                             if (iVar1 == 0) {
                                                               local_10 = (size_t *)0x0;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(local_c,"wan_ipoe");
                                                               if (iVar1 == 0) {
                                                                 local_10 = (size_t *)0x0;
                                                               }
                                                               else {
                                                                 iVar1 = strcmp(local_c,"wan_ipoa");
                                                                 if (iVar1 == 0) {
                                                                   local_10 = (size_t *)0x0;
                                                                 }
                                                                 else {
                                                                   iVar1 = strcmp(local_c,"wan_ppoa")
                                                                   ;
                                                                   if (iVar1 == 0) {
                                                                     local_10 = (size_t *)0x0;
                                                                   }
                                                                   else {
                                                                     iVar1 = strcmp(local_c,
                                                   "wan_ppoe");
                                                   if (iVar1 == 0) {
                                                     local_10 = (size_t *)0x1;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(local_c,"wan_static");
                                                     if (iVar1 == 0) {
                                                       local_10 = (size_t *)0x1;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(local_c,"wan_dhcp");
                                                       if (iVar1 == 0) {
                                                         local_10 = (size_t *)0x1;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(local_c,"wan_pptp");
                                                         if (iVar1 == 0) {
                                                           local_10 = (size_t *)0x1;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(local_c,"wan_l2tp");
                                                           if (iVar1 == 0) {
                                                             local_10 = (size_t *)0x1;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(local_c,"wan_double_pptp"
                                                                           );
                                                             if (iVar1 == 0) {
                                                               local_10 = (size_t *)0x1;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(local_c,
                                                   "wan_double_l2tp");
                                                   if (iVar1 == 0) {
                                                     local_10 = (size_t *)0x1;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(local_c,"wan_double_ppoe");
                                                     if (iVar1 == 0) {
                                                       local_10 = (size_t *)0x1;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(local_c,"pppoeserver");
                                                       if (iVar1 == 0) {
                                                         local_10 = (size_t *)0x0;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(local_c,"arpgateway");
                                                         if (iVar1 == 0) {
                                                           local_10 = (size_t *)0x0;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(local_c,"emailcc");
                                                           if (iVar1 == 0) {
                                                             local_10 = (size_t *)0x0;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(local_c,"ipsec");
                                                             if (iVar1 == 0) {
                                                               local_10 = (size_t *)0x0;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(local_c,"ftpserver");
                                                               if (iVar1 == 0) {
-                                                                local_10 = (size_t *)0x0;
+                                                                local_10 = (size_t *)0x1;
                                                               }
                                                               else {
                                                                 iVar1 = strcmp(local_c,"usb");
                                                                 if (iVar1 == 0) {
-                                                                  local_10 = (size_t *)0x0;
+                                                                  local_10 = (size_t *)0x1;
                                                                 }
                                                                 else {
                                                                   iVar1 = strcmp(local_c,"ippd");
                                                                   if (iVar1 == 0) {
-                                                                    local_10 = (size_t *)0x1;
+                                                                    local_10 = (size_t *)0x0;
                                                                   }
                                                                   else {
                                                                     iVar1 = strcmp(local_c,"samba");
                                                                     if (iVar1 == 0) {
-                                                                      local_10 = (size_t *)0x0;
+                                                                      local_10 = (size_t *)0x1;
                                                                     }
                                                                     else {
                                                                       iVar1 = strcmp(local_c,
                                                   "bt_client");
                                                   if (iVar1 == 0) {
                                                     local_10 = (size_t *)0x0;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(local_c,"multi_lan");
                                                     if (iVar1 == 0) {
                                                       local_10 = (size_t *)0x0;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(local_c,"lan_vlan");
                                                       if (iVar1 == 0) {
                                                         local_10 = (size_t *)0x0;
                                                       }
                                                     }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                   }
                                                 }
                                               }
                                             }
                                           }
                                         }
                                       }
                                     }
                                   }
                                 }
                               }
                             }
                           }
                         }
                       }
                     }
                   }
                 }
               }
             }
           }
         }
       }
     }
     websWrite(param_2,(size_t *)&DAT_2,local_10,ppcVar3);
   }
   return;
 }
 

```


# Modified (No Code Changes)


*Slightly modified functions have no code changes, rather differnces in:*
- refcount
- length
- called
- calling
- name
- fullname

## cJSON_CreateObject

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.89|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_CreateObject|cJSON_CreateObject|
|fullname|cJSON_CreateObject|cJSON_CreateObject|
|`refcount`|113|118|
|length|112|112|
|called|cJSON_New_Item|cJSON_New_Item|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink</summary>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink</summary>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|
|paramcount|0|0|
|`address`|0044cff4|0044d1f4|
|sig|void * __stdcall cJSON_CreateObject(void)|void * __stdcall cJSON_CreateObject(void)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_CreateObject Calling Diff


```diff
--- cJSON_CreateObject calling
+++ cJSON_CreateObject calling
@@ -24,0 +25 @@
+formGetSambaConf
@@ -31,0 +33 @@
+formGetUSBStatus
@@ -32,0 +35 @@
+formGetUsbCfg
```


## websTransfer

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.88|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|websTransfer|websTransfer|
|fullname|websTransfer|websTransfer|
|`refcount`|100|101|
|length|160|160|
|called|websDone<br>websWrite|websDone<br>websWrite|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>GetProduct<br>addWifiMacFilter<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddMacfilterRule<br>formAliScheduleStatus<br>formDelMacfilterRule<br>formGetDeviceDetail<br>formGetOnlineList<br>formGetParentCtrlList</summary>formGetQosBand<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysToolDDNS<br>formGetUpnpLists<br>formGetWanConnectStatus<br>formGetWifiWps<br>formSetAutoQosInfo<br>formSetClientState<br>formSetDeviceName<br>formSetMacFilterCfg<br>formSetParentControlEnable<br>formSetQosBand<br>formSetSafeWanWebMan<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetWifiWps<br>formStartWifiWps<br>formWifiAntijamSet<br>formWifiBasicGet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiDhcpGuestSet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiPowerSet<br>formWifiRadioGet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiStatisticClear<br>formWifiStatus<br>formWifiWpsGet<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_get<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>form_usb_get<br>formsetNotUpgrade<br>fromAdvSetLanip<br>fromAdvSetMacMtuWan<br>fromDhcpSetSer<br>fromGetWirelessRepeat<br>fromSetIpMacBind<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromsetApModeCfg<br>getSchedWifi<br>getSmartPowerManagement<br>mDMZSetCfg</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>GetProduct<br>addWifiMacFilter<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddMacfilterRule<br>formAliScheduleStatus<br>formDelMacfilterRule<br>formGetDeviceDetail<br>formGetOnlineList<br>formGetParentCtrlList</summary>formGetQosBand<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysToolDDNS<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetWanConnectStatus<br>formGetWifiWps<br>formSetAutoQosInfo<br>formSetClientState<br>formSetDeviceName<br>formSetMacFilterCfg<br>formSetParentControlEnable<br>formSetQosBand<br>formSetSafeWanWebMan<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetWifiWps<br>formStartWifiWps<br>formWifiAntijamSet<br>formWifiBasicGet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiDhcpGuestSet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiPowerSet<br>formWifiRadioGet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiStatisticClear<br>formWifiStatus<br>formWifiWpsGet<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_get<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>form_usb_get<br>formsetNotUpgrade<br>fromAdvSetLanip<br>fromAdvSetMacMtuWan<br>fromDhcpSetSer<br>fromGetWirelessRepeat<br>fromSetIpMacBind<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromsetApModeCfg<br>getSchedWifi<br>getSmartPowerManagement<br>mDMZSetCfg</details>|
|paramcount|4|4|
|`address`|004bcf04|004bce44|
|sig|undefined __stdcall websTransfer(int * param_1, size_t * param_2, size_t * param_3, undefined4 param_4)|undefined __stdcall websTransfer(int * param_1, size_t * param_2, size_t * param_3, undefined4 param_4)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### websTransfer Calling Diff


```diff
--- websTransfer calling
+++ websTransfer calling
@@ -16,0 +17 @@
+formGetUSBStatus
```


## cJSON_AddItemToArray

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.84|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_AddItemToArray|cJSON_AddItemToArray|
|fullname|cJSON_AddItemToArray|cJSON_AddItemToArray|
|`refcount`|44|46|
|length|204|204|
|called|suffix_object|suffix_object|
|`calling`|<details><summary>Expand for full list:<br>cJSON_AddItemReferenceToArray<br>cJSON_AddItemToObject<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRouteStatic</summary>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiDhcpGuestLists<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>cJSON_AddItemReferenceToArray<br>cJSON_AddItemToObject<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRouteStatic</summary>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiDhcpGuestLists<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>write_wan_infos</details>|
|paramcount|2|2|
|`address`|0044c4b8|0044c6b8|
|sig|undefined __stdcall cJSON_AddItemToArray(int param_1, int param_2)|undefined __stdcall cJSON_AddItemToArray(int param_1, int param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_AddItemToArray Calling Diff


```diff
--- cJSON_AddItemToArray calling
+++ cJSON_AddItemToArray calling
@@ -13,0 +14 @@
+formGetUsbCfg
```


## websFormDefine

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address|
|ratio|1.0|
|i_ratio|0.88|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|websFormDefine|websFormDefine|
|fullname|websFormDefine|websFormDefine|
|`refcount`|177|184|
|length|200|200|
|called|symEnter<br>valueInteger|symEnter<br>valueInteger|
|calling|formDefineTendDa<br>formDefineUcloudv2<br>formDefineUserMgmt|formDefineTendDa<br>formDefineUcloudv2<br>formDefineUserMgmt|
|paramcount|2|2|
|`address`|00416584|00416784|
|sig|undefined4 __stdcall websFormDefine(bType * param_1, int param_2)|undefined4 __stdcall websFormDefine(bType * param_1, int param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

## __ledf2

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.66|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|__ledf2|__ledf2|
|fullname|__ledf2|__ledf2|
|`refcount`|9|10|
|length|260|260|
|called|||
|`calling`|formatDataSize<br>print_number|formGetUsbCfg<br>formatDataSize<br>print_number|
|paramcount|4|4|
|`address`|005030b0|005057b0|
|sig|undefined4 __stdcall __ledf2(uint param_1, uint param_2, uint param_3, uint param_4)|undefined4 __stdcall __ledf2(uint param_1, uint param_2, uint param_3, uint param_4)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### __ledf2 Calling Diff


```diff
--- __ledf2 calling
+++ __ledf2 calling
@@ -0,0 +1 @@
+formGetUsbCfg
```


## set_cfm_mib

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.87|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|set_cfm_mib|set_cfm_mib|
|fullname|set_cfm_mib|set_cfm_mib|
|`refcount`|8|4|
|length|120|120|
|called|<EXTERNAL>::SetValue|<EXTERNAL>::SetValue|
|`calling`|ate_nvram_set_maxpower<br>ate_nvram_set_maxpower_2G<br>ate_nvram_set_maxpower_5G<br>rtl_ate_set_apmib|rtl_ate_set_apmib|
|paramcount|2|2|
|`address`|00479d90|0047a050|
|sig|undefined4 __stdcall set_cfm_mib(int param_1, int param_2)|undefined4 __stdcall set_cfm_mib(int param_1, int param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### set_cfm_mib Calling Diff


```diff
--- set_cfm_mib calling
+++ set_cfm_mib calling
@@ -1,3 +0,0 @@
-ate_nvram_set_maxpower
-ate_nvram_set_maxpower_2G
-ate_nvram_set_maxpower_5G
```


## cJSON_CreateArray

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.89|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_CreateArray|cJSON_CreateArray|
|fullname|cJSON_CreateArray|cJSON_CreateArray|
|`refcount`|40|42|
|length|112|112|
|called|cJSON_New_Item|cJSON_New_Item|
|`calling`|<details><summary>Expand for full list:<br>cJSON_CreateDoubleArray<br>cJSON_CreateFloatArray<br>cJSON_CreateIntArray<br>cJSON_CreateStringArray<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus</summary>formGetQosBand<br>formGetRouteStatic<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiClientList<br>formWifiClientListAll<br>formWifiDhcpGuestLists<br>formWifiRadioGet<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>initWifiMacFilter<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>cJSON_CreateDoubleArray<br>cJSON_CreateFloatArray<br>cJSON_CreateIntArray<br>cJSON_CreateStringArray<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus</summary>formGetQosBand<br>formGetRouteStatic<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiClientList<br>formWifiClientListAll<br>formWifiDhcpGuestLists<br>formWifiRadioGet<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>initWifiMacFilter<br>write_wan_infos</details>|
|paramcount|0|0|
|`address`|0044cf84|0044d184|
|sig|void * __stdcall cJSON_CreateArray(void)|void * __stdcall cJSON_CreateArray(void)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_CreateArray Calling Diff


```diff
--- cJSON_CreateArray calling
+++ cJSON_CreateArray calling
@@ -15,0 +16 @@
+formGetUsbCfg
```


## cJSON_Object_2String

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.79|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_Object_2String|cJSON_Object_2String|
|fullname|cJSON_Object_2String|cJSON_Object_2String|
|`refcount`|26|28|
|length|252|252|
|called|<EXTERNAL>::free<br><EXTERNAL>::puts<br><EXTERNAL>::strlen<br><EXTERNAL>::strncpy<br>cJSON_Delete<br>cJSON_Print|<EXTERNAL>::free<br><EXTERNAL>::puts<br><EXTERNAL>::strlen<br><EXTERNAL>::strncpy<br>cJSON_Delete<br>cJSON_Print|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysLog<br>formGetSysToolDDNS<br>formGetWifiWps<br>formWifiBasicGet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet</summary>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>fromGetWirelessRepeat<br>getSchedWifi<br>getSmartPowerManagement</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysLog<br>formGetSysToolDDNS<br>formGetUSBStatus<br>formGetWifiWps<br>formWifiBasicGet<br>formWifiClientList<br>formWifiClientListAll</summary>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>fromGetWirelessRepeat<br>getSchedWifi<br>getSmartPowerManagement</details>|
|paramcount|2|2|
|`address`|004bcd90|004bccd0|
|sig|char * __stdcall cJSON_Object_2String(double param_1, undefined4 * param_2)|char * __stdcall cJSON_Object_2String(double param_1, undefined4 * param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_Object_2String Calling Diff


```diff
--- cJSON_Object_2String calling
+++ cJSON_Object_2String calling
@@ -2,0 +3 @@
+formGetSambaConf
@@ -5,0 +7 @@
+formGetUSBStatus
```


## cJSON_AddItemToObject

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.89|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_AddItemToObject|cJSON_AddItemToObject|
|fullname|cJSON_AddItemToObject|cJSON_AddItemToObject|
|`refcount`|774|799|
|length|212|212|
|called|<EXTERNAL>::free<br>cJSON_AddItemToArray<br>cJSON_strdup|<EXTERNAL>::free<br>cJSON_AddItemToArray<br>cJSON_strdup|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>assembleChannelList2JsonArray<br>cJSON_AddItemReferenceToObject<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer</summary>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>assembleChannelList2JsonArray<br>cJSON_AddItemReferenceToObject<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer</summary>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|
|paramcount|3|3|
|`address`|0044c584|0044c784|
|sig|undefined __stdcall cJSON_AddItemToObject(int param_1, char * param_2, int param_3)|undefined __stdcall cJSON_AddItemToObject(int param_1, char * param_2, int param_3)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_AddItemToObject Calling Diff


```diff
--- cJSON_AddItemToObject calling
+++ cJSON_AddItemToObject calling
@@ -26,0 +27 @@
+formGetSambaConf
@@ -33,0 +35 @@
+formGetUSBStatus
@@ -34,0 +37 @@
+formGetUsbCfg
```


## cJSON_Print

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.92|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_Print|cJSON_Print|
|fullname|cJSON_Print|cJSON_Print|
|`refcount`|60|61|
|length|96|96|
|called|print_value|print_value|
|`calling`|<details><summary>Expand for full list:<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|<details><summary>Expand for full list:<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|
|paramcount|2|2|
|`address`|0044aa80|0044ac80|
|sig|undefined __stdcall cJSON_Print(double param_1, int param_2)|undefined __stdcall cJSON_Print(double param_1, int param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_Print Calling Diff


```diff
--- cJSON_Print calling
+++ cJSON_Print calling
@@ -29,0 +30 @@
+formGetUsbCfg
```


## cJSON_CreateString

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.9|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_CreateString|cJSON_CreateString|
|fullname|cJSON_CreateString|cJSON_CreateString|
|`refcount`|676|699|
|length|156|156|
|called|cJSON_New_Item<br>cJSON_strdup|cJSON_New_Item<br>cJSON_strdup|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>cJSON_CreateStringArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>queryaccount<br>querybasic<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>cJSON_CreateStringArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>queryaccount<br>querybasic<br>write_online_upgrade_info<br>write_wan_infos</details>|
|paramcount|1|1|
|`address`|0044cee8|0044d0e8|
|sig|void * __stdcall cJSON_CreateString(char * param_1)|void * __stdcall cJSON_CreateString(char * param_1)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_CreateString Calling Diff


```diff
--- cJSON_CreateString calling
+++ cJSON_CreateString calling
@@ -25,0 +26 @@
+formGetSambaConf
@@ -32,0 +34 @@
+formGetUSBStatus
@@ -33,0 +36 @@
+formGetUsbCfg
```


## websGetVar

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.82|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|websGetVar|websGetVar|
|fullname|websGetVar|websGetVar|
|`refcount`|483|494|
|length|196|196|
|called|symLookup|symLookup|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>R7WebsSecurityHandler<br>SetWebIpAccess<br>addWifiMacFilter<br>add_white_node<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>check_param_changed<br>cloudv2<br>cloudv2_manage</summary>cloudv2_olupgrade<br>cloudv2_wansta<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddAccessLimit<br>formAddGroup<br>formAddMacfilterRule<br>formAddUser<br>formBehaviorManager<br>formBulletinSet<br>formDelMacfilterRule<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetDeviceDetail<br>formGetWanStatus<br>formLoadUserManagement<br>formNatSet<br>formNotNowUpgrade<br>formQuickIndex<br>formSafeDemo<br>formSaveUserManagement<br>formSetAutoQosInfo<br>formSetCfm<br>formSetClientState<br>formSetDeviceName<br>formSetFirewallCfg<br>formSetIptv<br>formSetMacFilterCfg<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetParentControlEnable<br>formSetQosBand<br>formSetRebootTimer<br>formSetSafeWanWebMan<br>formSetSchedLed<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetVirtualSer<br>formSetWifiWps<br>formStartWifiWps<br>formWanInfoSet<br>formWanParameterSetting<br>formWifiAntijamSet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerSet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>formWriteFacMac<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>formexeCommand<br>formsetNotUpgrade<br>fromAddressNat<br>fromAdvSetLanip<br>fromAdvSetPortVlan<br>fromDhcpListClient<br>fromDhcpSetSer<br>fromGstDhcpSetSer<br>fromLogsSetting<br>fromNatStaticSetting<br>fromSetIpBind<br>fromSetIpMacBind<br>fromSetRouteStatic<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromSysStatusHandle<br>fromSysToolBaseUser<br>fromSysToolChangePwd<br>fromSysToolTime<br>fromWanPolicy<br>fromWizardHandle<br>fromsetApModeCfg<br>getRebootStatus<br>mDMZSetCfg<br>saveParentControlInfo<br>setDhcpConfig<br>setDnsCheck<br>setDoubleL2tpConfig<br>setDoublePppoeConfig<br>setDoublePptpConfig<br>setPppoeConfig<br>setSchedWifi<br>setSmartPowerManagement<br>setStaticConfig<br>setWanDownrate<br>setWifiGusetBasic<br>setaccount<br>setbasic<br>websCompareVar<br>websGetVarWithValidate<br>websRedirect<br>websRedirectOpCookie<br>websSetEnv<br>wl_guest_conf_change</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>R7WebsSecurityHandler<br>SetWebIpAccess<br>addWifiMacFilter<br>add_white_node<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>check_param_changed<br>cloudv2<br>cloudv2_manage</summary>cloudv2_olupgrade<br>cloudv2_wansta<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddAccessLimit<br>formAddGroup<br>formAddMacfilterRule<br>formAddUser<br>formBehaviorManager<br>formBulletinSet<br>formDelMacfilterRule<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetDeviceDetail<br>formGetWanStatus<br>formLoadUserManagement<br>formNatSet<br>formNotNowUpgrade<br>formQuickIndex<br>formSafeDemo<br>formSaveUserManagement<br>formSetAutoQosInfo<br>formSetCfm<br>formSetClientState<br>formSetDeviceName<br>formSetFirewallCfg<br>formSetIptv<br>formSetMacFilterCfg<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetParentControlEnable<br>formSetQosBand<br>formSetRebootTimer<br>formSetSafeWanWebMan<br>formSetSambaConf<br>formSetSchedLed<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetUsbPrint<br>formSetVirtualSer<br>formSetWifiWps<br>formStartWifiWps<br>formWanInfoSet<br>formWanParameterSetting<br>formWifiAntijamSet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerSet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>formWriteFacMac<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>formexeCommand<br>formsetNotUpgrade<br>formsetUsbUnload<br>fromAddressNat<br>fromAdvSetLanip<br>fromAdvSetPortVlan<br>fromDhcpListClient<br>fromDhcpSetSer<br>fromGstDhcpSetSer<br>fromLogsSetting<br>fromNatStaticSetting<br>fromSetIpBind<br>fromSetIpMacBind<br>fromSetRouteStatic<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromSysStatusHandle<br>fromSysToolBaseUser<br>fromSysToolChangePwd<br>fromSysToolTime<br>fromWanPolicy<br>fromWizardHandle<br>fromsetApModeCfg<br>getRebootStatus<br>mDMZSetCfg<br>saveParentControlInfo<br>setDhcpConfig<br>setDnsCheck<br>setDoubleL2tpConfig<br>setDoublePppoeConfig<br>setDoublePptpConfig<br>setPppoeConfig<br>setSchedWifi<br>setSmartPowerManagement<br>setStaticConfig<br>setWanDownrate<br>setWifiGusetBasic<br>setaccount<br>setbasic<br>websCompareVar<br>websGetVarWithValidate<br>websRedirect<br>websRedirectOpCookie<br>websSetEnv<br>wl_guest_conf_change</details>|
|paramcount|3|3|
|`address`|00430268|00430468|
|sig|undefined1 * __stdcall websGetVar(int param_1, char * param_2, undefined1 * param_3)|undefined1 * __stdcall websGetVar(int param_1, char * param_2, undefined1 * param_3)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### websGetVar Calling Diff


```diff
--- websGetVar calling
+++ websGetVar calling
@@ -48,0 +49 @@
+formSetSambaConf
@@ -52,0 +54 @@
+formSetUsbPrint
@@ -78,0 +81 @@
+formsetUsbUnload
```


## cJSON_Delete

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.86|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|cJSON_Delete|cJSON_Delete|
|fullname|cJSON_Delete|cJSON_Delete|
|`refcount`|80|81|
|length|320|320|
|called|<EXTERNAL>::free<br>cJSON_Delete|<EXTERNAL>::free<br>cJSON_Delete|
|`calling`|<details><summary>Expand for full list:<br>_cgi_get_sys_basic_info_<br>_cgi_query_uc_account_<br>_cgi_query_uc_manage_en_<br>_cgi_set_uc_manage_en_<br>_query_version_<br>cJSON_Delete<br>cJSON_DeleteItemFromArray<br>cJSON_DeleteItemFromObject<br>cJSON_Duplicate<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan</summary>cJSON_ParseWithOpts<br>cJSON_ReplaceItemInArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>formWifiMacFilterGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>parse_response_string<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|<details><summary>Expand for full list:<br>_cgi_get_sys_basic_info_<br>_cgi_query_uc_account_<br>_cgi_query_uc_manage_en_<br>_cgi_set_uc_manage_en_<br>_query_version_<br>cJSON_Delete<br>cJSON_DeleteItemFromArray<br>cJSON_DeleteItemFromObject<br>cJSON_Duplicate<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan</summary>cJSON_ParseWithOpts<br>cJSON_ReplaceItemInArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>formWifiMacFilterGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>parse_response_string<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|
|paramcount|1|1|
|`address`|00449300|00449500|
|sig|undefined __stdcall cJSON_Delete(undefined4 * param_1)|undefined __stdcall cJSON_Delete(undefined4 * param_1)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_Delete Calling Diff


```diff
--- cJSON_Delete calling
+++ cJSON_Delete calling
@@ -40,0 +41 @@
+formGetUsbCfg
```


## websDone

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.87|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|websDone|websDone|
|fullname|websDone|websDone|
|`refcount`|144|151|
|length|712|712|
|called|<details><summary>Expand for full list:<br>ringqFlush<br>socketCloseConnection<br>socketCreateHandler<br>socketDeleteHandler<br>socketFlush<br>socketSetBlock<br>websFree<br>websPageClose<br>websSSLFlush<br>websSchedCallBack<br>websSocketEvent</summary>websTimeout<br>websTimeoutCancel</details>|<details><summary>Expand for full list:<br>ringqFlush<br>socketCloseConnection<br>socketCreateHandler<br>socketDeleteHandler<br>socketFlush<br>socketSetBlock<br>websFree<br>websPageClose<br>websSSLFlush<br>websSchedCallBack<br>websSocketEvent</summary>websTimeout<br>websTimeoutCancel</details>|
|`calling`|<details><summary>Expand for full list:<br>DownloadCfg<br>DownloadFlash<br>DownloadLog<br>DownloadWebsite<br>R7WebsSecurityHandler<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>add_white_node<br>cgi_clear_arp_info<br>cgi_clear_ddos_fence</summary>cgi_clear_ip_opt<br>cgi_get_arp_info<br>cgi_get_ddos_fence<br>cgi_get_ip_opt<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>cloudv2_manage<br>cloudv2_olupgrade<br>cloudv2_wansta<br>file_clear<br>file_option<br>file_show<br>formAddAccessLimit<br>formAddGroup<br>formAddUser<br>formAdvGetLanIp<br>formBehaviorManager<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formLoadUserManagement<br>formMfgTest<br>formNotNowUpgrade<br>formSaveUserManagement<br>formSetFirewallCfg<br>formSetIptv<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetRebootTimer<br>formSetSchedLed<br>formSetVirtualSer<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBeamformingGet<br>formWriteFacMac<br>formexeCommand<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSetRouteStatic<br>fromSysStatusHandle<br>fromSysToolGetUpgrade<br>fromSysToolSetUpgrade<br>fromWizardHandle<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>get_online_ip_info<br>initWifiMacFilter<br>key_clear<br>key_option<br>key_show<br>mDMZGetCfg<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websCgiCleanup<br>websDefaultHandler<br>websDefaultWriteEvent<br>websFileDownUpCleanup<br>websGetInput<br>websResponse<br>websResponseOpCookie<br>websTimeout<br>websTransfer<br>write_ddos_fence_info<br>write_ipopt_fence_info</details>|<details><summary>Expand for full list:<br>DownloadCfg<br>DownloadFlash<br>DownloadLog<br>DownloadWebsite<br>R7WebsSecurityHandler<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>add_white_node<br>cgi_clear_arp_info<br>cgi_clear_ddos_fence</summary>cgi_clear_ip_opt<br>cgi_get_arp_info<br>cgi_get_ddos_fence<br>cgi_get_ip_opt<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>cloudv2_manage<br>cloudv2_olupgrade<br>cloudv2_wansta<br>file_clear<br>file_option<br>file_show<br>formAddAccessLimit<br>formAddGroup<br>formAddUser<br>formAdvGetLanIp<br>formBehaviorManager<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSambaConf<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUsbCfg<br>formGetUsbPrint<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formLoadUserManagement<br>formMfgTest<br>formNotNowUpgrade<br>formSaveUserManagement<br>formSetFirewallCfg<br>formSetIptv<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetRebootTimer<br>formSetSambaConf<br>formSetSchedLed<br>formSetUsbPrint<br>formSetVirtualSer<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBeamformingGet<br>formWriteFacMac<br>formexeCommand<br>formgetPptpOnlineClient<br>formsetUsbUnload<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSetRouteStatic<br>fromSysStatusHandle<br>fromSysToolGetUpgrade<br>fromSysToolSetUpgrade<br>fromWizardHandle<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>get_online_ip_info<br>initWifiMacFilter<br>key_clear<br>key_option<br>key_show<br>mDMZGetCfg<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websCgiCleanup<br>websDefaultHandler<br>websDefaultWriteEvent<br>websFileDownUpCleanup<br>websGetInput<br>websResponse<br>websResponseOpCookie<br>websTimeout<br>websTransfer<br>write_ddos_fence_info<br>write_ipopt_fence_info</details>|
|paramcount|2|2|
|`address`|00431668|00431868|
|sig|undefined __stdcall websDone(int * param_1, int param_2)|undefined __stdcall websDone(int * param_1, int param_2)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### websDone Calling Diff


```diff
--- websDone calling
+++ websDone calling
@@ -55,0 +56 @@
+formGetSambaConf
@@ -60,0 +62,2 @@
+formGetUsbCfg
+formGetUsbPrint
@@ -76,0 +80 @@
+formSetSambaConf
@@ -77,0 +82 @@
+formSetUsbPrint
@@ -87,0 +93 @@
+formsetUsbUnload
```


## websWrite

### Match Info



|Key|AC6_httpd - AC9_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.88|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC6_httpd|AC9_httpd|
| :---: | :---: | :---: |
|name|websWrite|websWrite|
|fullname|websWrite|websWrite|
|`refcount`|601|615|
|length|296|296|
|called|<EXTERNAL>::strlen<br>bfree<br>fmtValloc<br>trace<br>websWriteBlock|<EXTERNAL>::strlen<br>bfree<br>fmtValloc<br>trace<br>websWriteBlock|
|`calling`|<details><summary>Expand for full list:<br>DownloadFlash<br>R7WebsSecurityHandler<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>add_white_node<br>aspGenerateAccessLimitList<br>aspGenerateAccessMethodList<br>aspGenerateGroupList<br>aspGeneratePrivilegeList<br>aspGenerateUserList</summary>aspGetCfm<br>aspGetCharset<br>aspGetMaxNatNum<br>aspGetModeShow<br>aspGetParam<br>aspGetPortShow<br>aspGetWanNum<br>aspGetfilterMaxNum<br>aspGetifnlist<br>aspNatSet<br>aspTendaGetArpBindList<br>aspTendaGetDhcpClients<br>aspTendaGetStatus<br>asp_error_message<br>asp_error_redirect_url<br>aspmGetIPRate<br>aspmGetRouteTable<br>cgi_clear_arp_info<br>cgi_clear_ddos_fence<br>cgi_clear_ip_opt<br>cgi_get_arp_info<br>cgi_get_ddos_fence<br>cgi_get_ip_opt<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>cloudv2_manage<br>cloudv2_olupgrade<br>cloudv2_wansta<br>file_clear<br>file_option<br>file_show<br>formAddAccessLimit<br>formAddGroup<br>formAddUser<br>formAdvGetLanIp<br>formBehaviorManager<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formLoadUserManagement<br>formMfgTest<br>formNotNowUpgrade<br>formSaveUserManagement<br>formSetCfm<br>formSetFirewallCfg<br>formSetIptv<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetRebootTimer<br>formSetSchedLed<br>formSetVirtualSer<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formTendaModelStatus<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBeamformingGet<br>formWriteFacMac<br>formexeCommand<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSetRouteStatic<br>fromSysStatusHandle<br>fromSysToolGetUpgrade<br>fromSysToolSetUpgrade<br>fromWizardHandle<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>get_online_ip_info<br>initWifiMacFilter<br>key_clear<br>key_option<br>key_show<br>mDMZGetCfg<br>mNatGetStatic<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websAspRequest<br>websCgiGatherOutput<br>websDefaultHandler<br>websFooter<br>websHeader<br>websLongWrite<br>websMsgEnd<br>websMsgStart<br>websResponse<br>websResponseDownLoadFile<br>websResponseOpCookie<br>websTransfer<br>write_ddos_fence_info<br>write_ipopt_fence_info<br>write_list_data<br>write_list_data_n</details>|<details><summary>Expand for full list:<br>DownloadFlash<br>R7WebsSecurityHandler<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>add_white_node<br>aspGenerateAccessLimitList<br>aspGenerateAccessMethodList<br>aspGenerateGroupList<br>aspGeneratePrivilegeList<br>aspGenerateUserList</summary>aspGetCfm<br>aspGetCharset<br>aspGetMaxNatNum<br>aspGetModeShow<br>aspGetParam<br>aspGetPortShow<br>aspGetWanNum<br>aspGetfilterMaxNum<br>aspGetifnlist<br>aspNatSet<br>aspTendaGetArpBindList<br>aspTendaGetDhcpClients<br>aspTendaGetStatus<br>asp_error_message<br>asp_error_redirect_url<br>aspmGetIPRate<br>aspmGetRouteTable<br>cgi_clear_arp_info<br>cgi_clear_ddos_fence<br>cgi_clear_ip_opt<br>cgi_get_arp_info<br>cgi_get_ddos_fence<br>cgi_get_ip_opt<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>cloudv2_manage<br>cloudv2_olupgrade<br>cloudv2_wansta<br>file_clear<br>file_option<br>file_show<br>formAddAccessLimit<br>formAddGroup<br>formAddUser<br>formAdvGetLanIp<br>formBehaviorManager<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSambaConf<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUsbCfg<br>formGetUsbPrint<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formLoadUserManagement<br>formMfgTest<br>formNotNowUpgrade<br>formSaveUserManagement<br>formSetCfm<br>formSetFirewallCfg<br>formSetIptv<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetRebootTimer<br>formSetSambaConf<br>formSetSchedLed<br>formSetUsbPrint<br>formSetVirtualSer<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formTendaModelStatus<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBeamformingGet<br>formWriteFacMac<br>formexeCommand<br>formgetPptpOnlineClient<br>formsetUsbUnload<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSetRouteStatic<br>fromSysStatusHandle<br>fromSysToolGetUpgrade<br>fromSysToolSetUpgrade<br>fromWizardHandle<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>get_online_ip_info<br>initWifiMacFilter<br>key_clear<br>key_option<br>key_show<br>mDMZGetCfg<br>mNatGetStatic<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websAspRequest<br>websCgiGatherOutput<br>websDefaultHandler<br>websFooter<br>websHeader<br>websLongWrite<br>websMsgEnd<br>websMsgStart<br>websResponse<br>websResponseDownLoadFile<br>websResponseOpCookie<br>websTransfer<br>write_ddos_fence_info<br>write_ipopt_fence_info<br>write_list_data<br>write_list_data_n</details>|
|paramcount|4|4|
|`address`|00430f04|00431104|
|sig|int __stdcall websWrite(int param_1, size_t * param_2, size_t * param_3, undefined4 param_4)|int __stdcall websWrite(int param_1, size_t * param_2, size_t * param_3, undefined4 param_4)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### websWrite Calling Diff


```diff
--- websWrite calling
+++ websWrite calling
@@ -74,0 +75 @@
+formGetSambaConf
@@ -79,0 +81,2 @@
+formGetUsbCfg
+formGetUsbPrint
@@ -96,0 +100 @@
+formSetSambaConf
@@ -97,0 +102 @@
+formSetUsbPrint
@@ -108,0 +114 @@
+formsetUsbUnload
```




<sub>Generated with `ghidriff` version: 0.7.2 on 2025-05-13T16:49:20</sub>