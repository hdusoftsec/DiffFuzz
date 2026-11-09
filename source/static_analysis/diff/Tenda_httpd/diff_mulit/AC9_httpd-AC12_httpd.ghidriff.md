# AC9_httpd-AC12_httpd Diff

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
	* [<EXTERNAL>::usleep](#externalusleep)
	* [<EXTERNAL>::atof](#externalatof)
	* [<EXTERNAL>::opendir](#externalopendir)
* [Added](#added)
* [Modified](#modified)
	* [fromSetWirelessRepeat](#fromsetwirelessrepeat)
	* [formGetRouterStatus](#formgetrouterstatus)
	* [formDefineTendDa](#formdefinetendda)
	* [fromsetApModeCfg](#fromsetapmodecfg)
	* [fromSetSysTime](#fromsetsystime)
	* [setDoublePppoeConfig](#setdoublepppoeconfig)
	* [ate_nvram_set_pin](#ate_nvram_set_pin)
	* [iwpriv_wlan_set](#iwpriv_wlan_set)
	* [ate_Tenda_mfg_check_wpsbutton](#ate_tenda_mfg_check_wpsbutton)
	* [check_param_changed](#check_param_changed)
	* [fromGetSysTime](#fromgetsystime)
	* [setPppoeConfig](#setpppoeconfig)
	* [have_enough_mem](#have_enough_mem)
	* [aspGetModeShow](#aspgetmodeshow)
* [Modified (No Code Changes)](#modified-no-code-changes)
	* [cJSON_CreateObject](#cjson_createobject)
	* [websTransfer](#webstransfer)
	* [cJSON_AddItemToArray](#cjson_additemtoarray)
	* [websFormDefine](#websformdefine)
	* [__ledf2](#__ledf2)
	* [cJSON_CreateArray](#cjson_createarray)
	* [cJSON_Object_2String](#cjson_object_2string)
	* [cJSON_AddItemToObject](#cjson_additemtoobject)
	* [cJSON_Print](#cjson_print)
	* [setWanValue](#setwanvalue)
	* [cJSON_CreateString](#cjson_createstring)
	* [websGetVar](#websgetvar)
	* [cJSON_Delete](#cjson_delete)
	* [websDone](#websdone)

# Visual Chart Diff



```mermaid

flowchart LR

fromSetWirelessRepeat-3-old<--Match 99%-->fromSetWirelessRepeat-3-new
formGetRouterStatus-3-old<--Match 95%-->formGetRouterStatus-3-new
formDefineTendDa-0-old<--Match 98%-->formDefineTendDa-0-new
fromsetApModeCfg-3-old<--Match 84%-->fromsetApModeCfg-3-new
fromSetSysTime-3-old<--Match 67%-->fromSetSysTime-3-new
setDoublePppoeConfig-2-old<--Match 63%-->setDoublePppoeConfig-2-new
ate_nvram_set_pin-2-old<--Match 83%-->ate_nvram_set_pin-2-new
iwpriv_wlan_set-4-old<--Match 97%-->iwpriv_wlan_set-4-new
ate_Tenda_mfg_check_wpsbutton-2-old<--Match 99%-->ate_Tenda_mfg_check_wpsbutton-2-new
check_param_changed-3-old<--Match 98%-->check_param_changed-3-new
fromGetSysTime-3-old<--Match 66%-->fromGetSysTime-3-new
setPppoeConfig-2-old<--Match 96%-->setPppoeConfig-2-new
have_enough_mem-1-old<--Match 97%-->have_enough_mem-1-new
aspGetModeShow-4-old<--Match 96%-->aspGetModeShow-4-new

subgraph AC12_httpd
    fromSetWirelessRepeat-3-new
formGetRouterStatus-3-new
formDefineTendDa-0-new
fromsetApModeCfg-3-new
fromSetSysTime-3-new
setDoublePppoeConfig-2-new
ate_nvram_set_pin-2-new
iwpriv_wlan_set-4-new
ate_Tenda_mfg_check_wpsbutton-2-new
check_param_changed-3-new
fromGetSysTime-3-new
setPppoeConfig-2-new
have_enough_mem-1-new
aspGetModeShow-4-new
    
end

subgraph AC9_httpd
    fromSetWirelessRepeat-3-old
formGetRouterStatus-3-old
formDefineTendDa-0-old
fromsetApModeCfg-3-old
fromSetSysTime-3-old
setDoublePppoeConfig-2-old
ate_nvram_set_pin-2-old
iwpriv_wlan_set-4-old
ate_Tenda_mfg_check_wpsbutton-2-old
check_param_changed-3-old
fromGetSysTime-3-old
setPppoeConfig-2-old
have_enough_mem-1-old
aspGetModeShow-4-old
    subgraph Deleted
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
    EXTERNAL-usleep
    EXTERNAL-atof
    EXTERNAL-opendir
end
end

```


```mermaid
pie showData
    title Function Matches - 99.5444%
"unmatched_funcs_len" : 18
"matched_funcs_len" : 3933
```



```mermaid
pie showData
    title Matched Function Similarity - 99.2372%
"matched_funcs_with_code_changes_len" : 14
"matched_funcs_with_non_code_changes_len" : 16
"matched_funcs_no_changes_len" : 3903
```

# Metadata

## Ghidra Diff Engine

### Command Line

#### Captured Command Line


```
ghidriff --project-location ghidra_projects --project-name ghidriff --symbols-path symbols --threaded --log-level INFO --file-log-level INFO --log-path ghidriff.log --min-func-len 10 --gdt [] --bsim --max-ram-percent 60.0 --max-section-funcs 200 AC9_httpd AC12_httpd
```


#### Verbose Args


<details>

```
--old ['./AC6_httpd'] --new [['./AC9_httpd', './AC12_httpd']] --engine VersionTrackingDiff --output-path ./diff_mulit --summary True --project-location ghidra_projects --project-name ghidriff --symbols-path symbols --threaded True --force-analysis False --force-diff False --no-symbols False --log-level INFO --file-log-level INFO --log-path ghidriff.log --va False --min-func-len 10 --use-calling-counts False --gdt [] --bsim True --bsim-full False --max-ram-percent 60.0 --print-flags False --jvm-args None --side-by-side False --max-section-funcs 200 --md-title None
```


</details>

## Binary Metadata Diff


```diff
--- AC9_httpd Meta
+++ AC12_httpd Meta
@@ -1,178 +1,177 @@
-Program Name: AC9_httpd
+Program Name: AC12_httpd
 Language ID: MIPS:LE:32:default (1.8)
 Compiler ID: default
 Processor: MIPS
 Endian: Little
 Address Size: 32
 Minimum Address: 00400000
 Maximum Address: _elfSectionHeaders::00000757
-# of Bytes: 2148436
+# of Bytes: 2121791
 # of Memory Blocks: 48
-# of Instructions: 257313
-# of Defined Data: 17527
-# of Functions: 1987
-# of Symbols: 19797
-# of Data Types: 2138
-# of Data Type Categories: 205
+# of Instructions: 254274
+# of Defined Data: 17306
+# of Functions: 1964
+# of Symbols: 19595
+# of Data Types: 2113
+# of Data Type Categories: 202
 Analyzed: true
 Created With Ghidra Version: 11.3.2
 DWARF Loaded: true
 Date Created: Thu Apr 24 15:14:11 CST 2025
 ELF File Type: executable
 ELF Original Image Base: 0x400000
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
-ELF Source File [  88]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/usb.c
-ELF Source File [  89]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/behaviormanager_demo.c
-ELF Source File [  90]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/safe_demo.c
-ELF Source File [  91]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/ucloud_v2.c
-ELF Source File [  92]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/alischedule.c
-ELF Source File [  93]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/apclient.c
-ELF Source File [  94]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/iptv.c
-ELF Source File [  95]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/reboot_timer.c
-ELF Source File [  96]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/smart_power_management_cgi.c
-ELF Source File [  97]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/guest_ip_confilct.c
-ELF Source File [  98]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/vpn.c
-ELF Source File [  99]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/wan_err_info.c
-ELF Source File [ 100]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_common.c
-ELF Source File [ 101]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_mac_filter.c
-ELF Source File [ 102]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_advertisement.c
-ELF Source File [ 103]: matrixSsl.c
-ELF Source File [ 104]: sslDecode.c
-ELF Source File [ 105]: sslEncode.c
-ELF Source File [ 106]: sslv3.c
-ELF Source File [ 107]: linux.c
-ELF Source File [ 108]: md5.c
-ELF Source File [ 109]: mpi.c
-ELF Source File [ 110]: sha1.c
-ELF Source File [ 111]: rsaPki.c
-ELF Source File [ 112]: x509.c
-ELF Source File [ 113]: cipherSuite.c
-ELF Source File [ 114]: arc4.c
-ELF Source File [ 115]: base64.c
-ELF Source File [ 116]: des3.c
-ELF Source File [ 117]: rsa.c
-ELF Source File [ 118]: asn1.c
-ELF Source File [ 119]: libgcc2.c
-ELF Source File [ 120]: adddf3.c
-ELF Source File [ 121]: divdf3.c
-ELF Source File [ 122]: gedf2.c
-ELF Source File [ 123]: ledf2.c
-ELF Source File [ 124]: muldf3.c
-ELF Source File [ 125]: subdf3.c
-ELF Source File [ 126]: fixdfsi.c
-ELF Source File [ 127]: floatsidf.c
-ELF Source File [ 128]: floatunsidf.c
-ELF Source File [ 129]: extendsfdf2.c
-ELF Source File [ 130]: 
+ELF Source File [  88]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/behaviormanager_demo.c
+ELF Source File [  89]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/safe_demo.c
+ELF Source File [  90]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/ucloud_v2.c
+ELF Source File [  91]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/alischedule.c
+ELF Source File [  92]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/apclient.c
+ELF Source File [  93]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/iptv.c
+ELF Source File [  94]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/reboot_timer.c
+ELF Source File [  95]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/smart_power_management_cgi.c
+ELF Source File [  96]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/guest_ip_confilct.c
+ELF Source File [  97]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/vpn.c
+ELF Source File [  98]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/wan_err_info.c
+ELF Source File [  99]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_common.c
+ELF Source File [ 100]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_mac_filter.c
+ELF Source File [ 101]: /home/work/workspace/AC6V2.0/prod/httpd/11ac/cgi/cgi_advertisement.c
+ELF Source File [ 102]: matrixSsl.c
+ELF Source File [ 103]: sslDecode.c
+ELF Source File [ 104]: sslEncode.c
+ELF Source File [ 105]: sslv3.c
+ELF Source File [ 106]: linux.c
+ELF Source File [ 107]: md5.c
+ELF Source File [ 108]: mpi.c
+ELF Source File [ 109]: sha1.c
+ELF Source File [ 110]: rsaPki.c
+ELF Source File [ 111]: x509.c
+ELF Source File [ 112]: cipherSuite.c
+ELF Source File [ 113]: arc4.c
+ELF Source File [ 114]: base64.c
+ELF Source File [ 115]: des3.c
+ELF Source File [ 116]: rsa.c
+ELF Source File [ 117]: asn1.c
+ELF Source File [ 118]: libgcc2.c
+ELF Source File [ 119]: adddf3.c
+ELF Source File [ 120]: divdf3.c
+ELF Source File [ 121]: gedf2.c
+ELF Source File [ 122]: ledf2.c
+ELF Source File [ 123]: muldf3.c
+ELF Source File [ 124]: subdf3.c
+ELF Source File [ 125]: fixdfsi.c
+ELF Source File [ 126]: floatsidf.c
+ELF Source File [ 127]: floatunsidf.c
+ELF Source File [ 128]: extendsfdf2.c
+ELF Source File [ 129]: 
 Elf Comment[0]: GCC: (GNU) 3.3.2
 Elf Comment[1]: GCC: (Realtek MSDK-4.4.7 Build 2001) 4.4.7
 Executable Format: Executable and Linking Format (ELF)
-Executable Location: /root/FHFuzz/diff/Tenda_httpd/AC9_httpd
-Executable MD5: 8bcc3eee1768591e050db8ff4eff7da1
-Executable SHA256: 329d918f05c1a76bf41074eba35553b2517f2054c1c10ab8c41ac2e037e12c6f
-FSRL: file:///root/FHFuzz/diff/Tenda_httpd/AC9_httpd?MD5=8bcc3eee1768591e050db8ff4eff7da1
+Executable Location: /root/FHFuzz/diff/Tenda_httpd/AC12_httpd
+Executable MD5: eef92bf72be49feab9e4fff22bbf86cf
+Executable SHA256: 5c6330ab898620f25009d1dc5fa4046e2ca7c3beacf3cdbbf9b12a4e028b5661
+FSRL: file:///root/FHFuzz/diff/Tenda_httpd/AC12_httpd?MD5=eef92bf72be49feab9e4fff22bbf86cf
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
|DWARF.Default Calling Convention||
|DWARF.Ignore Parameter Storage Info|false|
|DWARF.Import Data Types|true|
|DWARF.Import Functions|true|
|DWARF.Import Local Variable Info|true|
|DWARF.Import Source Line Info|true|
|DWARF.Maximum Source Map Entry Length|2000|
|DWARF.Output DWARF DIE Info|false|
|DWARF.Output Source Info|false|
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
|Demangler GNU.Use Standard Text Replacements|true|
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
|MIPS Constant Reference Analyzer.Speculative reference min|1024|
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
|Stack.Create Param Variables|false|
|Stack.useNewFunctionStackAnalysis|true|
|Subroutine References|true|
|Subroutine References.Create Thunks Early|true|
|Variadic Function Signature Override|false|
|Variadic Function Signature Override.Create Analysis Bookmarks|false|

</details>


<details>
<summary>Ghidra AC12_httpd Decompiler Options</summary>


|Decompiler Option|Value|
| :---: | :---: |
|Prototype Evaluation|__stdcall|

</details>


<details>
<summary>Ghidra AC12_httpd Specification extensions Options</summary>


|Specification extensions Option|Value|
| :---: | :---: |
|FormatVersion|0|
|VersionCounter|0|

</details>


<details>
<summary>Ghidra AC12_httpd Analyzers Options</summary>


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
|DWARF.Default Calling Convention||
|DWARF.Ignore Parameter Storage Info|false|
|DWARF.Import Data Types|true|
|DWARF.Import Functions|true|
|DWARF.Import Local Variable Info|true|
|DWARF.Import Source Line Info|true|
|DWARF.Maximum Source Map Entry Length|2000|
|DWARF.Output DWARF DIE Info|false|
|DWARF.Output Source Info|false|
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
|Demangler GNU.Use Standard Text Replacements|true|
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
|MIPS Constant Reference Analyzer.Speculative reference min|1024|
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
|Stack.Create Param Variables|false|
|Stack.useNewFunctionStackAnalysis|true|
|Subroutine References|true|
|Subroutine References.Create Thunks Early|true|
|Variadic Function Signature Override|false|
|Variadic Function Signature Override.Create Analysis Bookmarks|false|

</details>

## Diff Stats



|Stat|Value|
| :---: | :---: |
|added_funcs_len|0|
|deleted_funcs_len|18|
|modified_funcs_len|30|
|added_symbols_len|55|
|deleted_symbols_len|56|
|diff_time|36.63484525680542|
|deleted_strings_len|37|
|added_strings_len|5|
|match_types|Counter({'SymbolsHash': 1671, 'ExternalsName': 279, 'StructuralGraphHash': 12, 'ExactInstructionsFunctionHasher': 4, 'SigCallingCalledHasher': 2, 'StrUniqueFuncRefsHasher': 2})|
|items_to_process|159|
|diff_types|Counter({'address': 30, 'length': 15, 'refcount': 15, 'code': 14, 'calling': 13, 'called': 6})|
|unmatched_funcs_len|18|
|total_funcs_len|3951|
|matched_funcs_len|3933|
|matched_funcs_with_code_changes_len|14|
|matched_funcs_with_non_code_changes_len|16|
|matched_funcs_no_changes_len|3903|
|match_func_similarity_percent|99.2372%|
|func_match_overall_percent|99.5444%|
|first_matches|Counter({'SymbolsHash': 1671, 'StructuralGraphHash': 12, 'ExactInstructionsFunctionHasher': 4, 'SigCallingCalledHasher': 2, 'StrUniqueFuncRefsHasher': 2})|



```mermaid
pie showData
    title All Matches
"SymbolsHash" : 1671
"ExternalsName" : 279
"ExactInstructionsFunctionHasher" : 4
"SigCallingCalledHasher" : 2
"StrUniqueFuncRefsHasher" : 2
"StructuralGraphHash" : 12
```



```mermaid
pie showData
    title First Matches
"SymbolsHash" : 1671
"ExactInstructionsFunctionHasher" : 4
"SigCallingCalledHasher" : 2
"StrUniqueFuncRefsHasher" : 2
"StructuralGraphHash" : 12
```



```mermaid
pie showData
    title Diff Stats
"added_funcs_len" : 0
"deleted_funcs_len" : 18
"modified_funcs_len" : 30
```



```mermaid
pie showData
    title Symbols
"added_symbols_len" : 55
"deleted_symbols_len" : 56
```

## Strings



```mermaid
pie showData
    title Strings
"deleted_strings_len" : 37
"added_strings_len" : 5
```

### Strings Diff


```diff
--- deleted strings
+++ added strings
@@ -1,37 +1,5 @@
-s_%[^:]:%[^*]*%s
-s_%[^;];%[^;];%[^_]
-s_%s_%d:_getWanIfName_return_NULL
-s_*******_unlink_/tmp/smbpasswd_is
-s_/js/macro_config.js
-s_/tmp/UDiskname
-s_/tmp/smbpasswd
-s_/tmp/usb/PrinterName
-s_/tmp/usb/UsbVolumeInfo
-s_10:27:30
-s_Feb
-s_V15.03.06.42
-s_admin
-s_busybox_deluser_%s
-s_cfm_post_netctrl_%d?op=%d,string
-s_dlna.en
-s_insmod_/lib/modules/2.6.36.4brcm
-s_rm_-rf_/tmp/core-*
-s_smbpasswd_-a_%s_-s_<_/tmp/smbpas
-s_usb.ftp.charset
-s_usb.ftp.guest.acess
-s_usb.ftp.guest.pwd
-s_usb.ftp.guest.user
-s_usb.ftp.port
-s_usb.ftp.pwd
-s_usb.ftp.remote.acess
-s_usb.ftp.remote.port
-s_usb.ippd.enable
-s_usb.samba.enable
-s_usb.samba.guest.acess
-s_usb.samba.guest.pwd
-s_usb.samba.guest.user
-s_usb.samba.pwd
-s_usb.samba.user
-s_usbNum
-s_usb_total=%s,usb_usable=%s
-s_{"printerEn":"%d","printerName":
+s_18:06:41
+s_Sep
+s_V15.03.06.23
+s_check
+s_lineup

```


### String References

#### Old



|String|Ref Count|Ref Func|
| :---: | :---: | :---: |
|s_Feb_6_2018_0050e8bc|1|aspTendaGetStatus|
|s_usb.ftp.guest.user_005203f8|1|formSetSambaConf|
|s_{"printerEn":"%d","printerName":_005202b4|1|formGetUsbPrint|
|s_usb_total=%s,usb_usable=%s_005206c8|1|formGetUsbCfg|
|s_usb.ftp.pwd_005203ec|1|formSetSambaConf|
|s_rm_-rf_/tmp/core-*_0050bcd0|1|have_enough_mem|
|s_V15.03.06.42_0050e7f8|1|aspTendaGetStatus|
|s_usb.ftp.remote.acess_00520434|3|formSetSambaConf,formGetSambaConf,formGetUSBStatus|
|s_usb.ftp.guest.acess_00520420|1|formSetSambaConf|
|s_%[^:]:%[^*]*%s_005206b0|1|formGetUsbCfg|
|s_usb.ftp.remote.port_0052044c|2|formSetSambaConf,formGetSambaConf|
|s_usb.samba.enable_00520470|1|formSetSambaConf|
|s_usb.samba.user_0052057c|1|writePasswd|
|s_dlna.en_00520614|1|formGetUSBStatus|
|s_10:27:30_0050a87c|1|get_compile_date_time|
|s_usb.ftp.charset_00520460|2|formSetSambaConf,formGetSambaConf|
|s_/tmp/UDiskname_0051fad8|1|Usb_Up|
|s_/tmp/usb/PrinterName_00520298|1|formGetUsbPrint|
|s_usb.ftp.port_005204a4|1|formGetSambaConf|
|s_insmod_/lib/modules/2.6.36.4brcm_0051fde4|1|fromSetWirelessRepeat|
|s_admin_005202e8|2|writePasswd|
|s_busybox_deluser_%s_0052039c|1|formSetSambaConf|
|s_cfm_post_netctrl_%d?op=%d,string_00520358|2|formSetSambaConf,formsetUsbUnload|
|s_/tmp/smbpasswd_00520540|2|fill_smbpasswd_input_file|
|s_usb.ippd.enable_00520248|3|formGetUsbPrint,formGetUSBStatus,formSetUsbPrint|
|s_%[^;];%[^;];%[^_]_00520680|1|formGetUsbCfg|
|s_usb.samba.guest.user_00520384|3|formSetSambaConf,formGetSambaConf|
|s_/tmp/usb/UsbVolumeInfo_00520668|1|formGetUsbCfg|
|s_usb.samba.guest.pwd_005203c0|2|formSetSambaConf,formGetSambaConf|
|s_/js/macro_config.js_0050a49c|1|R7WebsSecurityHandler|
|s_usb.samba.guest.acess_005203d4|2|formSetSambaConf,formGetSambaConf|
|s_usbNum_00510808|1|formGetRouterStatus|
|s_*******_unlink_/tmp/smbpasswd_is_00520550|1|fill_smbpasswd_input_file|
|s_usb.samba.pwd_005203b0|3|formSetSambaConf,writePasswd,formGetSambaConf|
|s_%s_%d:_getWanIfName_return_NULL_005204e4|1|formGetSambaConf|
|s_smbpasswd_-a_%s_-s_<_/tmp/smbpas_0052058c|1|writePasswd|
|s_usb.ftp.guest.pwd_0052040c|1|formSetSambaConf|

#### New



|String|Ref Count|Ref Func|
| :---: | :---: | :---: |
|s_Sep_6_2017_0050b68c|1|aspTendaGetStatus|
|s_18:06:41_005076bc|1|get_compile_date_time|
|s_V15.03.06.23_0050b5c8|1|aspTendaGetStatus|
|s_check_0050f21c|2||
|s_lineup_0050d5b4|1|formGetRouterStatus|

# Deleted

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
|sig|int get_usb_device_num(void)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- get_usb_device_num
+++ get_usb_device_num
@@ -1,31 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-int get_usb_device_num(void)
-
-{
-  FILE *__stream;
-  int iVar1;
-  char *pcVar2;
-  int num;
-  FILE *fp;
-  char buffer [256];
-  
-  num = 0;
-  memset(buffer,0,0x100);
-  __stream = fopen("/tmp/usb/UsbVolumeInfo","r");
-  if (__stream != (FILE *)0x0) {
-    while ((iVar1 = feof(__stream), iVar1 == 0 &&
-           (pcVar2 = fgets(buffer,0x100,__stream), pcVar2 != (char *)0x0))) {
-      num = num + 1;
-    }
-  }
-  if (__stream != (FILE *)0x0) {
-    fclose(__stream);
-  }
-  if (2 < num) {
-    num = 2;
-  }
-  return num;
-}
-

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
|sig|void Usb_Up(void)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- Usb_Up
+++ Usb_Up
@@ -1,32 +0,0 @@
-
-/* WARNING: Unknown calling convention -- yet parameter storage is locked */
-
-void Usb_Up(void)
-
-{
-  FILE *__stream;
-  int iVar1;
-  FILE *fp;
-  char disk_name [8];
-  
-  disk_name[0] = '\0';
-  disk_name[1] = '\0';
-  disk_name[2] = '\0';
-  disk_name[3] = '\0';
-  disk_name[4] = '\0';
-  disk_name[5] = '\0';
-  disk_name[6] = '\0';
-  disk_name[7] = '\0';
-  __stream = fopen("/tmp/UDiskname","r+");
-  if (__stream != (FILE *)0x0) {
-    while (iVar1 = feof(__stream), iVar1 == 0) {
-      fgets(disk_name,8,__stream);
-      if (disk_name[0] != '\0') {
-        doSystemCmd("cfm post netctrl %d?op=%d,string_info=%s",0x33,1,disk_name);
-      }
-    }
-    fclose(__stream);
-  }
-  return;
-}
-

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
|sig|int check_if_dir_empty(char * dirpath)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- check_if_dir_empty
+++ check_if_dir_empty
@@ -1,29 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-int check_if_dir_empty(char *dirpath)
-
-{
-  DIR *__dirp;
-  int iVar1;
-  dirent *pdVar2;
-  char *in_a0;
-  int found;
-  dirent *dirent;
-  DIR *dir;
-  
-  found = 0;
-  __dirp = opendir(in_a0);
-  if (__dirp != (DIR *)0x0) {
-    do {
-      pdVar2 = readdir(__dirp);
-      if (pdVar2 == (dirent *)0x0) goto LAB_004c7c00;
-      iVar1 = strcmp(pdVar2->d_name,".");
-    } while ((iVar1 == 0) || (iVar1 = strcmp(pdVar2->d_name,".."), iVar1 == 0));
-    found = 1;
-LAB_004c7c00:
-    closedir(__dirp);
-  }
-  return found;
-}
-

```


## formSetUsbPrint

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formSetUsbPrint|
|fullname|formSetUsbPrint|
|refcount|3|
|length|456|
|called|<EXTERNAL>::CommitCfm<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memset<br>websDone<br>websGetVar<br>websWrite|
|calling||
|paramcount|3|
|address|004c7c34|
|sig|void formSetUsbPrint(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formSetUsbPrint
+++ formSetUsbPrint
@@ -1,35 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-/* WARNING: Struct "sym_t": ignoring overlapping field "content" */
-
-void formSetUsbPrint(webs_t wp,char_t *path,char_t *query)
-
-{
-  char_t *__nptr;
-  int iVar1;
-  webs_t in_a0;
-  webs_t in_stack_ffffff58;
-  char_t *in_stack_ffffff5c;
-  char_t *in_stack_ffffff60;
-  char_t *ippenable;
-  char mib_value [64];
-  char buf [64];
-  
-  memset(mib_value,0,0x40);
-  memset(buf,0,0x40);
-  __nptr = websGetVar(in_stack_ffffff58,in_stack_ffffff5c,in_stack_ffffff60);
-  SetValue("usb.ippd.enable",__nptr);
-  iVar1 = atoi(__nptr);
-  if (iVar1 == 1) {
-    doSystemCmd("cfm post netctrl %d?op=%d",0x30,1);
-  }
-  else {
-    doSystemCmd("cfm post netctrl %d?op=%d",0x30,2);
-  }
-  CommitCfm();
-  websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
-  websWrite(in_a0,"{\"errCode\":0}");
-  websDone(in_stack_ffffff58,(int)in_stack_ffffff5c);
-  return;
-}
-

```


## formGetUsbPrint

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetUsbPrint|
|fullname|formGetUsbPrint|
|refcount|3|
|length|548|
|called|<EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::fclose<br><EXTERNAL>::fgets<br><EXTERNAL>::fopen<br><EXTERNAL>::memset<br><EXTERNAL>::strlen<br>websDone<br>websWrite|
|calling||
|paramcount|3|
|address|004c7dfc|
|sig|void formGetUsbPrint(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetUsbPrint
+++ formGetUsbPrint
@@ -1,38 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-void formGetUsbPrint(webs_t wp,char_t *path,char_t *query)
-
-{
-  FILE *__stream;
-  size_t sVar1;
-  char *pcVar2;
-  int iVar3;
-  webs_t in_a0;
-  webs_t in_stack_ffffff18;
-  int in_stack_ffffff1c;
-  FILE *fp;
-  int len;
-  char mib_value [64];
-  char usb_printer_name [128];
-  
-  memset(mib_value,0,0x40);
-  memset(usb_printer_name,0,0x80);
-  __stream = fopen("/tmp/usb/PrinterName","r");
-  if (__stream != (FILE *)0x0) {
-    while (pcVar2 = fgets(usb_printer_name,0x80,__stream), pcVar2 != (char *)0x0) {
-      sVar1 = strlen(usb_printer_name);
-      if (mib_value[sVar1 + 0x3f] == '\n') {
-        mib_value[sVar1 + 0x3f] = '\0';
-      }
-    }
-    fclose(__stream);
-  }
-  GetValue("usb.ippd.enable",mib_value);
-  websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
-  iVar3 = atoi(mib_value);
-  websWrite(in_a0,"{\"printerEn\":\"%d\",\"printerName\":\"%s\"}",iVar3,usb_printer_name);
-  websDone(in_stack_ffffff18,in_stack_ffffff1c);
-  return;
-}
-

```


## formSetSambaConf

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formSetSambaConf|
|fullname|formSetSambaConf|
|refcount|3|
|length|1308|
|called|<EXTERNAL>::CommitCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memset<br><EXTERNAL>::strcmp<br>websDone<br>websGetVar<br>websWrite|
|calling||
|paramcount|3|
|address|004c8020|
|sig|void formSetSambaConf(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formSetSambaConf
+++ formSetSambaConf
@@ -1,75 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-/* WARNING: Struct "sym_t": ignoring overlapping field "content" */
-
-void formSetSambaConf(webs_t wp,char_t *path,char_t *query)
-
-{
-  char_t *pcVar1;
-  char_t *pcVar2;
-  char_t *pcVar3;
-  char_t *__s1;
-  char_t *pcVar4;
-  char_t *pcVar5;
-  char_t *pcVar6;
-  char_t *pcVar7;
-  char_t *pcVar8;
-  int iVar9;
-  webs_t in_a0;
-  webs_t in_stack_ffffff78;
-  char_t *in_stack_ffffff7c;
-  char_t *in_stack_ffffff80;
-  char_t *usbname;
-  char_t *action;
-  char_t *remote_acess_port;
-  char_t *remote_acess;
-  char_t *guest_name;
-  char_t *ftp_charset;
-  char_t *guest_acess;
-  char_t *guest_passwd;
-  char_t *passwd;
-  char mib_value [64];
-  
-  memset(mib_value,0,0x40);
-  pcVar1 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  pcVar2 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  pcVar3 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  __s1 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  pcVar4 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  pcVar5 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  pcVar6 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  pcVar7 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  pcVar8 = websGetVar(in_stack_ffffff78,in_stack_ffffff7c,in_stack_ffffff80);
-  iVar9 = strcmp(__s1,"del");
-  if (iVar9 == 0) {
-    doSystemCmd("cfm post netctrl %d?op=%d,string_info=%s",0x33,3,pcVar4);
-    websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
-    websWrite(in_a0,"{\"errCode\":0}");
-    websDone(in_stack_ffffff78,(int)in_stack_ffffff7c);
-  }
-  else {
-    GetValue("usb.samba.guest.user",mib_value);
-    if (mib_value[0] != '\0') {
-      doSystemCmd("busybox deluser %s",mib_value);
-    }
-    SetValue("usb.samba.pwd",pcVar1);
-    SetValue("usb.samba.guest.user",pcVar6);
-    SetValue("usb.samba.guest.pwd",pcVar5);
-    SetValue("usb.samba.guest.acess",pcVar7);
-    SetValue("usb.ftp.pwd",pcVar1);
-    SetValue("usb.ftp.guest.user",pcVar6);
-    SetValue("usb.ftp.guest.pwd",pcVar5);
-    SetValue("usb.ftp.guest.acess",pcVar7);
-    SetValue("usb.ftp.remote.acess",pcVar2);
-    SetValue("usb.ftp.remote.port",pcVar3);
-    SetValue("usb.ftp.charset",pcVar8);
-    GetValue("usb.samba.enable",mib_value);
-    doSystemCmd("cfm post netctrl %d?op=%d",0x33,5);
-    CommitCfm();
-    websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
-    websWrite(in_a0,"{\"errCode\":0}");
-    websDone(in_stack_ffffff78,(int)in_stack_ffffff7c);
-  }
-  return;
-}
-

```


## formGetSambaConf

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetSambaConf|
|fullname|formGetSambaConf|
|refcount|3|
|length|2468|
|called|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::free<br><EXTERNAL>::getIfIp<br><EXTERNAL>::getLanIfName<br><EXTERNAL>::getWanIfName<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::strcmp<br><EXTERNAL>::tpi_wifi_get_ifname<br>cJSON_AddItemToObject</summary>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Object_2String<br>websDone<br>websWrite</details>|
|calling||
|paramcount|3|
|address|004c853c|
|sig|void formGetSambaConf(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetSambaConf
+++ formGetSambaConf
@@ -1,294 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-void formGetSambaConf(webs_t wp,char_t *path,char_t *query)
-
-{
-  int iVar1;
-  int iVar2;
-  undefined4 uVar3;
-  char *__ptr;
-  webs_t in_a0;
-  webs_t in_stack_fffffd98;
-  char *in_stack_fffffd9c;
-  cJSON *in_stack_fffffda0;
-  int wann;
-  char *pWanName;
-  char *out;
-  cJSON_conflict *root;
-  char lanip [64];
-  char wanip [64];
-  char ftp_remote_acess [16];
-  char passwd [64];
-  char guest_user [64];
-  char guest_passwd [64];
-  char guest_acess [16];
-  char ftp_charset [16];
-  char sys_mode [16];
-  char ftp_port [16];
-  char remote_acess_port [16];
-  char wl24g_work_mode [16];
-  char wl5g_work_mode [16];
-  char conn_type [16];
-  char wifi_chkHz [16];
-  char wl_buf [16];
-  char ifname [64];
-  
-  memset(lanip,0,0x40);
-  memset(wanip,0,0x40);
-  ftp_remote_acess[0] = '\0';
-  ftp_remote_acess[1] = '\0';
-  ftp_remote_acess[2] = '\0';
-  ftp_remote_acess[3] = '\0';
-  ftp_remote_acess[4] = '\0';
-  ftp_remote_acess[5] = '\0';
-  ftp_remote_acess[6] = '\0';
-  ftp_remote_acess[7] = '\0';
-  ftp_remote_acess[8] = '\0';
-  ftp_remote_acess[9] = '\0';
-  ftp_remote_acess[10] = '\0';
-  ftp_remote_acess[0xb] = '\0';
-  ftp_remote_acess[0xc] = '\0';
-  ftp_remote_acess[0xd] = '\0';
-  ftp_remote_acess[0xe] = '\0';
-  ftp_remote_acess[0xf] = '\0';
-  memset(passwd,0,0x40);
-  memset(guest_user,0,0x40);
-  memset(guest_passwd,0,0x40);
-  guest_acess[0] = '\0';
-  guest_acess[1] = '\0';
-  guest_acess[2] = '\0';
-  guest_acess[3] = '\0';
-  guest_acess[4] = '\0';
-  guest_acess[5] = '\0';
-  guest_acess[6] = '\0';
-  guest_acess[7] = '\0';
-  guest_acess[8] = '\0';
-  guest_acess[9] = '\0';
-  guest_acess[10] = '\0';
-  guest_acess[0xb] = '\0';
-  guest_acess[0xc] = '\0';
-  guest_acess[0xd] = '\0';
-  guest_acess[0xe] = '\0';
-  guest_acess[0xf] = '\0';
-  ftp_charset[0] = '\0';
-  ftp_charset[1] = '\0';
-  ftp_charset[2] = '\0';
-  ftp_charset[3] = '\0';
-  ftp_charset[4] = '\0';
-  ftp_charset[5] = '\0';
-  ftp_charset[6] = '\0';
-  ftp_charset[7] = '\0';
-  ftp_charset[8] = '\0';
-  ftp_charset[9] = '\0';
-  ftp_charset[10] = '\0';
-  ftp_charset[0xb] = '\0';
-  ftp_charset[0xc] = '\0';
-  ftp_charset[0xd] = '\0';
-  ftp_charset[0xe] = '\0';
-  ftp_charset[0xf] = '\0';
-  sys_mode[0] = '\0';
-  sys_mode[1] = '\0';
-  sys_mode[2] = '\0';
-  sys_mode[3] = '\0';
-  sys_mode[4] = '\0';
-  sys_mode[5] = '\0';
-  sys_mode[6] = '\0';
-  sys_mode[7] = '\0';
-  sys_mode[8] = '\0';
-  sys_mode[9] = '\0';
-  sys_mode[10] = '\0';
-  sys_mode[0xb] = '\0';
-  sys_mode[0xc] = '\0';
-  sys_mode[0xd] = '\0';
-  sys_mode[0xe] = '\0';
-  sys_mode[0xf] = '\0';
-  ftp_port[0] = '\0';
-  ftp_port[1] = '\0';
-  ftp_port[2] = '\0';
-  ftp_port[3] = '\0';
-  ftp_port[4] = '\0';
-  ftp_port[5] = '\0';
-  ftp_port[6] = '\0';
-  ftp_port[7] = '\0';
-  ftp_port[8] = '\0';
-  ftp_port[9] = '\0';
-  ftp_port[10] = '\0';
-  ftp_port[0xb] = '\0';
-  ftp_port[0xc] = '\0';
-  ftp_port[0xd] = '\0';
-  ftp_port[0xe] = '\0';
-  ftp_port[0xf] = '\0';
-  remote_acess_port[0] = '\0';
-  remote_acess_port[1] = '\0';
-  remote_acess_port[2] = '\0';
-  remote_acess_port[3] = '\0';
-  remote_acess_port[4] = '\0';
-  remote_acess_port[5] = '\0';
-  remote_acess_port[6] = '\0';
-  remote_acess_port[7] = '\0';
-  remote_acess_port[8] = '\0';
-  remote_acess_port[9] = '\0';
-  remote_acess_port[10] = '\0';
-  remote_acess_port[0xb] = '\0';
-  remote_acess_port[0xc] = '\0';
-  remote_acess_port[0xd] = '\0';
-  remote_acess_port[0xe] = '\0';
-  remote_acess_port[0xf] = '\0';
-  wl24g_work_mode[0] = '\0';
-  wl24g_work_mode[1] = '\0';
-  wl24g_work_mode[2] = '\0';
-  wl24g_work_mode[3] = '\0';
-  wl24g_work_mode[4] = '\0';
-  wl24g_work_mode[5] = '\0';
-  wl24g_work_mode[6] = '\0';
-  wl24g_work_mode[7] = '\0';
-  wl24g_work_mode[8] = '\0';
-  wl24g_work_mode[9] = '\0';
-  wl24g_work_mode[10] = '\0';
-  wl24g_work_mode[0xb] = '\0';
-  wl24g_work_mode[0xc] = '\0';
-  wl24g_work_mode[0xd] = '\0';
-  wl24g_work_mode[0xe] = '\0';
-  wl24g_work_mode[0xf] = '\0';
-  wl5g_work_mode[0] = '\0';
-  wl5g_work_mode[1] = '\0';
-  wl5g_work_mode[2] = '\0';
-  wl5g_work_mode[3] = '\0';
-  wl5g_work_mode[4] = '\0';
-  wl5g_work_mode[5] = '\0';
-  wl5g_work_mode[6] = '\0';
-  wl5g_work_mode[7] = '\0';
-  wl5g_work_mode[8] = '\0';
-  wl5g_work_mode[9] = '\0';
-  wl5g_work_mode[10] = '\0';
-  wl5g_work_mode[0xb] = '\0';
-  wl5g_work_mode[0xc] = '\0';
-  wl5g_work_mode[0xd] = '\0';
-  wl5g_work_mode[0xe] = '\0';
-  wl5g_work_mode[0xf] = '\0';
-  conn_type[0] = '\0';
-  conn_type[1] = '\0';
-  conn_type[2] = '\0';
-  conn_type[3] = '\0';
-  conn_type[4] = '\0';
-  conn_type[5] = '\0';
-  conn_type[6] = '\0';
-  conn_type[7] = '\0';
-  conn_type[8] = '\0';
-  conn_type[9] = '\0';
-  conn_type[10] = '\0';
-  conn_type[0xb] = '\0';
-  conn_type[0xc] = '\0';
-  conn_type[0xd] = '\0';
-  conn_type[0xe] = '\0';
-  conn_type[0xf] = '\0';
-  wifi_chkHz[0] = '\0';
-  wifi_chkHz[1] = '\0';
-  wifi_chkHz[2] = '\0';
-  wifi_chkHz[3] = '\0';
-  wifi_chkHz[4] = '\0';
-  wifi_chkHz[5] = '\0';
-  wifi_chkHz[6] = '\0';
-  wifi_chkHz[7] = '\0';
-  wifi_chkHz[8] = '\0';
-  wifi_chkHz[9] = '\0';
-  wifi_chkHz[10] = '\0';
-  wifi_chkHz[0xb] = '\0';
-  wifi_chkHz[0xc] = '\0';
-  wifi_chkHz[0xd] = '\0';
-  wifi_chkHz[0xe] = '\0';
-  wifi_chkHz[0xf] = '\0';
-  wl_buf[0] = '\0';
-  wl_buf[1] = '\0';
-  wl_buf[2] = '\0';
-  wl_buf[3] = '\0';
-  wl_buf[4] = '\0';
-  wl_buf[5] = '\0';
-  wl_buf[6] = '\0';
-  wl_buf[7] = '\0';
-  wl_buf[8] = '\0';
-  wl_buf[9] = '\0';
-  wl_buf[10] = '\0';
-  wl_buf[0xb] = '\0';
-  wl_buf[0xc] = '\0';
-  wl_buf[0xd] = '\0';
-  wl_buf[0xe] = '\0';
-  wl_buf[0xf] = '\0';
-  memset(ifname,0,0x40);
-  GetValue("wan1.connecttype",conn_type);
-  GetValue("sys.mode",sys_mode);
-  GetValue("usb.ftp.port",ftp_port);
-  GetValue("usb.ftp.remote.acess",ftp_remote_acess);
-  GetValue("usb.ftp.remote.port",remote_acess_port);
-  GetValue("usb.ftp.charset",ftp_charset);
-  GetValue("wl2g.public.mode",wl24g_work_mode);
-  GetValue("wl5g.public.mode",wl5g_work_mode);
-  iVar1 = strcmp(wl24g_work_mode,"wisp");
-  if (iVar1 == 0) {
-    tpi_wifi_get_ifname(0x18,4,ifname);
-    getIfIp(ifname,wanip);
-  }
-  else {
-    iVar1 = strcmp(wl5g_work_mode,"wisp");
-    if (iVar1 == 0) {
-      tpi_wifi_get_ifname(5,4,ifname);
-      getIfIp(ifname,wanip);
-    }
-    else {
-      iVar1 = atoi(sys_mode);
-      iVar2 = atoi(conn_type);
-      iVar1 = getWanIfName(1,iVar1,iVar2);
-      if (iVar1 == 0) {
-        printf("%s %d: getWanIfName return NULL\n","formGetSambaConf",0xfd);
-      }
-      else {
-        getIfIp(iVar1,wanip);
-      }
-    }
-  }
-  GetValue("extra_chkHz",wifi_chkHz);
-  iVar1 = atoi(wifi_chkHz);
-  if (iVar1 == 0) {
-    GetValue("wl2g.public.mode",wl_buf);
-  }
-  else {
-    GetValue("wl5g.public.mode",wl_buf);
-  }
-  uVar3 = getLanIfName();
-  getIfIp(uVar3,lanip);
-  cJSON_CreateObject();
-  GetValue("usb.samba.pwd",passwd);
-  GetValue("usb.samba.guest.user",guest_user);
-  GetValue("usb.samba.guest.pwd",guest_passwd);
-  GetValue("usb.samba.guest.acess",guest_acess);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  cJSON_CreateString((char *)in_stack_fffffd98);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffd98,in_stack_fffffd9c,in_stack_fffffda0);
-  __ptr = cJSON_Object_2String((cJSON_conflict *)in_stack_fffffd98);
-  websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
-  websWrite(in_a0,"%s",__ptr);
-  free(__ptr);
-  websDone(in_stack_fffffd98,(int)in_stack_fffffd9c);
-  return;
-}
-

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
|sig|int fill_smbpasswd_input_file(char * passwd)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- fill_smbpasswd_input_file
+++ fill_smbpasswd_input_file
@@ -1,35 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-int fill_smbpasswd_input_file(char *passwd)
-
-{
-  int iVar1;
-  size_t sVar2;
-  char *in_a0;
-  int iret;
-  int fd;
-  
-  iVar1 = unlink("/tmp/smbpasswd");
-  if (iVar1 == -1) {
-    puts("******* unlink /tmp/smbpasswd is fail ");
-  }
-  iVar1 = open("/tmp/smbpasswd",0x312);
-  if ((iVar1 < 1) || (in_a0 == (char *)0x0)) {
-    if (iVar1 == 0) {
-      close(0);
-    }
-    iVar1 = 0;
-  }
-  else {
-    sVar2 = strlen(in_a0);
-    write(iVar1,in_a0,sVar2);
-    write(iVar1,&DAT_00520578,1);
-    sVar2 = strlen(in_a0);
-    write(iVar1,in_a0,sVar2);
-    close(iVar1);
-    iVar1 = 1;
-  }
-  return iVar1;
-}
-

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
|sig|int writePasswd(void)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- writePasswd
+++ writePasswd
@@ -1,36 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-int writePasswd(void)
-
-{
-  size_t __n;
-  char *in_stack_fffffbd0;
-  FILE *fp;
-  char user [256];
-  char pwd [256];
-  char passwdtmp [256];
-  char cmd [256];
-  
-  memset(user,0,0x100);
-  memset(pwd,0,0x100);
-  memset(passwdtmp,0,0x100);
-  memset(cmd,0,0x100);
-  GetValue("usb.samba.user",user);
-  GetValue("usb.samba.pwd",pwd);
-  if (user[0] == '\0') {
-    memcpy(user,"admin",5);
-  }
-  if (pwd[0] == '\0') {
-    memcpy(passwdtmp,"admin",5);
-  }
-  else {
-    __n = strlen(pwd);
-    strncpy(passwdtmp,pwd,__n);
-  }
-  fill_smbpasswd_input_file(in_stack_fffffbd0);
-  sprintf(cmd,"smbpasswd -a %s -s < /tmp/smbpasswd",user);
-  system(cmd);
-  return 0;
-}
-

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
|sig|int SpecChConv(char * ConvCH)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- SpecChConv
+++ SpecChConv
@@ -1,43 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-int SpecChConv(char *ConvCH)
-
-{
-  char *pcVar1;
-  size_t sVar2;
-  char *in_a0;
-  char *q;
-  int iLen;
-  int i;
-  char Swp [1024];
-  char Specialch [100];
-  char DesCh [1024];
-  
-  i = 0;
-  memset(Swp,0,0x400);
-  Specialch[0] = '\'';
-  Specialch[1] = '`';
-  Specialch[2] = '\0';
-  memset(Specialch + 3,0,0x61);
-  memset(DesCh,0,0x400);
-  strcpy(DesCh,in_a0);
-  while( true ) {
-    sVar2 = strlen(in_a0);
-    if (sVar2 <= (uint)i) break;
-    pcVar1 = strchr(Specialch,(int)DesCh[i]);
-    if (pcVar1 == (char *)0x0) {
-      sVar2 = strlen(Swp);
-      Swp[sVar2] = DesCh[i];
-    }
-    else {
-      sVar2 = strlen(Swp);
-      Swp[sVar2] = '\\';
-      Swp[sVar2 + 1] = DesCh[i];
-    }
-    i = i + 1;
-  }
-  strcpy(in_a0,Swp);
-  return 0;
-}
-

```


## formGetUSBStatus

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetUSBStatus|
|fullname|formGetUSBStatus|
|refcount|3|
|length|996|
|called|<EXTERNAL>::GetValue<br><EXTERNAL>::strcmp<br>cJSON_AddItemToObject<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Object_2String<br>check_if_dir_empty<br>websTransfer|
|calling||
|paramcount|3|
|address|004c951c|
|sig|void formGetUSBStatus(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetUSBStatus
+++ formGetUSBStatus
@@ -1,85 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-void formGetUSBStatus(webs_t wp,char_t *path,char_t *query)
-
-{
-  int iVar1;
-  webs_t in_stack_ffffffc0;
-  char *in_stack_ffffffc4;
-  cJSON *in_stack_ffffffc8;
-  cJSON_conflict *root;
-  char *out;
-  char printer_enable [8];
-  char remote_acess [8];
-  char dlna_en [8];
-  
-  printer_enable[0] = '\0';
-  printer_enable[1] = '\0';
-  printer_enable[2] = '\0';
-  printer_enable[3] = '\0';
-  printer_enable[4] = '\0';
-  printer_enable[5] = '\0';
-  printer_enable[6] = '\0';
-  printer_enable[7] = '\0';
-  remote_acess[0] = '\0';
-  remote_acess[1] = '\0';
-  remote_acess[2] = '\0';
-  remote_acess[3] = '\0';
-  remote_acess[4] = '\0';
-  remote_acess[5] = '\0';
-  remote_acess[6] = '\0';
-  remote_acess[7] = '\0';
-  dlna_en[0] = '\0';
-  dlna_en[1] = '\0';
-  dlna_en[2] = '\0';
-  dlna_en[3] = '\0';
-  dlna_en[4] = '\0';
-  dlna_en[5] = '\0';
-  dlna_en[6] = '\0';
-  dlna_en[7] = '\0';
-  cJSON_CreateObject();
-  GetValue("usb.ippd.enable",printer_enable);
-  GetValue("usb.ftp.remote.acess",remote_acess);
-  GetValue("dlna.en",dlna_en);
-  iVar1 = strcmp(printer_enable,"1");
-  if (iVar1 == 0) {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  else {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  iVar1 = strcmp(remote_acess,"1");
-  if (iVar1 == 0) {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  else {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  iVar1 = check_if_dir_empty((char *)in_stack_ffffffc0);
-  if (iVar1 == 0) {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  else {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  iVar1 = strcmp(dlna_en,"1");
-  if (iVar1 == 0) {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  else {
-    cJSON_CreateString((char *)in_stack_ffffffc0);
-    cJSON_AddItemToObject((cJSON *)in_stack_ffffffc0,in_stack_ffffffc4,in_stack_ffffffc8);
-  }
-  cJSON_Object_2String((cJSON_conflict *)in_stack_ffffffc0);
-  websTransfer(in_stack_ffffffc0,in_stack_ffffffc4);
-  return;
-}
-

```


## formsetUsbUnload

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formsetUsbUnload|
|fullname|formsetUsbUnload|
|refcount|3|
|length|248|
|called|<EXTERNAL>::doSystemCmd<br>websDone<br>websGetVar<br>websWrite|
|calling||
|paramcount|3|
|address|004c9900|
|sig|void formsetUsbUnload(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formsetUsbUnload
+++ formsetUsbUnload
@@ -1,22 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-/* WARNING: Struct "sym_t": ignoring overlapping field "content" */
-
-void formsetUsbUnload(webs_t wp,char_t *path,char_t *query)
-
-{
-  char_t *pcVar1;
-  webs_t in_a0;
-  webs_t in_stack_ffffffd8;
-  char_t *in_stack_ffffffdc;
-  char_t *in_stack_ffffffe0;
-  char *usb_name;
-  
-  pcVar1 = websGetVar(in_stack_ffffffd8,in_stack_ffffffdc,in_stack_ffffffe0);
-  doSystemCmd("cfm post netctrl %d?op=%d,string_info=%s",0x33,3,pcVar1);
-  websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
-  websWrite(in_a0,"{\"errCode\":0}");
-  websDone(in_stack_ffffffd8,(int)in_stack_ffffffdc);
-  return;
-}
-

```


## formGetUsbCfg

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|formGetUsbCfg|
|fullname|formGetUsbCfg|
|refcount|3|
|length|1876|
|called|<details><summary>Expand for full list:<br><EXTERNAL>::atof<br><EXTERNAL>::fclose<br><EXTERNAL>::feof<br><EXTERNAL>::fgets<br><EXTERNAL>::fopen<br><EXTERNAL>::free<br><EXTERNAL>::memset<br><EXTERNAL>::perror<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf<br><EXTERNAL>::sscanf</summary><EXTERNAL>::strchr<br>__ledf2<br>cJSON_AddItemToArray<br>cJSON_AddItemToObject<br>cJSON_CreateArray<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>websDone<br>websWrite</details>|
|calling||
|paramcount|3|
|address|004c99f8|
|sig|void formGetUsbCfg(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|False|


```diff
--- formGetUsbCfg
+++ formGetUsbCfg
@@ -1,157 +0,0 @@
-
-/* WARNING: Unknown calling convention */
-
-void formGetUsbCfg(webs_t wp,char_t *path,char_t *query)
-
-{
-  FILE *__stream;
-  code *pcVar1;
-  int iVar2;
-  char *pcVar3;
-  char *pcVar4;
-  webs_t in_a0;
-  webs_t in_stack_fffff570;
-  cJSON *in_stack_fffff574;
-  cJSON *in_stack_fffff578;
-  char *tmp;
-  char *p;
-  char *q;
-  int disk_num;
-  int device_num;
-  FILE *fp;
-  char *out;
-  cJSON_conflict *array1;
-  cJSON_conflict *array;
-  cJSON_conflict *root2;
-  cJSON_conflict *root1;
-  cJSON_conflict *root;
-  char buffer [1024];
-  char usb_device_name [256];
-  char usb_device_id [16];
-  char usb_disk_buf [1024];
-  char usb_disk_name [256];
-  char usb_total [16];
-  char usb_usable [16];
-  
-  device_num = 0;
-  disk_num = 0;
-  memset(buffer,0,0x400);
-  memset(usb_device_name,0,0x100);
-  usb_device_id[0] = '\0';
-  usb_device_id[1] = '\0';
-  usb_device_id[2] = '\0';
-  usb_device_id[3] = '\0';
-  usb_device_id[4] = '\0';
-  usb_device_id[5] = '\0';
-  usb_device_id[6] = '\0';
-  usb_device_id[7] = '\0';
-  usb_device_id[8] = '\0';
-  usb_device_id[9] = '\0';
-  usb_device_id[10] = '\0';
-  usb_device_id[0xb] = '\0';
-  usb_device_id[0xc] = '\0';
-  usb_device_id[0xd] = '\0';
-  usb_device_id[0xe] = '\0';
-  usb_device_id[0xf] = '\0';
-  memset(usb_disk_buf,0,0x400);
-  memset(usb_disk_name,0,0x100);
-  usb_total[0] = '\0';
-  usb_total[1] = '\0';
-  usb_total[2] = '\0';
-  usb_total[3] = '\0';
-  usb_total[4] = '\0';
-  usb_total[5] = '\0';
-  usb_total[6] = '\0';
-  usb_total[7] = '\0';
-  usb_total[8] = '\0';
-  usb_total[9] = '\0';
-  usb_total[10] = '\0';
-  usb_total[0xb] = '\0';
-  usb_total[0xc] = '\0';
-  usb_total[0xd] = '\0';
-  usb_total[0xe] = '\0';
-  usb_total[0xf] = '\0';
-  usb_usable[0] = '\0';
-  usb_usable[1] = '\0';
-  usb_usable[2] = '\0';
-  usb_usable[3] = '\0';
-  usb_usable[4] = '\0';
-  usb_usable[5] = '\0';
-  usb_usable[6] = '\0';
-  usb_usable[7] = '\0';
-  usb_usable[8] = '\0';
-  usb_usable[9] = '\0';
-  usb_usable[10] = '\0';
-  usb_usable[0xb] = '\0';
-  usb_usable[0xc] = '\0';
-  usb_usable[0xd] = '\0';
-  usb_usable[0xe] = '\0';
-  usb_usable[0xf] = '\0';
-  cJSON_CreateObject();
-  cJSON_CreateArray();
-  cJSON_AddItemToObject((cJSON *)in_stack_fffff570,(char *)in_stack_fffff574,in_stack_fffff578);
-  __stream = fopen("/tmp/usb/UsbVolumeInfo","r");
-  if (__stream == (FILE *)0x0) {
-    perror((char *)fopen);
-  }
-  else {
-    for (; ((iVar2 = feof(__stream), iVar2 == 0 &&
-            (pcVar3 = fgets(buffer,0x400,__stream), pcVar3 != (char *)0x0)) && (device_num < 2));
-        device_num = device_num + 1) {
-      sscanf(buffer,"%[^;];%[^;];%[^\n]\n",usb_device_name,usb_device_id,usb_disk_buf);
-      cJSON_CreateObject();
-      cJSON_AddItemToArray((cJSON *)in_stack_fffff570,in_stack_fffff574);
-      cJSON_CreateString((char *)in_stack_fffff570);
-      cJSON_AddItemToObject((cJSON *)in_stack_fffff570,(char *)in_stack_fffff574,in_stack_fffff578);
-      cJSON_CreateString((char *)in_stack_fffff570);
-      cJSON_AddItemToObject((cJSON *)in_stack_fffff570,(char *)in_stack_fffff574,in_stack_fffff578);
-      cJSON_CreateArray();
-      cJSON_AddItemToObject((cJSON *)in_stack_fffff570,(char *)in_stack_fffff574,in_stack_fffff578);
-      tmp = strchr(usb_disk_buf,0x7e);
-      q = usb_disk_buf;
-      while ((tmp != (char *)0x0 && (disk_num < 8))) {
-        *tmp = '\0';
-        pcVar3 = tmp + 1;
-        pcVar4 = usb_disk_name;
-        sscanf(q,"%[^:]:%[^*]*%s",pcVar4,usb_total,usb_usable);
-        tmp = strchr(pcVar3,0x7e);
-        pcVar1 = atof;
-        atof(usb_total);
-        iVar2 = __ledf2((uint)pcVar1,(uint)pcVar4,0x88e368f1,0x3ee4f8b5);
-        q = pcVar3;
-        if (-1 < iVar2) {
-          pcVar1 = atof;
-          atof(usb_usable);
-          sprintf(usb_usable,"%.6f",pcVar1,pcVar4);
-          pcVar1 = atof;
-          atof(usb_total);
-          sprintf(usb_total,"%.6f",pcVar1,pcVar4);
-          printf("usb_total=%s,usb_usable=%s\n",usb_total,usb_usable);
-          cJSON_CreateObject();
-          cJSON_AddItemToArray((cJSON *)in_stack_fffff570,in_stack_fffff574);
-          cJSON_CreateString((char *)in_stack_fffff570);
-          cJSON_AddItemToObject
-                    ((cJSON *)in_stack_fffff570,(char *)in_stack_fffff574,in_stack_fffff578);
-          cJSON_CreateString((char *)in_stack_fffff570);
-          cJSON_AddItemToObject
-                    ((cJSON *)in_stack_fffff570,(char *)in_stack_fffff574,in_stack_fffff578);
-          cJSON_CreateString((char *)in_stack_fffff570);
-          cJSON_AddItemToObject
-                    ((cJSON *)in_stack_fffff570,(char *)in_stack_fffff574,in_stack_fffff578);
-          disk_num = disk_num + 1;
-        }
-      }
-    }
-  }
-  pcVar3 = cJSON_Print((cJSON *)in_stack_fffff570);
-  cJSON_Delete((cJSON *)in_stack_fffff570);
-  websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
-  websWrite(in_a0,"%s",pcVar3);
-  free(pcVar3);
-  websDone(in_stack_fffff570,(int)in_stack_fffff574);
-  if (__stream != (FILE *)0x0) {
-    fclose(__stream);
-  }
-  return;
-}
-

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
## <EXTERNAL>::usleep

### Function Meta



|Key|AC9_httpd|
| :---: | :---: |
|name|usleep|
|fullname|<EXTERNAL>::usleep|
|refcount|1|
|length|0|
|called||
|calling||
|paramcount|1|
|address|EXTERNAL:0000000f|
|sig|int usleep(__useconds_t __useconds)|
|sym_type|Function|
|sym_source|IMPORTED|
|external|True|


*No code available for <EXTERNAL>::usleep*
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
# Added

# Modified


*Modified functions contain code changes*
## fromSetWirelessRepeat

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|1.0|
|i_ratio|0.39|
|m_ratio|0.99|
|b_ratio|0.99|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|fromSetWirelessRepeat|fromSetWirelessRepeat|
|fullname|fromSetWirelessRepeat|fromSetWirelessRepeat|
|refcount|3|3|
|`length`|10028|9920|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::CommitSyncCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memcmp<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp</summary><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::sys_pktc_disable<br><EXTERNAL>::tpi_systool_reboot<br><EXTERNAL>::tpi_wifi_get_ifname<br>Usb_Up<br>set_cn_ssid_ori_encode<br>set_idx_to_mib<br>websGetVar<br>websGetVarWithValidate<br>websTransfer</details>|<details><summary>Expand for full list:<br><EXTERNAL>::CommitSyncCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::doSystemCmd<br><EXTERNAL>::memcmp<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp</summary><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::sys_pktc_disable<br><EXTERNAL>::tpi_systool_reboot<br><EXTERNAL>::tpi_wifi_get_ifname<br>set_cn_ssid_ori_encode<br>set_idx_to_mib<br>websGetVar<br>websGetVarWithValidate<br>websTransfer</details>|
|calling|||
|paramcount|3|3|
|`address`|004c293c|004c1ea0|
|sig|void fromSetWirelessRepeat(webs_t wp, char_t * path, char_t * query)|void fromSetWirelessRepeat(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### fromSetWirelessRepeat Called Diff


```diff
--- fromSetWirelessRepeat called
+++ fromSetWirelessRepeat called
@@ -17 +16,0 @@
-Usb_Up
```


### fromSetWirelessRepeat Diff


```diff
--- fromSetWirelessRepeat
+++ fromSetWirelessRepeat
@@ -1,659 +1,655 @@
 
-/* WARNING: Removing unreachable block (ram,0x004c4f84) */
+/* WARNING: Removing unreachable block (ram,0x004c447c) */
 /* WARNING: Unknown calling convention */
 /* WARNING: Struct "sym_t": ignoring overlapping field "content" */
 
 void fromSetWirelessRepeat(webs_t wp,char_t *path,char_t *query)
 
 {
   char_t *pcVar1;
   char_t *__s2;
   char_t *pcVar2;
   int iVar3;
   char *pcVar4;
   char_t *pcVar5;
   char_t *pcVar6;
   char_t *pcVar7;
   char_t *pcVar8;
   size_t sVar9;
   webs_t in_stack_fffff950;
   char *in_stack_fffff954;
   char_t *in_stack_fffff958;
   WIFI_BUF *in_stack_fffff95c;
   char *wpapsk_key_1;
   char *wpapsk_crypto_1;
   char *wpapsk_type_1;
   char *wepkey4_1;
   char *wepkey3_1;
   char *wepkey2_1;
   char *wepkey1_1;
   char *wepkey_1;
   char *wepauth_1;
   char *security_1;
   char *ssid_1;
   char *wpapsk_key;
   char *wpapsk_crypto;
   char *wpapsk_type;
   char *wepkey4;
   char *wepkey3;
   char *wepkey2;
   char *wepkey1;
   char *wepkey;
   char *wepauth;
   char *security;
   char *ssid;
   int need_reboot;
   cgi_msg errCode;
   int wan_restart;
   int wl5g_restart;
   int wl2g_restart;
   int lan_dhcp;
   WIFI_BUF *wl_buf;
   char *wl_hand;
   char *wl_mode;
   char *wifi_chkHz;
   char *mac;
   char wl24g_work_mode [16];
   char wl5g_work_mode [16];
   char wl_enable [8];
   char mib_value [256];
   char tmp [256];
   char wl24_guest_enable [16];
   char wl5_guest_enable [16];
   char mib_name [16];
   char ifname [16];
   WIFI_BUF wifi_buf_enty;
   char before_wl_mode [16];
   char wifi_timer [16];
   char smart_PowerSave [16];
   char mtu [8];
   char wpapsk_typevalue [16];
   char wpapsk_cryptovalue [16];
   char mtu_1 [8];
   char wpapsk_typevalue_1 [16];
   char wpapsk_cryptovalue_1 [16];
   char tmp_buf [32];
   char work_mode [32];
   
   wl24g_work_mode[0] = '\0';
   wl24g_work_mode[1] = '\0';
   wl24g_work_mode[2] = '\0';
   wl24g_work_mode[3] = '\0';
   wl24g_work_mode[4] = '\0';
   wl24g_work_mode[5] = '\0';
   wl24g_work_mode[6] = '\0';
   wl24g_work_mode[7] = '\0';
   wl24g_work_mode[8] = '\0';
   wl24g_work_mode[9] = '\0';
   wl24g_work_mode[10] = '\0';
   wl24g_work_mode[0xb] = '\0';
   wl24g_work_mode[0xc] = '\0';
   wl24g_work_mode[0xd] = '\0';
   wl24g_work_mode[0xe] = '\0';
   wl24g_work_mode[0xf] = '\0';
   wl5g_work_mode[0] = '\0';
   wl5g_work_mode[1] = '\0';
   wl5g_work_mode[2] = '\0';
   wl5g_work_mode[3] = '\0';
   wl5g_work_mode[4] = '\0';
   wl5g_work_mode[5] = '\0';
   wl5g_work_mode[6] = '\0';
   wl5g_work_mode[7] = '\0';
   wl5g_work_mode[8] = '\0';
   wl5g_work_mode[9] = '\0';
   wl5g_work_mode[10] = '\0';
   wl5g_work_mode[0xb] = '\0';
   wl5g_work_mode[0xc] = '\0';
   wl5g_work_mode[0xd] = '\0';
   wl5g_work_mode[0xe] = '\0';
   wl5g_work_mode[0xf] = '\0';
   memset(mib_value,0,0x100);
   memset(tmp,0,0x100);
   wl24_guest_enable[0] = '\0';
   wl24_guest_enable[1] = '\0';
   wl24_guest_enable[2] = '\0';
   wl24_guest_enable[3] = '\0';
   wl24_guest_enable[4] = '\0';
   wl24_guest_enable[5] = '\0';
   wl24_guest_enable[6] = '\0';
   wl24_guest_enable[7] = '\0';
   wl24_guest_enable[8] = '\0';
   wl24_guest_enable[9] = '\0';
   wl24_guest_enable[10] = '\0';
   wl24_guest_enable[0xb] = '\0';
   wl24_guest_enable[0xc] = '\0';
   wl24_guest_enable[0xd] = '\0';
   wl24_guest_enable[0xe] = '\0';
   wl24_guest_enable[0xf] = '\0';
   wl5_guest_enable[0] = '\0';
   wl5_guest_enable[1] = '\0';
   wl5_guest_enable[2] = '\0';
   wl5_guest_enable[3] = '\0';
   wl5_guest_enable[4] = '\0';
   wl5_guest_enable[5] = '\0';
   wl5_guest_enable[6] = '\0';
   wl5_guest_enable[7] = '\0';
   wl5_guest_enable[8] = '\0';
   wl5_guest_enable[9] = '\0';
   wl5_guest_enable[10] = '\0';
   wl5_guest_enable[0xb] = '\0';
   wl5_guest_enable[0xc] = '\0';
   wl5_guest_enable[0xd] = '\0';
   wl5_guest_enable[0xe] = '\0';
   wl5_guest_enable[0xf] = '\0';
   mib_name[0] = '\0';
   mib_name[1] = '\0';
   mib_name[2] = '\0';
   mib_name[3] = '\0';
   mib_name[4] = '\0';
   mib_name[5] = '\0';
   mib_name[6] = '\0';
   mib_name[7] = '\0';
   mib_name[8] = '\0';
   mib_name[9] = '\0';
   mib_name[10] = '\0';
   mib_name[0xb] = '\0';
   mib_name[0xc] = '\0';
   mib_name[0xd] = '\0';
   mib_name[0xe] = '\0';
   mib_name[0xf] = '\0';
   ifname[0] = '\0';
   ifname[1] = '\0';
   ifname[2] = '\0';
   ifname[3] = '\0';
   ifname[4] = '\0';
   ifname[5] = '\0';
   ifname[6] = '\0';
   ifname[7] = '\0';
   ifname[8] = '\0';
   ifname[9] = '\0';
   ifname[10] = '\0';
   ifname[0xb] = '\0';
   ifname[0xc] = '\0';
   ifname[0xd] = '\0';
   ifname[0xe] = '\0';
   ifname[0xf] = '\0';
   memset(&wifi_buf_enty,0,0x204);
   wifi_buf_enty.max_length = 0x100;
   errCode = CGI_OK;
   pcVar1 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
   wifi_chkHz = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
   __s2 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
   pcVar2 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
   GetValue("wl2g.public.mode",wl24g_work_mode);
   GetValue("wl5g.public.mode",wl5g_work_mode);
   GetValue("wl2g.ssid1.enable",wl24_guest_enable);
   GetValue("wl5g.ssid1.enable",wl5_guest_enable);
   iVar3 = strcmp("ap",__s2);
   if (iVar3 == 0) {
     work_mode[0] = '\0';
     work_mode[1] = '\0';
     work_mode[2] = '\0';
     work_mode[3] = '\0';
     work_mode[4] = '\0';
     work_mode[5] = '\0';
     work_mode[6] = '\0';
     work_mode[7] = '\0';
     work_mode[8] = '\0';
     work_mode[9] = '\0';
     work_mode[10] = '\0';
     work_mode[0xb] = '\0';
     work_mode[0xc] = '\0';
     work_mode[0xd] = '\0';
     work_mode[0xe] = '\0';
     work_mode[0xf] = '\0';
     work_mode[0x10] = '\0';
     work_mode[0x11] = '\0';
     work_mode[0x12] = '\0';
     work_mode[0x13] = '\0';
     work_mode[0x14] = '\0';
     work_mode[0x15] = '\0';
     work_mode[0x16] = '\0';
     work_mode[0x17] = '\0';
     work_mode[0x18] = '\0';
     work_mode[0x19] = '\0';
     work_mode[0x1a] = '\0';
     work_mode[0x1b] = '\0';
     work_mode[0x1c] = '\0';
     work_mode[0x1d] = '\0';
     work_mode[0x1e] = '\0';
     work_mode[0x1f] = '\0';
     SetValue("sys.workmode",work_mode);
     GetValue("wl.bcm11ac",tmp_buf);
     iVar3 = strcmp("0",tmp_buf);
     if (iVar3 == 0) {
       wifi_chkHz = "0";
     }
     else {
       iVar3 = strcmp("1",tmp_buf);
       if (iVar3 == 0) {
         wifi_chkHz = "1";
       }
     }
     iVar3 = strcmp(work_mode,"ap");
     if (iVar3 == 0) {
       SetValue("sys.workmode",&DAT_0);
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
     SetValue("dhcps.en",&DAT_1);
   }
   iVar3 = strcmp(wl24g_work_mode,"ap");
   if (((iVar3 == 0) && (iVar3 = strcmp(wl5g_work_mode,"ap"), iVar3 == 0)) &&
      (iVar3 = strcmp(__s2,"ap"), iVar3 == 0)) {
     errCode = CGI_OK;
     goto LAB_2;
   }
   strcmp(__s2,"apclient");
   before_wl_mode[0] = '\0';
   before_wl_mode[1] = '\0';
   before_wl_mode[2] = '\0';
   before_wl_mode[3] = '\0';
   before_wl_mode[4] = '\0';
   before_wl_mode[5] = '\0';
   before_wl_mode[6] = '\0';
   before_wl_mode[7] = '\0';
   before_wl_mode[8] = '\0';
   before_wl_mode[9] = '\0';
   before_wl_mode[10] = '\0';
   before_wl_mode[0xb] = '\0';
   before_wl_mode[0xc] = '\0';
   before_wl_mode[0xd] = '\0';
   before_wl_mode[0xe] = '\0';
   before_wl_mode[0xf] = '\0';
   iVar3 = strcmp(wl24g_work_mode,"wisp");
   if ((iVar3 == 0) || (iVar3 = strcmp(wl5g_work_mode,"wisp"), iVar3 == 0)) {
     memcpy(before_wl_mode,&DAT_3,5);
   }
   else {
     iVar3 = strcmp(wl24g_work_mode,"apclient");
     if ((iVar3 == 0) || (iVar3 = strcmp(wl5g_work_mode,"apclient"), iVar3 == 0)) {
       memcpy(before_wl_mode,"apclient",9);
     }
     else {
       memcpy(before_wl_mode,&DAT_0,3);
     }
   }
   iVar3 = strcmp(before_wl_mode,__s2);
   need_reboot = (int)(iVar3 != 0);
   iVar3 = atoi(wifi_chkHz);
   if (iVar3 == 0) {
     GetValue("wl5g.public.mode",g_work_mode_str);
     SetValue("extra_chkHz",wifi_chkHz);
     iVar3 = strcmp(__s2,"ap");
     if (iVar3 == 0) {
       SetValue("wl2g.public.mode",&DAT_0);
       SetValue("wl5g.public.mode",&DAT_0);
     }
     else {
       SetValue("wl.guest.dhcps_enable",&DAT_4);
       iVar3 = strcmp(wl24_guest_enable,"1");
       if (iVar3 != 0) {
         SetValue("wl2g.ssid1.enable",&DAT_4);
       }
       iVar3 = strcmp(wl5_guest_enable,"1");
       if (iVar3 != 0) {
         SetValue("wl5g.ssid1.enable",&DAT_4);
       }
       SetValue("wl.bcm11ac",wifi_chkHz);
       SetValue("wl2g.extra.mac",pcVar1);
       SetValue("extra_hand",pcVar2);
       tpi_wifi_get_ifname(0x18,4,ifname);
       SetValue("wl2g.extra.ifname",ifname);
       iVar3 = strcmp(__s2,"wisp");
       if (iVar3 == 0) {
         SetValue("wl.wisp.ifname",ifname);
       }
       iVar3 = strcmp(__s2,"apclient");
       if (iVar3 != 0) {
         strcmp(__s2,"wisp");
       }
       iVar3 = strcmp(g_work_mode_str,"ap");
       if (iVar3 != 0) {
         SetValue("wl5g.public.mode",&DAT_0);
       }
       SetValue("wl2g.public.mode",__s2);
       memset(mib_name,0,0x10);
       sprintf(mib_name,"wan%d_err_check",1);
       SetValue(mib_name,&DAT_4);
       memset(mib_name,0,0x10);
       sprintf(mib_name,"wan%d_isonln",1);
       SetValue(mib_name,&DAT_4);
       memset(mib_name,0,0x10);
       sprintf(mib_name,"wan%d_check",1);
       SetValue(mib_name,&DAT_4);
       pcVar1 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
       set_cn_ssid_ori_encode((char *)in_stack_fffff950,in_stack_fffff954);
       SetValue("wl2g.extra.ssid",pcVar1);
       iVar3 = strcmp(__s2,"wisp");
       if (iVar3 == 0) {
         SetValue("wan1.connecttype",&DAT_4);
         SetValue("wl.wisp.access_mode",&DAT_5);
         GetValue("wan1.dynamicMTU",mtu);
         SetValue("wl.wisp.mtu",mtu);
       }
       pcVar4 = websGetVarWithValidate
                          (in_stack_fffff950,in_stack_fffff954,(VALIDATE_ITEM)in_stack_fffff958);
       if (pcVar4 == (char *)0x0) {
         errCode = CGI_ERROR;
         goto LAB_2;
       }
       SetValue("wl2g.extra.security",pcVar4);
       iVar3 = strcmp(pcVar4,"none");
       if (iVar3 != 0) {
         iVar3 = strcmp(pcVar4,"wep");
         if (iVar3 == 0) {
           pcVar1 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           pcVar2 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           pcVar5 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           pcVar6 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           pcVar7 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           pcVar8 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           if (*pcVar5 == '\0') {
             errCode = CGI_ERROR;
             goto LAB_2;
           }
           SetValue("wl2g.extra.wep_type",pcVar1);
           SetValue("wl2g.extra.wep_key",pcVar2);
           SetValue("wl2g.extra.wep_key1",pcVar5);
           SetValue("wl2g.extra.wep_key2",pcVar6);
           SetValue("wl2g.extra.wep_key3",pcVar7);
           SetValue("wl2g.extra.wep_key4",pcVar8);
         }
         else {
           iVar3 = strcmp(pcVar4,"wpapsk");
           if (iVar3 != 0) {
             errCode = CGI_ERROR;
             goto LAB_2;
           }
           pcVar1 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           pcVar2 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           pcVar5 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
           if ((*pcVar5 == '\0') && (sVar9 = strlen(pcVar5), sVar9 < 8)) {
             errCode = CGI_ERROR;
             goto LAB_2;
           }
           iVar3 = strcmp(pcVar1,"wpa");
           if (iVar3 == 0) {
             memcpy(wpapsk_typevalue,&DAT_6,4);
           }
           else {
             iVar3 = strcmp(pcVar1,"wpa2");
             if (iVar3 == 0) {
               memcpy(wpapsk_typevalue,&DAT_7,5);
             }
             else {
               memcpy(wpapsk_typevalue,"psk psk2",9);
             }
           }
           iVar3 = strcmp(pcVar2,"tkip&aes");
           if (iVar3 == 0) {
             memcpy(wpapsk_cryptovalue,"tkip+aes",9);
           }
           else {
             strcpy(wpapsk_cryptovalue,pcVar2);
           }
           SetValue("wl2g.extra.wpapsk_type",wpapsk_typevalue);
           SetValue("wl2g.extra.wpapsk_crypto",wpapsk_cryptovalue);
           SetValue("wl2g.extra.wpapsk_psk",pcVar5);
         }
       }
     }
   }
   else {
     iVar3 = atoi(wifi_chkHz);
     if (iVar3 == 1) {
       GetValue("wl2g.public.mode",g_work_mode_str);
       SetValue("extra_chkHz",wifi_chkHz);
       iVar3 = strcmp(__s2,"ap");
       if (iVar3 == 0) {
         SetValue("wl2g.public.mode",&DAT_0);
         SetValue("wl5g.public.mode",&DAT_0);
       }
       else {
         SetValue("wl.guest.dhcps_enable",&DAT_4);
         iVar3 = strcmp(wl24_guest_enable,"1");
         if (iVar3 != 0) {
           SetValue("wl2g.ssid1.enable",&DAT_4);
         }
         iVar3 = strcmp(wl5_guest_enable,"1");
         if (iVar3 != 0) {
           SetValue("wl5g.ssid1.enable",&DAT_4);
         }
         SetValue("wl.bcm11ac",wifi_chkHz);
         SetValue("wl5g.extra.mac",pcVar1);
         SetValue("extra_hand",pcVar2);
         tpi_wifi_get_ifname(5,4,ifname);
         SetValue("wl5g.extra.ifname",ifname);
         iVar3 = strcmp(__s2,"wisp");
         if (iVar3 == 0) {
           SetValue("wl.wisp.ifname",ifname);
         }
         iVar3 = strcmp(__s2,"apclient");
         if (iVar3 != 0) {
           strcmp(__s2,"wisp");
         }
         iVar3 = strcmp(g_work_mode_str,"ap");
         if (iVar3 != 0) {
           SetValue("wl2g.public.mode",&DAT_0);
         }
         SetValue("wl5g.public.mode",__s2);
         memset(mib_name,0,0x10);
         sprintf(mib_name,"wan%d_err_check",1);
         SetValue(mib_name,&DAT_4);
         memset(mib_name,0,0x10);
         sprintf(mib_name,"wan%d_isonln",1);
         SetValue(mib_name,&DAT_4);
         memset(mib_name,0,0x10);
         sprintf(mib_name,"wan%d_check",1);
         SetValue(mib_name,&DAT_4);
         pcVar1 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
         set_cn_ssid_ori_encode((char *)in_stack_fffff950,in_stack_fffff954);
         SetValue("wl5g.extra.ssid",pcVar1);
         iVar3 = strcmp(__s2,"wisp");
         if (iVar3 == 0) {
           SetValue("wan1.connecttype",&DAT_4);
           SetValue("wl.wisp.access_mode",&DAT_5);
           GetValue("wan1.dynamicMTU",mtu_1);
           SetValue("wl.wisp.mtu",mtu_1);
         }
         pcVar4 = websGetVarWithValidate
                            (in_stack_fffff950,in_stack_fffff954,(VALIDATE_ITEM)in_stack_fffff958);
         if (pcVar4 == (char *)0x0) {
           errCode = CGI_ERROR;
           goto LAB_2;
         }
         SetValue("wl5g.extra.security",pcVar4);
         iVar3 = strcmp(pcVar4,"none");
         if (iVar3 != 0) {
           iVar3 = strcmp(pcVar4,"wep");
           if (iVar3 == 0) {
             pcVar1 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             pcVar2 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             pcVar5 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             pcVar6 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             pcVar7 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             pcVar8 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             if (*pcVar5 == '\0') {
               errCode = CGI_ERROR;
               goto LAB_2;
             }
             SetValue("wl5g.extra.wep_type",pcVar1);
             SetValue("wl5g.extra.wep_key",pcVar2);
             SetValue("wl5g.extra.wep_key1",pcVar5);
             SetValue("wl5g.extra.wep_key2",pcVar6);
             SetValue("wl5g.extra.wep_key3",pcVar7);
             SetValue("wl5g.extra.wep_key4",pcVar8);
           }
           else {
             iVar3 = strcmp(pcVar4,"wpapsk");
             if (iVar3 != 0) {
               errCode = CGI_ERROR;
               goto LAB_2;
             }
             pcVar1 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             pcVar2 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             pcVar5 = websGetVar(in_stack_fffff950,in_stack_fffff954,in_stack_fffff958);
             if ((*pcVar5 == '\0') && (sVar9 = strlen(pcVar5), sVar9 < 8)) {
               errCode = CGI_ERROR;
               goto LAB_2;
             }
             iVar3 = strcmp(pcVar1,"wpa");
             if (iVar3 == 0) {
               memcpy(wpapsk_typevalue_1,&DAT_6,4);
             }
             else {
               iVar3 = strcmp(pcVar1,"wpa2");
               if (iVar3 == 0) {
                 memcpy(wpapsk_typevalue_1,&DAT_7,5);
               }
               else {
                 memcpy(wpapsk_typevalue_1,"psk psk2",9);
               }
             }
             iVar3 = strcmp(pcVar2,"tkip&aes");
             if (iVar3 == 0) {
               memcpy(wpapsk_cryptovalue_1,"tkip+aes",9);
             }
             else {
               strcpy(wpapsk_cryptovalue_1,pcVar2);
             }
             SetValue("wl5g.extra.wpapsk_type",wpapsk_typevalue_1);
             SetValue("wl5g.extra.wpapsk_crypto",wpapsk_cryptovalue_1);
             SetValue("wl5g.extra.wpapsk_psk",pcVar5);
           }
         }
       }
     }
   }
   GetValue("wl2g.public.mode",mib_value);
   iVar3 = strcmp(mib_value,"ap");
   if (iVar3 != 0) {
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     SetValue("wl.guest.dhcps_enable",&DAT_4);
   }
   GetValue("wl5g.public.mode",mib_value);
   iVar3 = strcmp(mib_value,"ap");
   if (iVar3 != 0) {
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     set_idx_to_mib((char *)in_stack_fffff950,in_stack_fffff954,(int)in_stack_fffff958,
                    in_stack_fffff95c);
     SetValue("wl.guest.dhcps_enable",&DAT_4);
   }
   wifi_timer[0] = '\0';
   wifi_timer[1] = '\0';
   wifi_timer[2] = '\0';
   wifi_timer[3] = '\0';
   wifi_timer[4] = '\0';
   wifi_timer[5] = '\0';
   wifi_timer[6] = '\0';
   wifi_timer[7] = '\0';
   wifi_timer[8] = '\0';
   wifi_timer[9] = '\0';
   wifi_timer[10] = '\0';
   wifi_timer[0xb] = '\0';
   wifi_timer[0xc] = '\0';
   wifi_timer[0xd] = '\0';
   wifi_timer[0xe] = '\0';
   wifi_timer[0xf] = '\0';
   GetValue("sys.sched.wifi.enable",wifi_timer);
   iVar3 = strcmp(wifi_timer,"1");
   if (iVar3 == 0) {
     SetValue("sys.sched.wifi.enable",&DAT_4);
     SetValue("nkgw.wlan.listnum",&DAT_4);
     memset(work_mode,0,0x100);
     sprintf(work_mode,"op=%d",2);
     send_msg_to_netctrl(0x27,work_mode);
   }
   smart_PowerSave[0] = '\0';
   smart_PowerSave[1] = '\0';
   smart_PowerSave[2] = '\0';
   smart_PowerSave[3] = '\0';
   smart_PowerSave[4] = '\0';
   smart_PowerSave[5] = '\0';
   smart_PowerSave[6] = '\0';
   smart_PowerSave[7] = '\0';
   smart_PowerSave[8] = '\0';
   smart_PowerSave[9] = '\0';
   smart_PowerSave[10] = '\0';
   smart_PowerSave[0xb] = '\0';
   smart_PowerSave[0xc] = '\0';
   smart_PowerSave[0xd] = '\0';
   smart_PowerSave[0xe] = '\0';
   smart_PowerSave[0xf] = '\0';
   GetValue("sys.powersleep.enable",smart_PowerSave);
   iVar3 = strcmp(smart_PowerSave,"1");
   if (iVar3 == 0) {
     SetValue("sys.powersleep.enable",&DAT_4);
     doSystemCmd("cfm post netctrl %d",0x27);
-    Usb_Up();
-    doSystemCmd("insmod /lib/modules/2.6.36.4brcmarm/kernel/drivers/usb/host/ohci-hcd.ko");
-    doSystemCmd("insmod /lib/modules/2.6.36.4brcmarm/kernel/drivers/usb/host/ehci-hcd.ko");
-    doSystemCmd("insmod /lib/modules/2.6.36.4brcmarm/kernel/drivers/usb/host/xhci-hcd.ko");
   }
   iVar3 = strcmp(before_wl_mode,"apclient");
   if ((iVar3 == 0) || (iVar3 = strcmp(__s2,"apclient"), iVar3 == 0)) {
     SetValue("dhcps.en",&DAT_1);
   }
   iVar3 = strcmp(__s2,"wisp");
   if (iVar3 == 0) {
     SetValue("wan1.ppoe.double.access",&DAT_4);
   }
   GetValue("wl2g.public.mode",wl24g_work_mode);
   GetValue("wl5g.public.mode",wl5g_work_mode);
   iVar3 = strcmp(wl24g_work_mode,"wisp");
   if ((iVar3 == 0) || (iVar3 = strcmp(wl5g_work_mode,"wisp"), iVar3 == 0)) {
     SetValue("vpn.ser.pptpwanid",&DAT_8);
     SetValue("vpn.cli.pptpwanid",&DAT_8);
     SetValue("vpn.cli.l2tpwanid",&DAT_8);
   }
   else {
     SetValue("vpn.ser.pptpwanid",&DAT_1);
     SetValue("vpn.cli.pptpwanid",&DAT_1);
     SetValue("vpn.cli.l2tpwanid",&DAT_1);
   }
   iVar3 = memcmp(wl24g_work_mode,"apclient",8);
   if ((iVar3 == 0) || (iVar3 = memcmp(wl5g_work_mode,"apclient",8), iVar3 == 0)) {
     sys_pktc_disable(1);
   }
   else {
     sys_pktc_disable(0);
   }
   SetValue("wans.flag",&DAT_1);
   SetValue("wans.location","1 0 0 0 0");
   SetValue("iptv.enable",&DAT_4);
   SetValue("iptv.stb.enable",&DAT_4);
   SetValue("igmp.enable",&DAT_4);
   iVar3 = CommitSyncCfm();
   if (iVar3 == 0) {
     errCode = CGI_ERROR;
   }
 LAB_2:
   doSystemCmd("echo \"0 0\" > /etc/conntime1");
   sprintf(tmp,"{\"errCode\":%d}",errCode);
   websTransfer(in_stack_fffff950,in_stack_fffff954);
   if ((errCode == CGI_OK) && ((need_reboot == 1 || (iVar3 = strcmp(__s2,"ap"), iVar3 != 0)))) {
     tpi_systool_reboot();
   }
   return;
 }
 

```


## formGetRouterStatus

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.99|
|i_ratio|0.67|
|m_ratio|0.99|
|b_ratio|0.95|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|formGetRouterStatus|formGetRouterStatus|
|fullname|formGetRouterStatus|formGetRouterStatus|
|refcount|3|3|
|`length`|6116|5984|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::free<br><EXTERNAL>::getIfIp<br><EXTERNAL>::getLanIfName<br><EXTERNAL>::malloc<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::ntohl<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf</summary><EXTERNAL>::strcat<br><EXTERNAL>::strcmp<br><EXTERNAL>::strlen<br><EXTERNAL>::tpi_get_online_mac_info<br>__floatsidf<br>cJSON_AddItemToObject<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_all_phy_link<br>check_mac_in_blacklist<br>getIfMac<br>get_black_num<br>get_device_info<br>get_usb_device_num<br>get_work_mode<br>is_lan_host<br>strtoupper<br>wanErrGetInfo<br>websDone<br>websTransfer<br>websWrite<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::free<br><EXTERNAL>::getIfIp<br><EXTERNAL>::getLanIfName<br><EXTERNAL>::malloc<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::ntohl<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf</summary><EXTERNAL>::strcat<br><EXTERNAL>::strcmp<br><EXTERNAL>::strlen<br><EXTERNAL>::tpi_get_online_mac_info<br>__floatsidf<br>cJSON_AddItemToObject<br>cJSON_CreateNumber<br>cJSON_CreateObject<br>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>check_all_phy_link<br>check_mac_in_blacklist<br>getIfMac<br>get_black_num<br>get_device_info<br>get_work_mode<br>is_lan_host<br>strtoupper<br>wanErrGetInfo<br>websDone<br>websTransfer<br>websWrite<br>write_online_upgrade_info<br>write_wan_infos</details>|
|calling|||
|paramcount|3|3|
|`address`|0046ce44|0046c9a4|
|sig|void formGetRouterStatus(webs_t wp, char_t * path, char_t * query)|void formGetRouterStatus(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### formGetRouterStatus Called Diff


```diff
--- formGetRouterStatus called
+++ formGetRouterStatus called
@@ -28 +27,0 @@
-get_usb_device_num
```


### formGetRouterStatus Diff


```diff
--- formGetRouterStatus
+++ formGetRouterStatus
@@ -1,559 +1,551 @@
 
 /* WARNING: Unknown calling convention */
 
 void formGetRouterStatus(webs_t wp,char_t *path,char_t *query)
 
 {
   client_mac_info *__ptr;
   uint32_t uVar1;
   int iVar2;
   WANERRINFO WVar3;
   int iVar4;
   uint uVar5;
   undefined4 uVar6;
   size_t sVar7;
   char *__ptr_00;
   webs_t in_a0;
   webs_t in_stack_fffff778;
   device_info *in_stack_fffff77c;
   cJSON *in_stack_fffff780;
   uchar level_4;
   uchar level_3;
   uchar level_2;
   uchar level_1;
   uchar level;
   int host_type;
   int wan_id;
   int lan_phy_status;
   int err_check;
   int blackEn;
   int wan_status;
   int err_code;
   client_mac_info *info_ptr;
   client_mac_info *client_mac_info;
   list_head *pos;
   int j;
   int i;
   int arr_num;
   uint ip_count;
   ulonglong now;
   ulonglong last_time;
   int client_num;
   int black_num;
   char *client_mac_buf;
   int index;
   char *out;
   cJSON *root;
   char mib_name [128];
   char mib_value [1024];
   int list_num;
   int client_mac_count;
   device_info dev_info;
   char ret_buf [32];
   char name_temp [256];
   char err_check_buf [16];
   char phy_status [4];
   char all_phy_status [16];
   char lan_name [16];
   char lan_mac [32];
   char work_mode [16];
   char ipaddr_buf [32];
   uint ip_addr;
   char wl_enable [4];
   char wl_enable_5g [4];
   char wl_ssid [32];
   char wl_sec [16];
   char usb_num [4];
   char wans_flag [4];
   char cgi_debug [16];
   char cgi_debug_1 [16];
   char cgi_debug_2 [16];
   char cgi_debug_3 [16];
   char cgi_debug_4 [16];
   
   memset(mib_name,0,0x80);
   memset(mib_value,0,0x400);
   client_num = 0;
   client_mac_count = 0;
   client_mac_info = (client_mac_info *)0x0;
   ret_buf[0] = '\0';
   ret_buf[1] = '\0';
   ret_buf[2] = '\0';
   ret_buf[3] = '\0';
   ret_buf[4] = '\0';
   ret_buf[5] = '\0';
   ret_buf[6] = '\0';
   ret_buf[7] = '\0';
   ret_buf[8] = '\0';
   ret_buf[9] = '\0';
   ret_buf[10] = '\0';
   ret_buf[0xb] = '\0';
   ret_buf[0xc] = '\0';
   ret_buf[0xd] = '\0';
   ret_buf[0xe] = '\0';
   ret_buf[0xf] = '\0';
   ret_buf[0x10] = '\0';
   ret_buf[0x11] = '\0';
   ret_buf[0x12] = '\0';
   ret_buf[0x13] = '\0';
   ret_buf[0x14] = '\0';
   ret_buf[0x15] = '\0';
   ret_buf[0x16] = '\0';
   ret_buf[0x17] = '\0';
   ret_buf[0x18] = '\0';
   ret_buf[0x19] = '\0';
   ret_buf[0x1a] = '\0';
   ret_buf[0x1b] = '\0';
   ret_buf[0x1c] = '\0';
   ret_buf[0x1d] = '\0';
   ret_buf[0x1e] = '\0';
   ret_buf[0x1f] = '\0';
   memset(name_temp,0,0x100);
   err_check_buf[0] = '\0';
   err_check_buf[1] = '\0';
   err_check_buf[2] = '\0';
   err_check_buf[3] = '\0';
   err_check_buf[4] = '\0';
   err_check_buf[5] = '\0';
   err_check_buf[6] = '\0';
   err_check_buf[7] = '\0';
   err_check_buf[8] = '\0';
   err_check_buf[9] = '\0';
   err_check_buf[10] = '\0';
   err_check_buf[0xb] = '\0';
   err_check_buf[0xc] = '\0';
   err_check_buf[0xd] = '\0';
   err_check_buf[0xe] = '\0';
   err_check_buf[0xf] = '\0';
   phy_status[0] = '\0';
   phy_status[1] = '\0';
   phy_status[2] = '\0';
   phy_status[3] = '\0';
   all_phy_status[0] = '\0';
   all_phy_status[1] = '\0';
   all_phy_status[2] = '\0';
   all_phy_status[3] = '\0';
   all_phy_status[4] = '\0';
   all_phy_status[5] = '\0';
   all_phy_status[6] = '\0';
   all_phy_status[7] = '\0';
   all_phy_status[8] = '\0';
   all_phy_status[9] = '\0';
   all_phy_status[10] = '\0';
   all_phy_status[0xb] = '\0';
   all_phy_status[0xc] = '\0';
   all_phy_status[0xd] = '\0';
   all_phy_status[0xe] = '\0';
   all_phy_status[0xf] = '\0';
   lan_mac[0] = '\0';
   lan_mac[1] = '\0';
   lan_mac[2] = '\0';
   lan_mac[3] = '\0';
   lan_mac[4] = '\0';
   lan_mac[5] = '\0';
   lan_mac[6] = '\0';
   lan_mac[7] = '\0';
   lan_mac[8] = '\0';
   lan_mac[9] = '\0';
   lan_mac[10] = '\0';
   lan_mac[0xb] = '\0';
   lan_mac[0xc] = '\0';
   lan_mac[0xd] = '\0';
   lan_mac[0xe] = '\0';
   lan_mac[0xf] = '\0';
   lan_mac[0x10] = '\0';
   lan_mac[0x11] = '\0';
   lan_mac[0x12] = '\0';
   lan_mac[0x13] = '\0';
   lan_mac[0x14] = '\0';
   lan_mac[0x15] = '\0';
   lan_mac[0x16] = '\0';
   lan_mac[0x17] = '\0';
   lan_mac[0x18] = '\0';
   lan_mac[0x19] = '\0';
   lan_mac[0x1a] = '\0';
   lan_mac[0x1b] = '\0';
   lan_mac[0x1c] = '\0';
   lan_mac[0x1d] = '\0';
   lan_mac[0x1e] = '\0';
   lan_mac[0x1f] = '\0';
   work_mode[0] = '\0';
   work_mode[1] = '\0';
   work_mode[2] = '\0';
   work_mode[3] = '\0';
   work_mode[4] = '\0';
   work_mode[5] = '\0';
   work_mode[6] = '\0';
   work_mode[7] = '\0';
   work_mode[8] = '\0';
   work_mode[9] = '\0';
   work_mode[10] = '\0';
   work_mode[0xb] = '\0';
   work_mode[0xc] = '\0';
   work_mode[0xd] = '\0';
   work_mode[0xe] = '\0';
   work_mode[0xf] = '\0';
   ipaddr_buf[0] = '\0';
   ipaddr_buf[1] = '\0';
   ipaddr_buf[2] = '\0';
   ipaddr_buf[3] = '\0';
   ipaddr_buf[4] = '\0';
   ipaddr_buf[5] = '\0';
   ipaddr_buf[6] = '\0';
   ipaddr_buf[7] = '\0';
   ipaddr_buf[8] = '\0';
   ipaddr_buf[9] = '\0';
   ipaddr_buf[10] = '\0';
   ipaddr_buf[0xb] = '\0';
   ipaddr_buf[0xc] = '\0';
   ipaddr_buf[0xd] = '\0';
   ipaddr_buf[0xe] = '\0';
   ipaddr_buf[0xf] = '\0';
   ipaddr_buf[0x10] = '\0';
   ipaddr_buf[0x11] = '\0';
   ipaddr_buf[0x12] = '\0';
   ipaddr_buf[0x13] = '\0';
   ipaddr_buf[0x14] = '\0';
   ipaddr_buf[0x15] = '\0';
   ipaddr_buf[0x16] = '\0';
   ipaddr_buf[0x17] = '\0';
   ipaddr_buf[0x18] = '\0';
   ipaddr_buf[0x19] = '\0';
   ipaddr_buf[0x1a] = '\0';
   ipaddr_buf[0x1b] = '\0';
   ipaddr_buf[0x1c] = '\0';
   ipaddr_buf[0x1d] = '\0';
   ipaddr_buf[0x1e] = '\0';
   ipaddr_buf[0x1f] = '\0';
   wl_enable[0] = '\0';
   wl_enable[1] = '\0';
   wl_enable[2] = '\0';
   wl_enable[3] = '\0';
   wl_enable_5g[0] = '\0';
   wl_enable_5g[1] = '\0';
   wl_enable_5g[2] = '\0';
   wl_enable_5g[3] = '\0';
   wl_ssid[0] = '\0';
   wl_ssid[1] = '\0';
   wl_ssid[2] = '\0';
   wl_ssid[3] = '\0';
   wl_ssid[4] = '\0';
   wl_ssid[5] = '\0';
   wl_ssid[6] = '\0';
   wl_ssid[7] = '\0';
   wl_ssid[8] = '\0';
   wl_ssid[9] = '\0';
   wl_ssid[10] = '\0';
   wl_ssid[0xb] = '\0';
   wl_ssid[0xc] = '\0';
   wl_ssid[0xd] = '\0';
   wl_ssid[0xe] = '\0';
   wl_ssid[0xf] = '\0';
   wl_ssid[0x10] = '\0';
   wl_ssid[0x11] = '\0';
   wl_ssid[0x12] = '\0';
   wl_ssid[0x13] = '\0';
   wl_ssid[0x14] = '\0';
   wl_ssid[0x15] = '\0';
   wl_ssid[0x16] = '\0';
   wl_ssid[0x17] = '\0';
   wl_ssid[0x18] = '\0';
   wl_ssid[0x19] = '\0';
   wl_ssid[0x1a] = '\0';
   wl_ssid[0x1b] = '\0';
   wl_ssid[0x1c] = '\0';
   wl_ssid[0x1d] = '\0';
   wl_ssid[0x1e] = '\0';
   wl_ssid[0x1f] = '\0';
   wl_sec[0] = '\0';
   wl_sec[1] = '\0';
   wl_sec[2] = '\0';
   wl_sec[3] = '\0';
   wl_sec[4] = '\0';
   wl_sec[5] = '\0';
   wl_sec[6] = '\0';
   wl_sec[7] = '\0';
   wl_sec[8] = '\0';
   wl_sec[9] = '\0';
   wl_sec[10] = '\0';
   wl_sec[0xb] = '\0';
   wl_sec[0xc] = '\0';
   wl_sec[0xd] = '\0';
   wl_sec[0xe] = '\0';
   wl_sec[0xf] = '\0';
-  usb_num[0] = '\0';
-  usb_num[1] = '\0';
-  usb_num[2] = '\0';
-  usb_num[3] = '\0';
   __ptr = (client_mac_info *)malloc(0x5000);
   if (__ptr == (client_mac_info *)0x0) {
     sprintf(ret_buf,"{\"errCode\":%d}",1);
     websTransfer(in_stack_fffff778,in_stack_fffff77c->name);
   }
   else {
     tpi_get_online_mac_info(__ptr,0x5000,&client_mac_count);
     if (0 < client_mac_count) {
       client_mac_info = __ptr;
     }
     get_work_mode((char *)in_stack_fffff778);
     if (client_mac_count != 0) {
       for (i = 0; i < client_mac_count; i = i + 1) {
         uVar1 = ntohl(client_mac_info[i].client_ip);
         sprintf(ipaddr_buf,"%u.%u.%u.%u",uVar1 & 0xff,uVar1 >> 8 & 0xff,uVar1 >> 0x10 & 0xff,
                 uVar1 >> 0x18);
         cgi_debug[0] = '\0';
         cgi_debug[1] = '\0';
         cgi_debug[2] = '\0';
         cgi_debug[3] = '\0';
         cgi_debug[4] = '\0';
         cgi_debug[5] = '\0';
         cgi_debug[6] = '\0';
         cgi_debug[7] = '\0';
         cgi_debug[8] = '\0';
         cgi_debug[9] = '\0';
         cgi_debug[10] = '\0';
         cgi_debug[0xb] = '\0';
         cgi_debug[0xc] = '\0';
         cgi_debug[0xd] = '\0';
         cgi_debug[0xe] = '\0';
         cgi_debug[0xf] = '\0';
         iVar4 = GetValue("cgi_debug",cgi_debug);
         if ((iVar4 != 0) && (iVar4 = strcmp("on",cgi_debug), iVar4 == 0)) {
           printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
                  "formGetRouterStatus",0x8c7,debug_color[1],ipaddr_buf);
         }
         iVar4 = is_lan_host((uint)in_stack_fffff778);
         cgi_debug_1[0] = '\0';
         cgi_debug_1[1] = '\0';
         cgi_debug_1[2] = '\0';
         cgi_debug_1[3] = '\0';
         cgi_debug_1[4] = '\0';
         cgi_debug_1[5] = '\0';
         cgi_debug_1[6] = '\0';
         cgi_debug_1[7] = '\0';
         cgi_debug_1[8] = '\0';
         cgi_debug_1[9] = '\0';
         cgi_debug_1[10] = '\0';
         cgi_debug_1[0xb] = '\0';
         cgi_debug_1[0xc] = '\0';
         cgi_debug_1[0xd] = '\0';
         cgi_debug_1[0xe] = '\0';
         cgi_debug_1[0xf] = '\0';
         iVar2 = GetValue("cgi_debug",cgi_debug_1);
         if ((iVar2 != 0) && (iVar2 = strcmp("on",cgi_debug_1), iVar2 == 0)) {
           printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
                  "formGetRouterStatus",0x8c9,debug_color[1],ipaddr_buf);
         }
         iVar2 = strcmp(work_mode,"ap");
         if (((iVar2 != 0) || (iVar2 = strcmp(in_a0->ipaddr,ipaddr_buf), iVar2 == 0)) ||
            (client_mac_info[i].access_type == '\x02')) {
           cgi_debug_2[0] = '\0';
           cgi_debug_2[1] = '\0';
           cgi_debug_2[2] = '\0';
           cgi_debug_2[3] = '\0';
           cgi_debug_2[4] = '\0';
           cgi_debug_2[5] = '\0';
           cgi_debug_2[6] = '\0';
           cgi_debug_2[7] = '\0';
           cgi_debug_2[8] = '\0';
           cgi_debug_2[9] = '\0';
           cgi_debug_2[10] = '\0';
           cgi_debug_2[0xb] = '\0';
           cgi_debug_2[0xc] = '\0';
           cgi_debug_2[0xd] = '\0';
           cgi_debug_2[0xe] = '\0';
           cgi_debug_2[0xf] = '\0';
           iVar2 = GetValue("cgi_debug",cgi_debug_2);
           if ((iVar2 != 0) && (iVar2 = strcmp("on",cgi_debug_2), iVar2 == 0)) {
             printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
                    "formGetRouterStatus",0x8cf,debug_color[1],ipaddr_buf);
           }
           if ((iVar4 != 1) ||
              (iVar2 = check_mac_in_blacklist((char *)in_stack_fffff778), iVar2 == 0)) {
             cgi_debug_3[0] = '\0';
             cgi_debug_3[1] = '\0';
             cgi_debug_3[2] = '\0';
             cgi_debug_3[3] = '\0';
             cgi_debug_3[4] = '\0';
             cgi_debug_3[5] = '\0';
             cgi_debug_3[6] = '\0';
             cgi_debug_3[7] = '\0';
             cgi_debug_3[8] = '\0';
             cgi_debug_3[9] = '\0';
             cgi_debug_3[10] = '\0';
             cgi_debug_3[0xb] = '\0';
             cgi_debug_3[0xc] = '\0';
             cgi_debug_3[0xd] = '\0';
             cgi_debug_3[0xe] = '\0';
             cgi_debug_3[0xf] = '\0';
             iVar2 = GetValue("cgi_debug",cgi_debug_3);
             if ((iVar2 != 0) && (iVar2 = strcmp("on",cgi_debug_3), iVar2 == 0)) {
               printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
                      "formGetRouterStatus",0x8d6,debug_color[1],ipaddr_buf);
             }
             iVar2 = strcmp(work_mode,"ap");
             if (((iVar2 == 0) || (iVar4 != 2)) || (client_mac_info[i].client_ip == 0)) {
               cgi_debug_4[0] = '\0';
               cgi_debug_4[1] = '\0';
               cgi_debug_4[2] = '\0';
               cgi_debug_4[3] = '\0';
               cgi_debug_4[4] = '\0';
               cgi_debug_4[5] = '\0';
               cgi_debug_4[6] = '\0';
               cgi_debug_4[7] = '\0';
               cgi_debug_4[8] = '\0';
               cgi_debug_4[9] = '\0';
               cgi_debug_4[10] = '\0';
               cgi_debug_4[0xb] = '\0';
               cgi_debug_4[0xc] = '\0';
               cgi_debug_4[0xd] = '\0';
               cgi_debug_4[0xe] = '\0';
               cgi_debug_4[0xf] = '\0';
               iVar4 = GetValue("cgi_debug",cgi_debug_4);
               if ((iVar4 != 0) && (iVar4 = strcmp("on",cgi_debug_4), iVar4 == 0)) {
                 printf("%s[%s:%s:%d] %s___ip is: %s___\n\x1b[0m",debug_color[3],&DAT_0,
                        "formGetRouterStatus",0x8df,debug_color[1],ipaddr_buf);
               }
               client_num = client_num + 1;
             }
           }
         }
       }
     }
     cJSON_CreateObject();
     wans_flag[0] = '\0';
     wans_flag[1] = '\0';
     wans_flag[2] = '\0';
     wans_flag[3] = '\0';
     GetValue("wans.flag",wans_flag);
     atoi(wans_flag);
     WVar3 = wanErrGetInfo((int)in_stack_fffff778);
     GetValue("wl2g.public.enable",wl_enable);
     GetValue("wl5g.public.enable",wl_enable_5g);
     iVar4 = atoi(wl_enable_5g);
     if (iVar4 == 0) {
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     }
     else {
       memset(wl_ssid,0,0x20);
       memset(wl_sec,0,0x10);
       GetValue("wl5g.ssid0.ssid",wl_ssid);
       GetValue("wl5g.ssid0.security",wl_sec);
       iVar4 = strcmp(wl_sec,"none");
       if (iVar4 == 0) {
         memcpy(wl_sec,&DAT_1,2);
       }
       else {
         memcpy(wl_sec,&DAT_2,2);
       }
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     }
     iVar4 = atoi(wl_enable);
     if (iVar4 == 0) {
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     }
     else {
       memset(wl_ssid,0,0x20);
       memset(wl_sec,0,0x10);
       GetValue("wl2g.ssid0.ssid",wl_ssid);
       GetValue("wl2g.ssid0.security",wl_sec);
       iVar4 = strcmp(wl_sec,"none");
       if (iVar4 == 0) {
         memcpy(wl_sec,&DAT_1,2);
       }
       else {
         memcpy(wl_sec,&DAT_2,2);
       }
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     }
     for (i = 0; i < 5; i = i + 1) {
       iVar4 = check_all_phy_link((ulong)in_stack_fffff778);
       if (i == 0) {
         sprintf(phy_status,"%d",iVar4);
 LAB_3:
         strcat(all_phy_status,phy_status);
       }
       else if (i != 1) {
         sprintf(phy_status,"|%d",iVar4);
         goto LAB_3;
       }
     }
     cJSON_CreateString((char *)in_stack_fffff778);
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
-    iVar4 = get_usb_device_num();
-    sprintf(usb_num,"%d",iVar4);
-    cJSON_CreateString((char *)in_stack_fffff778);
-    cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     __floatsidf(client_num);
     cJSON_CreateNumber((double)CONCAT44(in_stack_fffff77c,in_stack_fffff778));
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     uVar5 = get_black_num((int *)in_stack_fffff778);
     __floatsidf(uVar5);
     cJSON_CreateNumber((double)CONCAT44(in_stack_fffff77c,in_stack_fffff778));
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     __floatsidf(0);
     cJSON_CreateNumber((double)CONCAT44(in_stack_fffff77c,in_stack_fffff778));
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     memset(&dev_info,0,0x124);
     get_device_info(in_stack_fffff778,in_stack_fffff77c);
     cJSON_CreateString((char *)in_stack_fffff778);
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     memset(mib_value,0,0x400);
     uVar6 = getLanIfName();
     iVar4 = getIfIp(uVar6,mib_value);
     if (iVar4 < 0) {
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     }
     else {
       cJSON_CreateString((char *)in_stack_fffff778);
       cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     }
     memset(mib_value,0,0x400);
     iVar4 = GetValue("lan.macaddr",mib_value);
     if ((iVar4 == 0) || (sVar7 = strlen(mib_value), sVar7 < 6)) {
       memset(mib_value,0,0x400);
       getLanIfName();
       iVar4 = getIfMac((char *)in_stack_fffff778,in_stack_fffff77c->name);
       if (iVar4 == 0) {
         strtoupper((char *)in_stack_fffff778,in_stack_fffff77c->name);
       }
       else {
         memcpy(lan_mac,"00:00:00:00:00:00",0x12);
       }
     }
     else {
       strtoupper((char *)in_stack_fffff778,in_stack_fffff77c->name);
     }
     cJSON_CreateString((char *)in_stack_fffff778);
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     cJSON_CreateString((char *)in_stack_fffff778);
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     sprintf(err_check_buf,"%d",WVar3);
     cJSON_CreateString((char *)in_stack_fffff778);
     cJSON_AddItemToObject((cJSON *)in_stack_fffff778,in_stack_fffff77c->name,in_stack_fffff780);
     write_wan_infos((cJSON **)in_stack_fffff778);
     write_online_upgrade_info((cJSON_conflict **)in_stack_fffff778,(WANERRINFO)in_stack_fffff77c);
     __ptr_00 = cJSON_Print((cJSON *)in_stack_fffff778);
     cJSON_Delete((cJSON *)in_stack_fffff778);
     websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
     websWrite(in_a0,"%s",__ptr_00);
     free(__ptr_00);
     free(__ptr);
     websDone(in_stack_fffff778,(int)in_stack_fffff77c);
   }
   return;
 }
 

```


## formDefineTendDa

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.98|
|i_ratio|0.19|
|m_ratio|0.98|
|b_ratio|0.98|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|formDefineTendDa|formDefineTendDa|
|fullname|formDefineTendDa|formDefineTendDa|
|refcount|4|4|
|`length`|6136|5912|
|called|formDefineUcloudv2<br>websAspDefine<br>websFormDefine|formDefineUcloudv2<br>websAspDefine<br>websFormDefine|
|calling|initWebs|initWebs|
|paramcount|0|0|
|`address`|0044d990|0044d720|
|sig|void formDefineTendDa(void)|void formDefineTendDa(void)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### formDefineTendDa Diff


```diff
--- formDefineTendDa
+++ formDefineTendDa
@@ -1,204 +1,197 @@
 
 /* WARNING: Unknown calling convention -- yet parameter storage is locked */
 /* WARNING: Enum "e_ret": Some values do not have unique names */
 /* WARNING: Enum "ENUM_VER_TYPE": Some values do not have unique names */
 
 void formDefineTendDa(void)
 
 {
   char_t *in_stack_ffffffe0;
   _func_int_int_webs_t_int_char_t_ptr_ptr *in_stack_ffffffe4;
   
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   formDefineUcloudv2();
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
-  websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
-  websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
-  websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
-  websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
-  websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
-  websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
-  websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websAspDefine(in_stack_ffffffe0,in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   websFormDefine(in_stack_ffffffe0,(_func_void_webs_t_char_t_ptr_char_t_ptr *)in_stack_ffffffe4);
   return;
 }
 

```


## fromsetApModeCfg

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|1.0|
|i_ratio|0.28|
|m_ratio|0.99|
|b_ratio|0.84|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|fromsetApModeCfg|fromsetApModeCfg|
|fullname|fromsetApModeCfg|fromsetApModeCfg|
|refcount|3|3|
|`length`|1452|1416|
|called|<EXTERNAL>::CommitSyncCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::tpi_systool_reboot<br>websGetVar<br>websTransfer|<EXTERNAL>::CommitSyncCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::tpi_systool_reboot<br>websGetVar<br>websTransfer|
|calling|||
|paramcount|3|3|
|`address`|004c2174|004c16fc|
|sig|void fromsetApModeCfg(webs_t wp, char_t * path, char_t * query)|void fromsetApModeCfg(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### fromsetApModeCfg Diff


```diff
--- fromsetApModeCfg
+++ fromsetApModeCfg
@@ -1,107 +1,106 @@
 
 /* WARNING: Unknown calling convention */
 /* WARNING: Struct "sym_t": ignoring overlapping field "content" */
 
 void fromsetApModeCfg(webs_t wp,char_t *path,char_t *query)
 
 {
   char_t *__s1;
   int iVar1;
   webs_t in_stack_fffffdb8;
   char *in_stack_fffffdbc;
   char_t *in_stack_fffffdc0;
   cgi_msg errCode;
   char *workmode;
   char pre_workmode [16];
   char cur_workmode [16];
   char msg_buf [256];
   char tmp [256];
   
   pre_workmode[0] = '\0';
   pre_workmode[1] = '\0';
   pre_workmode[2] = '\0';
   pre_workmode[3] = '\0';
   pre_workmode[4] = '\0';
   pre_workmode[5] = '\0';
   pre_workmode[6] = '\0';
   pre_workmode[7] = '\0';
   pre_workmode[8] = '\0';
   pre_workmode[9] = '\0';
   pre_workmode[10] = '\0';
   pre_workmode[0xb] = '\0';
   pre_workmode[0xc] = '\0';
   pre_workmode[0xd] = '\0';
   pre_workmode[0xe] = '\0';
   pre_workmode[0xf] = '\0';
   cur_workmode[0] = '\0';
   cur_workmode[1] = '\0';
   cur_workmode[2] = '\0';
   cur_workmode[3] = '\0';
   cur_workmode[4] = '\0';
   cur_workmode[5] = '\0';
   cur_workmode[6] = '\0';
   cur_workmode[7] = '\0';
   cur_workmode[8] = '\0';
   cur_workmode[9] = '\0';
   cur_workmode[10] = '\0';
   cur_workmode[0xb] = '\0';
   cur_workmode[0xc] = '\0';
   cur_workmode[0xd] = '\0';
   cur_workmode[0xe] = '\0';
   cur_workmode[0xf] = '\0';
   memset(msg_buf,0,0x100);
   errCode = CGI_ERROR;
   memset(tmp,0,0x100);
   __s1 = websGetVar(in_stack_fffffdb8,in_stack_fffffdbc,in_stack_fffffdc0);
   GetValue("sys.workmode",pre_workmode);
   iVar1 = strcmp(__s1,"true");
   if (iVar1 == 0) {
     memcpy(cur_workmode,&DAT_0,3);
   }
   else {
     iVar1 = strcmp(__s1,"false");
     if (iVar1 == 0) {
       memcpy(cur_workmode,"router",7);
     }
   }
   iVar1 = strcmp(pre_workmode,cur_workmode);
   if (iVar1 != 0) {
     iVar1 = strcmp(__s1,"true");
     if (iVar1 == 0) {
       SetValue("wans.location","0 0 0 0 0");
       SetValue("sys.workmode",&DAT_0);
       SetValue("wl2g.public.mode",&DAT_0);
       SetValue("wl5g.public.mode",&DAT_0);
-      SetValue("dhcps.en",&DAT_1);
       SetValue("wans.flag",&DAT_1);
       SetValue("iptv.enable",&DAT_2);
       SetValue("iptv.stb.enable",&DAT_2);
       SetValue("igmp.enable",&DAT_2);
       SetValue("wl.guest.dhcps_enable",&DAT_2);
       SetValue("wl5g.ssid1.enable",&DAT_2);
       SetValue("wl2g.ssid1.enable",&DAT_2);
       SetValue("wl2g.ssid1.guest_enable",&DAT_2);
       SetValue("wl5g.ssid1.guest_enable",&DAT_2);
     }
     else {
       iVar1 = strcmp(__s1,"false");
       if (iVar1 == 0) {
         SetValue("wans.location","1 0 0 0 0");
         SetValue("sys.workmode","router");
         SetValue("dhcps.en",&DAT_1);
         SetValue("vpn.ser.pptpwanid",&DAT_1);
         SetValue("vpn.cli.pptpwanid",&DAT_1);
         SetValue("vpn.cli.l2tpwanid",&DAT_1);
       }
     }
     iVar1 = CommitSyncCfm();
     errCode = (cgi_msg)(iVar1 == 0);
     if (errCode == CGI_OK) {
       tpi_systool_reboot();
     }
   }
   sprintf(tmp,"{\"errCode\":%d}",errCode);
   websTransfer(in_stack_fffffdb8,in_stack_fffffdbc);
   return;
 }
 

```


## fromSetSysTime

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.77|
|i_ratio|0.22|
|m_ratio|0.92|
|b_ratio|0.67|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|fromSetSysTime|fromSetSysTime|
|fullname|fromSetSysTime|fromSetSysTime|
|refcount|3|3|
|`length`|2120|1820|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::CommitCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::mktime<br><EXTERNAL>::puts<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::settimeofday<br><EXTERNAL>::sprintf</summary><EXTERNAL>::sscanf<br><EXTERNAL>::strchr<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br>websGetVar<br>websTransfer</details>|<details><summary>Expand for full list:<br><EXTERNAL>::CommitCfm<br><EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::memset<br><EXTERNAL>::mktime<br><EXTERNAL>::puts<br><EXTERNAL>::send_msg_to_netctrl<br><EXTERNAL>::settimeofday<br><EXTERNAL>::sprintf<br><EXTERNAL>::sscanf</summary><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br>websGetVar<br>websTransfer</details>|
|calling|||
|paramcount|3|3|
|`address`|004a8564|004a7e24|
|sig|void fromSetSysTime(webs_t wp, char_t * path, char_t * query)|void fromSetSysTime(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### fromSetSysTime Called Diff


```diff
--- fromSetSysTime called
+++ fromSetSysTime called
@@ -5 +4,0 @@
-<EXTERNAL>::memcpy
@@ -13 +11,0 @@
-<EXTERNAL>::strchr
```


### fromSetSysTime Diff


```diff
--- fromSetSysTime
+++ fromSetSysTime
@@ -1,202 +1,157 @@
 
 /* WARNING: Unknown calling convention */
 /* WARNING: Struct "sym_t": ignoring overlapping field "content" */
 
 void fromSetSysTime(webs_t wp,char_t *path,char_t *query)
 
 {
   char_t *pcVar1;
   int iVar2;
   char_t *__nptr;
   char_t *__src;
-  char *pcVar3;
-  time_t tVar4;
-  webs_t in_stack_fffffcd8;
-  char *in_stack_fffffcdc;
-  char_t *in_stack_fffffce0;
+  time_t tVar3;
+  webs_t in_stack_fffffd00;
+  char *in_stack_fffffd04;
+  char_t *in_stack_fffffd08;
   time_t timep;
   char_t *tmpstr;
-  char *p;
   char_t *timentpserver;
   char_t *timeper;
   char_t *timezone;
   cgi_msg errCode;
   char_t *mode;
   char tmp [256];
   char par [16];
   TPI_SNTP_CFG cfg;
-  char_t timezone_buf [16];
-  char_t timezone_min_buf [16];
   char timeen [8];
   char par_1 [16];
   char year [10];
   char month [10];
   char day [10];
   char hour [10];
   char min [10];
   char sec [10];
   timeval tv;
   tm tm_t;
   
   errCode = CGI_OK;
   memset(tmp,0,0x100);
   par[0] = '\0';
   par[1] = '\0';
   par[2] = '\0';
   par[3] = '\0';
   par[4] = '\0';
   par[5] = '\0';
   par[6] = '\0';
   par[7] = '\0';
   par[8] = '\0';
   par[9] = '\0';
   par[10] = '\0';
   par[0xb] = '\0';
   par[0xc] = '\0';
   par[0xd] = '\0';
   par[0xe] = '\0';
   par[0xf] = '\0';
   memset(&cfg,0,0x110);
-  pcVar1 = websGetVar(in_stack_fffffcd8,in_stack_fffffcdc,in_stack_fffffce0);
+  pcVar1 = websGetVar(in_stack_fffffd00,in_stack_fffffd04,in_stack_fffffd08);
   iVar2 = strcmp(pcVar1,"sync");
   if (iVar2 == 0) {
-    timezone_buf[0] = '0';
-    timezone_buf[1] = '\0';
-    timezone_buf[2] = '\0';
-    timezone_buf[3] = '\0';
-    timezone_buf[4] = '\0';
-    timezone_buf[5] = '\0';
-    timezone_buf[6] = '\0';
-    timezone_buf[7] = '\0';
-    timezone_buf[8] = '\0';
-    timezone_buf[9] = '\0';
-    timezone_buf[10] = '\0';
-    timezone_buf[0xb] = '\0';
-    timezone_buf[0xc] = '\0';
-    timezone_buf[0xd] = '\0';
-    timezone_buf[0xe] = '\0';
-    timezone_buf[0xf] = '\0';
-    timezone_min_buf[0] = '0';
-    timezone_min_buf[1] = '\0';
-    timezone_min_buf[2] = '\0';
-    timezone_min_buf[3] = '\0';
-    timezone_min_buf[4] = '\0';
-    timezone_min_buf[5] = '\0';
-    timezone_min_buf[6] = '\0';
-    timezone_min_buf[7] = '\0';
-    timezone_min_buf[8] = '\0';
-    timezone_min_buf[9] = '\0';
-    timezone_min_buf[10] = '\0';
-    timezone_min_buf[0xb] = '\0';
-    timezone_min_buf[0xc] = '\0';
-    timezone_min_buf[0xd] = '\0';
-    timezone_min_buf[0xe] = '\0';
-    timezone_min_buf[0xf] = '\0';
     timeen[0] = '\0';
     timeen[1] = '\0';
     timeen[2] = '\0';
     timeen[3] = '\0';
     timeen[4] = '\0';
     timeen[5] = '\0';
     timeen[6] = '\0';
     timeen[7] = '\0';
     par_1[0] = '\0';
     par_1[1] = '\0';
     par_1[2] = '\0';
     par_1[3] = '\0';
     par_1[4] = '\0';
     par_1[5] = '\0';
     par_1[6] = '\0';
     par_1[7] = '\0';
     par_1[8] = '\0';
     par_1[9] = '\0';
     par_1[10] = '\0';
     par_1[0xb] = '\0';
     par_1[0xc] = '\0';
     par_1[0xd] = '\0';
     par_1[0xe] = '\0';
     par_1[0xf] = '\0';
-    pcVar1 = websGetVar(in_stack_fffffcd8,in_stack_fffffcdc,in_stack_fffffce0);
-    __nptr = websGetVar(in_stack_fffffcd8,in_stack_fffffcdc,in_stack_fffffce0);
-    __src = websGetVar(in_stack_fffffcd8,in_stack_fffffcdc,in_stack_fffffce0);
-    pcVar3 = strchr(pcVar1,0x3a);
-    if (pcVar3 == (char *)0x0) {
-      strcpy(timezone_buf,pcVar1);
-      memcpy(timezone_min_buf,&DAT_0,2);
-    }
-    else {
-      sscanf(pcVar1,"%[^:]:%s",timezone_buf,timezone_min_buf);
-    }
-    SetValue("sys.timesyn",&DAT_1);
-    SetValue("sys.timemode",&DAT_2);
-    SetValue("sys.timezone",timezone_buf);
-    SetValue("sys.timenextzone",timezone_min_buf);
+    pcVar1 = websGetVar(in_stack_fffffd00,in_stack_fffffd04,in_stack_fffffd08);
+    __nptr = websGetVar(in_stack_fffffd00,in_stack_fffffd04,in_stack_fffffd08);
+    __src = websGetVar(in_stack_fffffd00,in_stack_fffffd04,in_stack_fffffd08);
+    SetValue("sys.timesyn",&DAT_0);
+    SetValue("sys.timemode",&DAT_1);
+    SetValue("sys.timezone",pcVar1);
+    SetValue("sys.timenextzone",&DAT_2);
     SetValue("sys.timefixper",__nptr);
     SetValue("sys.timentpserver",__src);
     iVar2 = CommitCfm();
     if (iVar2 == 0) {
       errCode = CGI_ERROR;
     }
     else {
       GetValue("sys.timesyn",timeen);
       iVar2 = atoi(timeen);
       if (iVar2 == 1) {
         cfg.sntp_en = atoi(timeen);
         cfg.time_zone = atoi(pcVar1);
-        cfg.time_next_zone = atoi(timezone_min_buf);
         cfg.check_time = atoi(__nptr);
         strcpy(cfg.sntp_server,__src);
         sprintf(par_1,"op=%d",3);
         send_msg_to_netctrl(0x18,par_1);
       }
       else {
         sprintf(par_1,"op=%d",2);
         send_msg_to_netctrl(0x18,par_1);
       }
     }
   }
   else {
     iVar2 = strcmp(pcVar1,"manual");
     if (iVar2 == 0) {
-      pcVar1 = websGetVar(in_stack_fffffcd8,in_stack_fffffcdc,in_stack_fffffce0);
+      pcVar1 = websGetVar(in_stack_fffffd00,in_stack_fffffd04,in_stack_fffffd08);
       sscanf(pcVar1,"%[^-]-%[^-]-%[^ ] %[^:]:%[^:]:%s",year,month,day,hour,min,sec);
       iVar2 = atoi(year);
       tm_t.tm_year = iVar2 + -0x76c;
       iVar2 = atoi(month);
       tm_t.tm_mon = iVar2 + -1;
       tm_t.tm_mday = atoi(day);
       tm_t.tm_hour = atoi(hour);
       tm_t.tm_min = atoi(min);
       tm_t.tm_sec = atoi(sec);
-      tVar4 = mktime((tm *)&tm_t);
-      if (tVar4 < 0xb) {
+      tVar3 = mktime((tm *)&tm_t);
+      if (tVar3 < 0xb) {
         errCode = CGI_ERROR;
       }
       else {
         tv.tv_usec = 0;
-        tv.tv_sec = tVar4;
+        tv.tv_sec = tVar3;
         iVar2 = settimeofday((timeval *)&tv,(timezone *)0x0);
         if (iVar2 < 0) {
           puts("Set   system   datatime   error!");
           errCode = CGI_ERROR;
         }
         else {
-          SetValue("sys.timesyn",&DAT_0);
+          SetValue("sys.timesyn",&DAT_2);
           SetValue("sys.timemode",&DAT_3);
           iVar2 = CommitCfm();
           if (iVar2 == 0) {
             errCode = CGI_ERROR;
           }
           else {
             sprintf(par,"op=%d",2);
             send_msg_to_netctrl(0x18,par);
           }
         }
       }
     }
   }
   sprintf(tmp,"{\"errCode\":%d}",errCode);
-  websTransfer(in_stack_fffffcd8,in_stack_fffffcdc);
+  websTransfer(in_stack_fffffd00,in_stack_fffffd04);
   return;
 }
 

```


## setDoublePppoeConfig

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.31|
|i_ratio|0.25|
|m_ratio|0.88|
|b_ratio|0.63|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|setDoublePppoeConfig|setDoublePppoeConfig|
|fullname|setDoublePppoeConfig|setDoublePppoeConfig|
|refcount|5|5|
|`length`|2092|1652|
|`called`|<EXTERNAL>::GetValue<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strlen<br><EXTERNAL>::strncmp<br>guest_ip_check<br>setWanValue<br>websGetVar|<EXTERNAL>::memset<br><EXTERNAL>::strcmp<br><EXTERNAL>::strlen<br>guest_ip_check<br>setWanValue<br>websGetVar|
|calling|formWanInfoSet<br>form_fast_setting_internet_set|formWanInfoSet<br>form_fast_setting_internet_set|
|paramcount|2|2|
|`address`|00484540|00483fd8|
|sig|void setDoublePppoeConfig(webs_t wp, int wan_id)|void setDoublePppoeConfig(webs_t wp, int wan_id)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### setDoublePppoeConfig Called Diff


```diff
--- setDoublePppoeConfig called
+++ setDoublePppoeConfig called
@@ -1 +0,0 @@
-<EXTERNAL>::GetValue
@@ -3 +1,0 @@
-<EXTERNAL>::sprintf
@@ -6 +3,0 @@
-<EXTERNAL>::strncmp
```


### setDoublePppoeConfig Diff


```diff
--- setDoublePppoeConfig
+++ setDoublePppoeConfig
@@ -1,94 +1,77 @@
 
 /* WARNING: Unknown calling convention */
 /* WARNING: Struct "sym_t": ignoring overlapping field "content" */
 
 void setDoublePppoeConfig(webs_t wp,int wan_id)
 
 {
-  char_t *__s2;
-  char_t *__s2_00;
   char_t *__s1;
   char_t *__s;
   char_t *__s_00;
-  int iVar1;
-  size_t sVar2;
-  undefined4 in_a1;
-  webs_t in_stack_fffffcb8;
-  char *in_stack_fffffcbc;
-  char *in_stack_fffffcc0;
+  size_t sVar1;
+  int iVar2;
+  webs_t in_stack_fffffeb8;
+  char *in_stack_fffffebc;
+  char *in_stack_fffffec0;
   char_t *wan_dns_auto;
   char_t *wan_dns2;
   char_t *wan_dns1;
   char_t *wan_gw;
   char_t *wan_mask;
   char_t *wan_ip;
   char_t *pppoe_pwd;
   char_t *pppoe_user;
   char_t *pppoe_mod;
   char_t *pppoe_server;
   char_t mib_name [256];
-  char_t pppoe_name [256];
-  char_t pppoe_passwd [256];
   
   memset(mib_name,0,0x100);
-  memset(pppoe_name,0,0x100);
-  memset(pppoe_passwd,0,0x100);
-  __s2 = websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  __s2_00 = websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  __s1 = websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  __s = websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  __s_00 = websGetVar(in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  memset(mib_name,0,0x100);
-  sprintf(mib_name,"wan%d.ppoe.userid",in_a1);
-  GetValue(mib_name,pppoe_name);
-  memset(mib_name,0,0x100);
-  sprintf(mib_name,"wan%d.ppoe.pwd",in_a1);
-  GetValue(mib_name,pppoe_passwd);
-  iVar1 = strncmp(pppoe_name,__s2,0x100);
-  if ((iVar1 != 0) || (iVar1 = strncmp(pppoe_passwd,__s2_00,0x100), iVar1 != 0)) {
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
+  websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  __s1 = websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  __s = websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  __s_00 = websGetVar(in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  sVar1 = strlen(__s);
+  if (sVar1 < 7) {
+    sVar1 = strlen(__s_00);
+    if (sVar1 < 7) goto LAB_0;
   }
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  sVar2 = strlen(__s);
-  if (sVar2 < 7) {
-    sVar2 = strlen(__s_00);
-    if (sVar2 < 7) goto LAB_0;
-  }
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-  setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+  setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
 LAB_0:
-  iVar1 = strcmp(__s1,"0");
-  if (iVar1 == 0) {
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    guest_ip_check((char *)in_stack_fffffcb8,in_stack_fffffcbc,(int)in_stack_fffffcc0);
+  iVar2 = strcmp(__s1,"0");
+  if (iVar2 == 0) {
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    guest_ip_check((char *)in_stack_fffffeb8,in_stack_fffffebc,(int)in_stack_fffffec0);
   }
   else {
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
-    setWanValue((int)in_stack_fffffcb8,in_stack_fffffcbc,in_stack_fffffcc0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
+    setWanValue((int)in_stack_fffffeb8,in_stack_fffffebc,in_stack_fffffec0);
   }
   return;
 }
 

```


## ate_nvram_set_pin

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.6|
|i_ratio|0.69|
|m_ratio|0.96|
|b_ratio|0.83|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|ate_nvram_set_pin|ate_nvram_set_pin|
|fullname|ate_nvram_set_pin|ate_nvram_set_pin|
|refcount|3|3|
|`length`|216|200|
|called|<EXTERNAL>::printf<br>ate_envram_set_common|<EXTERNAL>::printf<br>ate_envram_set_common|
|calling|||
|paramcount|2|2|
|`address`|0047a844|0047a324|
|sig|rtn_type ate_nvram_set_pin(char * arg, char * rtn)|rtn_type ate_nvram_set_pin(char * arg, char * rtn)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### ate_nvram_set_pin Diff


```diff
--- ate_nvram_set_pin
+++ ate_nvram_set_pin
@@ -1,23 +1,17 @@
 
 /* WARNING: Unknown calling convention */
 
 rtn_type ate_nvram_set_pin(char *arg,char *rtn)
 
 {
   rtn_type rVar1;
-  char *in_a0;
+  undefined4 in_a0;
   char *in_stack_ffffffe0;
   char *in_stack_ffffffe4;
   
   printf("%s : %d\n","ate_nvram_set_pin",0x261);
   printf("PIN=%s\n",in_a0);
-  if ((*in_a0 == '\0') ||
-     (rVar1 = ate_envram_set_common(in_stack_ffffffe0,in_stack_ffffffe4), rVar1 == RTN_SUCCESS)) {
-    rVar1 = RTN_SUCCESS;
-  }
-  else {
-    rVar1 = RTN_FAILED;
-  }
-  return rVar1;
+  rVar1 = ate_envram_set_common(in_stack_ffffffe0,in_stack_ffffffe4);
+  return (uint)(rVar1 != RTN_SUCCESS);
 }
 

```


## iwpriv_wlan_set

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.97|
|i_ratio|0.57|
|m_ratio|0.99|
|b_ratio|0.97|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|iwpriv_wlan_set|iwpriv_wlan_set|
|fullname|iwpriv_wlan_set|iwpriv_wlan_set|
|refcount|3|3|
|`length`|952|928|
|`called`|<EXTERNAL>::doSystemCmd<br><EXTERNAL>::printf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::strstr<br><EXTERNAL>::usleep<br>MP_get_ext|<EXTERNAL>::doSystemCmd<br><EXTERNAL>::printf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::strlen<br><EXTERNAL>::strstr<br>MP_get_ext|
|calling|ate_iwpriv_set|ate_iwpriv_set|
|paramcount|4|4|
|`address`|004806a0|00480174|
|sig|rtn_type iwpriv_wlan_set(int i, char * cmd_type, char * cmd_buf, char * mp_buf)|rtn_type iwpriv_wlan_set(int i, char * cmd_type, char * cmd_buf, char * mp_buf)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### iwpriv_wlan_set Called Diff


```diff
--- iwpriv_wlan_set called
+++ iwpriv_wlan_set called
@@ -7 +6,0 @@
-<EXTERNAL>::usleep
```


### iwpriv_wlan_set Diff


```diff
--- iwpriv_wlan_set
+++ iwpriv_wlan_set
@@ -1,64 +1,63 @@
 
 /* WARNING: Unknown calling convention */
 
 rtn_type iwpriv_wlan_set(int i,char *cmd_type,char *cmd_buf,char *mp_buf)
 
 {
   rtn_type rVar1;
   char *pcVar2;
   size_t sVar3;
   int iVar4;
   char *in_a1;
   char *in_a2;
   char *in_a3;
   char *in_stack_ffffff88;
   char *in_stack_ffffff8c;
   uint in_stack_ffffff90;
   char *p;
   char wlan [2] [16];
   char temp_buf [48];
   
   if (in_a2 == (char *)0x0) {
     rVar1 = RTN_FAILED;
   }
   else {
     pcVar2 = strstr(in_a2,in_a1);
     if (pcVar2 == (char *)0x0) {
-      printf("[%s:%d]Don\'t find iwpriv wlan!\n","iwpriv_wlan_set",0x859);
+      printf("[%s:%d]Don\'t find iwpriv wlan!\n","iwpriv_wlan_set",0x84f);
       rVar1 = RTN_FAILED;
     }
     else {
       sVar3 = strlen(in_a1);
       pcVar2 = pcVar2 + sVar3 + 1;
       iVar4 = strcmp(pcVar2,"mp_query");
       if (iVar4 == 0) {
         MP_get_ext(in_stack_ffffff88,in_stack_ffffff8c,in_stack_ffffff90);
         printf("---mp_query=%s\n",in_a2);
         strcpy(in_a3,in_a2);
       }
       else {
         iVar4 = strcmp(pcVar2,"mp_ther");
         if (iVar4 == 0) {
           MP_get_ext(in_stack_ffffff88,in_stack_ffffff8c,in_stack_ffffff90);
           printf("---mp_ther=%s\n",in_a2);
           strcpy(in_a3,in_a2);
         }
         else {
           iVar4 = strcmp(pcVar2,"mp_tssi");
           if (iVar4 == 0) {
             MP_get_ext(in_stack_ffffff88,in_stack_ffffff8c,in_stack_ffffff90);
             printf("---mp_tssi=%s\n",in_a2);
             strcpy(in_a3,in_a2);
           }
           else {
             doSystemCmd(in_a2);
-            usleep(2000);
           }
         }
       }
       rVar1 = RTN_SUCCESS;
     }
   }
   return rVar1;
 }
 

```


## ate_Tenda_mfg_check_wpsbutton

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.93|
|i_ratio|0.79|
|m_ratio|0.99|
|b_ratio|0.99|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|ate_Tenda_mfg_check_wpsbutton|ate_Tenda_mfg_check_wpsbutton|
|fullname|ate_Tenda_mfg_check_wpsbutton|ate_Tenda_mfg_check_wpsbutton|
|refcount|3|3|
|`length`|176|180|
|called|<EXTERNAL>::Get_Mfg_Button_Test_Result<br><EXTERNAL>::memcpy|<EXTERNAL>::Get_Mfg_Button_Test_Result<br><EXTERNAL>::memcpy|
|calling|||
|paramcount|2|2|
|`address`|0047e830|0047e300|
|sig|rtn_type ate_Tenda_mfg_check_wpsbutton(char * arg, char * rtn)|rtn_type ate_Tenda_mfg_check_wpsbutton(char * arg, char * rtn)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### ate_Tenda_mfg_check_wpsbutton Diff


```diff
--- ate_Tenda_mfg_check_wpsbutton
+++ ate_Tenda_mfg_check_wpsbutton
@@ -1,20 +1,20 @@
 
 /* WARNING: Unknown calling convention */
 
 rtn_type ate_Tenda_mfg_check_wpsbutton(char *arg,char *rtn)
 
 {
   bool bVar1;
   void *in_a1;
   int ret;
   int value [1];
   
   value[0] = 0;
   Get_Mfg_Button_Test_Result(value);
-  bVar1 = (value[0] & 4U) == 0;
+  bVar1 = (value[0] & 1U) == 0;
   if (!bVar1) {
     memcpy(in_a1,"success",8);
   }
   return (uint)bVar1;
 }
 

```


## check_param_changed

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.8|
|i_ratio|0.19|
|m_ratio|1.0|
|b_ratio|0.98|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|check_param_changed|check_param_changed|
|fullname|check_param_changed|check_param_changed|
|refcount|2|2|
|`length`|3372|3348|
|called|<EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcpy<br><EXTERNAL>::strncmp<br>getIpMac<br>websGetVar|<EXTERNAL>::GetValue<br><EXTERNAL>::atoi<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcpy<br><EXTERNAL>::strncmp<br>getIpMac<br>websGetVar|
|calling|fromAdvSetMacMtuWan|fromAdvSetMacMtuWan|
|paramcount|3|3|
|`address`|0048b570|0048ae50|
|sig|int check_param_changed(webs_t wp, int wan_id, WAN_ARGUMENT * wan_param)|int check_param_changed(webs_t wp, int wan_id, WAN_ARGUMENT * wan_param)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### check_param_changed Diff


```diff
--- check_param_changed
+++ check_param_changed
@@ -1,203 +1,218 @@
 
 /* WARNING: Unknown calling convention */
 /* WARNING: Struct "sym_t": ignoring overlapping field "content" */
 
 int check_param_changed(webs_t wp,int wan_id,WAN_ARGUMENT *wan_param)
 
 {
   int iVar1;
   char_t *pcVar2;
   int in_a1;
   char *in_a2;
-  webs_t in_stack_fffffea0;
-  char *in_stack_fffffea4;
-  char_t *in_stack_fffffea8;
+  webs_t in_stack_ffffff90;
+  char *in_stack_ffffff94;
+  char_t *in_stack_ffffff98;
   int wan_connect_type;
   int change_flag;
   char mib_name [32];
-  char mib_value [256];
+  char mib_value [16];
   char clone_type [16];
   
   mib_name[0] = '\0';
   mib_name[1] = '\0';
   mib_name[2] = '\0';
   mib_name[3] = '\0';
   mib_name[4] = '\0';
   mib_name[5] = '\0';
   mib_name[6] = '\0';
   mib_name[7] = '\0';
   mib_name[8] = '\0';
   mib_name[9] = '\0';
   mib_name[10] = '\0';
   mib_name[0xb] = '\0';
   mib_name[0xc] = '\0';
   mib_name[0xd] = '\0';
   mib_name[0xe] = '\0';
   mib_name[0xf] = '\0';
   mib_name[0x10] = '\0';
   mib_name[0x11] = '\0';
   mib_name[0x12] = '\0';
   mib_name[0x13] = '\0';
   mib_name[0x14] = '\0';
   mib_name[0x15] = '\0';
   mib_name[0x16] = '\0';
   mib_name[0x17] = '\0';
   mib_name[0x18] = '\0';
   mib_name[0x19] = '\0';
   mib_name[0x1a] = '\0';
   mib_name[0x1b] = '\0';
   mib_name[0x1c] = '\0';
   mib_name[0x1d] = '\0';
   mib_name[0x1e] = '\0';
   mib_name[0x1f] = '\0';
-  memset(mib_value,0,0x100);
+  mib_value[0] = '\0';
+  mib_value[1] = '\0';
+  mib_value[2] = '\0';
+  mib_value[3] = '\0';
+  mib_value[4] = '\0';
+  mib_value[5] = '\0';
+  mib_value[6] = '\0';
+  mib_value[7] = '\0';
+  mib_value[8] = '\0';
+  mib_value[9] = '\0';
+  mib_value[10] = '\0';
+  mib_value[0xb] = '\0';
+  mib_value[0xc] = '\0';
+  mib_value[0xd] = '\0';
+  mib_value[0xe] = '\0';
+  mib_value[0xf] = '\0';
   clone_type[0] = '\0';
   clone_type[1] = '\0';
   clone_type[2] = '\0';
   clone_type[3] = '\0';
   clone_type[4] = '\0';
   clone_type[5] = '\0';
   clone_type[6] = '\0';
   clone_type[7] = '\0';
   clone_type[8] = '\0';
   clone_type[9] = '\0';
   clone_type[10] = '\0';
   clone_type[0xb] = '\0';
   clone_type[0xc] = '\0';
   clone_type[0xd] = '\0';
   clone_type[0xe] = '\0';
   clone_type[0xf] = '\0';
   change_flag = 0;
   sprintf(mib_name,"wan%d.connecttype",in_a1);
   GetValue(mib_name,in_a2);
   iVar1 = atoi(in_a2);
   if (in_a2 == (char *)0x0) {
-    printf("[%s---%d]: wan_param is null!\n","check_param_changed",0x6f9);
+    printf("[%s---%d]: wan_param is null!\n","check_param_changed",0x6e2);
     change_flag = 0;
   }
   else {
     if (in_a1 == 1) {
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x10,pcVar2);
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x18,pcVar2);
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x20,pcVar2);
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x4c,pcVar2);
     }
     else {
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x10,pcVar2);
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x18,pcVar2);
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x20,pcVar2);
-      pcVar2 = websGetVar(in_stack_fffffea0,in_stack_fffffea4,in_stack_fffffea8);
+      pcVar2 = websGetVar(in_stack_ffffff90,in_stack_ffffff94,in_stack_ffffff98);
       strcpy(in_a2 + 0x4c,pcVar2);
     }
     switch(iVar1) {
     case 0:
       memset(mib_name,0,0x20);
-      memset(mib_value,0,0x100);
+      memset(mib_value,0,0x10);
       sprintf(mib_name,"wan%d.dynamicMTU",in_a1);
       GetValue(mib_name,mib_value);
-      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x100);
+      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x10);
       if (iVar1 != 0) {
         change_flag = 1;
       }
       break;
     case 1:
       memset(mib_name,0,0x20);
-      memset(mib_value,0,0x100);
+      memset(mib_value,0,0x10);
       sprintf(mib_name,"wan%d.staticMTU",in_a1);
       GetValue(mib_name,mib_value);
-      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x100);
+      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x10);
       if (iVar1 != 0) {
         change_flag = 1;
       }
       break;
     case 2:
       memset(mib_name,0,0x20);
-      memset(mib_value,0,0x100);
+      memset(mib_value,0,0x10);
       sprintf(mib_name,"wan%d.ppoe.mtu",in_a1);
       GetValue(mib_name,mib_value);
-      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x100);
+      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x10);
       if (iVar1 != 0) {
         change_flag = 1;
       }
       break;
     case 3:
       memset(mib_name,0,0x20);
-      memset(mib_value,0,0x100);
+      memset(mib_value,0,0x10);
       sprintf(mib_name,"wan%d.pptp.mtu",in_a1);
       GetValue(mib_name,mib_value);
-      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x100);
+      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x10);
       if (iVar1 != 0) {
         change_flag = 1;
       }
       break;
     case 4:
       memset(mib_name,0,0x20);
-      memset(mib_value,0,0x100);
+      memset(mib_value,0,0x10);
       sprintf(mib_name,"wan%d.l2tp.mtu",in_a1);
       GetValue(mib_name,mib_value);
-      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x100);
+      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x10);
       if (iVar1 != 0) {
         change_flag = 1;
       }
       break;
     case 5:
       memset(mib_name,0,0x20);
-      memset(mib_value,0,0x100);
+      memset(mib_value,0,0x10);
       sprintf(mib_name,"wan%d.ppoe.mtu",in_a1);
       GetValue(mib_name,mib_value);
-      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x100);
+      iVar1 = strncmp(mib_value,in_a2 + 0x10,0x10);
       if (iVar1 != 0) {
         change_flag = 1;
       }
     }
     memset(mib_name,0,0x20);
-    memset(mib_value,0,0x100);
+    memset(mib_value,0,0x10);
     sprintf(mib_name,"wan%d.param",in_a1);
     GetValue(mib_name,mib_value);
-    iVar1 = strncmp(mib_value,in_a2 + 0x18,0x100);
+    iVar1 = strncmp(mib_value,in_a2 + 0x18,0x10);
     if (iVar1 != 0) {
       change_flag = 1;
     }
     memset(mib_name,0,0x20);
     sprintf(mib_name,"wan%d.mac.clone.type",in_a1);
     GetValue(mib_name,clone_type);
     iVar1 = strncmp(clone_type,in_a2 + 0x20,0x10);
     if (iVar1 != 0) {
       change_flag = 1;
     }
     iVar1 = strncmp(clone_type,"1",0x10);
     if (iVar1 == 0) {
-      getIpMac((char *)in_stack_fffffea0,in_stack_fffffea4);
-      memset(mib_name,0,0x20);
-      memset(mib_value,0,0x100);
+      getIpMac((char *)in_stack_ffffff90,in_stack_ffffff94);
+      memset(mib_name,0,0x20);
+      memset(mib_value,0,0x10);
       sprintf(mib_name,"wan%d.macaddr",in_a1);
       GetValue(mib_name,mib_value);
-      iVar1 = strncmp(mib_value,in_a2 + 0x3a,0x100);
+      iVar1 = strncmp(mib_value,in_a2 + 0x3a,0x10);
       if (iVar1 != 0) {
         change_flag = 1;
       }
     }
     else {
       iVar1 = strncmp(clone_type,"2",0x10);
       if (iVar1 == 0) {
         memset(mib_name,0,0x20);
-        memset(mib_value,0,0x100);
+        memset(mib_value,0,0x10);
         sprintf(mib_name,"wan%d.macaddr",in_a1);
         GetValue(mib_name,mib_value);
-        iVar1 = strncmp(mib_value,in_a2 + 0x4c,0x100);
+        iVar1 = strncmp(mib_value,in_a2 + 0x4c,0x10);
         if (iVar1 != 0) {
           change_flag = 1;
         }
       }
     }
   }
   return change_flag;
 }
 

```


## fromGetSysTime

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address,called|
|ratio|0.73|
|i_ratio|0.53|
|m_ratio|0.92|
|b_ratio|0.66|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|fromGetSysTime|fromGetSysTime|
|fullname|fromGetSysTime|fromGetSysTime|
|refcount|3|3|
|`length`|1492|1272|
|`called`|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::free<br><EXTERNAL>::localtime<br><EXTERNAL>::memcpy<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::time<br>cJSON_AddItemToObject<br>cJSON_CreateObject</summary>cJSON_CreateString<br>cJSON_Delete<br>cJSON_Print<br>websDone<br>websWrite</details>|<details><summary>Expand for full list:<br><EXTERNAL>::GetValue<br><EXTERNAL>::free<br><EXTERNAL>::localtime<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strcmp<br><EXTERNAL>::strcpy<br><EXTERNAL>::time<br>cJSON_AddItemToObject<br>cJSON_CreateObject<br>cJSON_CreateString</summary>cJSON_Delete<br>cJSON_Print<br>websDone<br>websWrite</details>|
|calling|||
|paramcount|3|3|
|`address`|004a8dac|004a8540|
|sig|void fromGetSysTime(webs_t wp, char_t * path, char_t * query)|void fromGetSysTime(webs_t wp, char_t * path, char_t * query)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### fromGetSysTime Called Diff


```diff
--- fromGetSysTime called
+++ fromGetSysTime called
@@ -4 +3,0 @@
-<EXTERNAL>::memcpy
```


### fromGetSysTime Diff


```diff
--- fromGetSysTime
+++ fromGetSysTime
@@ -1,172 +1,132 @@
 
 /* WARNING: Unknown calling convention */
 
 void fromGetSysTime(webs_t wp,char_t *path,char_t *query)
 
 {
   tm *ptVar1;
   int iVar2;
   char *pcVar3;
   webs_t in_a0;
-  webs_t in_stack_fffffe60;
-  char *in_stack_fffffe64;
-  cJSON *in_stack_fffffe68;
+  webs_t in_stack_fffffe80;
+  char *in_stack_fffffe84;
+  cJSON *in_stack_fffffe88;
   cJSON_conflict *root;
   char *out;
   tm *p;
   char mode [16];
   time_t time_now;
   char value [16];
   char timezone [16];
   char timeper [16];
   char timentpserver [256];
-  char timezone_str [16];
-  char nextzone [16];
   
   mode[0] = '\0';
   mode[1] = '\0';
   mode[2] = '\0';
   mode[3] = '\0';
   mode[4] = '\0';
   mode[5] = '\0';
   mode[6] = '\0';
   mode[7] = '\0';
   mode[8] = '\0';
   mode[9] = '\0';
   mode[10] = '\0';
   mode[0xb] = '\0';
   mode[0xc] = '\0';
   mode[0xd] = '\0';
   mode[0xe] = '\0';
   mode[0xf] = '\0';
   value[0] = '\0';
   value[1] = '\0';
   value[2] = '\0';
   value[3] = '\0';
   value[4] = '\0';
   value[5] = '\0';
   value[6] = '\0';
   value[7] = '\0';
   value[8] = '\0';
   value[9] = '\0';
   value[10] = '\0';
   value[0xb] = '\0';
   value[0xc] = '\0';
   value[0xd] = '\0';
   value[0xe] = '\0';
   value[0xf] = '\0';
   timezone[0] = '\0';
   timezone[1] = '\0';
   timezone[2] = '\0';
   timezone[3] = '\0';
   timezone[4] = '\0';
   timezone[5] = '\0';
   timezone[6] = '\0';
   timezone[7] = '\0';
   timezone[8] = '\0';
   timezone[9] = '\0';
   timezone[10] = '\0';
   timezone[0xb] = '\0';
   timezone[0xc] = '\0';
   timezone[0xd] = '\0';
   timezone[0xe] = '\0';
   timezone[0xf] = '\0';
   timeper[0] = '\0';
   timeper[1] = '\0';
   timeper[2] = '\0';
   timeper[3] = '\0';
   timeper[4] = '\0';
   timeper[5] = '\0';
   timeper[6] = '\0';
   timeper[7] = '\0';
   timeper[8] = '\0';
   timeper[9] = '\0';
   timeper[10] = '\0';
   timeper[0xb] = '\0';
   timeper[0xc] = '\0';
   timeper[0xd] = '\0';
   timeper[0xe] = '\0';
   timeper[0xf] = '\0';
   memset(timentpserver,0,0x100);
-  timezone_str[0] = '\0';
-  timezone_str[1] = '\0';
-  timezone_str[2] = '\0';
-  timezone_str[3] = '\0';
-  timezone_str[4] = '\0';
-  timezone_str[5] = '\0';
-  timezone_str[6] = '\0';
-  timezone_str[7] = '\0';
-  timezone_str[8] = '\0';
-  timezone_str[9] = '\0';
-  timezone_str[10] = '\0';
-  timezone_str[0xb] = '\0';
-  timezone_str[0xc] = '\0';
-  timezone_str[0xd] = '\0';
-  timezone_str[0xe] = '\0';
-  timezone_str[0xf] = '\0';
-  nextzone[0] = '\0';
-  nextzone[1] = '\0';
-  nextzone[2] = '\0';
-  nextzone[3] = '\0';
-  nextzone[4] = '\0';
-  nextzone[5] = '\0';
-  nextzone[6] = '\0';
-  nextzone[7] = '\0';
-  nextzone[8] = '\0';
-  nextzone[9] = '\0';
-  nextzone[10] = '\0';
-  nextzone[0xb] = '\0';
-  nextzone[0xc] = '\0';
-  nextzone[0xd] = '\0';
-  nextzone[0xe] = '\0';
-  nextzone[0xf] = '\0';
   time(&time_now);
   ptVar1 = localtime(&time_now);
   GetValue("sys.timemode",mode);
   cJSON_CreateObject();
   iVar2 = strcmp(mode,"hand");
   if (iVar2 == 0) {
-    cJSON_CreateString((char *)in_stack_fffffe60);
-    cJSON_AddItemToObject((cJSON *)in_stack_fffffe60,in_stack_fffffe64,in_stack_fffffe68);
+    cJSON_CreateString((char *)in_stack_fffffe80);
+    cJSON_AddItemToObject((cJSON *)in_stack_fffffe80,in_stack_fffffe84,in_stack_fffffe88);
   }
   else {
-    cJSON_CreateString((char *)in_stack_fffffe60);
-    cJSON_AddItemToObject((cJSON *)in_stack_fffffe60,in_stack_fffffe64,in_stack_fffffe68);
+    cJSON_CreateString((char *)in_stack_fffffe80);
+    cJSON_AddItemToObject((cJSON *)in_stack_fffffe80,in_stack_fffffe84,in_stack_fffffe88);
   }
   GetValue("sys.timezone",timezone);
-  GetValue("sys.timenextzone",nextzone);
-  iVar2 = strcmp(nextzone,"0");
-  if ((iVar2 == 0) || (nextzone[0] == '\0')) {
-    memcpy(nextzone,&DAT_0,3);
-  }
-  sprintf(timezone_str,"%s:%s",timezone,nextzone);
-  cJSON_CreateString((char *)in_stack_fffffe60);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffe60,in_stack_fffffe64,in_stack_fffffe68);
+  cJSON_CreateString((char *)in_stack_fffffe80);
+  cJSON_AddItemToObject((cJSON *)in_stack_fffffe80,in_stack_fffffe84,in_stack_fffffe88);
   GetValue("sys.timefixper",timeper);
-  cJSON_CreateString((char *)in_stack_fffffe60);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffe60,in_stack_fffffe64,in_stack_fffffe68);
+  cJSON_CreateString((char *)in_stack_fffffe80);
+  cJSON_AddItemToObject((cJSON *)in_stack_fffffe80,in_stack_fffffe84,in_stack_fffffe88);
   GetValue("sys.timentpserver",timentpserver);
-  cJSON_CreateString((char *)in_stack_fffffe60);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffe60,in_stack_fffffe64,in_stack_fffffe68);
+  cJSON_CreateString((char *)in_stack_fffffe80);
+  cJSON_AddItemToObject((cJSON *)in_stack_fffffe80,in_stack_fffffe84,in_stack_fffffe88);
   sprintf(value,"%d-%02d-%02d %02d:%02d:%02d",ptVar1->tm_year + 0x76c,ptVar1->tm_mon + 1,
           ptVar1->tm_mday,ptVar1->tm_hour,ptVar1->tm_min,ptVar1->tm_sec);
-  cJSON_CreateString((char *)in_stack_fffffe60);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffe60,in_stack_fffffe64,in_stack_fffffe68);
+  cJSON_CreateString((char *)in_stack_fffffe80);
+  cJSON_AddItemToObject((cJSON *)in_stack_fffffe80,in_stack_fffffe84,in_stack_fffffe88);
   if (ptVar1->tm_year + 0x76c < 0x7d1) {
     pcVar3 = "false";
   }
   else {
     pcVar3 = "true";
   }
   strcpy(value,pcVar3);
-  cJSON_CreateString((char *)in_stack_fffffe60);
-  cJSON_AddItemToObject((cJSON *)in_stack_fffffe60,in_stack_fffffe64,in_stack_fffffe68);
-  pcVar3 = cJSON_Print((cJSON *)in_stack_fffffe60);
-  cJSON_Delete((cJSON *)in_stack_fffffe60);
+  cJSON_CreateString((char *)in_stack_fffffe80);
+  cJSON_AddItemToObject((cJSON *)in_stack_fffffe80,in_stack_fffffe84,in_stack_fffffe88);
+  pcVar3 = cJSON_Print((cJSON *)in_stack_fffffe80);
+  cJSON_Delete((cJSON *)in_stack_fffffe80);
   websWrite(in_a0,"HTTP/1.0 200 OK\r\n\r\n");
   websWrite(in_a0,"%s",pcVar3);
   free(pcVar3);
-  websDone(in_stack_fffffe60,(int)in_stack_fffffe64);
+  websDone(in_stack_fffffe80,(int)in_stack_fffffe84);
   return;
 }
 

```


## setPppoeConfig

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.99|
|i_ratio|0.36|
|m_ratio|0.99|
|b_ratio|0.96|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|setPppoeConfig|setPppoeConfig|
|fullname|setPppoeConfig|setPppoeConfig|
|refcount|5|5|
|`length`|2292|2252|
|called|<EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::UnSetValue<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strlen<br><EXTERNAL>::strncmp<br>setWanValue<br>websGetVar|<EXTERNAL>::GetValue<br><EXTERNAL>::SetValue<br><EXTERNAL>::UnSetValue<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf<br><EXTERNAL>::strlen<br><EXTERNAL>::strncmp<br>setWanValue<br>websGetVar|
|calling|formWanInfoSet<br>form_fast_setting_internet_set|formWanInfoSet<br>form_fast_setting_internet_set|
|paramcount|2|2|
|`address`|00483c4c|0048370c|
|sig|void setPppoeConfig(webs_t wp, int wan_id)|void setPppoeConfig(webs_t wp, int wan_id)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### setPppoeConfig Diff


```diff
--- setPppoeConfig
+++ setPppoeConfig
@@ -1,93 +1,92 @@
 
 /* WARNING: Unknown calling convention */
 /* WARNING: Struct "sym_t": ignoring overlapping field "content" */
 
 void setPppoeConfig(webs_t wp,int wan_id)
 
 {
   char_t *pcVar1;
   char_t *pcVar2;
   int iVar3;
   size_t sVar4;
   int in_a1;
   webs_t in_stack_fffffcc8;
   char *in_stack_fffffccc;
   char *in_stack_fffffcd0;
   char_t *hand_dns2;
   char_t *hand_dns1;
   char_t *wan_dns_auto;
   char_t *pppoe_pwd;
   char_t *pppoe_name;
   char_t mib_name [256];
   char_t pppoename [256];
   char_t pppoepwd [256];
   
   hand_dns1 = (char_t *)0x0;
   hand_dns2 = (char_t *)0x0;
   memset(mib_name,0,0x100);
   memset(pppoename,0,0x100);
   memset(pppoepwd,0,0x100);
   if (in_a1 == 1) {
     pcVar1 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     pcVar2 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     hand_dns1 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     hand_dns2 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     memset(mib_name,0,0x100);
     sprintf(mib_name,"wan%d.ppoe.userid",1);
     GetValue(mib_name,pppoename);
     memset(mib_name,0,0x100);
     sprintf(mib_name,"wan%d.ppoe.pwd",1);
     GetValue(mib_name,pppoepwd);
     iVar3 = strncmp(pppoename,pcVar1,0x100);
     if ((iVar3 == 0) && (iVar3 = strncmp(pppoepwd,pcVar2,0x100), iVar3 == 0)) {
       setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     }
     else {
       memset(mib_name,0,0x100);
       sprintf(mib_name,"wan%d.pppoe.encrypt.type",1);
       UnSetValue(mib_name);
       setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
       setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
-      setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     }
     SetValue("wl.wisp.access_mode","pppoe");
     SetValue("wl.wisp.ip",&DAT_0);
     SetValue("wl.wisp.mask",&DAT_0);
     SetValue("wl.wisp.gateway",&DAT_0);
     SetValue("wl.wisp.dns1",&DAT_0);
     SetValue("wl.wisp.dns2",&DAT_0);
     memset(mib_name,0,0x100);
     sprintf(mib_name,"wan%d.ppoe.double.access",1);
     SetValue(mib_name,&DAT_1);
   }
   else if (in_a1 == 2) {
     pcVar1 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     pcVar2 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     hand_dns1 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     hand_dns2 = websGetVar(in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     memset(mib_name,0,0x100);
     sprintf(mib_name,"wan%d.ppoe.userid",2);
     GetValue(mib_name,pppoename);
     memset(mib_name,0,0x100);
     sprintf(mib_name,"wan%d.ppoe.pwd",2);
     GetValue(mib_name,pppoepwd);
     iVar3 = strncmp(pppoename,pcVar1,0x100);
     if ((iVar3 != 0) || (iVar3 = strncmp(pppoepwd,pcVar2,0x100), iVar3 != 0)) {
       memset(mib_name,0,0x100);
       sprintf(mib_name,"wan%d.pppoe.encrypt.type",2);
       UnSetValue(mib_name);
     }
   }
   setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
   setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
   setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
   sVar4 = strlen(hand_dns1);
   if ((6 < sVar4) || (sVar4 = strlen(hand_dns2), 6 < sVar4)) {
     setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
     setWanValue((int)in_stack_fffffcc8,in_stack_fffffccc,in_stack_fffffcd0);
   }
   return;
 }
 

```


## have_enough_mem

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.93|
|i_ratio|0.69|
|m_ratio|0.97|
|b_ratio|0.97|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|have_enough_mem|have_enough_mem|
|fullname|have_enough_mem|have_enough_mem|
|refcount|4|4|
|`length`|488|460|
|called|<EXTERNAL>::doSystemCmd<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::sleep<br><EXTERNAL>::sysinfo|<EXTERNAL>::doSystemCmd<br><EXTERNAL>::memset<br><EXTERNAL>::printf<br><EXTERNAL>::sleep<br><EXTERNAL>::sysinfo|
|calling|webCgiGetUploadFile|webCgiGetUploadFile|
|paramcount|1|1|
|`address`|004447b4|00444564|
|sig|int have_enough_mem(int size)|int have_enough_mem(int size)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### have_enough_mem Diff


```diff
--- have_enough_mem
+++ have_enough_mem
@@ -1,26 +1,25 @@
 
 /* WARNING: Unknown calling convention */
 
 int have_enough_mem(int size)
 
 {
   int in_a0;
   long upgrade_need_min_memory;
   long result;
   sysinfo si;
   
   memset(&si,0,0x40);
-  doSystemCmd("rm -rf /tmp/core-*");
   doSystemCmd("killall -9 smbd");
   doSystemCmd("killall -9 nmbd");
   doSystemCmd("killall -9 stupid-ftpd");
   doSystemCmd("killall -9 minidlna");
   doSystemCmd(&DAT_0);
   doSystemCmd("echo 3 > /proc/sys/vm/drop_caches");
   doSystemCmd("echo 1024 > /proc/sys/vm/min_free_kbytes");
   sleep(1);
   sysinfo((sysinfo *)&si);
-  printf("%s %d: current remain memory is %ld\n","have_enough_mem",0x288,si.freeram);
+  printf("%s %d: current remain memory is %ld\n","have_enough_mem",0x287,si.freeram);
   return (uint)(in_a0 + 0x300000 < (int)si.freeram);
 }
 

```


## aspGetModeShow

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|code,length,address|
|ratio|0.99|
|i_ratio|0.05|
|m_ratio|1.0|
|b_ratio|0.96|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|aspGetModeShow|aspGetModeShow|
|fullname|aspGetModeShow|aspGetModeShow|
|refcount|3|3|
|`length`|3996|3988|
|called|<EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ejArgs<br>websWrite|<EXTERNAL>::puts<br><EXTERNAL>::strcmp<br>ejArgs<br>websWrite|
|calling|||
|paramcount|4|4|
|`address`|00451270|00450f20|
|sig|int aspGetModeShow(int eid, webs_t wp, int argc, char_t * * argv)|int aspGetModeShow(int eid, webs_t wp, int argc, char_t * * argv)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### aspGetModeShow Diff


```diff
--- aspGetModeShow
+++ aspGetModeShow
@@ -1,422 +1,422 @@
 
 /* WARNING: Unknown calling convention */
 
 int aspGetModeShow(int eid,webs_t wp,int argc,char_t **argv)
 
 {
   int iVar1;
   webs_t in_a1;
   int in_a2;
   char_t **in_a3;
   int modeshow;
   char_t *item;
   
   item = (char_t *)0x0;
   modeshow = -1;
   ejArgs(in_a2,in_a3,"%s",&item);
   if (*item == '\0') {
     iVar1 = websWrite(in_a1,"0");
   }
   else {
     iVar1 = strcmp(item,"multi_wan");
     if (iVar1 == 0) {
       modeshow = 1;
     }
     else {
       iVar1 = strcmp(item,"parent_control");
       if (iVar1 == 0) {
         modeshow = 0;
       }
       else {
         iVar1 = strcmp(item,"ppoesv");
         if (iVar1 == 0) {
           modeshow = 0;
         }
         else {
           iVar1 = strcmp(item,"webauth");
           if (iVar1 == 0) {
             modeshow = 0;
           }
           else {
             iVar1 = strcmp(item,"vpn");
             if (iVar1 == 0) {
               modeshow = 1;
             }
             else {
               iVar1 = strcmp(item,"GMAC");
               if (iVar1 == 0) {
                 modeshow = 1;
               }
               else {
                 iVar1 = strcmp(item,"natSessionLimit");
                 if (iVar1 == 0) {
                   modeshow = 0;
                 }
                 else {
                   iVar1 = strcmp(item,"safeAttack");
                   if (iVar1 == 0) {
                     modeshow = 1;
                   }
                   else {
                     iVar1 = strcmp(item,"safe_arp");
                     if (iVar1 == 0) {
                       modeshow = 0;
                     }
                     else {
                       iVar1 = strcmp(item,"ssl");
                       if (iVar1 == 0) {
                         modeshow = 1;
                       }
                       else {
                         iVar1 = strcmp(item,"lan_access");
                         if (iVar1 == 0) {
                           modeshow = 0;
                         }
                         else {
                           iVar1 = strcmp(item,"wan_access");
                           if (iVar1 == 0) {
                             modeshow = 1;
                           }
                           else {
                             iVar1 = strcmp(item,"cfg_wan");
                             if (iVar1 == 0) {
                               modeshow = 1;
                             }
                             else {
                               iVar1 = strcmp(item,"cfg_mirror");
                               if (iVar1 == 0) {
                                 modeshow = 0;
                               }
                               else {
                                 iVar1 = strcmp(item,"cfg_port");
                                 if (iVar1 == 0) {
                                   modeshow = 1;
                                 }
                                 else {
                                   iVar1 = strcmp(item,"url");
                                   if (iVar1 == 0) {
                                     puts("udefine\t url");
                                     modeshow = 0;
                                   }
                                   else {
                                     iVar1 = strcmp(item,"url_class");
                                     if (iVar1 == 0) {
                                       modeshow = 0;
                                     }
                                     else {
                                       iVar1 = strcmp(item,"filter_layer7");
                                       if (iVar1 == 0) {
                                         modeshow = 0;
                                       }
                                       else {
                                         iVar1 = strcmp(item,"filter_im");
                                         if (iVar1 == 0) {
                                           modeshow = 0;
                                         }
                                         else {
                                           iVar1 = strcmp(item,"turbo_qos");
                                           if (iVar1 == 0) {
                                             modeshow = 0;
                                           }
                                           else {
                                             iVar1 = strcmp(item,"qos_priority");
                                             if (iVar1 == 0) {
                                               modeshow = 0;
                                             }
                                             else {
                                               iVar1 = strcmp(item,"notification");
                                               if (iVar1 == 0) {
                                                 modeshow = 0;
                                               }
                                               else {
                                                 iVar1 = strcmp(item,"p2p_NAT");
                                                 if (iVar1 == 0) {
                                                   modeshow = 0;
                                                 }
                                                 else {
                                                   iVar1 = strcmp(item,"ddns_ddns");
                                                   if (iVar1 == 0) {
                                                     modeshow = 1;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(item,"ddns_3322");
                                                     if (iVar1 == 0) {
                                                       modeshow = 1;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(item,"ddns_88ip");
                                                       if (iVar1 == 0) {
                                                         modeshow = 1;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(item,"ddns_GNWAY");
                                                         if (iVar1 == 0) {
                                                           modeshow = 0;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(item,"ddns_oray");
                                                           if (iVar1 == 0) {
                                                             modeshow = 1;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(item,"ddns_noip");
                                                             if (iVar1 == 0) {
                                                               modeshow = 1;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(item,"ddns_dyn");
                                                               if (iVar1 == 0) {
                                                                 modeshow = 1;
                                                               }
                                                               else {
                                                                 iVar1 = strcmp(item,"update_layer7")
                                                                 ;
                                                                 if (iVar1 == 0) {
                                                                   modeshow = 0;
                                                                 }
                                                                 else {
                                                                   iVar1 = strcmp(item,"cfg_dsl");
                                                                   if (iVar1 == 0) {
                                                                     modeshow = 0;
                                                                   }
                                                                   else {
                                                                     iVar1 = strcmp(item,
                                                   "dsl_annex_a");
                                                   if (iVar1 == 0) {
                                                     modeshow = 0;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(item,"dsl_annex_b");
                                                     if (iVar1 == 0) {
                                                       modeshow = 0;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(item,"cfg_wifi");
                                                       if (iVar1 == 0) {
                                                         modeshow = 1;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(item,"wifi_auth_1x");
                                                         if (iVar1 == 0) {
                                                           modeshow = 1;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(item,"wifi_auth_wps");
                                                           if (iVar1 == 0) {
                                                             modeshow = 1;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(item,"wifi_auth_wds");
                                                             if (iVar1 == 0) {
                                                               modeshow = 0;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(item,
                                                   "wifi_auth_apClient");
                                                   if (iVar1 == 0) {
                                                     modeshow = 0;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(item,"wifi_tempNetwork");
                                                     if (iVar1 == 0) {
                                                       modeshow = 0;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(item,"wifi_guest");
                                                       if (iVar1 == 0) {
                                                         modeshow = 1;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(item,"cfg_tr069");
                                                         if (iVar1 == 0) {
                                                           modeshow = 0;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(item,"cfg_ipv6");
                                                           if (iVar1 == 0) {
                                                             modeshow = 0;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(item,"wan_ipoe");
                                                             if (iVar1 == 0) {
                                                               modeshow = 0;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(item,"wan_ipoa");
                                                               if (iVar1 == 0) {
                                                                 modeshow = 0;
                                                               }
                                                               else {
                                                                 iVar1 = strcmp(item,"wan_ppoa");
                                                                 if (iVar1 == 0) {
                                                                   modeshow = 0;
                                                                 }
                                                                 else {
                                                                   iVar1 = strcmp(item,"wan_ppoe");
                                                                   if (iVar1 == 0) {
                                                                     modeshow = 1;
                                                                   }
                                                                   else {
                                                                     iVar1 = strcmp(item,"wan_static"
                                                                                   );
                                                                     if (iVar1 == 0) {
                                                                       modeshow = 1;
                                                                     }
                                                                     else {
                                                                       iVar1 = strcmp(item,"wan_dhcp"
                                                                                     );
                                                                       if (iVar1 == 0) {
                                                                         modeshow = 1;
                                                                       }
                                                                       else {
                                                                         iVar1 = strcmp(item,
                                                   "wan_pptp");
                                                   if (iVar1 == 0) {
                                                     modeshow = 1;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(item,"wan_l2tp");
                                                     if (iVar1 == 0) {
                                                       modeshow = 1;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(item,"wan_double_pptp");
                                                       if (iVar1 == 0) {
                                                         modeshow = 1;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(item,"wan_double_l2tp");
                                                         if (iVar1 == 0) {
                                                           modeshow = 1;
                                                         }
                                                         else {
                                                           iVar1 = strcmp(item,"wan_double_ppoe");
                                                           if (iVar1 == 0) {
                                                             modeshow = 1;
                                                           }
                                                           else {
                                                             iVar1 = strcmp(item,"pppoeserver");
                                                             if (iVar1 == 0) {
                                                               modeshow = 0;
                                                             }
                                                             else {
                                                               iVar1 = strcmp(item,"arpgateway");
                                                               if (iVar1 == 0) {
                                                                 modeshow = 0;
                                                               }
                                                               else {
                                                                 iVar1 = strcmp(item,"emailcc");
                                                                 if (iVar1 == 0) {
                                                                   modeshow = 0;
                                                                 }
                                                                 else {
                                                                   iVar1 = strcmp(item,"ipsec");
                                                                   if (iVar1 == 0) {
                                                                     modeshow = 0;
                                                                   }
                                                                   else {
                                                                     iVar1 = strcmp(item,"ftpserver")
                                                                     ;
                                                                     if (iVar1 == 0) {
-                                                                      modeshow = 1;
+                                                                      modeshow = 0;
                                                                     }
                                                                     else {
                                                                       iVar1 = strcmp(item,"usb");
                                                                       if (iVar1 == 0) {
-                                                                        modeshow = 1;
+                                                                        modeshow = 0;
                                                                       }
                                                                       else {
                                                                         iVar1 = strcmp(item,"ippd");
                                                                         if (iVar1 == 0) {
-                                                                          modeshow = 0;
+                                                                          modeshow = 1;
                                                                         }
                                                                         else {
                                                                           iVar1 = strcmp(item,
                                                   "samba");
                                                   if (iVar1 == 0) {
-                                                    modeshow = 1;
+                                                    modeshow = 0;
                                                   }
                                                   else {
                                                     iVar1 = strcmp(item,"bt_client");
                                                     if (iVar1 == 0) {
                                                       modeshow = 0;
                                                     }
                                                     else {
                                                       iVar1 = strcmp(item,"multi_lan");
                                                       if (iVar1 == 0) {
                                                         modeshow = 0;
                                                       }
                                                       else {
                                                         iVar1 = strcmp(item,"lan_vlan");
                                                         if (iVar1 == 0) {
                                                           modeshow = 0;
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
     iVar1 = websWrite(in_a1,"%d",modeshow);
   }
   return iVar1;
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



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.89|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_CreateObject|cJSON_CreateObject|
|fullname|cJSON_CreateObject|cJSON_CreateObject|
|`refcount`|118|113|
|length|112|112|
|called|cJSON_New_Item|cJSON_New_Item|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink</summary>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink</summary>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|
|paramcount|0|0|
|`address`|0044d1f4|0044cf84|
|sig|cJSON * cJSON_CreateObject(void)|cJSON * cJSON_CreateObject(void)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_CreateObject Calling Diff


```diff
--- cJSON_CreateObject calling
+++ cJSON_CreateObject calling
@@ -25 +24,0 @@
-formGetSambaConf
@@ -33 +31,0 @@
-formGetUSBStatus
@@ -35 +32,0 @@
-formGetUsbCfg
```


## websTransfer

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.88|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|websTransfer|websTransfer|
|fullname|websTransfer|websTransfer|
|`refcount`|101|100|
|length|160|160|
|called|websDone<br>websWrite|websDone<br>websWrite|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>GetProduct<br>addWifiMacFilter<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddMacfilterRule<br>formAliScheduleStatus<br>formDelMacfilterRule<br>formGetDeviceDetail<br>formGetOnlineList<br>formGetParentCtrlList</summary>formGetQosBand<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysToolDDNS<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetWanConnectStatus<br>formGetWifiWps<br>formSetAutoQosInfo<br>formSetClientState<br>formSetDeviceName<br>formSetMacFilterCfg<br>formSetParentControlEnable<br>formSetQosBand<br>formSetSafeWanWebMan<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetWifiWps<br>formStartWifiWps<br>formWifiAntijamSet<br>formWifiBasicGet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiDhcpGuestSet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiPowerSet<br>formWifiRadioGet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiStatisticClear<br>formWifiStatus<br>formWifiWpsGet<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_get<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>form_usb_get<br>formsetNotUpgrade<br>fromAdvSetLanip<br>fromAdvSetMacMtuWan<br>fromDhcpSetSer<br>fromGetWirelessRepeat<br>fromSetIpMacBind<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromsetApModeCfg<br>getSchedWifi<br>getSmartPowerManagement<br>mDMZSetCfg</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>GetProduct<br>addWifiMacFilter<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddMacfilterRule<br>formAliScheduleStatus<br>formDelMacfilterRule<br>formGetDeviceDetail<br>formGetOnlineList<br>formGetParentCtrlList</summary>formGetQosBand<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysToolDDNS<br>formGetUpnpLists<br>formGetWanConnectStatus<br>formGetWifiWps<br>formSetAutoQosInfo<br>formSetClientState<br>formSetDeviceName<br>formSetMacFilterCfg<br>formSetParentControlEnable<br>formSetQosBand<br>formSetSafeWanWebMan<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetWifiWps<br>formStartWifiWps<br>formWifiAntijamSet<br>formWifiBasicGet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiDhcpGuestSet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiPowerSet<br>formWifiRadioGet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiStatisticClear<br>formWifiStatus<br>formWifiWpsGet<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_get<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>form_usb_get<br>formsetNotUpgrade<br>fromAdvSetLanip<br>fromAdvSetMacMtuWan<br>fromDhcpSetSer<br>fromGetWirelessRepeat<br>fromSetIpMacBind<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromsetApModeCfg<br>getSchedWifi<br>getSmartPowerManagement<br>mDMZSetCfg</details>|
|paramcount|2|2|
|`address`|004bce44|004bc504|
|sig|void websTransfer(webs_t wp, char * output)|void websTransfer(webs_t wp, char * output)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### websTransfer Calling Diff


```diff
--- websTransfer calling
+++ websTransfer calling
@@ -17 +16,0 @@
-formGetUSBStatus
```


## cJSON_AddItemToArray

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.84|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_AddItemToArray|cJSON_AddItemToArray|
|fullname|cJSON_AddItemToArray|cJSON_AddItemToArray|
|`refcount`|46|44|
|length|204|204|
|called|suffix_object|suffix_object|
|`calling`|<details><summary>Expand for full list:<br>cJSON_AddItemReferenceToArray<br>cJSON_AddItemToObject<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRouteStatic</summary>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiDhcpGuestLists<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>cJSON_AddItemReferenceToArray<br>cJSON_AddItemToObject<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRouteStatic</summary>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiDhcpGuestLists<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>get_client_list<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>write_wan_infos</details>|
|paramcount|2|2|
|`address`|0044c6b8|0044c448|
|sig|void cJSON_AddItemToArray(cJSON * array, cJSON * item)|void cJSON_AddItemToArray(cJSON * array, cJSON * item)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_AddItemToArray Calling Diff


```diff
--- cJSON_AddItemToArray calling
+++ cJSON_AddItemToArray calling
@@ -14 +13,0 @@
-formGetUsbCfg
```


## websFormDefine

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address|
|ratio|1.0|
|i_ratio|0.88|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|websFormDefine|websFormDefine|
|fullname|websFormDefine|websFormDefine|
|`refcount`|184|177|
|length|200|200|
|called|symEnter<br>valueInteger|symEnter<br>valueInteger|
|calling|formDefineTendDa<br>formDefineUcloudv2<br>formDefineUserMgmt|formDefineTendDa<br>formDefineUcloudv2<br>formDefineUserMgmt|
|paramcount|2|2|
|`address`|00416784|00416564|
|sig|int websFormDefine(char_t * name, _func_void_webs_t_char_t_ptr_char_t_ptr * fn)|int websFormDefine(char_t * name, _func_void_webs_t_char_t_ptr_char_t_ptr * fn)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

## __ledf2

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.66|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|__ledf2|__ledf2|
|fullname|__ledf2|__ledf2|
|`refcount`|10|9|
|length|260|260|
|called|||
|`calling`|formGetUsbCfg<br>formatDataSize<br>print_number|formatDataSize<br>print_number|
|paramcount|4|4|
|`address`|005057b0|00502660|
|sig|undefined4 __stdcall __ledf2(uint param_1, uint param_2, uint param_3, uint param_4)|undefined4 __stdcall __ledf2(uint param_1, uint param_2, uint param_3, uint param_4)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### __ledf2 Calling Diff


```diff
--- __ledf2 calling
+++ __ledf2 calling
@@ -1 +0,0 @@
-formGetUsbCfg
```


## cJSON_CreateArray

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.89|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_CreateArray|cJSON_CreateArray|
|fullname|cJSON_CreateArray|cJSON_CreateArray|
|`refcount`|42|40|
|length|112|112|
|called|cJSON_New_Item|cJSON_New_Item|
|`calling`|<details><summary>Expand for full list:<br>cJSON_CreateDoubleArray<br>cJSON_CreateFloatArray<br>cJSON_CreateIntArray<br>cJSON_CreateStringArray<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus</summary>formGetQosBand<br>formGetRouteStatic<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiClientList<br>formWifiClientListAll<br>formWifiDhcpGuestLists<br>formWifiRadioGet<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>initWifiMacFilter<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>cJSON_CreateDoubleArray<br>cJSON_CreateFloatArray<br>cJSON_CreateIntArray<br>cJSON_CreateStringArray<br>formGetBlackAllInfo<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus</summary>formGetQosBand<br>formGetRouteStatic<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiApScan<br>formWifiClientList<br>formWifiClientListAll<br>formWifiDhcpGuestLists<br>formWifiRadioGet<br>formWifiStatistic<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>getDnsCheck<br>getParentControlAllInfo<br>initWifiMacFilter<br>write_wan_infos</details>|
|paramcount|0|0|
|`address`|0044d184|0044cf14|
|sig|cJSON * cJSON_CreateArray(void)|cJSON * cJSON_CreateArray(void)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_CreateArray Calling Diff


```diff
--- cJSON_CreateArray calling
+++ cJSON_CreateArray calling
@@ -16 +15,0 @@
-formGetUsbCfg
```


## cJSON_Object_2String

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.79|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_Object_2String|cJSON_Object_2String|
|fullname|cJSON_Object_2String|cJSON_Object_2String|
|`refcount`|28|26|
|length|252|252|
|called|<EXTERNAL>::free<br><EXTERNAL>::puts<br><EXTERNAL>::strlen<br><EXTERNAL>::strncpy<br>cJSON_Delete<br>cJSON_Print|<EXTERNAL>::free<br><EXTERNAL>::puts<br><EXTERNAL>::strlen<br><EXTERNAL>::strncpy<br>cJSON_Delete<br>cJSON_Print|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysLog<br>formGetSysToolDDNS<br>formGetUSBStatus<br>formGetWifiWps<br>formWifiBasicGet<br>formWifiClientList<br>formWifiClientListAll</summary>formWifiConfigGet<br>formWifiDhcpGuestGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>fromGetWirelessRepeat<br>getSchedWifi<br>getSmartPowerManagement</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysLog<br>formGetSysToolDDNS<br>formGetWifiWps<br>formWifiBasicGet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiDhcpGuestGet</summary>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>fromGetWirelessRepeat<br>getSchedWifi<br>getSmartPowerManagement</details>|
|paramcount|1|1|
|`address`|004bccd0|004bc390|
|sig|char * cJSON_Object_2String(cJSON.conflict * root)|char * cJSON_Object_2String(cJSON.conflict * root)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_Object_2String Calling Diff


```diff
--- cJSON_Object_2String calling
+++ cJSON_Object_2String calling
@@ -3 +2,0 @@
-formGetSambaConf
@@ -7 +5,0 @@
-formGetUSBStatus
```


## cJSON_AddItemToObject

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.89|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_AddItemToObject|cJSON_AddItemToObject|
|fullname|cJSON_AddItemToObject|cJSON_AddItemToObject|
|`refcount`|799|772|
|length|212|212|
|called|<EXTERNAL>::free<br>cJSON_AddItemToArray<br>cJSON_strdup|<EXTERNAL>::free<br>cJSON_AddItemToArray<br>cJSON_strdup|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>assembleChannelList2JsonArray<br>cJSON_AddItemReferenceToObject<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer</summary>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>assembleChannelList2JsonArray<br>cJSON_AddItemReferenceToObject<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer</summary>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiRadioGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>prod_new_ack<br>prod_new_up_ack<br>prod_new_ver_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic<br>write_online_upgrade_info<br>write_wan_infos</details>|
|paramcount|3|3|
|`address`|0044c784|0044c514|
|sig|void cJSON_AddItemToObject(cJSON * object, char * string, cJSON * item)|void cJSON_AddItemToObject(cJSON * object, char * string, cJSON * item)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_AddItemToObject Calling Diff


```diff
--- cJSON_AddItemToObject calling
+++ cJSON_AddItemToObject calling
@@ -27 +26,0 @@
-formGetSambaConf
@@ -35 +33,0 @@
-formGetUSBStatus
@@ -37 +34,0 @@
-formGetUsbCfg
```


## cJSON_Print

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.92|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_Print|cJSON_Print|
|fullname|cJSON_Print|cJSON_Print|
|`refcount`|61|60|
|length|96|96|
|called|print_value|print_value|
|`calling`|<details><summary>Expand for full list:<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|<details><summary>Expand for full list:<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|
|paramcount|1|1|
|`address`|0044ac80|0044aa10|
|sig|char * cJSON_Print(cJSON * item)|char * cJSON_Print(cJSON * item)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_Print Calling Diff


```diff
--- cJSON_Print calling
+++ cJSON_Print calling
@@ -30 +29,0 @@
-formGetUsbCfg
```


## setWanValue

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address|
|ratio|1.0|
|i_ratio|0.85|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|setWanValue|setWanValue|
|fullname|setWanValue|setWanValue|
|`refcount`|105|103|
|length|264|264|
|called|<EXTERNAL>::SetValue<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf|<EXTERNAL>::SetValue<br><EXTERNAL>::memset<br><EXTERNAL>::sprintf|
|calling|formWanInfoSet<br>form_fast_setting_internet_set<br>setDhcpConfig<br>setDoubleL2tpConfig<br>setDoublePppoeConfig<br>setDoublePptpConfig<br>setPppoeConfig<br>setStaticConfig<br>setWanDownrate|formWanInfoSet<br>form_fast_setting_internet_set<br>setDhcpConfig<br>setDoubleL2tpConfig<br>setDoublePppoeConfig<br>setDoublePptpConfig<br>setPppoeConfig<br>setStaticConfig<br>setWanDownrate|
|paramcount|3|3|
|`address`|00483338|00482df8|
|sig|int setWanValue(int wan_id, char * name, char * value)|int setWanValue(int wan_id, char * name, char * value)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

## cJSON_CreateString

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.9|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_CreateString|cJSON_CreateString|
|fullname|cJSON_CreateString|cJSON_CreateString|
|`refcount`|699|674|
|length|156|156|
|called|cJSON_New_Item<br>cJSON_strdup|cJSON_New_Item<br>cJSON_strdup|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>cJSON_CreateStringArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSambaConf<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUSBStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>queryaccount<br>querybasic<br>write_online_upgrade_info<br>write_wan_infos</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>cJSON_CreateStringArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg</summary>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSafeWanWebMan<br>formGetSchedLed<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSysToolDDNS<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWifiWps<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBasicGet<br>formWifiBeamformingGet<br>formWifiDhcpGuestLists<br>formWifiMacFilterGet<br>formWifiMultiSsid<br>formWifiPowerGet<br>formWifiStatistic<br>formWifiStatus<br>formWifiWpsGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWirelessRepeat<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>getSchedWifi<br>getSmartPowerManagement<br>get_client_list<br>get_index_mib_2cJSONString<br>get_mib_2cJSONString<br>get_sta_info_2cJSONArray<br>initWifiMacFilter<br>mDMZGetCfg<br>queryaccount<br>querybasic<br>write_online_upgrade_info<br>write_wan_infos</details>|
|paramcount|1|1|
|`address`|0044d0e8|0044ce78|
|sig|cJSON * cJSON_CreateString(char * string)|cJSON * cJSON_CreateString(char * string)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_CreateString Calling Diff


```diff
--- cJSON_CreateString calling
+++ cJSON_CreateString calling
@@ -26 +25,0 @@
-formGetSambaConf
@@ -34 +32,0 @@
-formGetUSBStatus
@@ -36 +33,0 @@
-formGetUsbCfg
```


## websGetVar

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.82|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|websGetVar|websGetVar|
|fullname|websGetVar|websGetVar|
|`refcount`|494|483|
|length|196|196|
|called|symLookup|symLookup|
|`calling`|<details><summary>Expand for full list:<br>GetParentControlInfo<br>R7WebsSecurityHandler<br>SetWebIpAccess<br>addWifiMacFilter<br>add_white_node<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>check_param_changed<br>cloudv2<br>cloudv2_manage</summary>cloudv2_olupgrade<br>cloudv2_wansta<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddAccessLimit<br>formAddGroup<br>formAddMacfilterRule<br>formAddUser<br>formBehaviorManager<br>formBulletinSet<br>formDelMacfilterRule<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetDeviceDetail<br>formGetWanStatus<br>formLoadUserManagement<br>formNatSet<br>formNotNowUpgrade<br>formQuickIndex<br>formSafeDemo<br>formSaveUserManagement<br>formSetAutoQosInfo<br>formSetCfm<br>formSetClientState<br>formSetDeviceName<br>formSetFirewallCfg<br>formSetIptv<br>formSetMacFilterCfg<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetParentControlEnable<br>formSetQosBand<br>formSetRebootTimer<br>formSetSafeWanWebMan<br>formSetSambaConf<br>formSetSchedLed<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetUsbPrint<br>formSetVirtualSer<br>formSetWifiWps<br>formStartWifiWps<br>formWanInfoSet<br>formWanParameterSetting<br>formWifiAntijamSet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerSet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>formWriteFacMac<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>formexeCommand<br>formsetNotUpgrade<br>formsetUsbUnload<br>fromAddressNat<br>fromAdvSetLanip<br>fromAdvSetPortVlan<br>fromDhcpListClient<br>fromDhcpSetSer<br>fromGstDhcpSetSer<br>fromLogsSetting<br>fromNatStaticSetting<br>fromSetIpBind<br>fromSetIpMacBind<br>fromSetRouteStatic<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromSysStatusHandle<br>fromSysToolBaseUser<br>fromSysToolChangePwd<br>fromSysToolTime<br>fromWanPolicy<br>fromWizardHandle<br>fromsetApModeCfg<br>getRebootStatus<br>mDMZSetCfg<br>saveParentControlInfo<br>setDhcpConfig<br>setDnsCheck<br>setDoubleL2tpConfig<br>setDoublePppoeConfig<br>setDoublePptpConfig<br>setPppoeConfig<br>setSchedWifi<br>setSmartPowerManagement<br>setStaticConfig<br>setWanDownrate<br>setWifiGusetBasic<br>setaccount<br>setbasic<br>websCompareVar<br>websGetVarWithValidate<br>websRedirect<br>websRedirectOpCookie<br>websSetEnv<br>wl_guest_conf_change</details>|<details><summary>Expand for full list:<br>GetParentControlInfo<br>R7WebsSecurityHandler<br>SetWebIpAccess<br>addWifiMacFilter<br>add_white_node<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>check_param_changed<br>cloudv2<br>cloudv2_manage</summary>cloudv2_olupgrade<br>cloudv2_wansta<br>delParentControlOneInfo<br>delWifiMacFilter<br>formAddAccessLimit<br>formAddGroup<br>formAddMacfilterRule<br>formAddUser<br>formBehaviorManager<br>formBulletinSet<br>formDelMacfilterRule<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetDeviceDetail<br>formGetWanStatus<br>formLoadUserManagement<br>formNatSet<br>formNotNowUpgrade<br>formQuickIndex<br>formSafeDemo<br>formSaveUserManagement<br>formSetAutoQosInfo<br>formSetCfm<br>formSetClientState<br>formSetDeviceName<br>formSetFirewallCfg<br>formSetIptv<br>formSetMacFilterCfg<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetParentControlEnable<br>formSetQosBand<br>formSetRebootTimer<br>formSetSafeWanWebMan<br>formSetSchedLed<br>formSetSpeedWan<br>formSetSysToolDDNS<br>formSetUpnp<br>formSetVirtualSer<br>formSetWifiWps<br>formStartWifiWps<br>formWanInfoSet<br>formWanParameterSetting<br>formWifiAntijamSet<br>formWifiBasicSet<br>formWifiBeamformingSet<br>formWifiClientList<br>formWifiClientListAll<br>formWifiConfigGet<br>formWifiMacFilterGet<br>formWifiMacFilterSet<br>formWifiMultiSsid<br>formWifiPowerSet<br>formWifiRadioSet<br>formWifiStatistic<br>formWifiWpsOOB<br>formWifiWpsSet<br>formWifiWpsStart<br>formWriteFacMac<br>form_fast_setting_internet_set<br>form_fast_setting_pppoe_set<br>form_fast_setting_wifi_set<br>formexeCommand<br>formsetNotUpgrade<br>fromAddressNat<br>fromAdvSetLanip<br>fromAdvSetPortVlan<br>fromDhcpListClient<br>fromDhcpSetSer<br>fromGstDhcpSetSer<br>fromLogsSetting<br>fromNatStaticSetting<br>fromSetIpBind<br>fromSetIpMacBind<br>fromSetRouteStatic<br>fromSetSysTime<br>fromSetWifiGusetBasic<br>fromSetWirelessRepeat<br>fromSysStatusHandle<br>fromSysToolBaseUser<br>fromSysToolChangePwd<br>fromSysToolTime<br>fromWanPolicy<br>fromWizardHandle<br>fromsetApModeCfg<br>getRebootStatus<br>mDMZSetCfg<br>saveParentControlInfo<br>setDhcpConfig<br>setDnsCheck<br>setDoubleL2tpConfig<br>setDoublePppoeConfig<br>setDoublePptpConfig<br>setPppoeConfig<br>setSchedWifi<br>setSmartPowerManagement<br>setStaticConfig<br>setWanDownrate<br>setWifiGusetBasic<br>setaccount<br>setbasic<br>websCompareVar<br>websGetVarWithValidate<br>websRedirect<br>websRedirectOpCookie<br>websSetEnv<br>wl_guest_conf_change</details>|
|paramcount|3|3|
|`address`|00430468|00430248|
|sig|char_t * websGetVar(webs_t wp, char_t * var, char_t * defaultGetValue)|char_t * websGetVar(webs_t wp, char_t * var, char_t * defaultGetValue)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### websGetVar Calling Diff


```diff
--- websGetVar calling
+++ websGetVar calling
@@ -49 +48,0 @@
-formSetSambaConf
@@ -54 +52,0 @@
-formSetUsbPrint
@@ -81 +78,0 @@
-formsetUsbUnload
```


## cJSON_Delete

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.86|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|cJSON_Delete|cJSON_Delete|
|fullname|cJSON_Delete|cJSON_Delete|
|`refcount`|81|80|
|length|320|320|
|called|<EXTERNAL>::free<br>cJSON_Delete|<EXTERNAL>::free<br>cJSON_Delete|
|`calling`|<details><summary>Expand for full list:<br>_cgi_get_sys_basic_info_<br>_cgi_query_uc_account_<br>_cgi_query_uc_manage_en_<br>_cgi_set_uc_manage_en_<br>_query_version_<br>cJSON_Delete<br>cJSON_DeleteItemFromArray<br>cJSON_DeleteItemFromObject<br>cJSON_Duplicate<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan</summary>cJSON_ParseWithOpts<br>cJSON_ReplaceItemInArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetUsbCfg<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>formWifiMacFilterGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>parse_response_string<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|<details><summary>Expand for full list:<br>_cgi_get_sys_basic_info_<br>_cgi_query_uc_account_<br>_cgi_query_uc_manage_en_<br>_cgi_set_uc_manage_en_<br>_query_version_<br>cJSON_Delete<br>cJSON_DeleteItemFromArray<br>cJSON_DeleteItemFromObject<br>cJSON_Duplicate<br>cJSON_Object_2String<br>cJSON_Object_2String_apscan</summary>cJSON_ParseWithOpts<br>cJSON_ReplaceItemInArray<br>formAdvGetLanIp<br>formGetAdvanceStatus<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUpnpLists<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanConnectStatus<br>formGetWanParameter<br>formGetWanStatistic<br>formWifiAntijamGet<br>formWifiBeamformingGet<br>formWifiMacFilterGet<br>form_SyncAccount_get<br>form_fast_setting_get<br>form_fast_setting_pppoe_get<br>form_usb_get<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSysToolGetUpgrade<br>fromgetApModeCfg<br>getAdvanceStatus<br>getParentControlAllInfo<br>getRebootStatus<br>mDMZGetCfg<br>parse_response_string<br>prod_new_ack<br>queryaccount<br>querybasic<br>setaccount<br>setbasic</details>|
|paramcount|1|1|
|`address`|00449500|00449290|
|sig|void cJSON_Delete(cJSON * c)|void cJSON_Delete(cJSON * c)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### cJSON_Delete Calling Diff


```diff
--- cJSON_Delete calling
+++ cJSON_Delete calling
@@ -41 +40,0 @@
-formGetUsbCfg
```


## websDone

### Match Info



|Key|AC9_httpd - AC12_httpd|
| :---: | :---: |
|diff_type|refcount,address,calling|
|ratio|1.0|
|i_ratio|0.87|
|m_ratio|1.0|
|b_ratio|1.0|
|match_types|SymbolsHash|

### Function Meta Diff



|Key|AC9_httpd|AC12_httpd|
| :---: | :---: | :---: |
|name|websDone|websDone|
|fullname|websDone|websDone|
|`refcount`|151|144|
|length|712|712|
|called|<details><summary>Expand for full list:<br>ringqFlush<br>socketCloseConnection<br>socketCreateHandler<br>socketDeleteHandler<br>socketFlush<br>socketSetBlock<br>websFree<br>websPageClose<br>websSSLFlush<br>websSchedCallBack<br>websTimeoutCancel</summary></details>|<details><summary>Expand for full list:<br>ringqFlush<br>socketCloseConnection<br>socketCreateHandler<br>socketDeleteHandler<br>socketFlush<br>socketSetBlock<br>websFree<br>websPageClose<br>websSSLFlush<br>websSchedCallBack<br>websTimeoutCancel</summary></details>|
|`calling`|<details><summary>Expand for full list:<br>DownloadCfg<br>DownloadFlash<br>DownloadLog<br>DownloadWebsite<br>R7WebsSecurityHandler<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>add_white_node<br>cgi_clear_arp_info<br>cgi_clear_ddos_fence</summary>cgi_clear_ip_opt<br>cgi_get_arp_info<br>cgi_get_ddos_fence<br>cgi_get_ip_opt<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>cloudv2_manage<br>cloudv2_olupgrade<br>cloudv2_wansta<br>file_clear<br>file_option<br>file_show<br>formAddAccessLimit<br>formAddGroup<br>formAddUser<br>formAdvGetLanIp<br>formBehaviorManager<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSambaConf<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetUsbCfg<br>formGetUsbPrint<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formLoadUserManagement<br>formMfgTest<br>formNotNowUpgrade<br>formSaveUserManagement<br>formSetFirewallCfg<br>formSetIptv<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetRebootTimer<br>formSetSambaConf<br>formSetSchedLed<br>formSetUsbPrint<br>formSetVirtualSer<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBeamformingGet<br>formWriteFacMac<br>formexeCommand<br>formgetPptpOnlineClient<br>formsetUsbUnload<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSetRouteStatic<br>fromSysStatusHandle<br>fromSysToolGetUpgrade<br>fromSysToolSetUpgrade<br>fromWizardHandle<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>get_online_ip_info<br>initWifiMacFilter<br>key_clear<br>key_option<br>key_show<br>mDMZGetCfg<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websCgiCleanup<br>websDefaultHandler<br>websDefaultWriteEvent<br>websFileDownUpCleanup<br>websGetInput<br>websResponse<br>websResponseOpCookie<br>websTimeout<br>websTransfer<br>write_ddos_fence_info<br>write_ipopt_fence_info</details>|<details><summary>Expand for full list:<br>DownloadCfg<br>DownloadFlash<br>DownloadLog<br>DownloadWebsite<br>R7WebsSecurityHandler<br>SysToolpassword<br>TendaAte<br>TendaTelnet<br>add_white_node<br>cgi_clear_arp_info<br>cgi_clear_ddos_fence</summary>cgi_clear_ip_opt<br>cgi_get_arp_info<br>cgi_get_ddos_fence<br>cgi_get_ip_opt<br>cgi_set_arp_info<br>cgi_set_ddos_fence<br>cgi_set_ip_opt<br>cloudv2_manage<br>cloudv2_olupgrade<br>cloudv2_wansta<br>file_clear<br>file_option<br>file_show<br>formAddAccessLimit<br>formAddGroup<br>formAddUser<br>formAdvGetLanIp<br>formBehaviorManager<br>formDeleteAccessLimit<br>formDeleteGroup<br>formDeleteUser<br>formDisplayUser<br>formGetAdvanceStatus<br>formGetAllWanInfo<br>formGetAutoQosInfo<br>formGetBandWidthSpeed<br>formGetBlackAllInfo<br>formGetDdosDefenceList<br>formGetDeviceDetail<br>formGetDhcpServer<br>formGetFirewallCfg<br>formGetHomeLink<br>formGetIptv<br>formGetMacFilterCfg<br>formGetMacfilterRuleList<br>formGetOnlineList<br>formGetPPTPClient<br>formGetPPTPServer<br>formGetParentCtrlList<br>formGetPortStatus<br>formGetQosBand<br>formGetRebootTimer<br>formGetRouteStatic<br>formGetRouterStatus<br>formGetSysInfo<br>formGetSysLog<br>formGetSysStatus<br>formGetSystemSet<br>formGetSystemStatus<br>formGetVirtualSer<br>formGetVpnStatus<br>formGetWanNum<br>formGetWanParameter<br>formGetWanStatistic<br>formGetWanStatus<br>formLoadUserManagement<br>formMfgTest<br>formNotNowUpgrade<br>formSaveUserManagement<br>formSetFirewallCfg<br>formSetIptv<br>formSetPPTPClient<br>formSetPPTPServer<br>formSetPPTPUserList<br>formSetRebootTimer<br>formSetSchedLed<br>formSetVirtualSer<br>formTendaGetDhcpClients<br>formTendaGetGuestDhcpClients<br>formWanParameterSetting<br>formWifiAntijamGet<br>formWifiApScan<br>formWifiBeamformingGet<br>formWriteFacMac<br>formexeCommand<br>formgetPptpOnlineClient<br>fromAdvGetMacMtuWan<br>fromGetIpMacBind<br>fromGetSysTime<br>fromGetWifiGusetBasic<br>fromGetWrlStatus<br>fromSetRouteStatic<br>fromSysStatusHandle<br>fromSysToolGetUpgrade<br>fromSysToolSetUpgrade<br>fromWizardHandle<br>fromgetApModeCfg<br>getAdvanceStatus<br>getDnsCheck<br>getParentControlAllInfo<br>getRebootStatus<br>get_online_ip_info<br>initWifiMacFilter<br>key_clear<br>key_option<br>key_show<br>mDMZGetCfg<br>saveParentControlInfo<br>setDnsCheck<br>setSchedWifi<br>setSmartPowerManagement<br>updateUrlLog<br>websCgiCleanup<br>websDefaultHandler<br>websDefaultWriteEvent<br>websFileDownUpCleanup<br>websGetInput<br>websResponse<br>websResponseOpCookie<br>websTimeout<br>websTransfer<br>write_ddos_fence_info<br>write_ipopt_fence_info</details>|
|paramcount|2|2|
|`address`|00431868|00431648|
|sig|void websDone(webs_t wp, int code)|void websDone(webs_t wp, int code)|
|sym_type|Function|Function|
|sym_source|IMPORTED|IMPORTED|
|external|False|False|

### websDone Calling Diff


```diff
--- websDone calling
+++ websDone calling
@@ -56 +55,0 @@
-formGetSambaConf
@@ -62,2 +60,0 @@
-formGetUsbCfg
-formGetUsbPrint
@@ -80 +76,0 @@
-formSetSambaConf
@@ -82 +77,0 @@
-formSetUsbPrint
@@ -93 +87,0 @@
-formsetUsbUnload
```




<sub>Generated with `ghidriff` version: 0.8.0 on 2025-04-24T15:16:04</sub>