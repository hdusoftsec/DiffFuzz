#!/usr/bin/env python3

import json
import os
import sys
import argparse
import subprocess
import shutil
from summary_hook_func import get_hook_function, get_hook_function_name, get_all_hook_implementations

def extract_arch(json_file):
    """从 JSON 文件中提取程序架构信息"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # 获取程序架构
    arch = data.get("program_arch", "unknown")
    
    return arch

def extract_callers(json_file):
    """从 JSON 文件中提取所有调用者（callers）并去重"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # 收集所有 callers
    all_callers = {}  # 使用字典确保地址唯一性
    
    for func in data.get("extract_functions", []):
        for caller in func.get("callers", []):
            caller_name = caller.get("name", "unknown")
            caller_addr = caller.get("address", None)
            
            if caller_addr:
                # 将十六进制字符串转换为整数（如果不是整数）
                if isinstance(caller_addr, str) and caller_addr.startswith("0x"):
                    caller_addr = int(caller_addr, 16)
                
                # 地址作为键，确保唯一性
                if caller_addr not in all_callers:
                    all_callers[caller_addr] = {
                        "name": caller_name,
                        "address": caller_addr
                    }
                else:
                    # 如果地址已存在，检查名字是否不同，打印提示
                    existing_name = all_callers[caller_addr]["name"]
                    if existing_name != caller_name:
                        print(f"[提示] 函数 '{caller_name}' (0x{caller_addr:x}) 与已存在的 '{existing_name}' 地址相同，跳过生成。")
    
    return list(all_callers.values())

def extract_io_functions(json_file):
    """提取所有 IO 函数和地址"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    io_functions = []
    for func in data.get("extract_functions", []):
        name = func.get("name", "")
        addr = func.get("address", "")
        para_count = func.get("parameter_count", 0)
        if addr:
            # 将字符串地址转为整数
            if isinstance(addr, str) and addr.startswith("0x"):
                addr = int(addr, 16)
            
            io_functions.append({
                "name": name,
                "address": addr,
                "parameter_count": para_count
            })
    
    return io_functions

def extract_remove_functions(json_file):
    """提取需要移除的函数及其地址"""
    with open(json_file, 'r') as f:
        data = json.load(f)
        
    remove_funcs = []
    for func in data.get("remove_functions", []):
        name = func.get("name", "")
        addr = func.get("address", "")
        ret_val= func.get("return_value", 0)
        if addr:
            # 将字符串地址转为整数
            if isinstance(addr, str) and addr.startswith("0x"):
                addr = int(addr, 16)
            
            remove_funcs.append({
                "name": name,
                "address": addr,
                "return_value": ret_val
            })
    
    return remove_funcs


def generate_hooks_c(target_funcs, io_funcs, remove_funcs, output_dir,arch_name):
    """为每个目标函数生成 hooks.c 文件"""
    template = """#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdarg.h>
#include <assert.h>
#include <ctype.h>

static const char *input = NULL;  // 全局输入字符串
static size_t current_pos = 0;    // 当前读取位置

// 钩子目标的结构体
typedef struct {
    void *target_addr;          // 目标函数地址
    unsigned char original[16]; // 保存原始指令
    void (*hook_func)();        // 钩子函数
} HookTarget;

// 键值对结构体
typedef struct {
    char key[64];
    char value[4096];
} KeyValuePair;

static KeyValuePair *pairs = NULL; // 键值对数组
static int pair_count = 0;        // 键值对数量

// 根据键名查找值
char *get_value_by_key(const char *key) {
    for (int i = 0; i < pair_count; i++) {
        if (strcmp(pairs[i].key, key) == 0) {
            return pairs[i].value;
        }
    }
    return NULL; // 未找到匹配项
}

// 高效读取键值对文件
void load_key_values(const char *filename) {
    FILE *fp = fopen(filename, "rb");
    if (!fp) {
        perror("无法打开文件");
        return;
    }
    
    // 释放之前可能存在的键值对数组
    if (pairs) {
        free(pairs);
        pairs = NULL;
    }
    
    // 分配初始容量
    int capacity = 16;
    pairs = malloc(capacity * sizeof(KeyValuePair));
    if (!pairs) {
        perror("内存分配失败");
        fclose(fp);
        return;
    }
    
    pair_count = 0;
    char line[4096];  // 增加行缓冲区大小以适应长值
    
    // 一次性读取所有行
    while (fgets(line, sizeof(line), fp)) {
        // 移除换行符
        size_t len = strlen(line);
        if (len > 0 && (line[len-1] == '\\n' || line[len-1] == '\\r')) {
            line[len-1] = '\\0';
        }
        
        // 查找等号
        char *equals = strchr(line, '=');
        if (!equals) continue; // 跳过没有等号的行
        
        // 动态扩展数组
        if (pair_count >= capacity) {
            capacity *= 2;
            KeyValuePair *temp = realloc(pairs, capacity * sizeof(KeyValuePair));
            if (!temp) {
                fprintf(stderr, "内存重分配失败\\n");
                break;
            }
            pairs = temp;
        }
        
        // 计算键长度并复制键
        size_t key_len = equals - line;
        if (key_len >= sizeof(pairs[0].key)) key_len = sizeof(pairs[0].key) - 1;
        memcpy(pairs[pair_count].key, line, key_len);
        pairs[pair_count].key[key_len] = '\\0';
        
        // 复制值
        strncpy(pairs[pair_count].value, equals + 1, sizeof(pairs[0].value) - 1);
        pairs[pair_count].value[sizeof(pairs[0].value) - 1] = '\\0';
        
        pair_count++;
    }
    
    fclose(fp);
    printf("已加载 %d 个键值对\\n", pair_count);
}

// 钩子函数实现
"""
    
    # 为每个目标函数生成独立的钩子文件
    for i, func in enumerate(target_funcs):
        func_name = func["name"]
        func_addr = func["address"]
        
        # 创建目标函数所在的目录结构
        func_dir = os.path.join(output_dir, func_name)
        os.makedirs(func_dir, exist_ok=True)
        
        # 构建特定于当前目标函数的模板
        func_template = template
        
        # 添加所有钩子函数的实现
        func_template += get_all_hook_implementations()
        func_template += f"\n\n// TARGET 函数声明\nint (*target_func)(int) = (void*)0x{func_addr:08x}; // {func_name}\n\n"
        
        # 添加钩子目标数组
        func_template += """
// 钩子目标数组
HookTarget hook_targets[] = {
"""
        
        # 添加 IO 函数 hooks
        for io_func in io_funcs:
            name = io_func["name"]
            addr = io_func["address"]
            para_count = io_func["parameter_count"]
            hook_func_name = get_hook_function_name(para_count)
            func_template += f"    {{(void *)0x{addr:08x}, {{0}}, (void *){hook_func_name}}},  // {name}\n"
        
        # 添加 remove 函数 hooks
        for r_func in remove_funcs:
            name = r_func["name"]
            addr = r_func["address"]
            ret_val = r_func.get("return_value", 0)
            func_template += f"    {{(void *)0x{addr:08x}, {{0}}, (void *)skip{ret_val}_hook}},  // {name} (removed)\n"

        # 添加主要的目标函数
        func_template += """};

// 钩子目标的数量
#define HOOK_TARGET_COUNT (sizeof(hook_targets) / sizeof(HookTarget))

// 修改内存保护，使目标函数地址可写
void make_memory_writable(void *addr) {
    long page_size = sysconf(_SC_PAGESIZE);
    void *aligned_addr = (void *)((long)addr & ~(page_size - 1));
    if (mprotect(aligned_addr, page_size, PROT_READ | PROT_WRITE | PROT_EXEC)) {
        perror("mprotect failed");
        exit(1);
    }
}

"""
        # 根据架构生成不同的inline hook函数
        arch_upper = arch_name.upper()
        if arch_upper in ["ARMEL", "ARMEB"]:
            # ARM 架构 inline hook
            if arch_upper == "ARMEB":
                # ARM Big Endian 版本
                func_template += """// 安装 Inline Hook (ARM Big Endian 版本)
void install_inline_hook() {
    unsigned char jump[16];

    for (int i = 0; i < HOOK_TARGET_COUNT; i++) {
        HookTarget *target = &hook_targets[i];

        // 保存目标函数的前 16 字节（ARM 的 4 条指令）
        memcpy(target->original, target->target_addr, 16);

        // 设置目标函数所在页面为可写
        make_memory_writable(target->target_addr);

        // 构建跳转指令到钩子函数
        unsigned int hook_addr = (unsigned int)target->hook_func;
        
        // ARM Big Endian 跳转指令序列:
        // ldr pc, [pc, #-4]    ; 0xe51ff004 - 从PC相对地址加载目标地址到PC
        // .word hook_addr      ; 目标函数地址
        // nop                  ; 0xe1a00000 - 填充对齐
        // nop                  ; 0xe1a00000 - 填充对齐
        
        // Big Endian 字节序
        jump[0] = 0xe5; jump[1] = 0x1f; jump[2] = 0xf0; jump[3] = 0x04;  // ldr pc, [pc, #-4]
        jump[4] = (hook_addr >> 24) & 0xFF;  // 目标地址高字节
        jump[5] = (hook_addr >> 16) & 0xFF;
        jump[6] = (hook_addr >> 8) & 0xFF;
        jump[7] = hook_addr & 0xFF;          // 目标地址低字节
        jump[8] = 0xe1; jump[9] = 0xa0; jump[10] = 0x00; jump[11] = 0x00;  // nop
        jump[12] = 0xe1; jump[13] = 0xa0; jump[14] = 0x00; jump[15] = 0x00; // nop

        // 覆盖目标函数的前 16 字节
        memcpy(target->target_addr, jump, 16);
    }
}
"""
            else:
                # ARM Little Endian 版本 (ARMEL)
                func_template += """// 安装 Inline Hook (ARM Little Endian 版本)
void install_inline_hook() {
    unsigned char jump[16];

    for (int i = 0; i < HOOK_TARGET_COUNT; i++) {
        HookTarget *target = &hook_targets[i];

        // 保存目标函数的前 16 字节（ARM 的 4 条指令）
        memcpy(target->original, target->target_addr, 16);

        // 设置目标函数所在页面为可写
        make_memory_writable(target->target_addr);

        // 构建跳转指令到钩子函数
        unsigned int hook_addr = (unsigned int)target->hook_func;
        
        // ARM Little Endian 跳转指令序列:
        // ldr pc, [pc, #-4]    ; 0xe51ff004 - 从PC相对地址加载目标地址到PC
        // .word hook_addr      ; 目标函数地址
        // nop                  ; 0xe1a00000 - 填充对齐
        // nop                  ; 0xe1a00000 - 填充对齐
        
        *(unsigned int *)&jump[0] = 0xe51ff004;  // ldr pc, [pc, #-4]
        *(unsigned int *)&jump[4] = hook_addr;   // 目标地址
        *(unsigned int *)&jump[8] = 0xe1a00000;  // nop (mov r0, r0)
        *(unsigned int *)&jump[12] = 0xe1a00000; // nop (mov r0, r0)

        // 覆盖目标函数的前 16 字节
        memcpy(target->target_addr, jump, 16);
    }
}
"""
        
        elif arch_upper in ["MIPSEL", "MIPSEB"]:
            # MIPS 架构 inline hook
            if arch_upper == "MIPSEB":
                # MIPS Big Endian 版本
                func_template += """// 安装 Inline Hook (MIPS Big Endian 版本)
void install_inline_hook() {
    unsigned char jump[16];

    for (int i = 0; i < HOOK_TARGET_COUNT; i++) {
        HookTarget *target = &hook_targets[i];

        // 保存目标函数的前 16 字节（MIPS 的 4 条指令）
        memcpy(target->original, target->target_addr, 16);

        // 设置目标函数所在页面为可写
        make_memory_writable(target->target_addr);

        // 构建跳转指令到钩子函数
        unsigned int hook_addr = (unsigned int)target->hook_func;
        unsigned int high = (hook_addr >> 16) & 0xFFFF;
        unsigned int low = hook_addr & 0xFFFF;

        // MIPS Big Endian 跳转指令序列:
        // lui $t9, high (装载高 16 位)
        jump[0] = 0x3C; jump[1] = 0x19; jump[2] = (high >> 8) & 0xFF; jump[3] = high & 0xFF;
        
        // ori $t9, $t9, low (装载低 16 位)
        jump[4] = 0x37; jump[5] = 0x39; jump[6] = (low >> 8) & 0xFF; jump[7] = low & 0xFF;
        
        // jr $t9 (跳转到钩子函数)
        jump[8] = 0x03; jump[9] = 0x20; jump[10] = 0x00; jump[11] = 0x08;
        
        // nop (MIPS 指令对齐)
        jump[12] = 0x00; jump[13] = 0x00; jump[14] = 0x00; jump[15] = 0x00;

        // 覆盖目标函数的前 16 字节
        memcpy(target->target_addr, jump, 16);
    }
}
"""
            else:
                # MIPS Little Endian 版本 (MIPSEL)
                func_template += """// 安装 Inline Hook (MIPS Little Endian 版本)
void install_inline_hook() {
    unsigned char jump[16];

    for (int i = 0; i < HOOK_TARGET_COUNT; i++) {
        HookTarget *target = &hook_targets[i];

        // 保存目标函数的前 16 字节（MIPS 的 4 条指令）
        memcpy(target->original, target->target_addr, 16);

        // 设置目标函数所在页面为可写
        make_memory_writable(target->target_addr);

        // 构建跳转指令到钩子函数
        unsigned int hook_addr = (unsigned int)target->hook_func;
        unsigned int high = (hook_addr >> 16) & 0xFFFF;
        unsigned int low = hook_addr & 0xFFFF;

        // lui $t9, high (装载高 16 位)
        *(unsigned int *)&jump[0] = 0x3C190000 | high;

        // ori $t9, $t9, low (装载低 16 位)
        *(unsigned int *)&jump[4] = 0x37390000 | low;

        // jr $t9 (跳转到钩子函数)
        *(unsigned int *)&jump[8] = 0x03200008;

        // nop (MIPS 指令对齐)
        *(unsigned int *)&jump[12] = 0x00000000;

        // 覆盖目标函数的前 16 字节
        memcpy(target->target_addr, jump, 16);
    }
}
"""
        
        func_template += """
// 卸载 Inline Hook (恢复原始指令)
void uninstall_inline_hook() {
    for (int i = 0; i < HOOK_TARGET_COUNT; i++) {
        HookTarget *target = &hook_targets[i];
        // 恢复目标函数的原始指令
        memcpy(target->target_addr, target->original, 16);
    }
}

// 主函数钩子，处理输入文件和目标函数执行
int main_hook(int argc, char **argv, char **envp) {
    printf("Starting function hook for %s\\n");
    
    // 检查命令行参数
    if (argc < 2) {
        printf("使用方法: %%s <键值对文件>\\n", argv[0]);
        return 1;
    }
    
    // 从命令行参数获取文件名
    const char *filename = argv[1];
    printf("从文件加载键值对: %%s\\n", filename);
    
    // 加载键值对
    load_key_values(filename);
    
    // 调用目标函数
    target_func(0);
    
    return 0;
}

// 包装 __libc_start_main
int __libc_start_main(
    int (*main)(int, char **, char **),
    int argc,
    char **argv,
    int (*init)(int, char **, char **),
    void (*fini)(void),
    void (*rtld_fini)(void),
    void *stack_end) 
{
    static int (*main_orig)(int, char **, char **) = NULL;
    if (!main_orig) {
        main_orig = main;
    }
    install_inline_hook();
    typeof(&__libc_start_main) orig = dlsym(RTLD_NEXT, "__libc_start_main");
    return orig(main_hook, argc, argv, init, fini, rtld_fini, stack_end);
}

// 包装 __uClibc_main
int __uClibc_main(
    int (*main)(int, char **, char **),
    int argc,
    char **argv,
    int (*init)(int, char **, char **),
    void (*fini)(void),
    void (*rtld_fini)(void),
    void *stack_end)
{
    static int (*main_orig)(int, char **, char **) = NULL;
    if (!main_orig) {
        main_orig = main;
    }
    install_inline_hook();
    /* Find the real __uClibc_main()... */
    typeof(&__uClibc_main) orig = dlsym(RTLD_NEXT, "__uClibc_main");

    /* ... and call it with our custom main function */
    return orig(main_hook, argc, argv, init, fini, rtld_fini, stack_end);
}

// 当共享库被加载时自动调用
__attribute__((constructor)) void init() {
    install_inline_hook();
}

__attribute__((destructor)) void cleanup() {
    uninstall_inline_hook();
}
""" % (func_name)
        
        # 写入生成的代码到文件
        output_file = os.path.join(func_dir, "hooks.c")
        with open(output_file, 'w') as f:
            f.write(func_template)
            
        print(f"已生成 {func_name} 的钩子文件: {output_file}")
        
        # 创建config和input子目录
        config_dir = os.path.join(func_dir, "config")
        input_dir = os.path.join(func_dir, "input")
        os.makedirs(config_dir, exist_ok=True)
        os.makedirs(input_dir, exist_ok=True)

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='为指定的JSON文件生成hooks.c文件')
    parser.add_argument('json_path', help='提取结果的JSON文件路径')
    parser.add_argument('output_dir', help='输出目录')
    return parser.parse_args()

def compile_hooks_c(output_dir,arch_name):
    """编译所有生成的hooks.c文件为函数名_hooks.so"""
    print("开始批量编译钩子文件...")
    
    # 交叉编译器路径
    if arch_name.upper() == "ARMEL":
        compiler = "~/uClibc-Cross-Compilers/arm-buildroot-linux-uclibcgnueabi_sdk-buildroot/bin/arm-buildroot-linux-uclibcgnueabi-gcc"
        print(f"检测到ARMEL架构，使用ARM交叉编译器")
    elif arch_name.upper() == "ARMEB":
        compiler = "~/uClibc-Cross-Compilers/armeb-buildroot-linux-uclibcgnueabi_sdk-buildroot/bin/armeb-buildroot-linux-uclibcgnueabi-gcc"
        print(f"检测到ARMEB架构，使用ARM交叉编译器")
    elif arch_name.upper() == "MIPSEL":
        compiler = "~/uClibc-Cross-Compilers/mipsel-buildroot-linux-uclibc_sdk-buildroot/bin/mipsel-buildroot-linux-uclibc-gcc"
        print(f"检测到MIPSEL架构，使用MIPS交叉编译器")
    elif arch_name.upper() == "MIPSEB":
        compiler = "~/uClibc-Cross-Compilers/mips-buildroot-linux-uclibc_sdk-buildroot/bin/mips-buildroot-linux-uclibc-gcc"
        print(f"检测到MIPSEB架构，使用MIPS交叉编译器")
    else:
        print(f"未知架构: {arch_name}，请检查配置")
        return False
    # 展开用户路径
    compiler = os.path.expanduser(compiler)
    
    # 检查输出目录的父目录是否有lib文件夹
    parent_dir = os.path.dirname(output_dir)
    lib_dir = os.path.join(parent_dir, "lib")
    has_lib_dir = os.path.isdir(lib_dir)
    
    if has_lib_dir:
        print(f"检测到lib目录: {lib_dir}，将同步复制SO文件")
    else:
        print(f"未检测到lib目录: {lib_dir}")
    
    # 统计编译结果
    success_count = 0
    fail_count = 0
    
    # 遍历输出目录下的所有目录
    for func_dir in os.listdir(output_dir):
        func_path = os.path.join(output_dir, func_dir)
        
        # 检查是否为目录且包含hooks.c文件
        if os.path.isdir(func_path):
            hooks_c = os.path.join(func_path, "hooks.c")
            if os.path.isfile(hooks_c):
                # 构建编译命令，使用函数名作为文件名前缀
                hooks_so = os.path.join(func_path, f"{func_dir}_hooks.so")
                compile_cmd = f'{compiler} -fPIC -shared -o "{hooks_so}" "{hooks_c}" -ldl'
                
                print(f"正在编译: {hooks_c}")
                try:
                    # 执行编译命令
                    print(f"编译命令: {compile_cmd}")
                    result = os.system(compile_cmd)
                    if result == 0:
                        success_count += 1
                        print(f"✓ 成功编译: {hooks_so}")
                        
                        # 如果有lib目录，复制so文件到lib目录
                        if has_lib_dir:
                            lib_so_path = os.path.join(lib_dir, f"{func_dir}_hooks.so")
                            try:
                                shutil.copy2(hooks_so, lib_so_path)
                                print(f"  ✓ 已复制到lib目录: {lib_so_path}")
                            except Exception as e:
                                print(f"  ✗ 复制到lib目录失败: {str(e)}")
                    else:
                        fail_count += 1
                        print(f"✗ 编译失败: {hooks_c}, 错误代码: {result}")
                except Exception as e:
                    fail_count += 1
                    print(f"✗ 编译异常: {hooks_c}, 错误: {str(e)}")
    
    print(f"编译完成! 成功: {success_count}, 失败: {fail_count}")
    return success_count, fail_count

def setup_binaries_and_patch(json_path, output_dir):
    """
    从JSON文件中提取二进制程序路径，复制到每个函数目录，并使用patchelf添加hooks依赖
    
    Args:
        json_path: 提取结果的JSON文件路径
        output_dir: 生成钩子文件的输出目录
    """
    print("开始设置二进制文件并添加钩子依赖...")
    
    # 读取JSON文件获取二进制程序路径
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        
        binary_path = data.get("program_path", "")
        if not binary_path or not os.path.exists(binary_path):
            print(f"错误: 无法找到二进制程序文件: {binary_path}")
            return False
        
        print(f"找到二进制程序: {binary_path}")
        binary_name = os.path.basename(binary_path)
        
        # 遍历输出目录下的所有函数目录
        success_count = 0
        fail_count = 0
        
        for func_dir in os.listdir(output_dir):
            func_path = os.path.join(output_dir, func_dir)
            
            # 检查是否为目录且包含hooks.so文件
            if not os.path.isdir(func_path):
                continue
                
            # 使用函数名来命名共享库
            func_hooks_name = f"{func_dir}_hooks.so"
            func_hooks_path = os.path.join(func_path, func_hooks_name)
            
            # 确保hooks.so存在
            if not os.path.exists(func_hooks_path):
                print(f"⚠️ 未找到钩子库: {func_hooks_path}, 跳过")
                continue
                
            # 复制二进制程序到函数目录
            target_binary = os.path.join(func_path, binary_name)
            try:
                shutil.copy2(binary_path, target_binary)
                print(f"已复制二进制程序到: {target_binary}")
                
                # 使用patchelf添加钩子库依赖
                patch_cmd = f'patchelf --add-needed "{func_hooks_name}" "{target_binary}"'
                result = subprocess.run(patch_cmd, shell=True, check=True)
                if result.returncode == 0:
                    print(f"✓ 成功添加钩子依赖: {target_binary} -> {func_hooks_name}")
                    success_count += 1
                else:
                    print(f"✗ 添加钩子依赖失败: {target_binary}")
                    fail_count += 1
                    
            except Exception as e:
                fail_count += 1
                print(f"✗ 处理失败: {func_dir}, 错误: {str(e)}")
        
        print(f"二进制设置完成! 成功: {success_count}, 失败: {fail_count}")
        return True
        
    except Exception as e:
        print(f"处理JSON文件时出错: {str(e)}")
        return False

def main():
    args = parse_arguments()
    json_path = args.json_path
    output_dir = args.output_dir
    
    
    # 提取函数信息
    arch_name=extract_arch(json_path)
    callers = extract_callers(json_path)
    io_functions = extract_io_functions(json_path)
    remove_functions = extract_remove_functions(json_path)
    
    print(f"提取了 {len(callers)} 个调用者函数")
    print(f"提取了 {len(io_functions)} 个 IO 函数")
    print(f"提取了 {len(remove_functions)} 个需要跳过的函数")
    
    # 生成 hooks.c 文件到对应目录
    generate_hooks_c(callers, io_functions, remove_functions, output_dir,arch_name)
    print(f"成功生成所有钩子文件到目录: {output_dir}")

    # 编译生成的钩子文件
    compile_hooks_c(output_dir,arch_name)
    
    # 复制二进制文件并添加依赖
    setup_binaries_and_patch(json_path, output_dir)
    
if __name__ == '__main__':
    main()