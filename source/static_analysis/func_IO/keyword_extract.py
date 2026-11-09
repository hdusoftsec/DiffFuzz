import os
import re

# 配置
SEARCH_ROOT = '/root/FHFuzz/experiment'
TARGET_FILES = {'httpd.result', 'boa.result', 'goahead.result', 'webs.result'}
WORDLIST_PATH = '/root/FHFuzz/static_analysis/func_IO/httpd.wordlist'
OUTPUT_DIR = '/root/FHFuzz/experiment/firmware_keywords'

def parse_wordlist(path):
    """解析 httpd.wordlist 文件，提取现有的关键字值"""
    keywords = []
    if not os.path.exists(path):
        print(f"Warning: {path} not found.")
        return keywords
    
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            # 匹配 strN="content" 格式
            # 使用非贪婪匹配或者假设内容直到最后一个引号
            match = re.match(r'str\d+="(.+)"', line)
            if match:
                keywords.append(match.group(1))
    return keywords

def parse_result_file(path):
    """解析结果文件，提取空格分隔的关键字"""
    keywords = set()
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # 假设关键字由空白字符分隔
            words = content.split()
            for w in words:
                if w:
                    keywords.add(w)
    except Exception as e:
        print(f"Error reading {path}: {e}")
    return list(keywords)

def get_firmware_name(path):
    """从文件路径中推断固件名称"""
    parts = path.split(os.sep)
    
    # 策略 1: 查找 firmware_SaTC 目录，取其后的 Brand/Name
    try:
        if 'firmware_SaTC' in parts:
            idx = parts.index('firmware_SaTC')
            # 尝试取 Brand_Model，例如 Tenda_AC6
            if idx + 2 < len(parts):
                return f"{parts[idx+1]}_{parts[idx+2]}"
            elif idx + 1 < len(parts):
                return parts[idx+1]
    except ValueError:
        pass
    
    # 策略 2: 查找 keyword_extract_result 的上级目录
    try:
        if 'keyword_extract_result' in parts:
            idx = parts.index('keyword_extract_result')
            if idx > 0:
                # 如果上级是 simple 或 .data 等，继续向上找
                name = parts[idx-1]
                if name in ['.data', 'simple'] and idx > 1:
                    return parts[idx-2]
                return name
    except ValueError:
        pass

    # 策略 3: 如果路径中包含 _result 结尾的目录，取该目录名
    for part in parts:
        if part.endswith('_result') and part != 'keyword_extract_result':
            return part.replace('_result', '')

    # 策略 4: 默认取文件所在目录的上两级（假设结构为 .../Firmware/subdir/file）
    if len(parts) > 2:
        # 避免取到 .data 或 simple 这样的名字
        parent = parts[-2]
        if parent in ['.data', 'simple', 'keyword_extract_result'] and len(parts) > 3:
            return parts[-3]
        return parent
    
    return "unknown_firmware"

def main():
    # 创建输出目录
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Created output directory: {OUTPUT_DIR}")

    # 1. 读取基础 wordlist
    base_keywords = parse_wordlist(WORDLIST_PATH)
    print(f"Loaded {len(base_keywords)} base keywords from {WORDLIST_PATH}")

    # 2. 遍历目录查找目标文件
    found_count = 0
    for root, dirs, files in os.walk(SEARCH_ROOT):
        # 跳过输出目录，防止循环处理
        if OUTPUT_DIR in root:
            continue
            
        for file in files:
            if file in TARGET_FILES:
                full_path = os.path.join(root, file)
                found_count += 1
                print(f"\nProcessing: {full_path}")
                
                # 3. 确定固件名称
                firmware_name = get_firmware_name(full_path)
                print(f"  -> Firmware Name: {firmware_name}")
                
                # 4. 提取新关键字
                new_keywords = parse_result_file(full_path)
                print(f"  -> Found {len(new_keywords)} keywords in file.")
                
                # 5. 合并关键字 (保持 base_keywords 顺序，追加新的)
                combined_keywords = list(base_keywords)
                existing_set = set(base_keywords)
                
                added_count = 0
                for k in new_keywords:
                    if k not in existing_set:
                        combined_keywords.append(k)
                        existing_set.add(k)
                        added_count += 1
                print(f"  -> Added {added_count} new keywords.")
                
                # 6. 写入结果文件
                output_filename = f"{firmware_name}_keywords"
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                
                try:
                    with open(output_path, 'w', encoding='utf-8') as f:
                        for i, k in enumerate(combined_keywords):
                            f.write(f'str{i}="{k}"\n')
                    print(f"  -> Saved to {output_path}")
                except Exception as e:
                    print(f"  -> Error writing output: {e}")

    if found_count == 0:
        print("\nNo target files found.")
    else:
        print(f"\nDone. Processed {found_count} files.")

if __name__ == '__main__':
    main()