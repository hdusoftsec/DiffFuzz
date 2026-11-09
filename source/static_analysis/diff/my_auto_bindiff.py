'''
1. 读取所有BinExport文件
2. 创建所有可能的两两组合
3. 对每对文件运行bindiff
4. 分析结果并整合函数名称
'''

import sqlite3
import pandas as pd
import glob
import subprocess, os
import itertools
import time
import argparse

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='对多个二进制文件执行BinDiff分析')
    parser.add_argument('--binexport_dir', required=True, help='BinExport文件所在目录')
    parser.add_argument('--output_dir', required=True, help='输出结果的根目录')
    parser.add_argument('--sample_functions', help='包含函数信息的CSV文件路径（可选）')
    parser.add_argument('--similarity_threshold', type=float, default=85.0, help='相似度分类阈值（默认85.0）')
    return parser.parse_args()

def make_all_pairs(files):
    """创建所有文件的两两组合"""
    # 使用itertools.combinations生成所有可能的组合
    all_pairs = []
    for file1, file2 in itertools.combinations(files, 2):
        all_pairs.append((file1, file2))
    return all_pairs

def make_bindiff(original, patched, output_dir):
    """执行bindiff比对"""
    bindiff_dir = os.path.join(output_dir, 'bindiffs')
    # 确保输出目录存在
    os.makedirs(bindiff_dir, exist_ok=True)
    
    orig_name = os.path.basename(original).replace('.BinExport','')
    patched_name = os.path.basename(patched).replace('.BinExport','')
    full_path = os.path.join(bindiff_dir, orig_name + '_vs_' + patched_name + '.BinDiff')
    
    # 执行bindiff命令
    cmd = ['/root/bindiff/build/out/bindiff', original, patched, '--output_dir=' + bindiff_dir]
    print(f"执行命令: {' '.join(cmd)}")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #process.wait()  # 等待命令完成
    stdout_bytes, stderr_bytes = process.communicate()
    stdout = stdout_bytes.decode('utf-8', errors='replace')
    stderr = stderr_bytes.decode('utf-8', errors='replace')
    # 检查文件是否存在，如果不存在等待一段时间再检查
    retry = 0
    while not os.path.exists(full_path) and retry < 5:
        time.sleep(2)
        retry += 1
    
    # 从输出中提取相似度信息
    similarity = None
    confidence = None
    if stdout:
        # 查找相似度行
        for line in stdout.split('\n'):
            if 'Similarity:' in line:
                # 提取相似度和置信度
                try:
                    sim_parts = line.split('Similarity:')[1].strip().split('(Confidence:')
                    if len(sim_parts) >= 2:
                        similarity = float(sim_parts[0].replace('%', '').strip())
                        confidence = float(sim_parts[1].split('%')[0].strip())
                except Exception as e:
                    print(f"无法从输出解析相似度: {e}")
    
    # 从stderr中查找，因为有些版本可能输出到stderr
    if stderr and similarity is None:
        for line in stderr.split('\n'):
            if 'Similarity:' in line:
                try:
                    sim_parts = line.split('Similarity:')[1].strip().split('(Confidence:')
                    if len(sim_parts) >= 2:
                        similarity = float(sim_parts[0].replace('%', '').strip())
                        confidence = float(sim_parts[1].split('%')[0].strip())
                except Exception as e:
                    print(f"无法从错误输出解析相似度: {e}")
    
    result = {
        'path': full_path,
        'similarity': similarity,
        'confidence': confidence,
        'original': orig_name,
        'patched': patched_name
    }
    
    if os.path.exists(full_path):
        return result
    else:
        print(f"无法创建BinDiff文件: {full_path}")
        return None

def bindiff_to_csv(bindiff_diff, output_dir):
    """将bindiff结果转换为CSV"""
    if bindiff_diff is None:
        return 'error'
    
    print('bindiff to csv: ', bindiff_diff)
    funtables_dir = os.path.join(output_dir, 'bindiffs', 'funtables')
    os.makedirs(funtables_dir, exist_ok=True)
    
    try:
        db = sqlite3.connect(bindiff_diff)
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        # 查找包含"function"或"Function"的表
        function_table_name = 'function'
        for table in tables:
            if 'function' in table[0].lower() and table[0].lower()!='functionalgorithm':
                function_table_name = table[0]
                break
                
        if not function_table_name and len(tables) >= 5:
            # 如果没找到函数表名称，尝试使用第5个表（索引4）
            function_table_name = tables[4][0]
        
        if function_table_name:
            table = pd.read_sql_query(f"SELECT * from {function_table_name}", db)
            
            name = os.path.join(funtables_dir, os.path.basename(bindiff_diff) + '_funtable.csv')
            table.to_csv(name, index_label='index')
            cursor.close()
            db.close()
            return name
        else:
            print(f"在 {bindiff_diff} 中找不到函数表")
            return 'error'
    except Exception as e:
        print(f"处理 {bindiff_diff} 时出错: {e}")
        return 'error'

def get_fcn(name_sample_addr, fun_df):
    """获取函数名称"""
    try:
        index = fun_df.index[fun_df['sample_name_addr'] == name_sample_addr].tolist()[0]
        fun_name = fun_df.iloc[index]['fun_name']
    except:
        fun_name='not_found'
    return fun_name

def load_or_create_function_df(sample_functions_path, output_dir):
    """加载或创建函数数据框架"""
    resources_dir = os.path.join(output_dir, 'resources')
    os.makedirs(resources_dir, exist_ok=True)
    
    default_path = os.path.join(resources_dir, 'sample_functions.csv')
    
    # 如果提供了sample_functions路径且文件存在，则使用它
    if sample_functions_path and os.path.exists(sample_functions_path):
        fun_df = pd.read_csv(sample_functions_path)
        # 确保列名正确
        if 'fun_name' not in fun_df.columns and len(fun_df.columns) >= 2:
            fun_df.columns = ['path', 'fun_name', 'addr'] + list(fun_df.columns[3:])
    elif os.path.exists(default_path):
        # 否则尝试使用默认路径
        fun_df = pd.read_csv(default_path)
        if 'fun_name' not in fun_df.columns and len(fun_df.columns) >= 2:
            fun_df.columns = ['path', 'fun_name', 'addr'] + list(fun_df.columns[3:])
    else:
        # 如果都不存在，创建一个空的DataFrame
        fun_df = pd.DataFrame(columns=['path', 'fun_name', 'addr'])
        fun_df.to_csv(default_path, index=False)
    
    # 处理名称和地址列
    fun_df['name'] = fun_df['path'].apply(lambda x: os.path.basename(x) if isinstance(x, str) else '')
    fun_df['sample_name_addr'] = fun_df.apply(
        lambda row: row['name'] + '_' + str(row['addr']) if pd.notnull(row['addr']) else '', 
        axis=1
    )
    
    return fun_df, resources_dir

def coorelate_fun_names(table_path, fun_df, resources_dir):
    """关联函数名称"""
    if table_path == 'error':
        return None
    
    try:
        bindiff_df = pd.read_csv(table_path, index_col=[0])
        # 提取原始样本和修补样本的名称
        bindiff_filename = os.path.basename(table_path).replace('_funtable.csv','')
        parts = bindiff_filename.split('_vs_')
        if len(parts) >= 2:
            original_sample = parts[0]
            patched_sample = parts[1].replace('.BinDiff', '')
        else:
            print(f"无法从 {table_path} 中提取样本名称")
            return None
        
        bindiff_df['original_sample'] = original_sample
        bindiff_df['patched_sample'] = patched_sample
        
        # 确保address列是字符串类型
        bindiff_df['address1'] = bindiff_df['address1'].astype(str)
        bindiff_df['address2'] = bindiff_df['address2'].astype(str)
        
        bindiff_df['original_sample_addr'] = bindiff_df['original_sample'] + '_' + bindiff_df['address1']
        bindiff_df['patched_sample_addr'] = bindiff_df['patched_sample'] + '_' + bindiff_df['address2']
        
        #bindiff_df['orig_fun_name'] = bindiff_df['original_sample_addr'].apply(lambda x: get_fcn(x, fun_df))
        #bindiff_df['patched_fun_name'] = bindiff_df['patched_sample_addr'].apply(lambda x: get_fcn(x, fun_df))
        
        csv_name = os.path.join(resources_dir, bindiff_filename + '_finaldf.csv')
        bindiff_df.to_csv(csv_name)
        return bindiff_df
    except Exception as e:
        print(f"处理 {table_path} 时出错: {e}")
        return None

def classify_files_by_similarity(similarity_results, threshold, resources_dir):
    """
    根据相似度将文件分类
    
    参数:
    - similarity_results: 相似度结果列表
    - threshold: 相似度阈值，大于等于此值的文件被归为一类
    - resources_dir: 资源输出目录
    
    返回:
    - 分类结果列表
    """
    if not similarity_results:
        print("没有相似度数据，无法进行分类")
        return []
    
    # 创建相似度DataFrame并保存
    similarity_df = pd.DataFrame(similarity_results)
    sim_csv_path = os.path.join(resources_dir, 'similarity_results.csv')
    similarity_df.to_csv(sim_csv_path, index=False)
    print(f"相似度结果已保存到 {sim_csv_path}")
    
    # 提取所有唯一的文件名
    all_files = set()
    for record in similarity_results:
        all_files.add(record['file1'])
        all_files.add(record['file2'])
    
    print(f"\n使用相似度阈值 {threshold}% 对文件进行分类...")
    
    # 创建文件分组
    file_groups = []
    ungrouped = set(all_files)
    
    while ungrouped:
        # 从未分组文件中取第一个作为新组的种子
        seed = next(iter(ungrouped))
        current_group = {seed}
        ungrouped.remove(seed)
        
        # 扩展当前组
        changed = True
        while changed:
            changed = False
            to_add = set()
            
            # 检查所有未分组文件
            for file in list(ungrouped):
                # 检查此文件与当前组中任何文件的相似度
                for grouped_file in current_group:
                    # 在similarity_results中查找这对文件
                    for record in similarity_results:
                        if ((record['file1'] == file and record['file2'] == grouped_file) or
                            (record['file1'] == grouped_file and record['file2'] == file)):
                            # 如果相似度高于阈值，将此文件添加到当前组
                            if record['similarity'] >= threshold:
                                to_add.add(file)
                                break
            
            # 将找到的文件添加到当前组
            for file in to_add:
                current_group.add(file)
                ungrouped.remove(file)
                changed = True
        
        # 将当前组添加到组列表
        file_groups.append(current_group)
    
    # 输出分组结果
    print(f"\n根据相似度 >= {threshold}% 的标准，文件被分为 {len(file_groups)} 组：")
    
    # 创建分组结果数据
    group_data = []
    for i, group in enumerate(file_groups, 1):
        print(f"\n组 {i}:")
        for file in sorted(group):
            print(f"  - {file}")
            group_data.append({
                'group_id': i,
                'filename': file
            })
    
    # 保存分组结果
    groups_df = pd.DataFrame(group_data)
    groups_csv_path = os.path.join(resources_dir, 'file_groups.csv')
    groups_df.to_csv(groups_csv_path, index=False)
    print(f"\n文件分组结果已保存到 {groups_csv_path}")
    
    # 生成详细的分组报告
    generate_grouping_report(file_groups, similarity_results, all_files, threshold, resources_dir)
    
    return file_groups

def generate_grouping_report(file_groups, similarity_results, all_files, threshold, resources_dir):
    """生成详细的分组报告"""
    report_path = os.path.join(resources_dir, 'grouping_report.txt')
    with open(report_path, 'w') as f:
        f.write(f"文件相似度分组报告 (阈值: {threshold}%)\n")
        f.write("=" * 50 + "\n\n")
        
        f.write(f"总文件数: {len(all_files)}\n")
        f.write(f"总分组数: {len(file_groups)}\n\n")
        
        for i, group in enumerate(file_groups, 1):
            f.write(f"组 {i} (包含 {len(group)} 个文件):\n")
            for file in sorted(group):
                # 计算此文件与组内其他文件的平均相似度
                similarities = []
                for other in group:
                    if other != file:
                        for record in similarity_results:
                            if ((record['file1'] == file and record['file2'] == other) or
                                (record['file1'] == other and record['file2'] == file)):
                                similarities.append(record['similarity'])
                
                avg_sim = sum(similarities) / len(similarities) if similarities else 0
                f.write(f"  - {file} (组内平均相似度: {avg_sim:.2f}%)\n")
            
            # 添加组间相似度信息
            f.write("\n  组内相似度详情:\n")
            for file1 in sorted(group):
                for file2 in sorted(group):
                    if file1 < file2:  # 避免重复对
                        for record in similarity_results:
                            if ((record['file1'] == file1 and record['file2'] == file2) or
                                (record['file1'] == file2 and record['file2'] == file1)):
                                f.write(f"    {file1} <-> {file2}: {record['similarity']:.2f}%\n")
            
            f.write("\n")
        
        f.write("\n完整相似度矩阵:\n")
        # 创建文件名列表
        file_list = sorted(all_files)
        
        # 写入表头
        f.write("File")
        for file in file_list:
            f.write(f",{file}")
        f.write("\n")
        
        # 写入相似度矩阵
        for file1 in file_list:
            f.write(file1)
            for file2 in file_list:
                if file1 == file2:
                    f.write(",100.00")  # 自己与自己的相似度为100%
                else:
                    sim = None
                    for record in similarity_results:
                        if ((record['file1'] == file1 and record['file2'] == file2) or
                            (record['file1'] == file2 and record['file2'] == file1)):
                            sim = record['similarity']
                            break
                    f.write(f",{sim:.2f}" if sim is not None else ",N/A")
            f.write("\n")
    
    print(f"详细分组报告已保存到 {report_path}")

def main():
    """主函数"""
    # 解析命令行参数
    args = parse_arguments()
    
    # 获取所有BinExport文件
    files = sorted([file for file in glob.glob(f'{args.binexport_dir}/*.BinExport')])
    if not files:
        print(f"在 {args.binexport_dir} 中未找到BinExport文件")
        return
    
    print(f"找到 {len(files)} 个BinExport文件")
    
    # 加载或创建函数数据框架
    fun_df, resources_dir = load_or_create_function_df(args.sample_functions, args.output_dir)
    
    # 创建所有可能的文件对
    pairs = make_all_pairs(files)
    print(f"总共有 {len(pairs)} 对文件需要比对")
    
    # 执行bindiff比对
    bindiffs = []
    similar_bindiffs= []
    similarity_results = []
    for file1, file2 in pairs:
        print(f"比对 {os.path.basename(file1)} 和 {os.path.basename(file2)}...")
        result = make_bindiff(file1, file2, args.output_dir)
        if result:
            bindiffs.append(result)
            
            # 记录相似度信息
            orig_name = result['original']
            patched_name = result['patched']
            similarity = result['similarity']
            confidence = result['confidence']
            
            if similarity is not None:
                similarity_results.append({
                    'file1': orig_name,
                    'file2': patched_name,
                    'similarity': similarity,
                    'confidence': confidence
                })
                print(f"相似度: {similarity:.2f}%, 置信度: {confidence:.2f}%")
                
                # 只对相似度大于阈值的结果进行后续处理
                if similarity >= args.similarity_threshold:
                    similar_bindiffs.append(result)
                    print(f"相似度大于{args.similarity_threshold}%，将进行详细分析")
                else:
                    print(f"相似度低于{args.similarity_threshold}%，跳过详细分析")
    
        # 根据相似度对文件进行分类
    if similarity_results:
        file_groups = classify_files_by_similarity(
            similarity_results, 
            args.similarity_threshold, 
            resources_dir
        )
        
    # 转换相似bindiff结果为CSV
    bindiff_fcn_paths = []
    for bindiff in similar_bindiffs:
        if isinstance(bindiff, dict) and 'path' in bindiff:
            result = bindiff_to_csv(bindiff['path'], args.output_dir)
        if result != 'error':
            bindiff_fcn_paths.append(result)
    
    # 关联函数名称
    final_dfs = []
    for path in bindiff_fcn_paths:
        result = coorelate_fun_names(path, fun_df, resources_dir)
        if result is not None:
            final_dfs.append(result)
    
    # 合并所有结果
    if final_dfs:
        final_combined = pd.concat(final_dfs, axis=0)
        final_output_path = os.path.join(resources_dir, 'final_combined.csv')
        final_combined.to_csv(final_output_path)
        print(f"结果已保存到 {final_output_path}")
    else:
        print("没有有效的比对结果")

if __name__ == "__main__":
    main()