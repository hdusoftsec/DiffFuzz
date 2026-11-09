# 命令注入相关的危险函数
COMMAND_INJECTION_SINKS = [
    "system",
    "_system",
    "twsystem",
    "execFormatCmd",
    "exec_cmd",
    "___system",
    "bstar_system",
    "doSystemCmd",
    "doShell",
    "CsteSystem",
    "cgi_deal_popen",
    "ExeCmd",
    "ExecShell",
    "exec_shell_popen",
    "exec_shell_popen_str",
    "popen",
    "execl",
    "execlp",
    "execle",
    "execv",
    "execvp",
    "execvpe",
    "execve",
    "tp_systemEx",
    "exec_shell_async",
    "exec_shell_sync",
    "exec_shell_sync2",
    "SLIBCSystem",
    "SLIBCExecl",
    "SLIBCExec",
    "SLIBCExecv",
    "SLIBCPopen",
    "pegaSystem",
]

# 路径遍历相关的危险函数
PATH_TRAVERSAL_SINKS = [
    "popen",
    "fopen",
]

# 缓冲区溢出相关的危险函数
BUFFER_OVERFLOW_SINKS = [
    "strcpy",
]

# 字符串拼接相关的危险函数
STRCAT_SINKS = [
    "strcat",
]

# 内存复制相关的危险函数
MEMCPY_SINKS = [
    "memcpy",
]

# 格式化输入相关的危险函数。
# 当输入可控且格式串中的 %s/%[...] 未指定最大字段宽度时，输出缓冲区可能溢出。
FORMATTED_INPUT_SINKS = [
    "sscanf",
    "__isoc99_sscanf",
]

# 字符串格式化相关的危险函数
STRING_FORMAT_SINKS = [
    "sprintf",
    "snprintf",
]

# 所有危险函数列表
ALL_DANGEROUS_FUNCS = (
    COMMAND_INJECTION_SINKS + 
    PATH_TRAVERSAL_SINKS + 
    BUFFER_OVERFLOW_SINKS + 
    STRCAT_SINKS + 
    MEMCPY_SINKS + 
    FORMATTED_INPUT_SINKS +
    STRING_FORMAT_SINKS
)
