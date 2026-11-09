# 函数字符串参数使用统计报告

## 分析目标
- 二进制文件: httpd
- 原始文件名: httpd
- 二进制路径: /root/FHFuzz/firmware_SaTC/D-Link/DIR-825/_DIR825B1_FW206WWB05.bin.extracted/squashfs-root/sbin/httpd
- 总参数名数量: 965
- 程序中总字符串数量: 3596
- 发现的使用函数数量: 54

## 函数使用频率统计 (按使用次数降序排列)

| 排名 | 函数名 | 使用次数 | 精确匹配数 | 部分匹配数 |
|------|--------|----------|------------|------------|
| 1 | `nvram_safe_get` | 356 | 159 | 197 |
| 2 | `sprintf` | 344 | 0 | 344 |
| 3 | `strlen` | 318 | 1 | 317 |
| 4 | `nvram_set` | 135 | 84 | 51 |
| 5 | `nvram_match` | 57 | 39 | 18 |
| 6 | `strcmp` | 46 | 18 | 28 |
| 7 | `FUN_00432c20` | 39 | 27 | 12 |
| 8 | `strstr` | 29 | 6 | 23 |
| 9 | `puts` | 19 | 0 | 19 |
| 10 | `FUN_00436654` | 16 | 0 | 16 |
| 11 | `nvram_get` | 16 | 7 | 9 |
| 12 | `fopen` | 14 | 0 | 14 |
| 13 | `printf` | 11 | 0 | 11 |
| 14 | `get_cgi` | 11 | 6 | 5 |
| 15 | `sleep` | 8 | 0 | 8 |
| 16 | `_system` | 8 | 0 | 8 |
| 17 | `FUN_00434f28` | 7 | 0 | 7 |
| 18 | `FUN_00434158` | 6 | 0 | 6 |
| 19 | `FUN_00435b3c` | 5 | 0 | 5 |
| 20 | `wfprintf` | 5 | 0 | 5 |
| 21 | `__assert` | 5 | 0 | 5 |
| 22 | `FUN_0043f504` | 4 | 0 | 4 |
| 23 | `save2file` | 4 | 0 | 4 |
| 24 | `absolute_path` | 4 | 0 | 4 |
| 25 | `nvram_commit` | 4 | 0 | 4 |
| 26 | `artblock_safe_get` | 4 | 4 | 0 |
| 27 | `strcasecmp` | 3 | 1 | 2 |
| 28 | `create_device_name_plus_mac` | 3 | 1 | 2 |
| 29 | `strncmp` | 3 | 1 | 2 |
| 30 | `logout` | 3 | 0 | 3 |
| 31 | `artblock_get` | 3 | 2 | 1 |
| 32 | `strcpy` | 2 | 0 | 2 |
| 33 | `FUN_0040b7d0` | 2 | 0 | 2 |
| 34 | `nvram_flag_set` | 2 | 1 | 1 |
| 35 | `artblock_fast_get` | 2 | 0 | 2 |
| 36 | `wan_statue` | 2 | 1 | 1 |
| 37 | `unlink` | 2 | 0 | 2 |
| 38 | `snprintf` | 2 | 0 | 2 |
| 39 | `fgets` | 2 | 0 | 2 |
| 40 | `get_old_value_by_file` | 2 | 2 | 0 |
| 41 | `fwrite` | 2 | 0 | 2 |
| 42 | `FUN_0040e9f0` | 2 | 0 | 2 |
| 43 | `system` | 2 | 0 | 2 |
| 44 | `FUN_00437090` | 1 | 0 | 1 |
| 45 | `strncasecmp` | 1 | 0 | 1 |
| 46 | `init_file` | 1 | 0 | 1 |
| 47 | `get_ipaddr` | 1 | 0 | 1 |
| 48 | `read_pid` | 1 | 0 | 1 |
| 49 | `lease_time_execute` | 1 | 0 | 1 |
| 50 | `memset` | 1 | 0 | 1 |
| 51 | `usleep` | 1 | 0 | 1 |
| 52 | `clear_login_list` | 1 | 0 | 1 |
| 53 | `FUN_0043f484` | 1 | 0 | 1 |
| 54 | `popen` | 1 | 0 | 1 |

## 详细使用信息 (Top 15)

### 1. 函数: `nvram_safe_get` (使用次数: 356)

#### 精确匹配 (159 次)

**字符串**: `DHCPServerEnabled`
- 调用地址: `00439c0c`
- 引用地址: `00439bf4`
- 参数位置: 2
- 包含函数: `FUN_00439b20`
- 搜索距离: 6 条指令

**字符串**: `ddns_enable`
- 调用地址: `00444cc0`
- 引用地址: `00444cb4`
- 参数位置: 0
- 包含函数: `create_ddns_xml`
- 搜索距离: 3 条指令

**字符串**: `graph_auth_enable`
- 调用地址: `00419e0c`
- 引用地址: `00419e08`
- 参数位置: 0
- 包含函数: `FUN_00419d0c`
- 搜索距离: 1 条指令

**字符串**: `ipv6_static_default_gw`
- 调用地址: `0042b21c`
- 引用地址: `0042b1d0`
- 参数位置: 0
- 包含函数: `read_ipv6defaultgatewy`
- 搜索距离: 19 条指令

**字符串**: `lan_ipaddr`
- 调用地址: `00425664`
- 引用地址: `00425658`
- 参数位置: 0
- 包含函数: `commit_nvram_config`
- 搜索距离: 3 条指令

#### 部分匹配 (197 次)

**目标子串**: `Enabled`
- 完整字符串: `DHCPServerEnabled`
- 调用地址: `00439c0c`
- 引用地址: `00439bf4`
- 参数位置: 2
- 包含函数: `FUN_00439b20`
- 搜索距离: 6 条指令

**目标子串**: `Enabled`
- 完整字符串: `DHCPServerEnabled`
- 调用地址: `00439c40`
- 引用地址: `00439bf4`
- 参数位置: 2
- 包含函数: `FUN_00439b20`
- 搜索距离: 19 条指令

**目标子串**: `SSID`
- 完整字符串: `SSID: %s
<br />`
- 调用地址: `00416e28`
- 引用地址: `00416e08`
- 参数位置: 1
- 包含函数: `FUN_00416814`
- 搜索距离: 8 条指令

**目标子串**: `auto_channel`
- 完整字符串: `wlan0_auto_channel_enable`
- 调用地址: `0044e964`
- 引用地址: `0044e960`
- 参数位置: 0
- 包含函数: `do_widget_action`
- 搜索距离: 1 条指令

**目标子串**: `auto_channel`
- 完整字符串: `<wlan_auto_channel_enable>%s</wlan_auto_channel_enable>`
- 调用地址: `0044e99c`
- 引用地址: `0044e960`
- 参数位置: 1
- 包含函数: `do_widget_action`
- 搜索距离: 15 条指令

---

### 2. 函数: `sprintf` (使用次数: 344)

#### 部分匹配 (344 次)

**目标子串**: `Channel`
- 完整字符串: `<RadioID %s>RADIO_5GHz</RadioID><Frequency %s>5</Frequency><SupportedModes %s><string>802.11a</string><string>802.11n</string><string>802.11an</string></SupportedModes><Channels %s>%s</Channels><WideChannels %s>%s</WideChannels><SupportedSecurity %s>%s</SupportedSecurity>`
- 调用地址: `0043d934`
- 引用地址: `0043d900`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 13 条指令

**目标子串**: `Channel`
- 完整字符串: `<RadioID %s>RADIO_5GHz</RadioID><Frequency %s>5</Frequency><SupportedModes %s><string>802.11a</string><string>802.11n</string><string>802.11an</string></SupportedModes><Channels %s>%s</Channels><WideChannels %s>%s</WideChannels><SupportedSecurity %s>%s</SupportedSecurity>`
- 调用地址: `0043ea2c`
- 引用地址: `0043e9f4`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 14 条指令

**目标子串**: `Channel`
- 完整字符串: `<RadioID %s>RADIO_5GHz</RadioID><Frequency %s>5</Frequency><SupportedModes %s><string>802.11a</string><string>802.11n</string><string>802.11an</string></SupportedModes><Channels %s>%s</Channels><WideChannels %s>%s</WideChannels><SupportedSecurity %s>%s</SupportedSecurity>`
- 调用地址: `0043ee38`
- 引用地址: `0043ee08`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 12 条指令

**目标子串**: `Channel`
- 完整字符串: `<RadioID %s>RADIO_24GHz</RadioID><Frequency %s>2</Frequency><SupportedModes %s><string>802.11b</string><string>802.11g</string><string>802.11n</string><string>802.11bg</string><string>802.11gn</string><string>802.11bgn</string></SupportedModes><Channels %s>%s</Channels><WideChannels %s>%s</WideChannels><SupportedSecurity %s>%s</SupportedSecurity>`
- 调用地址: `0043d82c`
- 引用地址: `0043d81c`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 4 条指令

**目标子串**: `Channel`
- 完整字符串: `<RadioID %s>RADIO_24GHz</RadioID><Frequency %s>2</Frequency><SupportedModes %s><string>802.11b</string><string>802.11g</string><string>802.11n</string><string>802.11bg</string><string>802.11gn</string><string>802.11bgn</string></SupportedModes><Channels %s>%s</Channels><WideChannels %s>%s</WideChannels><SupportedSecurity %s>%s</SupportedSecurity>`
- 调用地址: `0043ef70`
- 引用地址: `0043ef64`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 3 条指令

---

### 3. 函数: `strlen` (使用次数: 318)

#### 精确匹配 (1 次)

**字符串**: `routing_table`
- 调用地址: `004220c8`
- 引用地址: `004220c4`
- 参数位置: 0
- 包含函数: `ej_cmo_get_list`
- 搜索距离: 1 条指令

#### 部分匹配 (317 次)

**目标子串**: `<% CmoGetCfg(`
- 完整字符串: `<% CmoGetCfg("countdown_time","none"); %>`
- 调用地址: `0040f3e4`
- 引用地址: `0040f3cc`
- 参数位置: 0
- 包含函数: `redirect_count_down_page`
- 搜索距离: 6 条指令

**目标子串**: `<% CmoGetCfg(`
- 完整字符串: `<% CmoGetCfg("countdown_time","none"); %>`
- 调用地址: `0040f3e4`
- 引用地址: `0040f3cc`
- 参数位置: 1
- 包含函数: `redirect_count_down_page`
- 搜索距离: 6 条指令

**目标子串**: `<% CmoGetCfg(`
- 完整字符串: `<% CmoGetCfg("html_response_return_page","none"); %>`
- 调用地址: `0040f1e0`
- 引用地址: `0040f1b8`
- 参数位置: 0
- 包含函数: `redirect_count_down_page`
- 搜索距离: 10 条指令

**目标子串**: `<% CmoGetCfg(`
- 完整字符串: `<% CmoGetCfg("html_response_return_page","none"); %>`
- 调用地址: `0040f1e0`
- 引用地址: `0040f1b8`
- 参数位置: 1
- 包含函数: `redirect_count_down_page`
- 搜索距离: 10 条指令

**目标子串**: `<% CmoGetCfg(`
- 完整字符串: `<% CmoGetCfg("html_response_return_page","none"); %>`
- 调用地址: `0040f1e0`
- 引用地址: `0040f1dc`
- 参数位置: 0
- 包含函数: `redirect_count_down_page`
- 搜索距离: 1 条指令

---

### 4. 函数: `nvram_set` (使用次数: 135)

#### 精确匹配 (84 次)

**字符串**: `asp_temp_37`
- 调用地址: `0043bdc0`
- 引用地址: `0043bdbc`
- 参数位置: 0
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**字符串**: `asp_temp_37`
- 调用地址: `0043bfb8`
- 引用地址: `0043bfb4`
- 参数位置: 0
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**字符串**: `asp_temp_53`
- 调用地址: `0043b4f8`
- 引用地址: `0043b4f4`
- 参数位置: 0
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**字符串**: `asp_temp_53`
- 调用地址: `0043c704`
- 引用地址: `0043c700`
- 参数位置: 0
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**字符串**: `blank_status`
- 调用地址: `0043c3e8`
- 引用地址: `0043c3e4`
- 参数位置: 0
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

#### 部分匹配 (51 次)

**目标子串**: `auto_channel`
- 完整字符串: `wlan0_auto_channel_enable`
- 调用地址: `0043bcc0`
- 引用地址: `0043bcbc`
- 参数位置: 0
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**目标子串**: `auto_channel`
- 完整字符串: `wlan1_auto_channel_enable`
- 调用地址: `0043c068`
- 引用地址: `0043c064`
- 参数位置: 0
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**目标子串**: `d_enable`
- 完整字符串: `dhcpd_enable`
- 调用地址: `00439d40`
- 引用地址: `00439d3c`
- 参数位置: 0
- 包含函数: `FUN_00439b20`
- 搜索距离: 1 条指令

**目标子串**: `d_enable`
- 完整字符串: `dhcpd_enable`
- 调用地址: `00439d64`
- 引用地址: `00439d3c`
- 参数位置: 0
- 包含函数: `FUN_00439b20`
- 搜索距离: 10 条指令

**目标子串**: `d_enable`
- 完整字符串: `dhcpd_enable`
- 调用地址: `00439d64`
- 引用地址: `00439d60`
- 参数位置: 0
- 包含函数: `FUN_00439b20`
- 搜索距离: 1 条指令

---

### 5. 函数: `nvram_match` (使用次数: 57)

#### 精确匹配 (39 次)

**字符串**: `admin_password`
- 调用地址: `0041b7e0`
- 引用地址: `0041b7dc`
- 参数位置: 0
- 包含函数: `set_basic_api`
- 搜索距离: 1 条指令

**字符串**: `auto_uplink`
- 调用地址: `0043174c`
- 引用地址: `00431730`
- 参数位置: 0
- 包含函数: `if_measure_now`
- 搜索距离: 7 条指令

**字符串**: `ddns_enable`
- 调用地址: `0042077c`
- 引用地址: `00420778`
- 参数位置: 0
- 包含函数: `return_ddns_status`
- 搜索距离: 1 条指令

**字符串**: `dhcpd_enable`
- 调用地址: `00428938`
- 引用地址: `00428934`
- 参数位置: 0
- 包含函数: `get_dhcp_client_list`
- 搜索距离: 1 条指令

**字符串**: `ipv6_pppoe_share`
- 调用地址: `0045973c`
- 引用地址: `00459738`
- 参数位置: 0
- 包含函数: `do_ajax_action`
- 搜索距离: 1 条指令

#### 部分匹配 (18 次)

**目标子串**: `auto_channel`
- 完整字符串: `wlan0_auto_channel_enable`
- 调用地址: `00435700`
- 引用地址: `004356fc`
- 参数位置: 0
- 包含函数: `FUN_00434f28`
- 搜索距离: 1 条指令

**目标子串**: `auto_channel`
- 完整字符串: `wlan1_auto_channel_enable`
- 调用地址: `00435248`
- 引用地址: `00435244`
- 参数位置: 0
- 包含函数: `FUN_00434f28`
- 搜索距离: 1 条指令

**目标子串**: `auto_channel`
- 完整字符串: `wlan1_auto_channel_enable`
- 调用地址: `00435468`
- 引用地址: `00435464`
- 参数位置: 0
- 包含函数: `FUN_00434f28`
- 搜索距离: 1 条指令

**目标子串**: `d_enable`
- 完整字符串: `dhcpd_enable`
- 调用地址: `00428938`
- 引用地址: `00428934`
- 参数位置: 0
- 包含函数: `get_dhcp_client_list`
- 搜索距离: 1 条指令

**目标子串**: `dhcp`
- 完整字符串: `dhcpd_enable`
- 调用地址: `00428938`
- 引用地址: `00428934`
- 参数位置: 0
- 包含函数: `get_dhcp_client_list`
- 搜索距离: 1 条指令

---

### 6. 函数: `strcmp` (使用次数: 46)

#### 精确匹配 (18 次)

**字符串**: `Enabled`
- 调用地址: `00458830`
- 引用地址: `0045882c`
- 参数位置: 1
- 包含函数: `do_ajax_action`
- 搜索距离: 1 条指令

**字符串**: `asp_temp_34`
- 调用地址: `00423270`
- 引用地址: `0042326c`
- 参数位置: 1
- 包含函数: `ej_cmo_get_cfg`
- 搜索距离: 1 条指令

**字符串**: `asp_temp_35`
- 调用地址: `004231b0`
- 引用地址: `004231ac`
- 参数位置: 1
- 包含函数: `ej_cmo_get_cfg`
- 搜索距离: 1 条指令

**字符串**: `asp_temp_38`
- 调用地址: `00423290`
- 引用地址: `0042328c`
- 参数位置: 1
- 包含函数: `ej_cmo_get_cfg`
- 搜索距离: 1 条指令

**字符串**: `dhcpd_domain_name`
- 调用地址: `00422df4`
- 引用地址: `00422df0`
- 参数位置: 1
- 包含函数: `ej_cmo_get_cfg`
- 搜索距离: 1 条指令

#### 部分匹配 (28 次)

**目标子串**: `dhcp`
- 完整字符串: `dhcpd_domain_name`
- 调用地址: `00422df4`
- 引用地址: `00422df0`
- 参数位置: 1
- 包含函数: `ej_cmo_get_cfg`
- 搜索距离: 1 条指令

**目标子串**: `dhcp`
- 完整字符串: `dhcpc`
- 调用地址: `004558d0`
- 引用地址: `004558cc`
- 参数位置: 1
- 包含函数: `get_internetonline_check`
- 搜索距离: 1 条指令

**目标子串**: `dhcp`
- 完整字符串: `dhcpc`
- 调用地址: `00420f20`
- 引用地址: `00420f1c`
- 参数位置: 1
- 包含函数: `return_internetonline_check`
- 搜索距离: 1 条指令

**目标子串**: `dhcp`
- 完整字符串: `dhcpc`
- 调用地址: `004301bc`
- 引用地址: `004301b4`
- 参数位置: 1
- 包含函数: `get_napt_session`
- 搜索距离: 2 条指令

**目标子串**: `dhcp`
- 完整字符串: `dhcpc`
- 调用地址: `0042c2f8`
- 引用地址: `0042c2f4`
- 参数位置: 1
- 包含函数: `wan_statue`
- 搜索距离: 1 条指令

---

### 7. 函数: `FUN_00432c20` (使用次数: 39)

#### 精确匹配 (27 次)

**字符串**: `AutoReconnect`
- 调用地址: `0043839c`
- 引用地址: `00438398`
- 参数位置: 2
- 包含函数: `FUN_004381b4`
- 搜索距离: 1 条指令

**字符串**: `Channel`
- 调用地址: `0043ae44`
- 引用地址: `0043ae40`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**字符串**: `Channel`
- 调用地址: `0043a524`
- 引用地址: `0043a51c`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 2 条指令

**字符串**: `Channel`
- 调用地址: `0043a524`
- 引用地址: `0043a4fc`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 10 条指令

**字符串**: `DeviceName`
- 调用地址: `0043a944`
- 引用地址: `0043a940`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

#### 部分匹配 (12 次)

**目标子串**: `Channel`
- 完整字符串: `ChannelWidth`
- 调用地址: `0043a504`
- 引用地址: `0043a4fc`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 2 条指令

**目标子串**: `Channel`
- 完整字符串: `SecondaryChannel`
- 调用地址: `0043a540`
- 引用地址: `0043a53c`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**目标子串**: `IPAddress`
- 完整字符串: `RouterIPAddress`
- 调用地址: `00439bb4`
- 引用地址: `00439b64`
- 参数位置: 2
- 包含函数: `FUN_00439b20`
- 搜索距离: 20 条指令

**目标子串**: `Name`
- 完整字符串: `DeviceName`
- 调用地址: `0043a944`
- 引用地址: `0043a940`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

**目标子串**: `SSID`
- 完整字符串: `SSIDBroadcast`
- 调用地址: `0043ae24`
- 引用地址: `0043ae20`
- 参数位置: 2
- 包含函数: `FUN_00439f24`
- 搜索距离: 1 条指令

---

### 8. 函数: `strstr` (使用次数: 29)

#### 精确匹配 (6 次)

**字符串**: `Channel`
- 调用地址: `0041e928`
- 引用地址: `0041e924`
- 参数位置: 1
- 包含函数: `return_wireless_ap_scan_list`
- 搜索距离: 1 条指令

**字符串**: `lan_stats`
- 调用地址: `00440388`
- 引用地址: `00440384`
- 参数位置: 1
- 包含函数: `get_widget_info`
- 搜索距离: 1 条指令

**字符串**: `lan_stats`
- 调用地址: `00440388`
- 引用地址: `00440324`
- 参数位置: 1
- 包含函数: `get_widget_info`
- 搜索距离: 25 条指令

**字符串**: `routing_table`
- 调用地址: `00440508`
- 引用地址: `00440504`
- 参数位置: 1
- 包含函数: `get_widget_info`
- 搜索距离: 1 条指令

**字符串**: `wan_stats`
- 调用地址: `004403c8`
- 引用地址: `004403c4`
- 参数位置: 1
- 包含函数: `get_widget_info`
- 搜索距离: 1 条指令

#### 部分匹配 (23 次)

**目标子串**: `<% CmoGetCfg(`
- 完整字符串: `<% CmoGetCfg("html_response_return_page","none"); %>`
- 调用地址: `0040f1bc`
- 引用地址: `0040f1b8`
- 参数位置: 1
- 包含函数: `redirect_count_down_page`
- 搜索距离: 1 条指令

**目标子串**: `<% CmoGetCfg(`
- 完整字符串: `<% CmoGetCfg("html_response_message","none"); %>`
- 调用地址: `0040f258`
- 引用地址: `0040f254`
- 参数位置: 1
- 包含函数: `redirect_count_down_page`
- 搜索距离: 1 条指令

**目标子串**: `ForwardedPorts`
- 完整字符串: `SetForwardedPorts`
- 调用地址: `00433390`
- 引用地址: `00433354`
- 参数位置: 1
- 包含函数: `get_pure_content`
- 搜索距离: 15 条指令

**目标子串**: `SSID`
- 完整字符串: `ESSID`
- 调用地址: `0041e868`
- 引用地址: `0041e864`
- 参数位置: 1
- 包含函数: `return_wireless_ap_scan_list`
- 搜索距离: 1 条指令

**目标子串**: `device`
- 完整字符串: `device.xml=`
- 调用地址: `0040d410`
- 引用地址: `0040d40c`
- 参数位置: 1
- 包含函数: `FUN_0040ba90`
- 搜索距离: 1 条指令

---

### 9. 函数: `puts` (使用次数: 19)

#### 部分匹配 (19 次)

**目标子串**: `Channel`
- 完整字符串: `<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><soap:Body><GetWLanRadioSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanRadioSettingsResult>%s</GetWLanRadioSettingsResult><Enabled>%s</Enabled><Mode>%s</Mode><MacAddress>%s</MacAddress><SSID>%s</SSID><SSIDBroadcast>%s</SSIDBroadcast><ChannelWidth>%s</ChannelWidth><Channel>%s</Channel><SecondaryChannel>%s</SecondaryChannel><QoS>%s</QoS></GetWLanRadioSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043d5ac`
- 引用地址: `0043d580`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 11 条指令

**目标子串**: `Enabled`
- 完整字符串: `<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><soap:Body><GetWLanRadioSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanRadioSettingsResult>%s</GetWLanRadioSettingsResult><Enabled>%s</Enabled><Mode>%s</Mode><MacAddress>%s</MacAddress><SSID>%s</SSID><SSIDBroadcast>%s</SSIDBroadcast><ChannelWidth>%s</ChannelWidth><Channel>%s</Channel><SecondaryChannel>%s</SecondaryChannel><QoS>%s</QoS></GetWLanRadioSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043d564`
- 引用地址: `0043d538`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 11 条指令

**目标子串**: `Enabled`
- 完整字符串: `<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><soap:Body><GetWLanRadioSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanRadioSettingsResult>%s</GetWLanRadioSettingsResult><Enabled>%s</Enabled><Mode>%s</Mode><MacAddress>%s</MacAddress><SSID>%s</SSID><SSIDBroadcast>%s</SSIDBroadcast><ChannelWidth>%s</ChannelWidth><Channel>%s</Channel><SecondaryChannel>%s</SecondaryChannel><QoS>%s</QoS></GetWLanRadioSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043d5ac`
- 引用地址: `0043d538`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 29 条指令

**目标子串**: `Enabled`
- 完整字符串: `<?xml version="1.0" encoding="UTF-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><soap:Body><GetWLanRadioSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanRadioSettingsResult>%s</GetWLanRadioSettingsResult><Enabled>%s</Enabled><Mode>%s</Mode><MacAddress>%s</MacAddress><SSID>%s</SSID><SSIDBroadcast>%s</SSIDBroadcast><ChannelWidth>%s</ChannelWidth><Channel>%s</Channel><SecondaryChannel>%s</SecondaryChannel><QoS>%s</QoS></GetWLanRadioSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043d5ac`
- 引用地址: `0043d580`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 11 条指令

**目标子串**: `GetNetworkStatsResult`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetNetworkStatsResponse xmlns="http://purenetworks.com/HNAP1/"><GetNetworkStatsResult>OK</GetNetworkStatsResult><Stats><NetworkStats><PortName>LAN</PortName><PacketsReceived>%s</PacketsReceived><PacketsSent>%s</PacketsSent><BytesReceived>%s</BytesReceived><BytesSent>%s</BytesSent></NetworkStats><NetworkStats><PortName>WLAN 802.11g</PortName><PacketsReceived>%s</PacketsReceived><PacketsSent>%s</PacketsSent><BytesReceived>%s</BytesReceived><BytesSent>%s</BytesSent></NetworkStats></Stats></GetNetworkStatsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043d41c`
- 引用地址: `0043d3dc`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 16 条指令

---

### 10. 函数: `FUN_00436654` (使用次数: 16)

#### 部分匹配 (16 次)

**目标子串**: `AutoReconnect`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWanSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWanSettingsResult>%s</GetWanSettingsResult><Type>%s</Type><Username>%s</Username><Password>%s</Password><MaxIdleTime>%s</MaxIdleTime><ServiceName>%s</ServiceName><AutoReconnect>%s</AutoReconnect><IPAddress>%s</IPAddress><SubnetMask>%s</SubnetMask><Gateway>%s</Gateway><DNS><Primary>%s</Primary><Secondary>%s</Secondary></DNS><OpenDNS><enable>%s</enable></OpenDNS><MacAddress>%s</MacAddress><MTU>%s</MTU></GetWanSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e038`
- 引用地址: `0043e030`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 2 条指令

**目标子串**: `Gateway`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWanSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWanSettingsResult>%s</GetWanSettingsResult><Type>%s</Type><Username>%s</Username><Password>%s</Password><MaxIdleTime>%s</MaxIdleTime><ServiceName>%s</ServiceName><AutoReconnect>%s</AutoReconnect><IPAddress>%s</IPAddress><SubnetMask>%s</SubnetMask><Gateway>%s</Gateway><DNS><Primary>%s</Primary><Secondary>%s</Secondary></DNS><OpenDNS><enable>%s</enable></OpenDNS><MacAddress>%s</MacAddress><MTU>%s</MTU></GetWanSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e038`
- 引用地址: `0043e030`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 2 条指令

**目标子串**: `GetWanSettingsResult`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWanSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWanSettingsResult>%s</GetWanSettingsResult><Type>%s</Type><Username>%s</Username><Password>%s</Password><MaxIdleTime>%s</MaxIdleTime><ServiceName>%s</ServiceName><AutoReconnect>%s</AutoReconnect><IPAddress>%s</IPAddress><SubnetMask>%s</SubnetMask><Gateway>%s</Gateway><DNS><Primary>%s</Primary><Secondary>%s</Secondary></DNS><OpenDNS><enable>%s</enable></OpenDNS><MacAddress>%s</MacAddress><MTU>%s</MTU></GetWanSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e038`
- 引用地址: `0043e030`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 2 条指令

**目标子串**: `IPAddress`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWanSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWanSettingsResult>%s</GetWanSettingsResult><Type>%s</Type><Username>%s</Username><Password>%s</Password><MaxIdleTime>%s</MaxIdleTime><ServiceName>%s</ServiceName><AutoReconnect>%s</AutoReconnect><IPAddress>%s</IPAddress><SubnetMask>%s</SubnetMask><Gateway>%s</Gateway><DNS><Primary>%s</Primary><Secondary>%s</Secondary></DNS><OpenDNS><enable>%s</enable></OpenDNS><MacAddress>%s</MacAddress><MTU>%s</MTU></GetWanSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e038`
- 引用地址: `0043e030`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 2 条指令

**目标子串**: `MacAddress`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWanSettingsResponse xmlns="http://purenetworks.com/HNAP1/"><GetWanSettingsResult>%s</GetWanSettingsResult><Type>%s</Type><Username>%s</Username><Password>%s</Password><MaxIdleTime>%s</MaxIdleTime><ServiceName>%s</ServiceName><AutoReconnect>%s</AutoReconnect><IPAddress>%s</IPAddress><SubnetMask>%s</SubnetMask><Gateway>%s</Gateway><DNS><Primary>%s</Primary><Secondary>%s</Secondary></DNS><OpenDNS><enable>%s</enable></OpenDNS><MacAddress>%s</MacAddress><MTU>%s</MTU></GetWanSettingsResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e038`
- 引用地址: `0043dff0`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 18 条指令

---

### 11. 函数: `nvram_get` (使用次数: 16)

#### 精确匹配 (7 次)

**字符串**: `lan_ipaddr`
- 调用地址: `0041023c`
- 引用地址: `00410230`
- 参数位置: 0
- 包含函数: `absolute_path`
- 搜索距离: 3 条指令

**字符串**: `lan_ipaddr`
- 调用地址: `004102c4`
- 引用地址: `004102a8`
- 参数位置: 0
- 包含函数: `absolute_path`
- 搜索距离: 7 条指令

**字符串**: `log_system_activity`
- 调用地址: `00422284`
- 引用地址: `00422280`
- 参数位置: 0
- 包含函数: `ej_cmo_get_log`
- 搜索距离: 1 条指令

**字符串**: `vs_rule_00`
- 调用地址: `00433c10`
- 引用地址: `00433c0c`
- 参数位置: 0
- 包含函数: `FUN_00433a18`
- 搜索距离: 1 条指令

**字符串**: `vs_rule_00`
- 调用地址: `00433e7c`
- 引用地址: `00433e78`
- 参数位置: 0
- 包含函数: `FUN_00433a18`
- 搜索距离: 1 条指令

#### 部分匹配 (9 次)

**目标子串**: `name`
- 完整字符串: `user_username`
- 调用地址: `0042309c`
- 引用地址: `0042305c`
- 参数位置: 1
- 包含函数: `ej_cmo_get_cfg`
- 搜索距离: 16 条指令

**目标子串**: `name`
- 完整字符串: `user_username`
- 调用地址: `0042309c`
- 引用地址: `00423084`
- 参数位置: 1
- 包含函数: `ej_cmo_get_cfg`
- 搜索距离: 6 条指令

**目标子串**: `vs_rule_0`
- 完整字符串: `vs_rule_00`
- 调用地址: `00433c10`
- 引用地址: `00433c0c`
- 参数位置: 0
- 包含函数: `FUN_00433a18`
- 搜索距离: 1 条指令

**目标子串**: `vs_rule_0`
- 完整字符串: `vs_rule_00`
- 调用地址: `00433e7c`
- 引用地址: `00433e78`
- 参数位置: 0
- 包含函数: `FUN_00433a18`
- 搜索距离: 1 条指令

**目标子串**: `vs_rule_0`
- 完整字符串: `vs_rule_00`
- 调用地址: `00433e1c`
- 引用地址: `00433e18`
- 参数位置: 0
- 包含函数: `FUN_00433a18`
- 搜索距离: 1 条指令

---

### 12. 函数: `fopen` (使用次数: 14)

#### 部分匹配 (14 次)

**目标子串**: `dhcp`
- 完整字符串: `/var/tmp/test_dhcp_res.txt`
- 调用地址: `00421ba0`
- 引用地址: `00421b88`
- 参数位置: 0
- 包含函数: `return_internet_connect_type`
- 搜索距离: 6 条指令

**目标子串**: `dhcp`
- 完整字符串: `/var/run/udhcpd.pid`
- 调用地址: `004289b0`
- 引用地址: `004289ac`
- 参数位置: 0
- 包含函数: `get_dhcp_client_list`
- 搜索距离: 1 条指令

**目标子串**: `dhcp`
- 完整字符串: `/var/tmp/dhcpc.tmp`
- 调用地址: `0043108c`
- 引用地址: `00431080`
- 参数位置: 0
- 包含函数: `lease_time_execute`
- 搜索距离: 3 条指令

**目标子串**: `dhcp`
- 完整字符串: `/var/tmp/dhcp_pd`
- 调用地址: `00459484`
- 引用地址: `00459480`
- 参数位置: 0
- 包含函数: `do_ajax_action`
- 搜索距离: 1 条指令

**目标子串**: `dhcp`
- 完整字符串: `vation>%s</dhcpd_reservation>`
- 调用地址: `00459484`
- 引用地址: `00459480`
- 参数位置: 3
- 包含函数: `do_ajax_action`
- 搜索距离: 1 条指令

---

### 13. 函数: `printf` (使用次数: 11)

#### 部分匹配 (11 次)

**目标子串**: `device`
- 完整字符串: `is_3g_device_connect`
- 调用地址: `00431a20`
- 引用地址: `00431a1c`
- 参数位置: 1
- 包含函数: `is_3g_device_connect`
- 搜索距离: 1 条指令

**目标子串**: `device`
- 完整字符串: `is_3g_device_connect`
- 调用地址: `004319fc`
- 引用地址: `004319f8`
- 参数位置: 1
- 包含函数: `is_3g_device_connect`
- 搜索距离: 1 条指令

**目标子串**: `device`
- 完整字符串: `is_3g_device_connect`
- 调用地址: `00431a20`
- 引用地址: `004319f8`
- 参数位置: 1
- 包含函数: `is_3g_device_connect`
- 搜索距离: 10 条指令

**目标子串**: `generate_pin`
- 完整字符串: `generate_pin_by_wan_mac`
- 调用地址: `004246d4`
- 引用地址: `004246d0`
- 参数位置: 1
- 包含函数: `generate_pin_by_wan_mac`
- 搜索距离: 1 条指令

**目标子串**: `restart`
- 完整字符串: `qos sent restart signal to rc`
- 调用地址: `0040ed70`
- 引用地址: `0040ed6c`
- 参数位置: 0
- 包含函数: `rc_action`
- 搜索距离: 1 条指令

---

### 14. 函数: `get_cgi` (使用次数: 11)

#### 精确匹配 (6 次)

**字符串**: `hostname`
- 调用地址: `0041b3ac`
- 引用地址: `0041b3a8`
- 参数位置: 0
- 包含函数: `set_basic_api`
- 搜索距离: 1 条指令

**字符串**: `ntp_server`
- 调用地址: `00413ec0`
- 引用地址: `00413eb0`
- 参数位置: 0
- 包含函数: `FUN_00413ddc`
- 搜索距离: 4 条指令

**字符串**: `ping6_ipaddr`
- 调用地址: `00413054`
- 引用地址: `00413044`
- 参数位置: 0
- 包含函数: `FUN_00412fa8`
- 搜索距离: 4 条指令

**字符串**: `ping_ipaddr`
- 调用地址: `00412eb0`
- 引用地址: `00412ea0`
- 参数位置: 0
- 包含函数: `FUN_00412e04`
- 搜索距离: 4 条指令

**字符串**: `revoke_ip`
- 调用地址: `00412cf4`
- 引用地址: `00412ce4`
- 参数位置: 0
- 包含函数: `FUN_00412c74`
- 搜索距离: 4 条指令

#### 部分匹配 (5 次)

**目标子串**: `login`
- 完整字符串: `login_name`
- 调用地址: `00419db4`
- 引用地址: `00419d9c`
- 参数位置: 0
- 包含函数: `FUN_00419d0c`
- 搜索距离: 6 条指令

**目标子串**: `name`
- 完整字符串: `hostname`
- 调用地址: `0041b3ac`
- 引用地址: `0041b3a8`
- 参数位置: 0
- 包含函数: `set_basic_api`
- 搜索距离: 1 条指令

**目标子串**: `ping`
- 完整字符串: `ping_ipaddr`
- 调用地址: `00412eb0`
- 引用地址: `00412ea0`
- 参数位置: 0
- 包含函数: `FUN_00412e04`
- 搜索距离: 4 条指令

**目标子串**: `ping`
- 完整字符串: `ping6_ipaddr`
- 调用地址: `00413054`
- 引用地址: `00413044`
- 参数位置: 0
- 包含函数: `FUN_00412fa8`
- 搜索距离: 4 条指令

**目标子串**: `type`
- 完整字符串: `page_type`
- 调用地址: `00410600`
- 引用地址: `004105d8`
- 参数位置: 0
- 包含函数: `FUN_0041053c`
- 搜索距离: 10 条指令

---

### 15. 函数: `sleep` (使用次数: 8)

#### 部分匹配 (8 次)

**目标子串**: `Enabled`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWLanSecurityResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanSecurityResult>%s</GetWLanSecurityResult><Enabled>%s</Enabled><Type>%s</Type><WEPKeyBits>%s</WEPKeyBits><SupportedWEPKeyBits><int>0</int><int>64</int><int>128</int><int>152</int></SupportedWEPKeyBits><Key>%s</Key><RadiusIP1>%s</RadiusIP1><RadiusPort1>%s</RadiusPort1><RadiusIP2>%s</RadiusIP2><RadiusPort2>%s</RadiusPort2></GetWLanSecurityResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e500`
- 引用地址: `0043e4dc`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 9 条指令

**目标子串**: `GetWLanSecurityResult`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWLanSecurityResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanSecurityResult>%s</GetWLanSecurityResult><Enabled>%s</Enabled><Type>%s</Type><WEPKeyBits>%s</WEPKeyBits><SupportedWEPKeyBits><int>0</int><int>64</int><int>128</int><int>152</int></SupportedWEPKeyBits><Key>%s</Key><RadiusIP1>%s</RadiusIP1><RadiusPort1>%s</RadiusPort1><RadiusIP2>%s</RadiusIP2><RadiusPort2>%s</RadiusPort2></GetWLanSecurityResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e500`
- 引用地址: `0043e4dc`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 9 条指令

**目标子串**: `RadiusIP1`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWLanSecurityResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanSecurityResult>%s</GetWLanSecurityResult><Enabled>%s</Enabled><Type>%s</Type><WEPKeyBits>%s</WEPKeyBits><SupportedWEPKeyBits><int>0</int><int>64</int><int>128</int><int>152</int></SupportedWEPKeyBits><Key>%s</Key><RadiusIP1>%s</RadiusIP1><RadiusPort1>%s</RadiusPort1><RadiusIP2>%s</RadiusIP2><RadiusPort2>%s</RadiusPort2></GetWLanSecurityResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e500`
- 引用地址: `0043e4dc`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 9 条指令

**目标子串**: `RadiusIP2`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWLanSecurityResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanSecurityResult>%s</GetWLanSecurityResult><Enabled>%s</Enabled><Type>%s</Type><WEPKeyBits>%s</WEPKeyBits><SupportedWEPKeyBits><int>0</int><int>64</int><int>128</int><int>152</int></SupportedWEPKeyBits><Key>%s</Key><RadiusIP1>%s</RadiusIP1><RadiusPort1>%s</RadiusPort1><RadiusIP2>%s</RadiusIP2><RadiusPort2>%s</RadiusPort2></GetWLanSecurityResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e500`
- 引用地址: `0043e4dc`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 9 条指令

**目标子串**: `RadiusPort1`
- 完整字符串: `<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetWLanSecurityResponse xmlns="http://purenetworks.com/HNAP1/"><GetWLanSecurityResult>%s</GetWLanSecurityResult><Enabled>%s</Enabled><Type>%s</Type><WEPKeyBits>%s</WEPKeyBits><SupportedWEPKeyBits><int>0</int><int>64</int><int>128</int><int>152</int></SupportedWEPKeyBits><Key>%s</Key><RadiusIP1>%s</RadiusIP1><RadiusPort1>%s</RadiusPort1><RadiusIP2>%s</RadiusIP2><RadiusPort2>%s</RadiusPort2></GetWLanSecurityResponse></soap:Body></soap:Envelope>`
- 调用地址: `0043e500`
- 引用地址: `0043e4dc`
- 参数位置: 1
- 包含函数: `do_pure_action`
- 搜索距离: 9 条指令

---

