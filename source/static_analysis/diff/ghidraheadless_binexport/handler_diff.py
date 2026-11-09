import json
import pandas as pd
import os
import argparse
#bindiff的量化，但是现在没什么用
def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='分析IO函数调用者的差异情况')
    parser.add_argument('--json_file', required=True, help='IO函数调用者提取结果的JSON文件')
    parser.add_argument('--file_groups', required=True, help='文件分组信息CSV文件')
    parser.add_argument('--diff_file', required=True, help='BinDiff差异结果CSV文件')
    parser.add_argument('--output_file', default='io_callers_diff.csv', help='输出结果CSV文件')
    return parser.parse_args()

def extract_callers_from_json(json_file):
    """
    从JSON文件中提取IO函数的调用者并去重
    
    Args:
        json_file: JSON文件路径
    
    Returns:
        去重后的调用者列表 [(name, address), ...]
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # 获取程序名称和路径信息
        program_name = data.get("program_name", "")
        program_path = data.get("program_path", "")
        
        # 获取待移除函数地址列表
        removed_addrs = set()
        for remove_func in data.get("remove_functions", []):
            addr = remove_func.get("address", "")
            if addr:
                removed_addrs.add(addr)
                
        # 提取IO函数的调用者
        callers_dict = {}  # 使用字典去重
        
        for extract_function in data.get("extract_functions", []):
            func_name = extract_function.get("name", "")
            func_addr = extract_function.get("address", "")
            
            for caller in extract_function.get("callers", []):
                caller_name = caller.get("name", "")
                caller_addr = caller.get("address", "")
                
                if caller_addr in removed_addrs:
                    continue
                # 以调用者地址作为唯一标识符
                caller_key = f"{caller_name}_{caller_addr}"
                
                if caller_key not in callers_dict:
                    callers_dict[caller_key] = {
                        "name": caller_name,
                        "address": caller_addr,
                        "called_functions": []
                    }
                
                # 记录此调用者调用了哪个IO函数
                if func_name not in callers_dict[caller_key]["called_functions"]:
                    callers_dict[caller_key]["called_functions"].append(func_name)
        
        # 转换为列表
        callers = []
        for key, info in callers_dict.items():
            callers.append({
                "name": info["name"],
                "address": info["address"],
                "called_functions": info["called_functions"]
            })
        
        return {
            "program_name": program_name,
            "program_path": program_path,
            "callers": callers
        }
        
    except Exception as e:
        print(f"处理JSON文件时出错: {e}")
        return None

def load_file_groups(file_path):
    """
    加载文件分组信息
    
    Args:
        file_path: CSV文件路径
    
    Returns:
        文件分组字典 {filename: group_id, ...}
    """
    try:
        df = pd.read_csv(file_path)
        file_groups = {}
        
        for _, row in df.iterrows():
            file_groups[row['filename']] = row['group_id']
            
        return file_groups
    except Exception as e:
        print(f"加载文件分组时出错: {e}")
        return {}

def load_diff_results(diff_file):
    """
    加载差异结果
    
    Args:
        diff_file: CSV差异结果文件路径
    
    Returns:
        差异结果DataFrame
    """
    try:
        return pd.read_csv(diff_file)
    except Exception as e:
        print(f"加载差异结果时出错: {e}")
        return pd.DataFrame()

def find_matches_in_diff(callers_info, file_groups, diff_results):
    """
    查找调用者在差异结果中的匹配项
    
    Args:
        callers_info: 调用者信息
        file_groups: 文件分组信息
        diff_results: 差异结果
    
    Returns:
        匹配的差异结果
    """
    program_name = callers_info["program_name"]
    # 从路径中提取文件名（假设格式为AC6_httpd）
    if program_name.endswith("httpd"):
        binary_name = program_name
    else:
        binary_name = f"{program_name.split('_')[-1]}_httpd"
    
    # 获取所有调用者名称
    caller_names = [caller["name"] for caller in callers_info["callers"]]
    
    print(f"程序名称: {program_name}")
    print(f"二进制名称: {binary_name}")
    print(f"找到 {len(caller_names)} 个调用者")
    
    # 查找这个二进制文件所在的组
    group_id = file_groups.get(binary_name)
    if not group_id:
        print(f"警告: 在文件分组中未找到 {binary_name}")
        return pd.DataFrame()
    
    # 找出同组的其他文件
    group_files = [f for f, g in file_groups.items() if g == group_id]
    print(f"同组文件: {group_files}")
    
    # 筛选包含这个二进制文件的差异结果
    binary_diff = diff_results[
        (diff_results['original_sample'].str.contains(binary_name) |
         diff_results['patched_sample'].str.contains(binary_name))
    ]
    
    # 进一步筛选调用者相关的差异
    matches = []
    for caller_name in caller_names:
        # 查找name1或name2中包含调用者名称的行
        caller_matches = binary_diff[
            (binary_diff['name1']==caller_name) |
            (binary_diff['name2']==caller_name)
        ]
        
        if not caller_matches.empty:
            matches.append(caller_matches)
    
    # 合并所有匹配结果
    if matches:
        result = pd.concat(matches, ignore_index=True).drop_duplicates()
        # 添加标识列,表明是否为调用者
        result['is_io_caller'] = True
        return result
    else:
        print("未找到调用者的差异结果")
        return pd.DataFrame()

def main():
    # 设置文件路径
    args= parse_arguments()
    
    # 提取调用者信息
    print(f"正在处理JSON文件: {args.json_file}")
    callers_info = extract_callers_from_json(args.json_file)
    if not callers_info:
        print("无法提取调用者信息")
        return
    
    # 加载文件分组
    print(f"正在加载文件分组: {args.file_groups}")
    file_groups = load_file_groups(args.file_groups)
    if not file_groups:
        print("无法加载文件分组")
        return
    
    # 加载差异结果
    print(f"正在加载差异结果: {args.diff_file}")
    diff_results = load_diff_results(args.diff_file)
    if diff_results.empty:
        print("无法加载差异结果")
        return
    
    # 查找调用者在差异结果中的匹配项
    matched_diffs = find_matches_in_diff(callers_info, file_groups, diff_results)
    
    # 保存结果
    if not matched_diffs.empty:
        output_file = args.output_file
        matched_diffs.to_csv(output_file, index=False)
        print(f"找到 {len(matched_diffs)} 个匹配结果，已保存到 {output_file}")
        
        # 统计相似度分布
        similarity_stats = matched_diffs['similarity'].describe()
        print("\n相似度统计:")
        print(f"平均值: {similarity_stats['mean']:.2f}%")
        print(f"最小值: {similarity_stats['min']:.2f}%")
        print(f"最大值: {similarity_stats['max']:.2f}%")
        print(f"标准差: {similarity_stats['std']:.2f}%")
        
        potential_fixes = matched_diffs[matched_diffs['similarity'] < 1]
        if not potential_fixes.empty:
            print(f"\n发现 {len(potential_fixes)} 个相似度低于100%的函数，可能存在漏洞修复:")
            for _, row in potential_fixes.iterrows():
                print(f"- {row['name1']} <-> {row['name2']} (相似度: {row['similarity']:.2f}%)")
    else:
        print("未找到匹配结果")

if __name__ == "__main__":
    main()