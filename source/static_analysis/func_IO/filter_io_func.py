#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析handler函数和函数使用统计的关联性
统计function_usage_analysis中的函数在多少个handler函数中被调用
"""

import json
import os
import sys
import argparse
from collections import defaultdict, Counter
from openai import OpenAI

def LLM_analysis(func_info):
    """
    使用LLM分析二进制文件之间的差异
    """
    
    client=OpenAI(api_key="",base_url="")
    try:
        system_prompt='''
        分析固件二进制程序中的web程序中的函数，帮我判断其是否是读取用户输入的函数。类似于websGetVar(wp,name,default_value)这种读取用户输入然后在handler函数中进行处理的函数。
        我会分别给你提供需要分析的函数名、该函数使用场景的反编译代码。
        请你分析这个函数自身是否是读取用户输入的IO函数。你需要关注的是这个函数而不是使用场景的其他函数。
        
        输出格式必须是以下JSON对象：
        {
            "significant": true/false, 
            "reason": "简要解释"
        }
            reason应简明扼要地说明您对significant的判断理由。
        '''
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                    {"role": "system","content":system_prompt},
                    {"role": "user", "content":f"请分析函数:{func_info['function_name']},\n使用场景: {func_info['sample_call_context_pseudocode']}"},
            ],
            top_p=0.8,
            temperature=0.7,
            stream=True,
            # extra_body={
            #     "enable_thinking":True,
            #     "thinking_budget":4000
            # },
            # response_format={
            #         'type': 'json_object'
            # }
        )
        # 收集流式输出
        collected_content = ""
        # 迭代流式响应的每个部分
        for chunk in response:
            # 提取当前块的内容
            if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content is not None:
                content_piece = chunk.choices[0].delta.content
                collected_content += content_piece
        
        return collected_content
        # return response.choices[0].message.content
    except Exception as e:
        print(f"调用LLM时发生错误: {e}")
        return None
def parse_llm_response(llm_response):
    """解析LLM响应，提取significant和reason"""
    try:
        # 尝试从响应中提取JSON
        if '```json' in llm_response:
            # 提取```json```之间的内容
            start = llm_response.find('```json') + 7
            end = llm_response.find('```', start)
            json_str = llm_response[start:end].strip()
        elif '{' in llm_response and '}' in llm_response:
            # 提取第一个完整的JSON对象
            start = llm_response.find('{')
            end = llm_response.rfind('}') + 1
            json_str = llm_response[start:end]
        else:
            return None, "无法解析LLM响应"
        
        # 解析JSON
        result = json.loads(json_str)
        significant = result.get('significant', False)
        reason = result.get('reason', '未提供原因')
        
        return significant, reason
        
    except json.JSONDecodeError as e:
        return None, f"JSON解析失败: {str(e)}"
    except Exception as e:
        return None, f"解析错误: {str(e)}"
    
def load_json_file(file_path):
    """加载JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"错误: 文件不存在 - {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"错误: JSON解析失败 - {file_path}: {e}")
        return None
    except Exception as e:
        print(f"错误: 读取文件失败 - {file_path}: {e}")
        return None

def extract_handler_subcalls(handler_data):
    """从handler数据中提取所有子调用函数名"""
    all_subcalls = set()
    
    for handler in handler_data:
        handler_name = handler.get('name', 'unknown')
        subcalls = handler.get('subcalls', [])
        
        for subcall in subcalls:
            subcall_name = subcall.get('name', '')
            if subcall_name:
                all_subcalls.add(subcall_name)
    
    return all_subcalls

def count_handler_usage(handler_data, target_functions):
    """统计每个目标函数在多少个handler中被使用"""
    function_handler_count = defaultdict(int)
    function_handler_details = defaultdict(list)
    
    for handler in handler_data:
        handler_name = handler.get('name', 'unknown')
        handler_address = handler.get('address', 'unknown')
        subcalls = handler.get('subcalls', [])
        
        # 获取这个handler中调用的所有函数名
        handler_subcall_names = {subcall.get('name', '') for subcall in subcalls}
        
        # 检查目标函数是否在这个handler中被调用
        for target_func in target_functions:
            if target_func in handler_subcall_names:
                function_handler_count[target_func] += 1
                function_handler_details[target_func].append({
                    'handler_name': handler_name,
                    'handler_address': handler_address,
                    'subcalls_count': len(subcalls)
                })
    
    return function_handler_count, function_handler_details

def get_function_usage_info(usage_data, function_name):
    """获取函数的使用统计信息（包括sample_call_context_pseudocode）"""
    for func_stat in usage_data.get('function_statistics', []):
        if func_stat.get('function_name') == function_name:
            return {
                'rank': func_stat.get('rank', 0),
                'usage_count': func_stat.get('usage_count', 0),
                'exact_matches': func_stat.get('exact_matches', 0),
                'partial_matches': func_stat.get('partial_matches', 0),
                'is_external': func_stat.get('is_external', False),
                'function_address': func_stat.get('function_address', 'unknown'),
                'function_pseudocode': func_stat.get('function_pseudocode', ''),
                'sample_call_context_pseudocode': func_stat.get('sample_call_context_pseudocode', ''),
                'usage_examples': func_stat.get('usage_examples', [])
            }
    return None

def analyze_function_handler_correlation(input_dir, output_dir,ai_flag=False):
    """分析函数与handler的关联性"""
    
    # 文件路径
    handler_file = os.path.join(input_dir, "combined_handler_functions.json")
    usage_file = os.path.join(input_dir, "function_usage_analysis.json")
    
    # 检查文件是否存在
    if not os.path.exists(handler_file):
        print(f"错误: 未找到文件 {handler_file}")
        return False
    
    if not os.path.exists(usage_file):
        print(f"错误: 未找到文件 {usage_file}")
        return False
    
    # 加载数据
    print("正在加载数据文件...")
    handler_data = load_json_file(handler_file)
    usage_data = load_json_file(usage_file)
    
    if handler_data is None or usage_data is None:
        return False
    
    print(f"加载了 {len(handler_data)} 个handler函数")
    print(f"加载了 {len(usage_data.get('function_statistics', []))} 个函数使用统计")
    
    # 提取所有handler中的子调用函数
    all_handler_subcalls = extract_handler_subcalls(handler_data)
    print(f"handler函数中总共调用了 {len(all_handler_subcalls)} 个不同的函数")
    
    # 获取function_usage_analysis中的函数列表
    usage_functions = [func.get('function_name') for func in usage_data.get('function_statistics', [])]
    print(f"函数使用统计中有 {len(usage_functions)} 个函数")
    
    # 找到既在handler中被调用，又在usage统计中的函数
    common_functions = set(usage_functions) & all_handler_subcalls
    print(f"同时存在于两个数据集中的函数: {len(common_functions)} 个")
    
    if not common_functions:
        print("没有找到共同的函数，无法进行分析")
        return False
    
    # 统计每个函数在多少个handler中被使用
    print("\n正在统计函数在handler中的使用情况...")
    function_handler_count, function_handler_details = count_handler_usage(handler_data, common_functions)
    
    # 按使用的handler数量排序
    sorted_functions = sorted(function_handler_count.items(), key=lambda x: x[1], reverse=True)
    
    # 过滤掉使用次数为0的函数
    filtered_functions = [(func, count) for func, count in sorted_functions if count > 0]
    
    if not filtered_functions:
        print("没有找到在handler中被调用的函数")
        return False
    
    print(f"找到 {len(filtered_functions)} 个在handler中被调用的函数")
    analysis_results = []
    ai_filtered_count = 0
    ai_total_analyzed = 0
    if ai_flag:
        print("\n开始AI辅助分析...")
        
        for i, (function_name, handler_count) in enumerate(filtered_functions, 1):
            usage_info = get_function_usage_info(usage_data, function_name)
            if usage_info :
                ai_total_analyzed += 1
                print(f"[{i}/{len(filtered_functions)}] AI分析函数: {function_name}")
                if usage_info.get('is_external', False):
                    print(f"  函数 {function_name} 是外部函数，跳过AI分析")
                    continue
                # 使用LLM分析函数调用情况
                analysis_result = LLM_analysis({
                    'function_name': function_name,
                    'function_pseudocode': usage_info['function_pseudocode'],
                    'sample_call_context_pseudocode': usage_info['sample_call_context_pseudocode']
                })
                
                if analysis_result:
                    significant, reason = parse_llm_response(analysis_result)
                    
                    if significant is not None:
                        # 添加AI分析结果到usage_info
                        usage_info['ai_analysis'] = {
                            'significant': significant,
                            'reason': reason,
                            'raw_response': analysis_result
                        }
                        
                        print(f"  AI分析结果: {'重要' if significant else '不重要'} - {reason}")
                        
                        # 只有AI认为重要的函数才加入结果
                        if significant:
                            ai_filtered_count += 1
                            result = {
                                'function_name': function_name,
                                'handler_count': handler_count,
                                'handler_details': function_handler_details[function_name],
                                'usage_info': usage_info
                            }
                            analysis_results.append(result)
                        else:
                            print(f"  函数 {function_name} 被AI过滤掉")
                    else:
                        print(f"  AI分析解析失败: {reason}")
                        # 解析失败时，保守地加入结果
                        usage_info['ai_analysis'] = {
                            'significant': None,
                            'reason': f"解析失败: {reason}",
                            'raw_response': analysis_result
                        }
                        result = {
                            'function_name': function_name,
                            'handler_count': handler_count,
                            'handler_details': function_handler_details[function_name],
                            'usage_info': usage_info
                        }
                        analysis_results.append(result)
                else:
                    print(f"  LLM分析失败 for {function_name}")
                    # LLM分析失败时，保守地加入结果
                    usage_info['ai_analysis'] = {
                        'significant': None,
                        'reason': "LLM调用失败",
                        'raw_response': None
                    }
                    result = {
                        'function_name': function_name,
                        'handler_count': handler_count,
                        'handler_details': function_handler_details[function_name],
                        'usage_info': usage_info
                    }
                    analysis_results.append(result)
        
        print(f"\nAI分析完成:")
        print(f"  - 总分析函数数: {ai_total_analyzed}")
        print(f"  - AI认为重要的函数数: {ai_filtered_count}")
        print(f"  - 过滤比例: {(ai_total_analyzed - ai_filtered_count) / ai_total_analyzed * 100:.1f}%" if ai_total_analyzed > 0 else "0%")
        
    else:
        print("\n未启用AI分析，使用原始方法...")
        # 未启用AI分析，按原先的方法处理所有函数
        for function_name, handler_count in filtered_functions:
            usage_info = get_function_usage_info(usage_data, function_name)
            
            result = {
                'function_name': function_name,
                'handler_count': handler_count,
                'handler_details': function_handler_details[function_name],
                'usage_info': usage_info
            }
            analysis_results.append(result)
    
    if not analysis_results:
        print("没有函数通过筛选")
        return False
    
    # 按handler使用数量重新排序（因为AI过滤可能改变了顺序）
    analysis_results.sort(key=lambda x: x['handler_count'], reverse=True)
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 保存详细分析结果为JSON
    json_output_file = os.path.join(output_dir, "function_handler_correlation_analysis.json")
    output_data = {
        'summary': {
            'total_handlers': len(handler_data),
            'total_usage_functions': len(usage_functions),
            'common_functions': len(common_functions),
            'functions_used_in_handlers': len(filtered_functions),
            'final_selected_functions': len(analysis_results),
            'ai_analysis_enabled': ai_flag,
            'ai_filter_stats': {
                'total_analyzed': ai_total_analyzed,
                'ai_significant_count': ai_filtered_count,
                'filter_rate': (ai_total_analyzed - ai_filtered_count) / ai_total_analyzed if ai_total_analyzed > 0 else 0
            } if ai_flag else None,
            'analysis_timestamp': None
        },
        'detailed_results': analysis_results
    }
    
    with open(json_output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    # 保存简化的统计报告
    report_file = os.path.join(output_dir, "function_handler_correlation_report.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# 函数在Handler中的使用分析报告\n\n")
        
        f.write("## 分析摘要\n\n")
        f.write(f"- 总Handler函数数: {len(handler_data)}\n")
        f.write(f"- 函数使用统计中的函数数: {len(usage_functions)}\n")
        f.write(f"- 共同函数数: {len(common_functions)}\n")
        f.write(f"- 在Handler中被调用的函数数: {len(filtered_functions)}\n")
        f.write(f"- 最终筛选出的函数数: {len(analysis_results)}\n")
        f.write(f"- AI分析已启用: {'是' if ai_flag else '否'}\n")
        
        if ai_flag:
            f.write(f"- AI分析统计:\n")
            f.write(f"  - 总分析函数数: {ai_total_analyzed}\n")
            f.write(f"  - AI认为重要的函数数: {ai_filtered_count}\n")
            f.write(f"  - 过滤比例: {(ai_total_analyzed - ai_filtered_count) / ai_total_analyzed * 100:.1f}%\n" if ai_total_analyzed > 0 else "  - 过滤比例: 0%\n")
        
        f.write("\n")
        
        f.write("## 函数使用统计 (按Handler使用数量排序)\n\n")
        if ai_flag:
            f.write("| 排名 | 函数名 | Handler使用数 | 字符串使用统计排名 | 字符串使用次数 | 是否外部函数 | AI重要性 | AI分析原因 |\n")
            f.write("|------|--------|---------------|-------------------|----------------|-------------|----------|------------|\n")
        else:
            f.write("| 排名 | 函数名 | Handler使用数 | 字符串使用统计排名 | 字符串使用次数 | 是否外部函数 |\n")
            f.write("|------|--------|---------------|-------------------|----------------|-------------|\n")
        
        for i, result in enumerate(analysis_results, 1):
            function_name = result['function_name']
            handler_count = result['handler_count']
            usage_info = result['usage_info']
            
            if usage_info:
                rank = usage_info['rank']
                usage_count = usage_info['usage_count']
                is_external = '是' if usage_info['is_external'] else '否'
            else:
                rank = 'N/A'
                usage_count = 'N/A'
                is_external = 'N/A'
            
            if ai_flag and usage_info and 'ai_analysis' in usage_info:
                ai_significant = usage_info['ai_analysis']['significant']
                ai_reason = usage_info['ai_analysis']['reason']
                ai_significant_str = '是' if ai_significant else '否' if ai_significant is not None else '未知'
                f.write(f"| {i} | `{function_name}` | {handler_count} | {rank} | {usage_count} | {is_external} | {ai_significant_str} | {ai_reason[:50]}... |\n")
            else:
                f.write(f"| {i} | `{function_name}` | {handler_count} | {rank} | {usage_count} | {is_external} |\n")
        
        f.write(f"\n## 详细分析 (Top 20)\n\n")
        
        for i, result in enumerate(analysis_results[:20], 1):
            function_name = result['function_name']
            handler_count = result['handler_count']
            usage_info = result['usage_info']
            handler_details = result['handler_details']
            
            f.write(f"### {i}. {function_name}\n\n")
            f.write(f"**在 {handler_count} 个Handler中被调用**\n\n")
            
            if usage_info:
                f.write(f"**字符串使用统计信息:**\n")
                f.write(f"- 排名: {usage_info['rank']}\n")
                f.write(f"- 使用次数: {usage_info['usage_count']}\n")
                f.write(f"- 精确匹配: {usage_info['exact_matches']}\n")
                f.write(f"- 部分匹配: {usage_info['partial_matches']}\n")
                f.write(f"- 是否外部函数: {'是' if usage_info['is_external'] else '否'}\n")
                f.write(f"- 函数地址: {usage_info['function_address']}\n\n")
                
                # 添加AI分析结果
                if ai_flag and 'ai_analysis' in usage_info:
                    ai_analysis = usage_info['ai_analysis']
                    f.write(f"**AI分析结果:**\n")
                    f.write(f"- 重要性: {'重要' if ai_analysis['significant'] else '不重要' if ai_analysis['significant'] is not None else '未知'}\n")
                    f.write(f"- 分析原因: {ai_analysis['reason']}\n\n")
                
                # 添加使用场景信息
                if usage_info.get('sample_call_context_pseudocode'):
                    f.write(f"**调用上下文示例:**\n")
                    f.write(f"```c\n{usage_info['sample_call_context_pseudocode']}\n```\n\n")
            
            f.write(f"**调用此函数的Handler列表:**\n")
            for detail in handler_details:
                f.write(f"- `{detail['handler_name']}` @ {detail['handler_address']} (子调用数: {detail['subcalls_count']})\n")
            f.write("\n")
    
    # 控制台输出结果
    print(f"\n=== 函数在Handler中的使用统计 (Top 30) ===")
    if ai_flag:
        print(f"{'排名':<4} {'函数名':<35} {'Handler使用数':<12} {'字符串统计排名':<12} {'字符串使用次数':<12} {'AI重要性':<8}")
        print("-" * 95)
    else:
        print(f"{'排名':<4} {'函数名':<35} {'Handler使用数':<12} {'字符串统计排名':<12} {'字符串使用次数':<12}")
        print("-" * 85)
    
    for i, result in enumerate(analysis_results[:30], 1):
        function_name = result['function_name']
        handler_count = result['handler_count']
        usage_info = result['usage_info']
        
        if usage_info:
            rank = usage_info['rank']
            usage_count = usage_info['usage_count']
        else:
            rank = 'N/A'
            usage_count = 'N/A'
        
        if ai_flag and usage_info and 'ai_analysis' in usage_info:
            ai_significant = usage_info['ai_analysis']['significant']
            ai_significant_str = '重要' if ai_significant else '不重要' if ai_significant is not None else '未知'
            print(f"{i:<4} {function_name:<35} {handler_count:<12} {rank:<12} {usage_count:<12} {ai_significant_str:<8}")
        else:
            print(f"{i:<4} {function_name:<35} {handler_count:<12} {rank:<12} {usage_count:<12}")
    
    print(f"\n分析完成!")
    print(f"详细结果已保存到: {json_output_file}")
    print(f"报告已保存到: {report_file}")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='分析函数在Handler中的使用情况')
    parser.add_argument('input_dir', help='输入目录路径（包含combined_handler_functions.json和function_usage_analysis.json）')
    parser.add_argument('output_dir', help='输出目录路径')
    parser.add_argument('--ai_flag', action='store_true', help='是否使用AI分析函数调用情况')
    
    if len(sys.argv) < 3:
        print("用法: python filter_io_func.py <输入目录> <输出目录>")
        print("例如: python filter_io_func.py /root/FHFuzz/dir825_analyis /root/output")
        sys.exit(1)
    
    args = parser.parse_args()
    
    input_dir = args.input_dir
    output_dir = args.output_dir
    ai_flag = args.ai_flag
    # 验证输入目录
    if not os.path.exists(input_dir):
        print(f"错误: 输入目录不存在: {input_dir}")
        sys.exit(1)
    
    # 创建输出目录
    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"输出目录: {output_dir}")
    except Exception as e:
        print(f"错误: 无法创建输出目录 {output_dir}: {e}")
        sys.exit(1)
    
    # 执行分析
    success = analyze_function_handler_correlation(input_dir, output_dir,ai_flag)
    
    if not success:
        print("分析失败")
        sys.exit(1)

if __name__ == "__main__":
    main()