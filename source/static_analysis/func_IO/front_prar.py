#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#解析satc的输出，然后生成prar_statistics.json文件
import re
import json
import os
import sys
import argparse
    
def parse_prar_detail(file_path):
    """
    解析Prar_detail.result文件，提取参数名称和对应的二进制文件路径
    
    Args:
        file_path: Prar_detail.result文件路径
    
    Returns:
        按二进制文件分类的参数字典，同时保存完整路径
    """
    # 初始化结果字典，使用更丰富的结构
    bin_files = {}
    prar_names = []
    try:
        # 按行读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # 找到参数名
            if line.startswith("Prar name :"):
                prar_name = line.split(":", 1)[1].strip()
                prar_names.append(prar_name)
                # 跳过Source File行
                i += 1
                
                # 跳过Text File行及其内容
                while i < len(lines) and not lines[i].strip().startswith("Bin File:"):
                    i += 1
                
                # 找到Bin File行
                if i < len(lines) and lines[i].strip().startswith("Bin File:"):
                    i += 1  # 移到第一个可能的二进制文件路径
                    
                    # 收集所有二进制文件路径
                    bin_paths = []
                    while i < len(lines) and lines[i].strip() and lines[i].strip().startswith("/"):
                        bin_path = lines[i].strip()
                        bin_paths.append(bin_path)
                        i += 1
                    
                    # 为每个二进制文件添加参数名
                    for bin_path in bin_paths:
                        bin_filename = os.path.basename(bin_path)
                        
                        if bin_filename not in bin_files:
                            bin_files[bin_filename] = {
                                "full_paths": set(),  # 使用集合避免路径重复
                                "prar_names": []
                            }
                        
                        # 添加完整路径
                        bin_files[bin_filename]["full_paths"].add(bin_path)
                        
                        # 添加参数名
                        if prar_name not in bin_files[bin_filename]["prar_names"]:
                            bin_files[bin_filename]["prar_names"].append(prar_name)
            
            i += 1
            
    except Exception as e:
        print(f"解析文件时出错: {e}")
        import traceback
        traceback.print_exc()
    
    # 将路径集合转换为列表，便于JSON序列化
    for bin_file in bin_files:
        bin_files[bin_file]["full_paths"] = list(bin_files[bin_file]["full_paths"])
        
    return bin_files,prar_names

def generate_json_output(bin_files, output_file):
    """
    将处理结果输出为JSON格式，包含完整路径
    
    Args:
        bin_files: 按二进制文件分类的参数字典
        output_file: 输出文件路径
    """
    try:
        # 构建JSON结构
        result = {
            "bin_files": []
        }
        
        for bin_file, data in bin_files.items():
            result["bin_files"].append({
                "file_name": bin_file,
                "bin_paths": data["full_paths"],
                "prar_names": data["prar_names"]
            })
        
        # 写入JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        
        print(f"已成功输出到 {output_file}")
    
    except Exception as e:
        print(f"生成JSON输出时出错: {e}")
        
def find_prar_detail_file(input_dir):
    """
    在输入目录中查找Prar_detail.result文件
    
    Args:
        input_dir: 输入目录路径
    
    Returns:
        Prar_detail.result文件的完整路径，如果找不到则返回None
    """
    # 构建预期的文件路径
    expected_path = os.path.join(input_dir, "keyword_extract_result", "detail", "Prar_detail.result")
    
    if os.path.exists(expected_path):
        print(f"找到Prar_detail.result文件: {expected_path}")
        return expected_path
    else:
        print(f"未找到Prar_detail.result文件: {expected_path}")
        
        # 尝试递归搜索
        print("尝试在输入目录中递归搜索Prar_detail.result文件...")
        for root, dirs, files in os.walk(input_dir):
            if "Prar_detail.result" in files:
                found_path = os.path.join(root, "Prar_detail.result")
                print(f"在以下位置找到文件: {found_path}")
                return found_path
        
        return None
    
def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='解析SaTC输出并生成prar_statistics.json文件')
    parser.add_argument('input_dir', help='输入文件夹路径（包含keyword_extract_result/detail/Prar_detail.result）')
    parser.add_argument('output_dir', help='输出文件夹路径（将生成prar_statistics.json）')
    
    # 如果没有提供命令行参数，尝试从sys.argv获取
    if len(sys.argv) < 3:
        print("用法: python front_prar.py <输入文件夹> <输出文件夹>")
        print("例如: python front_prar.py /root/FHFuzz/SaTC/satc_front/result/G0_tenda /root/output")
        sys.exit(1)
    args = parser.parse_args()
    
    input_dir = args.input_dir
    output_dir = args.output_dir
        # 验证输入目录是否存在
    if not os.path.exists(input_dir):
        print(f"错误: 输入目录不存在: {input_dir}")
        sys.exit(1)
    
    # 创建输出目录（如果不存在）
    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"输出目录: {output_dir}")
    except Exception as e:
        print(f"错误: 无法创建输出目录 {output_dir}: {e}")
        sys.exit(1)
    
    # 查找输入文件
    input_file = find_prar_detail_file(input_dir)
    if input_file is None:
        print(f"错误: 在输入目录 {input_dir} 中未找到 Prar_detail.result 文件")
        print("请确保输入目录包含 keyword_extract_result/detail/Prar_detail.result 文件")
        sys.exit(1)
    
    # 设置输出文件路径
    output_file = os.path.join(output_dir, "prar_statistics.json")
    
    print(f"输入文件: {input_file}")
    print(f"输出文件: {output_file}")  
    
      
    # 解析输入文件
    try:
        bin_files, prar_names = parse_prar_detail(input_file)
        
        if not bin_files:
            print("警告: 未解析到任何数据")
            return
        
        # 按参数数量排序
        sorted_bin_files = sorted(bin_files.items(), key=lambda x: len(x[1]["prar_names"]), reverse=True)
        sorted_bin_files_dict = dict(sorted_bin_files)
        
        # 输出结果
        generate_json_output(sorted_bin_files_dict, output_file)
        
        # 打印统计信息
        total_bin_files = len(sorted_bin_files)
        total_prar_names = len(set(prar_names))  # 使用集合去重参数名称
        
        print(f"\n统计结果:")
        print(f"- 总共有 {total_bin_files} 个二进制文件")
        print(f"- 总共有 {total_prar_names} 个参数名称")
        
        # 找出包含最多参数的文件
        if total_bin_files > 0:
            print(f"\n包含参数最多的前3个文件:")
            for i, (file_name, data) in enumerate(sorted_bin_files):
                if i < 3:
                    print(f"  {i+1}. 文件 '{file_name}' 包含 {len(data['prar_names'])} 个参数")
            
            if total_bin_files > 0:
                print(f"\n文件 '{sorted_bin_files[0][0]}' 包含最多参数，共 {len(sorted_bin_files[0][1]['prar_names'])} 个")
    
    except Exception as e:
        print(f"处理过程中出错: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()