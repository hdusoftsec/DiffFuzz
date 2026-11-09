import subprocess
import sys
import os
import argparse

def run_command(cmd, description):
    """运行命令并处理错误"""
    print(f"\n{'='*60}")
    print(f"正在执行: {description}")
    print(f"命令: {cmd}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                              capture_output=False, text=True)
        print(f"✓ {description} 执行成功")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} 执行失败，返回码: {e.returncode}")
        return False

def main():
    parser = argparse.ArgumentParser(description="综合运行静态分析工具链")
    parser.add_argument("firmware_dir", help="固件解压目录 (例如: squashfs-root)")
    parser.add_argument("output_dir", help="输出目录")
    
    args = parser.parse_args()
    
    # 验证输入目录是否存在
    if not os.path.exists(args.firmware_dir):
        print(f"错误: 固件目录不存在: {args.firmware_dir}")
        sys.exit(1)
    
    # 创建输出目录
    os.makedirs(args.output_dir, exist_ok=True)
    
    success_count = 0
    total_commands = 2
    
    # 第一步: 运行 SaTC
    satc_cmd = f'python3 ./SaTC/satc_front/satc.py -d "{args.firmware_dir}" -o "{args.output_dir}" --ghidra_script=all'
    if run_command(satc_cmd, "SaTC 静态分析"):
        success_count += 1
    
    # 第二步: 运行 func_IO
    func_io_cmd = f'python3 ./static_analysis/func_IO/front_prar.py "{args.output_dir}" "{args.output_dir}"'
    if run_command(func_io_cmd, "func_IO 分析"):
        success_count += 1
    
    # 输出总结
    print(f"\n{'='*60}")
    print(f"执行完成: {success_count}/{total_commands} 个命令成功")
    print(f"输出目录: {args.output_dir}")
    print(f"{'='*60}")
    
    if success_count == total_commands:
        print("✓ 所有命令执行成功")
        sys.exit(0)
    else:
        print("✗ 部分命令执行失败")
        sys.exit(1)

if __name__ == "__main__":
    main()