#!/usr/bin/env python3

"""
钩子函数实现集合
包含各种常用的钩子函数实现，用于函数劫持和监控
"""

def get_one_param_hook():
    """返回单参数钩子函数的 C 代码实现"""
    return '''char * one_para_getval(const char *name) {
    printf("one_para_getval 钩子函数被调用，键名: %s\\n", name);
    
    char *value = get_value_by_key(name);
    if (value) {
        printf("找到键 '%s' 的值: '%s'\\n", name, value);
        return value;
    } else {
        printf("未找到键 '%s'，默认返回0\\n", name);
        return 0;
    }
}'''

def get_two_param_hook():
    """返回双参数钩子函数的 C 代码实现"""
    return '''char * two_para_getval(int* wp, const char *name) {
    printf("two_para_getval 钩子函数被调用，键名: %s\\n", name);
    
    char *value = get_value_by_key(name);
    if (value) {
        printf("找到键 '%s' 的值: '%s'\\n", name, value);
        return value;
    } else {
        printf("未找到键 '%s'，默认返回0\\n", name);
        return 0;
    }
}'''

def get_three_param_hook():
    """返回三参数钩子函数的 C 代码实现"""
    return '''char * three_para_getval(int* wp, const char *name, void *default_val) {
    printf("three_para_getval 钩子函数被调用，键名: %s\\n", name);
    
    char *value = get_value_by_key(name);
    if (value) {
        printf("找到键 '%s' 的值: '%s'\\n", name, value);
        return value;
    } else {
        if (default_val == 0) {
            printf("未找到键 '%s'，且默认值为NULL，返回空字符串\\n", name);
            // 分配可写内存返回空字符串，防止调用者修改只读内存导致崩溃
            char *empty = calloc(1, 1);
            return empty;
        }
        printf("未找到键 '%s'，默认返回'%s'\\n", name,default_val);
        return default_val;
    }
}'''

def get_four_param_hook():
    """返回四参数钩子函数的 C 代码实现"""
    return '''char * four_para_getval(int* wp, const char *name, int *default_val, int len) {
    printf("four_para_getval 钩子函数被调用，键名: %s\\n", name);
    
    char *value = get_value_by_key(name);
    if (value) {
        printf("找到键 '%s' 的值: '%s'\\n", name, value);
        size_t value_len = strlen(value);
        if(value_len >=len) {
            value[len - 1] = '\\0'; // 确保值不会超过指定长度
        }
        return value;
    } else {
        printf("未找到键 '%s'，默认返回0\\n", name);
        return 0;
    }
}'''

def get_getvalue_hook():
    """返回 GetValue 钩子函数的 C 代码实现"""
    return '''// 定义原始的 GetValue 函数指针
int (*original_GetValue)(const char*, char*);

// 初始化函数，获取原始的 GetValue 函数
__attribute__((constructor)) int hook_GetValue()
{
    // 使用 dlsym 获取原始 GetValue 函数的地址
    original_GetValue = dlsym(RTLD_NEXT, "GetValue");
    if (!original_GetValue) {
        fprintf(stderr, "Error in `dlsym`: %s\\n", dlerror());
        // 不需要退出
    } else {
        printf("Successfully hooked GetValue function.\\n");
    }
}

// 新的 GetValue 函数定义
int GetValue(const char* name, char *value)
{
    printf("Custom GetValue called with name: %s\\n", name);
    // 修改 value 的内容，这里示例为将 value 设为 "0"
    if (value) value[0] = '\\0';
    return 1;
}'''

def check_dangerous_command():
    return '''int check_dangerous_command(const char *command) {
    if (!command || !pairs) {
        return 0; // 没有命令或没有加载键值对，认为安全
    }
    
    printf("[SECURITY CHECK] Checking command: %s\\n", command);
    
    // 遍历所有键值对，检查命令中是否包含这些值
    for (int i = 0; i < pair_count; i++) {
        // 跳过空白键值
        if (strlen(pairs[i].value) == 0) {
            printf("[SKIP] Skipping empty value for key: '%s'\\n", pairs[i].key);
            continue;
        }

        if (strlen(pairs[i].value) < 5) {
            continue;
        }
        
        // 跳过只包含空白字符的键值
        int is_whitespace_only = 1;
        for (int j = 0; j < strlen(pairs[i].value); j++) {
            char c = pairs[i].value[j];
            if (c != ' ' && c != '\\t' && c != '\\n' && c != '\\r' && c != '\\f' && c != '\\v') {
                is_whitespace_only = 0;
                break;
            }
        }
        
        if (is_whitespace_only) {
            printf("[SKIP] Skipping whitespace-only value for key: '%s'\\n", pairs[i].key);
            continue;
        }
        
        // 检查命令中是否包含键值
        if (strstr(command, pairs[i].value) != NULL) {
            printf("[DANGER DETECTED] Command contains value: '%s' (from key: '%s')\\n", 
                   pairs[i].value, pairs[i].key);
            return 1; // 发现危险内容
        }
    }
    
    return 0; // 命令安全
}'''

def trigger_crash():
    """返回触发崩溃的钩子函数的 C 代码实现"""
    return '''void trigger_crash(const char *reason) {
    printf("\\n=== CRASH TRIGGERED ===\\n");
    printf("Reason: %s\\n", reason);
    printf("Aborting program for security reasons...\\n");
    fflush(stdout);
    
    // 触发段错误
    assert(0);
}'''

def get_dosystemcmd_hook():
    """返回 doSystemCmd 钩子函数的 C 代码实现"""
    return '''// 定义原始的 doSystemCmd 函数指针
int (*original_doSystemCmd)(const char*, ...);

// 初始化函数，获取原始的 doSystemCmd 函数
__attribute__((constructor)) void hook_doSystemCmd()
{
    // 使用 dlsym 获取原始 doSystemCmd 函数的地址
    original_doSystemCmd = dlsym(RTLD_NEXT, "doSystemCmd");
    if (!original_doSystemCmd) {
        fprintf(stderr, "Error in `dlsym`: %s\\n", dlerror());
        // 不需要退出
    } else {
        printf("Successfully hooked doSystemCmd function.\\n");
    }
}

// 新的 doSystemCmd 函数定义
int doSystemCmd(const char* format, ...)
{
    char command[4096]; // 足够大的缓冲区来存储命令
    va_list args;
    
    // 使用可变参数列表格式化命令字符串
    va_start(args, format);
    vsnprintf(command, sizeof(command), format, args);
    va_end(args);
    
    // 打印出要执行的命令而不是真正执行它
    printf("[钩子函数] doSystemCmd 被调用: %s\\n", command);
    if (check_dangerous_command(command)) {
        // 发现危险命令，触发崩溃
        char crash_reason[1024];
        snprintf(crash_reason, sizeof(crash_reason), 
                "Dangerous command detected in system(): %s", 
                command ? command : "(null)");
        trigger_crash(crash_reason);
    }
    // 可选：返回0表示命令"成功"执行
    return 0;
}'''

def get_skip0_hook():
    """返回跳过执行的钩子函数实现"""
    return '''int skip0_hook() {
    return 0;
}'''
def get_skip1_hook():
    """返回跳过执行的钩子函数实现"""
    return '''int skip1_hook() {
    return 1;
}'''

def get_apmib_get_hook():
    """返回 apmib_get 钩子函数的 C 代码实现"""
    return '''int apmib_get_hook(int a1, char *a2) {
    printf("apmib_get_hook called.\\n");
    if (a2) {
        a2[0] = 'a';
        a2[1] = '\\0'; // 确保字符串以空字符结尾
    }
    return 1; // 强制返回 1
}'''

def get_nvram_get_hook():
    """返回 nvram_get 钩子函数的 C 代码实现"""
    return '''char *nvram_get_hook(const char *name) {
    printf("nvram_get 钩子函数被调用，键名: %s\\n", name);
    
    char *value = get_value_by_key(name);
    if (value) {
        printf("找到键 '%s' 的值: '%s'\\n", name, value);
        return value;
    } else {
        printf("未找到键 '%s'，返回NULL\\n", name);
        return NULL;
    }
}'''

def get_nvram_set_hook():
    """返回 nvram_set 钩子函数的 C 代码实现"""
    return '''int nvram_set_hook(const char *name, const char *value) {
    printf("nvram_set 钩子函数被调用，键名: %s, 值: %s\\n", name, value ? value : "(null)");
    // 这里可以选择是否真正设置值，或者只是记录
    return 0; // 返回成功
}'''

def get_system_hook():
    """返回 system 钩子函数的 C 代码实现"""
    return '''int system(const char *command) {
    printf("system 钩子函数被调用，命令: %s\\n", command ? command : "(null)");
    // 不执行实际命令，只记录
        if (check_dangerous_command(command)) {
        // 发现危险命令，触发崩溃
        char crash_reason[1024];
        snprintf(crash_reason, sizeof(crash_reason), 
                "Dangerous command detected in system(): %s", 
                command ? command : "(null)");
        trigger_crash(crash_reason);
    }
    return 0;
}'''

def get_popen_hook():
    """返回 popen 钩子函数的 C 代码实现"""
    return '''FILE *popen(const char *command, const char *type) {
    printf("popen 钩子函数被调用，命令: %s, 类型: %s\\n", 
           command ? command : "(null)", type ? type : "(null)");
    if (check_dangerous_command(command)) {
    // 发现危险命令，触发崩溃
    char crash_reason[1024];
    snprintf(crash_reason, sizeof(crash_reason), 
            "Dangerous command detected in system(): %s", 
            command ? command : "(null)");
    trigger_crash(crash_reason);
    }
    // 返回一个虚拟的文件指针或NULL
    return NULL;
}'''

def get_execve_hook():
    """返回 execve 钩子函数的 C 代码实现"""
    return '''int execve(const char *pathname, char *const argv[], char *const envp[])
    {
        printf("execve 钩子函数被调用，路径: %s\\n", pathname ? pathname : "(null)");
        
        // 构建完整命令行用于检查
        char command_line[4096] = {0};
        if (pathname) {
            strncpy(command_line, pathname, sizeof(command_line) - 1);
            
            // 添加参数到命令行
            if (argv) {
                printf("参数: ");
                for (int i = 0; argv[i]; i++) {
                    printf("%s ", argv[i]);
                    if (i > 0) { // 跳过argv[0]，因为通常是程序名
                        strncat(command_line, " ", sizeof(command_line) - strlen(command_line) - 1);
                        strncat(command_line, argv[i], sizeof(command_line) - strlen(command_line) - 1);
                    }
                }
                printf("\\n");
            }
        }
        
        // 检查命令是否包含危险内容
        if (check_dangerous_command(command_line)) {
            // 发现危险命令，触发崩溃
            char crash_reason[1024];
            snprintf(crash_reason, sizeof(crash_reason), 
                    "Dangerous command detected in execve(): %s", 
                    command_line);
            trigger_crash(crash_reason);
        }
        
        // 如果没有危险内容，可以选择调用原始函数或者阻止执行
        printf("[HOOK] execve 命令检查通过，阻止执行: %s\\n", command_line);
        return 1;
}'''
def get_CommitCfm_hook():
    """返回 CommitCfm 钩子函数的 C 代码实现"""
    return '''int CommitCfm(int a) {
    return 1; // 返回成功
}'''

def get_sleep_hook():
    """返回 sleep 钩子函数的 C 代码实现"""
    return '''unsigned int sleep(unsigned int seconds) {
    printf("sleep 钩子函数被调用，秒数: %u\\n", seconds);
    // 不执行实际的 sleep，只记录
    
    return 0; // 返回成功
}'''

# 钩子函数映射表
HOOK_FUNCTIONS = {
    'get_one_para_getval': get_one_param_hook,
    'get_two_para_getval': get_two_param_hook,
    'get_three_para_getval': get_three_param_hook,
    'get_four_para_getval': get_four_param_hook,
    'GetValue': get_getvalue_hook,
    'check_dangerous_command': check_dangerous_command,
    'trigger_crash': trigger_crash,
    'doSystemCmd': get_dosystemcmd_hook,
    'skip0': get_skip0_hook,
    'skip1': get_skip1_hook,
    'nvram_get': get_nvram_get_hook,
    'nvram_set': get_nvram_set_hook,
    'system': get_system_hook,
    'popen': get_popen_hook,
    'execve': get_execve_hook,
    'CommitCfm': get_CommitCfm_hook, 
    'sleep': get_sleep_hook,
    'apmib_get': get_apmib_get_hook
}

def get_hook_function(func_name):
    """
    根据函数名获取对应的钩子函数实现
    
    Args:
        func_name: 函数名称
        
    Returns:
        str: 钩子函数的C代码实现，如果未找到则返回默认的skip_hook
    """
    return HOOK_FUNCTIONS.get(func_name, get_skip0_hook)()

def get_hook_function_name(para_count):
    """
    根据原始函数名生成钩子函数名
    
    Args:
        func_name: 原始函数名
        
    Returns:
        str: 钩子函数名
    """
    if para_count == 1:
        return 'one_para_getval'
    elif para_count == 2:
        return 'two_para_getval'
    elif para_count == 3:
        return 'three_para_getval'
    elif para_count == 4:
        return 'four_para_getval'
    else:
        return 'skip0_hook'  # 默认返回skip0钩子

def get_all_hook_implementations():
    """
    获取所有钩子函数的实现代码
    
    Returns:
        str: 所有钩子函数的C代码实现
    """
    implementations = []
        
    # 添加所有其他钩子函数
    for func_name, func_getter in HOOK_FUNCTIONS.items():
        implementations.append(func_getter())
    
    return '\n\n'.join(implementations)