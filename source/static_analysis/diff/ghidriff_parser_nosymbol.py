import json
import sys
import os
import argparse
import time
import datetime
from openai import OpenAI
from itertools import combinations
import concurrent.futures

# Add a simple stats collector class
class StatsCollector:
    def __init__(self, model_name):
        self.model_name = model_name
        self.query_count = 0
        self.total_query_time = 0
        self.queries = []
        self.start_time = time.time()
    
    def add_query(self, duration, success, function_name=None, binary_pair=None, result=None):
        self.query_count += 1
        self.total_query_time += duration
        
        entry = {
            "duration": duration,
            "success": success,
            "timestamp": time.time()
        }
        
        if function_name:
            entry["function_name"] = function_name
        if binary_pair:
            entry["binary_pair"] = binary_pair
        if result:
            # 结果已经是字典形式，直接使用
            if isinstance(result, dict):
                entry["result"] = result
            else:
                try:
                    # 尝试解析JSON结果以便在日志中更好地显示
                    parsed_result = parse_llm_json(result)
                    if parsed_result:
                        entry["result"] = parsed_result
                    else:
                        entry["result"] = result
                except:
                    entry["result"] = result
            
        self.queries.append(entry)
        
    def get_summary(self):
        end_time = time.time()
        total_analysis_time = end_time - self.start_time
        avg_query_time = self.total_query_time / self.query_count if self.query_count > 0 else 0
        
        return {
            "model": self.model_name,
            "total_analysis_time": total_analysis_time,
            "query_count": self.query_count,
            "total_query_time": self.total_query_time,
            "average_query_time": avg_query_time
        }
    
    def save_log(self, output_dir, prefix=None):
        summary = self.get_summary()
        
        if prefix:
            log_name = f"{prefix}_{self.model_name}"
        else:
            log_name = self.model_name
            
        log_file = os.path.join(output_dir, f"{log_name}_stats.json")
        
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"统计信息已保存到: {log_file}")
        
        # Also save a detailed log
        detailed_log_file = os.path.join(output_dir, f"{log_name}_detailed_log.json")
        with open(detailed_log_file, 'w', encoding='utf-8') as f:
            json.dump(self.queries, f, indent=2)

import re

def parse_llm_json(content):
    """
    尝试从LLM的输出中解析JSON对象
    支持处理Markdown代码块和包含其他文本的情况
    """
    if not content:
        return None
        
    try:
        # 1. 尝试直接解析
        return json.loads(content)
    except:
        pass
        
    try:
        # 2. 尝试提取Markdown代码块 ```json ... ``` 或 ``` ... ```
        match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', content, re.DOTALL)
        if match:
            return json.loads(match.group(1))
            
        # 3. 尝试查找第一个 { 和最后一个 } 之间的内容
        match = re.search(r'(\{.*\})', content, re.DOTALL)
        if match:
            return json.loads(match.group(1))
            
    except Exception as e:
        # print(f"JSON解析失败: {e}")
        pass
        
    return None

def build_function_name_mapping(diff_results):
    """
    构建函数名称的等价映射关系，处理相同函数在不同固件中名称不同的情况
    使用并查集思想来合并等价类
    
    Args:
        diff_results: 固件间的差异分析结果
        
    Returns:
        func_name_mapping: 原始函数名到规范名称的映射
        canonical_groups: 规范名称到等价函数集合的映射
    """
    # 第一阶段：收集所有固件对之间的名称映射
    name_mapping_pairs = []  # 存储所有发现的名称对，格式为(name1, name2)
    # 跟踪函数所属的二进制文件，用于防止同一二进制中的不同函数被合并
    function_owners = {}  # name -> set(binaries)
    
    print("\n构建函数名称映射关系...")
    
    for binary_pair, diff_data in diff_results.items():
        binary1, binary2 = binary_pair.split("-")
        matches = diff_data.get("matches", {})
        name_matches = matches.get("name_matches", {})
        
        # 遍历name_matches中的映射关系
        for func_name, match_infos in name_matches.items():
            for match_info in match_infos:
                # 根据提供的结构，match_info是一个列表，第一个元素是匹配的函数名
                if isinstance(match_info, list) and len(match_info) > 0:
                    matched_name = match_info[0]
                    
                    # 记录这对匹配的名称
                    name_mapping_pairs.append((func_name, matched_name))
                    
                    # 记录函数归属
                    if func_name not in function_owners:
                        function_owners[func_name] = set()
                    function_owners[func_name].add(binary1)
                    
                    if matched_name not in function_owners:
                        function_owners[matched_name] = set()
                    function_owners[matched_name].add(binary2)
                    #print(f"  发现匹配: {func_name} <-> {matched_name} (在 {binary1}-{binary2} 之间)")
    
    # 第二阶段：构建等价类，使用并查集的思想
    # 收集所有函数名
    all_func_names = set()
    for name1, name2 in name_mapping_pairs:
        all_func_names.add(name1)
        all_func_names.add(name2)
    
    # 初始化映射，每个函数名映射到自身作为初始规范名称
    func_name_mapping = {name: name for name in all_func_names}
    canonical_groups = {name: {name} for name in all_func_names}
    
    # 合并等价类
    for name1, name2 in name_mapping_pairs:
        root1 = func_name_mapping[name1]
        root2 = func_name_mapping[name2]
        
        if root1 != root2:
            # 检查合并是否会导致同一二进制文件中的不同函数被归为同一类（冲突检测）
            group1 = canonical_groups[root1]
            group2 = canonical_groups[root2]
            
            has_conflict = False
            # 检查所有涉及的二进制文件
            involved_binaries = set()
            for name in group1:
                if name in function_owners:
                    involved_binaries.update(function_owners[name])
            for name in group2:
                if name in function_owners:
                    involved_binaries.update(function_owners[name])
            
            for binary in involved_binaries:
                # 在group1中属于该binary的函数
                funcs_in_g1 = {n for n in group1 if n in function_owners and binary in function_owners[n]}
                # 在group2中属于该binary的函数
                funcs_in_g2 = {n for n in group2 if n in function_owners and binary in function_owners[n]}
                
                # 如果两个组都包含该binary的函数，且这些函数集合不重叠（即不同的函数），则存在冲突
                # 注意：如果集合有交集，说明是同一个函数名（可能是同一个函数），这不算是冲突
                if funcs_in_g1 and funcs_in_g2 and funcs_in_g1.isdisjoint(funcs_in_g2):
                    has_conflict = True
                    # print(f"  跳过合并 {root1} 和 {root2}: 在 {binary} 中存在冲突 ({funcs_in_g1} vs {funcs_in_g2})")
                    break
            
            if has_conflict:
                continue

            # 选择字典序较小的名称作为新的规范名称，确保结果的确定性
            new_root = min(root1, root2)
            old_root = root1 if new_root == root2 else root2
            
            # 合并两个等价类
            merged_group = canonical_groups[root1].union(canonical_groups[root2])
            
            # 更新所有成员的规范名称
            for name in merged_group:
                func_name_mapping[name] = new_root
            
            # 更新等价类集合
            canonical_groups[new_root] = merged_group
            # 删除旧的等价类
            if old_root in canonical_groups and old_root != new_root:
                del canonical_groups[old_root]
    
    # 输出映射统计
    valid_groups = [group for group in canonical_groups.values() if len(group) > 1]
    print(f"\n找到 {len(valid_groups)} 个函数等价组，涉及 {sum(len(g)-1 for g in valid_groups)} 个映射关系")
    
    # 打印等价组信息
    for group_root, group in canonical_groups.items():
        if len(group) > 1:
            group_members = ", ".join(sorted(group))
            print(f"  等价组 [{group_root}]: {group_members}")
    
    return func_name_mapping, canonical_groups

def print_classification_results(classification, binaries):
    """
    打印函数分类结果的统计信息和详细列表
    
    Args:
        classification: 分类结果字典
        binaries: 固件二进制名称列表
    """
    print(f"\n===== 函数分类结果 =====")
    print(f"所有固件共有且相同的handler函数: {len(classification['common_handlers'])}")
    if classification['common_handlers']:
        print("  函数列表:")
        for handler in classification['common_handlers']:
            # 显示在不同固件中的名称
            names_str = ""
            for binary, name in handler.get('names_in_binaries', {}).items():
                if name != handler['canonical_name']:
                    if names_str:
                        names_str += ", "
                    names_str += f"{binary}:{name}"
            
            name_display = handler['canonical_name']
            if names_str:
                name_display += f" (在其他固件中名称: {names_str})"
                
            print(f"    - {name_display} (在 {handler['reference_binary']} 中地址为 {handler['address']})")
    
    print(f"\n部分固件共享且相同的handler函数: {len(classification['partially_shared'])}")
    if classification['partially_shared']:
        print("  函数列表:")
        for handler in classification['partially_shared']:
            shared_binaries = ", ".join(handler['shared_across'])
            
            # 显示在不同固件中的名称
            names_str = ""
            for binary, name in handler.get('names_in_binaries', {}).items():
                if name != handler['canonical_name']:
                    if names_str:
                        names_str += ", "
                    names_str += f"{binary}:{name}"
            
            name_display = handler['canonical_name']
            if names_str:
                name_display += f" (在其他固件中名称: {names_str})"
                
            print(f"    - {name_display} (在 {handler['reference_binary']} 中地址为 {handler['address']}, 共享于: {shared_binaries})")
    
    for binary in binaries:
        unique_count = len(classification["unique_handlers"][binary])
        print(f"\n{binary} 独有的handler函数: {unique_count}")
        if unique_count > 0:
            print("  函数列表:")
            for handler in classification["unique_handlers"][binary]:
                name_display = handler['orig_name']
                if handler['canonical_name'] != handler['orig_name']:
                    name_display = f"{handler['orig_name']} (规范名: {handler['canonical_name']})"
                print(f"    - {name_display} (地址: {handler['address']})")
    
    for key, modified_funcs in classification["modified_handlers"].items():
        print(f"\n{key} 之间修改的handler函数: {len(modified_funcs)}")
        if modified_funcs:
            print("  函数列表:")
            for handler in modified_funcs:
                binary1, binary2 = key.split("-")
                name1 = handler['original_names'].get(binary1, handler['canonical_name'])
                name2 = handler['original_names'].get(binary2, handler['canonical_name'])
                
                if handler['canonical_name'] != name1 or handler['canonical_name'] != name2:
                    print(f"    - {handler['canonical_name']} (规范名)")
                    print(f"      在 {binary1} 中名称为: {name1}, 地址: {handler['old']['address']}")
                    print(f"      在 {binary2} 中名称为: {name2}, 地址: {handler['new']['address']}")
                else:
                    print(f"    - {handler['canonical_name']}")
                    print(f"      在 {binary1} 中地址: {handler['old']['address']}")
                    print(f"      在 {binary2} 中地址: {handler['new']['address']}")
def extract_diff_changes(diff_code):
    """
    从diff代码中提取+++和---对应的代码行
    
    Args:
        diff_code: 完整的diff代码文本
    
    Returns:
        cleaned_diff: 只包含变更部分的代码
    """
    if not diff_code:
        return ""
    
    lines = diff_code.splitlines()
    extracted_lines = []
    in_diff_block = False
    
    for line in lines:
        # 检测diff块的开始
        if line.startswith("@@") and "@@" in line[2:]:
            in_diff_block = True
            # 可选：保留hunk头部信息，帮助理解变更位置
            extracted_lines.append(line)
            continue
        
        # 如果我们在一个diff块内
        if in_diff_block:
            # 提取添加的行
            if line.startswith("+") and not line.startswith("+++"):
                extracted_lines.append(line)
            # 提取删除的行
            elif line.startswith("-") and not line.startswith("---"):
                extracted_lines.append(line)
    
    # 将提取的行组合回一个字符串
    cleaned_diff = "\n".join(extracted_lines)
    return cleaned_diff
def LLM_diff(diff_code, model_type="claude", stats_collector=None, function_name=None, binary_pair=None):
    """
    使用LLM分析二进制文件之间的差异
    
    Args:
        diff_code: 差异代码内容
        model_type: 模型类型，默认为 "claude"，可选 "gpt", "deepseek" 等
        stats_collector: 统计收集器对象
        function_name: 当前分析的函数名
        binary_pair: 当前分析的二进制对
    """
    
    # 配置不同模型的信息
    config = {
        "claude": {
            "api_key": "",
            "base_url": "",
            "model_name": ""
        },
        "gpt": {
            # 可以在这里添加 GPT-5.4 的配置
            "api_key": "",
            "base_url": "", 
            "model_name": ""
        },
        "deepseek": {
            "api_key": "",
            "base_url": "",
            "model_name": ""
        }
    }
    
    start_time = time.time()
    current_config = config.get(model_type, config["claude"])
    
    client = OpenAI(
        api_key=current_config["api_key"],
        base_url=current_config["base_url"]
    )
    
    try:
        system_prompt='''
        Analyze the provided binary diff code and determine if it contains significant changes. Please focus on analyzing the code between lines starting with + and -.
        
        Significant changes are defined as modifications that directly affect program behavior, functionality, or security. 
        

        These include:
        * Function call changes: Adding or removing user-defined functions or standard library functions.
        * Security risk changes: Any introduction, removal, or modification of security-related checks, validations, or operations. Removing a `strncmp` or similar check is a HIGH IMPACT security change.
        * Branch/Check modifications: Changing, adding, or removing branch conditions (if, else if, switch). 
        * Logic flow changes: Modifying operation sequences or algorithms within code blocks, causing different results for the same input.
        * Control flow structure changes: Altering loop structures (for, while), exception handling, or other mechanisms that fundamentally change the sequence of instruction execution.
        * For input functions like websGetVar involving external input processing, changes in their calling method, parameters, or related logic should also be considered significant.
        
        Non-significant changes include:
        * Debug/Log calls: Adding, removing, or modifying calls to printf, logging libraries, or other debugging aids that do not affect the main operation of the program.
        * Variable renaming: Changing variable names without altering their scope or purpose.
        * Offset adjustments: Minor changes to memory offsets that do not reflect fundamental changes in data structures or access logic.
        * Function name adjustments: For stripped functions, changes in address offsets within function names do not affect their functionality or calling method, provided that the parameter count and types remain consistent.
        
        The output format must be the following JSON object:
        {
            "significant": true/false, 
            "reason": "Brief explanation"
        }
            The reason should strictly and briefly explain your judgment for "significant".
        '''

        def _single_query_task(_diff_code):
            max_retries = 3
            for attempt in range(max_retries):
                t_start = time.time()
                try:
                    response = client.chat.completions.create(
                        model=current_config["model_name"],
                        messages=[
                                {"role": "system","content":system_prompt},
                                {"role": "user", "content":f"Please analyze the following diff code:\n\n{_diff_code}\n"}
                        ],
                        top_p=0.8,
                        temperature=0.7,
                    )
                    t_end = time.time()
                    return (response.choices[0].message.content, t_end - t_start)
                except Exception as e:
                    print(f"调用LLM查询失败 (尝试 {attempt+1}/{max_retries}): {e}")
                    if attempt < max_retries - 1:
                        time.sleep(2)  # 等待2秒后重试
            
            return (None, 0)

        # 并行询问3次
        results = []
        durations = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = {executor.submit(_single_query_task, diff_code): i for i in range(3)}
            
            for future in concurrent.futures.as_completed(futures):
                res_content, res_duration = future.result()
                if res_content:
                    results.append(res_content)
                if res_duration > 0:
                    durations.append(res_duration)
        
        end_time = time.time()
        # duration = end_time - start_time
        if durations:
            duration = sum(durations) / len(durations)
        else:
            duration = end_time - start_time
        
        # 投票决策
        votes = []
        valid_results = []
        
        for res_content in results:
            parsed = parse_llm_json(res_content)
            if parsed and 'significant' in parsed:
                votes.append(parsed['significant'])
                valid_results.append(parsed)
                
        final_result_json = None
        log_content = None
        
        if valid_results:
            # 统计票数
            true_votes = votes.count(True)
            false_votes = votes.count(False)
            
            # 只要True票数过半就算显著修改
            is_significant = true_votes > false_votes
            
            # 选取一个理由
            selected_reason = "No reason found"
            # 优先选择与投票结果一致的理由
            for r in valid_results:
                if r['significant'] == is_significant:
                    selected_reason = r.get('reason', '')
                    break
            
            if not selected_reason and valid_results:
                 selected_reason = valid_results[0].get('reason', '')

            final_result_json = {
                "significant": is_significant,
                "reason": f"[投票结果 True:{true_votes} False:{false_votes}] {selected_reason}"
            }
            log_content = final_result_json
        else:
            # 如果全部失败或者无法解析
            if results:
                # 有返回但解析失败，记录原始第一个返回
                log_content = results[0]
            else:
                # 连LLM调用都失败了
                log_content = "All queries failed"
                
        if stats_collector:
            stats_collector.add_query(duration, bool(final_result_json), function_name, binary_pair, log_content)
            
        return final_result_json if final_result_json else log_content

    except Exception as e:
        print(f"调用LLM流程时发生错误: {e}")
        end_time_err = time.time()
        if stats_collector:
            stats_collector.add_query(end_time_err - start_time, False, function_name, binary_pair, f"Error: {e}")
        return None
 
def classify_handler_functions(binaries, binary_extracts, diff_results, model_type="claude", stats_collector=None):
    """
    将多个固件版本的handler函数分类为公共函数、修改函数、独有函数和部分共享函数
    使用name_matches信息建立不同名称但相同函数的映射关系
    
    Args:
        binaries: 固件二进制名称列表
        binary_extracts: 每个固件的handler提取结果
        diff_results: 固件间的差异分析结果
        model_type: 使用的LLM模型类型
        stats_collector: 统计收集器
        
    Returns:
        分类结果字典
    """
    # 初始化结果结构
    classification = {
        "common_handlers": [],       # 所有固件共有且相同的handler
        "modified_handlers": {},     # 存在于多个固件但有修改的handler
        "analysis_results": {},      # [新增] 存储所有分析过的函数结果(包括未修改的)
        "unique_handlers": {},       # 在单个固件中独有的handler
        "partially_shared": [],       # 部分固件中共享且相同的handler
        "all_modified_functions": {} # 所有修改过的函数的完整信息（包含未修改版本的固件信息）
    }
    
    # 为每个固件初始化独有函数列表
    for binary in binaries:
        classification["unique_handlers"][binary] = []
    
    # 为每对固件初始化修改过的函数列表
    for binary1, binary2 in combinations(binaries, 2):
        key = f"{binary1}-{binary2}"
        classification["modified_handlers"][key] = []
    
    # 步骤1: 建立函数名映射关系，处理相同函数在不同固件中名称不同的情况
    func_name_mapping, canonical_groups = build_function_name_mapping(diff_results)
    
    # 步骤2: 收集每个固件中的所有handler函数(使用规范名称)
    all_handlers = {}
    canonical_to_original = {}  # 规范名称 -> {binary: 原始名称}
    
    for binary, extract_data in binary_extracts.items():
        handlers = extract_data.get("handler_functions", [])
        all_handlers[binary] = {}
        
        for handler in handlers:
            orig_name = handler["name"]
            # 获取规范名称，如果没有映射则使用原名
            canonical_name = func_name_mapping.get(orig_name, orig_name)
            
            all_handlers[binary][canonical_name] = handler
            
            # 记录规范名称到原始名称的映射
            if canonical_name not in canonical_to_original:
                canonical_to_original[canonical_name] = {}
            canonical_to_original[canonical_name][binary] = orig_name
    
    # 步骤3: 找出所有固件中的handler函数名集合(使用规范名称)
    handler_names_per_binary = {binary: set(handlers.keys()) for binary, handlers in all_handlers.items()}
    
    
    #common_handler_names = set.intersection(*handler_names_per_binary.values()) if handler_names_per_binary else set()
    
    # 步骤4: 创建函数状态字典，记录每个函数存在于哪些固件中以及是否被修改
    handler_status = {}
    
    # 收集所有handler名称(规范名称)
    all_handler_names = set()
    for handlers in handler_names_per_binary.values():
        all_handler_names.update(handlers)
    
    # 初始化每个handler的状态
    for name in all_handler_names:
        handler_status[name] = {
            "modified": False, 
            "binaries": [],  # 包含此函数的固件列表
            "modified_pairs": []  # 有修改的固件对列表
        }
    
    # 记录每个handler存在于哪些固件中
    for binary, handlers in all_handlers.items():
        for name in handlers:
            handler_status[name]["binaries"].append(binary)
    time_start=time.time()
    # 检查每对固件之间的函数修改情况
    for binary_pair, diff_data in diff_results.items():
        binary1, binary2 = binary_pair.split("-")
        # 检查修改的函数
        for func in diff_data.get("modified", []):
            old_name = func["old"]["name"]
            new_name = func["new"]["name"]
            diff_code= func.get("diff")
            clean_diff_code=extract_diff_changes(diff_code)
            # 获取规范名称
            canonical_old = func_name_mapping.get(old_name, old_name)
            canonical_new = func_name_mapping.get(new_name, new_name)
            
            # 使用规范名称检查是否为同一函数
            canonical_name = canonical_old if canonical_old == canonical_new else canonical_old
            
            # 如果修改的函数是handler
            if canonical_name in handler_status:
                print(f"  分析函数 {canonical_name} 在 {binary_pair} 之间的修改")
                time_tmp_start=time.time()
                result=LLM_diff(
                    clean_diff_code, 
                    model_type=model_type, 
                    stats_collector=stats_collector,
                    function_name=canonical_name,
                    binary_pair=binary_pair
                )
                # result='{"significant": true, "reason": "函数调用变化"}'
                time_tmp_end=time.time()
                print(f"    LLM分析结果: {result}\n    耗时: {time_tmp_end-time_tmp_start:.2f}秒")
                if result:
                    try:
                        is_significant = False
                        
                        # 检查result类型
                        if isinstance(result, dict):
                            # 如果是字典，获取significant字段
                            is_significant = result.get("significant", False)
                            # 如果值为字符串"true"，也应该视为True
                            if isinstance(is_significant, str) and is_significant.lower() == 'true':
                                is_significant = True
                        elif isinstance(result, str):
                            # 如果是字符串，降级到简单匹配
                            is_significant = 'true' in result.lower()

                        # 无论结果如何，都记录到analysis_results中
                        if binary_pair not in classification["analysis_results"]:
                            classification["analysis_results"][binary_pair] = []
                            
                        # 尝试获取原因
                        analysis_reason = "No reason provided"
                        if isinstance(result, dict):
                            analysis_reason = result.get("reason", "No reason provided")
                        elif isinstance(result, str):
                            analysis_reason = result # 如果是纯文本，直接用文本
                            
                        classification["analysis_results"][binary_pair].append({
                            "canonical_name": canonical_name,
                            "original_names": {
                                binary1: old_name,
                                binary2: new_name
                            },
                            "significant": is_significant,
                            "reason": analysis_reason
                        })

                        if is_significant:
                            # 标记为修改过
                            handler_status[canonical_name]["modified"] = True
                            handler_status[canonical_name]["modified_pairs"].append(binary_pair)
                            # 添加到这对固件的修改列表
                            classification["modified_handlers"][binary_pair].append({
                                "canonical_name": canonical_name,
                                "original_names": {
                                    binary1: old_name,
                                    binary2: new_name
                                },
                                "old": {"binary": binary1, "address": func["old"]["address"]},
                                "new": {"binary": binary2, "address": func["new"]["address"]},
                                "reason": analysis_reason
                            })
                    except Exception as e:
                        print(f"    无法解析LLM结果: {result} - 错误: {e}")
                else:
                    print(f"    LLM分析失败，无法判断函数 {canonical_name} 的修改情况")
    time_end=time.time()
    print(f"分析函数修改耗时: {time_end-time_start:.2f}秒")
    # 步骤5: 分类所有handler函数
    partially_shared_groups = {}  # 用于存储部分共享函数的组
    
    for canonical_name, info in handler_status.items():
        # 如果函数被标记为 modify，记录所有拥有该函数的固件信息
        if info["modified"]:
            classification["all_modified_functions"][canonical_name] = {}
            for binary in info["binaries"]:
                if canonical_name in all_handlers[binary]:
                    h_info = all_handlers[binary][canonical_name]
                    classification["all_modified_functions"][canonical_name][binary] = {
                        "name": h_info["name"], 
                        "address": h_info["address"]
                    }

        if len(info["binaries"]) == len(binaries):
            # 存在于所有固件中
            if info["modified"]:
                # 但有修改，已经在前面添加到modified_handlers
                pass
            else:
                # 在所有固件中都相同
                # 取第一个固件的handler信息作为代表
                reference_binary = binaries[0]
                handler_info = all_handlers[reference_binary][canonical_name]
                
                # 获取在各固件中的原始名称
                orig_names = {}
                for binary in binaries:
                    if binary in canonical_to_original.get(canonical_name, {}):
                        orig_names[binary] = canonical_to_original[canonical_name][binary]
                
                classification["common_handlers"].append({
                    "canonical_name": canonical_name,
                    "orig_name": handler_info["name"],
                    "address": handler_info["address"],
                    "reference_binary": reference_binary,
                    "names_in_binaries": orig_names
                })
        elif len(info["binaries"]) == 1:
            # 仅存在于一个固件中 - 独有函数
            binary = info["binaries"][0]
            handler_info = all_handlers[binary][canonical_name]
            classification["unique_handlers"][binary].append({
                "canonical_name": canonical_name,
                "orig_name": handler_info["name"],
                "address": handler_info["address"]
            })
        else:
            # 存在于部分固件中，但不是全部
            if not info["modified"]:
                # 未修改的部分共享函数 - 我们只需要在其中一个固件中测试
                # 为了一致性，我们选择在 binaries 参数中顺序靠前的固件作为代表
                binaries_with_func = sorted(info["binaries"], key=lambda x: binaries.index(x) if x in binaries else 9999)
                reference_binary = binaries_with_func[0]
                
                # 生成一个共享组的标识
                # group_key 仍然使用字母排序以保持唯一性，不影响 reference_binary 的选择
                group_key = "-".join(sorted(info["binaries"]))
                
                if group_key not in partially_shared_groups:
                    partially_shared_groups[group_key] = {
                        "binaries": info["binaries"],
                        "reference_binary": reference_binary,
                        "functions": []
                    }
                
                handler_info = all_handlers[reference_binary][canonical_name]
                
                # 获取在各固件中的原始名称
                orig_names = {}
                for binary in info["binaries"]:
                    if binary in canonical_to_original.get(canonical_name, {}):
                        orig_names[binary] = canonical_to_original[canonical_name][binary]
                
                partially_shared_groups[group_key]["functions"].append({
                    "canonical_name": canonical_name,
                    "orig_name": handler_info["name"],
                    "address": handler_info["address"],
                    "names_in_binaries": orig_names
                })
    
    # 整理部分共享函数的结果
    for group_key, group_info in partially_shared_groups.items():
        for func in group_info["functions"]:
            classification["partially_shared"].append({
                "canonical_name": func["canonical_name"],
                "orig_name": func["orig_name"],
                "address": func["address"],
                "reference_binary": group_info["reference_binary"],
                "shared_across": list(group_info["binaries"]),
                "names_in_binaries": func["names_in_binaries"]
            })
    
    # 输出分类统计信息和结果
    print_classification_results(classification, binaries)
    
    return classification

def analyze_modified_handlers(classification, binaries):
    """
    分析classification["modified_handlers"]，确定每个修改过的handler在哪几个二进制版本之间存在差异，
    并生成最优测试策略
    
    Args:
        classification: 分类结果字典
        binaries: 二进制文件列表
    
    Returns:
        handler_test_strategy: 每个handler的测试策略字典
    """
    # 初始化结果
    handler_test_strategy = {}
    
    # 创建规范名到二进制版本信息的映射
    canonical_to_versions = {}
    
    # 1A. 首先从 all_modified_functions 收集所有版本信息，确保覆盖所有包含该函数的二进制文件
    # 即使它们没有涉及到"修改对"中（例如某两个版本相同，而被判定未修改）
    if "all_modified_functions" in classification:
        for canonical_name, details in classification["all_modified_functions"].items():
            if canonical_name not in canonical_to_versions:
                canonical_to_versions[canonical_name] = {
                    "binary_versions": {},
                    "modified_pairs": []
                }
            
            for binary, h_info in details.items():
                canonical_to_versions[canonical_name]["binary_versions"][binary] = h_info

    # 1B. 收集并合并所有修改过的handler信息 (用于填充 modified_pairs)
    for binary_pair, handlers in classification["modified_handlers"].items():
        binary1, binary2 = binary_pair.split("-")
        
        for handler in handlers:
            canonical_name = handler["canonical_name"]
            
            # 初始化handler信息 (如果是通过all_modified_functions添加的，这就不是必需的，但作为保险)
            if canonical_name not in canonical_to_versions:
                canonical_to_versions[canonical_name] = {
                    "binary_versions": {},  # 记录每个binary版本的函数信息
                    "modified_pairs": []    # 记录修改的二进制对
                }
            
            # 记录修改对 (去重)
            if binary_pair not in canonical_to_versions[canonical_name]["modified_pairs"]:
                canonical_to_versions[canonical_name]["modified_pairs"].append(binary_pair)
            
            # 记录二进制版本信息 (如果步骤1A没覆盖到)
            if binary1 not in canonical_to_versions[canonical_name]["binary_versions"]:
                canonical_to_versions[canonical_name]["binary_versions"][binary1] = {
                    "name": handler["original_names"].get(binary1, canonical_name),
                    "address": handler["old"]["address"]
                }
            
            if binary2 not in canonical_to_versions[canonical_name]["binary_versions"]:
                canonical_to_versions[canonical_name]["binary_versions"][binary2] = {
                    "name": handler["original_names"].get(binary2, canonical_name),
                    "address": handler["new"]["address"]
                }
    
    # 2. 为每个handler分析版本关系图
    for canonical_name, info in canonical_to_versions.items():
        # 确定哪些二进制版本包含此函数
        versions_with_func = set(info["binary_versions"].keys())
        
        # 创建版本差异图 - 记录哪些版本对之间有差异
        diff_graph = {binary: set() for binary in versions_with_func}
        
        # 填充差异图
        for binary_pair in info["modified_pairs"]:
            binary1, binary2 = binary_pair.split("-")
            diff_graph[binary1].add(binary2)
            diff_graph[binary2].add(binary1)
        
        # 3. 根据差异图确定等价类
        version_groups = []
        remaining = set(versions_with_func)
        
        while remaining:
            current = next(iter(remaining))  # 取一个未处理的版本
            group = {current}  # 初始化一个新组
            remaining.remove(current)
            
            # 寻找与当前版本等价的其他版本
            for binary in list(remaining):
                # 如果两个版本之间没有差异记录，则它们是等价的
                if binary not in diff_graph[current]:
                    group.add(binary)
                    remaining.remove(binary)
            
            # 添加已找到的等价组
            # 按照binaries列表中的顺序排序组内元素
            sorted_group = sorted(list(group), key=lambda x: binaries.index(x) if x in binaries else 9999)
            version_groups.append(sorted_group)

        # 按照binaries列表中的顺序排序各个组
        version_groups.sort(key=lambda g: binaries.index(g[0]) if g and g[0] in binaries else 9999)
        
        # 4. 生成测试策略描述
        description = ""
        if len(version_groups) == 1:
            # 所有版本功能相同 
            description = f"所有版本 ({','.join(version_groups[0])}) 功能相同，只需测试一个版本"
        elif len(version_groups) == len(versions_with_func):
            # 所有版本都不同 
            sorted_versions = sorted(list(versions_with_func), key=lambda x: binaries.index(x) if x in binaries else 9999)
            description = f"所有版本 ({','.join(sorted_versions)}) 功能各不相同，需分别测试"
        else:
            # 部分版本相同 
            groups_desc = []
            for group in version_groups:
                if len(group) > 1:
                    groups_desc.append(f"[{','.join(group)}]")
                else:
                    groups_desc.append(f"[{group[0]}]")
            description = f"版本分组: {' '.join(groups_desc)}，每组测试一个版本即可"
        
        # 存储测试策略
        handler_test_strategy[canonical_name] = {
            "version_groups": version_groups,
            "modified_pairs": info["modified_pairs"],
            "binary_info": info["binary_versions"],
            "description": description
        }
    
    # 5. 打印汇总结果
    print("\n===== 修改函数的优化测试策略 =====")
    total_handlers = len(handler_test_strategy)
    print(f"共有 {total_handlers} 个修改过的handler函数")
    
    # 按测试组数量分类
    strategy_groups = {}
    for name, info in handler_test_strategy.items():
        group_count = len(info["version_groups"])
        if group_count not in strategy_groups:
            strategy_groups[group_count] = []
        strategy_groups[group_count].append(name)
    
    # 打印各类测试策略
    for group_count in sorted(strategy_groups.keys()):
        handlers = strategy_groups[group_count]
        print(f"\n需要测试 {group_count} 个版本的函数: {len(handlers)}")
        
        for handler in handlers:
            info = handler_test_strategy[handler]
            print(f"  - {handler}:")
            print(f"    {info['description']}")
            print(f"    修改对: {', '.join(info['modified_pairs'])}")
    
    # 计算优化效果
    naive_test_count = 0
    for name, info in handler_test_strategy.items():
        binary_count = len(info["binary_info"])
        naive_test_count += binary_count
    
    optimized_test_count = sum(len(info["version_groups"]) for info in handler_test_strategy.values())
    
    if naive_test_count > 0:
        optimization_percent = (naive_test_count - optimized_test_count) / naive_test_count * 100
        print(f"\n修改函数测试优化: 从 {naive_test_count} 降到 {optimized_test_count} 测试项，节省 {optimization_percent:.1f}%")
    
    return handler_test_strategy
def compare_model_results(all_results, diff_results, output_file):
    """
    比较不同模型的分析结果并生成汇总报告
    
    Args:
        all_results: 字典 {model_name: classification_dict}
        diff_results: 原始的差异分析结果
        output_file: 输出报告的文件路径
    """
    if not all_results:
        return

    print(f"\n正在生成模型对比报告: {output_file}")
    
    comparison = {
        "summary": {
            "total_modified_candidates": 0,  
            "consensus_modified": 0,         
            "consensus_unmodified": 0,       
            "conflict": 0,
            "models": list(all_results.keys())
        },
        "details": []
    }
    
    # 收集所有的差异函数候选者 (pair, old_name)
    candidates = set()
    
    # 仅收集在 classification 结果中实际被分析过的函数 (即 handler 函数)
    # 只要在任意一个模型的结果中出现过，就视为候选者
    for model_name, classification in all_results.items():
        # 从 analysis_results 获取
        if "analysis_results" in classification:
            for binary_pair, results_list in classification["analysis_results"].items():
                binary1 = binary_pair.split("-")[0]
                for func_res in results_list:
                    # 使用 binary1 的原始名称作为标识
                    old_name = func_res["original_names"].get(binary1)
                    if old_name:
                        candidates.add((binary_pair, old_name))
        
        # 兼容旧逻辑: 从 modified_handlers 获取 (如果 analysis_results 为空)
        if "modified_handlers" in classification:
            for binary_pair, handlers in classification["modified_handlers"].items():
                binary1 = binary_pair.split("-")[0]
                for handler in handlers:
                    old_name = handler["original_names"].get(binary1)
                    if old_name:
                        candidates.add((binary_pair, old_name))
    
    # 将集合转为列表并排序，确保结果稳定
    sorted_candidates = sorted(list(candidates))
    comparison["summary"]["total_modified_candidates"] = len(sorted_candidates)
    
    detailed_entries = []
    
    for binary_pair, func_name in sorted_candidates:
        entry = {
            "binary_pair": binary_pair,
            "function_name": func_name,
            "models": {},
            "status": "unknown"
        }
        
        modified_count = 0
        total_models = len(all_results)
        binary1 = binary_pair.split("-")[0]
        
        for model_name, classification in all_results.items():
            is_modified = False
            reason = "Not analyzed"
            
            # 使用新的 analysis_results 来查找，因为无论 true/false 都在里面
            target_results = []
            
            # 尝试正向 key (binary1-binary2)
            if binary_pair in classification.get("analysis_results", {}):
                target_results = classification["analysis_results"][binary_pair]
            else:
                # 尝试反向 key
                parts = binary_pair.split("-")
                rev_key = f"{parts[1]}-{parts[0]}"
                if rev_key in classification.get("analysis_results", {}):
                     target_results = classification["analysis_results"][rev_key]
            
            # 在结果列表中查找对应函数
            found = False
            for res in target_results:
                if res["original_names"].get(binary1) == func_name:
                    is_modified = res["significant"]
                    reason = res.get("reason", "No reason provided")
                    found = True
                    break
            
            # 如果没在 analysis_results 找到 (兼容旧逻辑或未运行 LLM 的情况)
            if not found:
                # 回退到旧逻辑：在 modified_handlers 中查找
                if binary_pair in classification.get("modified_handlers", {}):
                     for handler in classification["modified_handlers"][binary_pair]:
                         if handler["original_names"].get(binary1) == func_name:
                             is_modified = True
                             reason = handler.get("reason", "Significant change")
                             break
            
            entry["models"][model_name] = {
                "significant": is_modified,
                "reason": reason
            }
            
            if is_modified:
                modified_count += 1
        
        if modified_count == total_models:
            entry["status"] = "CONSENSUS_MODIFIED"
            comparison["summary"]["consensus_modified"] += 1
        elif modified_count == 0:
            entry["status"] = "CONSENSUS_UNMODIFIED"
            comparison["summary"]["consensus_unmodified"] += 1
        else:
            entry["status"] = "CONFLICT"
            comparison["summary"]["conflict"] += 1
            
        detailed_entries.append(entry)
        
    comparison["details"] = detailed_entries
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(comparison, f, indent=2, ensure_ascii=False)
        print(f"对比报告已保存到: {output_file}")
        
        print("\n===== 模型对比摘要 =====")
        print(f"参与模型: {', '.join(comparison['summary']['models'])}")
        print(f"总候选差异函数: {comparison['summary']['total_modified_candidates']}")
        print(f"一致认为修改: {comparison['summary']['consensus_modified']}")
        print(f"一致认为未改: {comparison['summary']['consensus_unmodified']}")
        print(f"存在分歧: {comparison['summary']['conflict']}")
        
    except Exception as e:
        print(f"保存对比报告失败: {e}")

def organize_test_plan_by_binary(test_plan, output_file):
    """
    将测试计划按二进制文件分组并保存为指定JSON格式
    
    Args:
        test_plan: 测试计划列表
        output_file: 输出文件路径
    """
    try:
        # 按二进制文件分组
        binary_grouped_plan = {}
        
        # 遍历测试项并按二进制文件分组
        for test in test_plan:
            binary = test.get("binary")
            
            # 如果二进制文件不在结果字典中，初始化它
            if binary not in binary_grouped_plan:
                binary_grouped_plan[binary] = []
            
            # 创建简化的测试项
            simplified_test = {
                "func_name": test.get("function_name"),
                "address": test.get("address"),
                "type": test.get("type"),
                "reason": test.get("reason")
            }
            
            # 将测试项添加到对应的二进制文件数组中
            binary_grouped_plan[binary].append(simplified_test)
        
        # 构建符合要求的JSON格式
        test_groups = []
        for binary, tests in binary_grouped_plan.items():
            test_groups.append({
                "binary": binary,
                "test_plan": tests
            })
        
        result = {
            "test_group": test_groups
        }
        
        # 保存为JSON文件
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
            
        # 输出统计信息
        print(f"\n===== 按二进制文件分组的测试计划 =====")
        print(f"总测试项: {len(test_plan)}")
        print(f"包含的二进制文件数量: {len(test_groups)}")
        
        for group in test_groups:
            print(f"  - {group['binary']}: {len(group['test_plan'])} 个测试项")
            
        print(f"分组后的测试计划已保存到 {output_file}")
        
        return result
    except Exception as e:
        print(f"组织测试计划时出错: {e}")
        return None
    
def save_analysis_report(classification, binaries, binary_extracts, handler_test_strategy, test_plan, output_file):
    """
    将分析日志保存为JSON报告文件
    
    Args:
        classification: 分类结果字典
        binaries: 二进制文件列表
        binary_extracts: 每个二进制文件的提取结果
        handler_test_strategy: 修改函数的测试策略
        test_plan: 测试计划列表
        output_file: 输出文件路径
    """
    report = {}
    
    # 1. 每个固件的原始handler数量
    report["binary_handler_counts"] = {}
    for binary in binaries:
        if binary in binary_extracts:
            report["binary_handler_counts"][binary] = len(binary_extracts[binary].get("handler_functions", []))
    
    # 2. 函数分类结果
    report["classification_summary"] = {
        "common_handlers": len(classification["common_handlers"]),
        "partially_shared": len(classification["partially_shared"]),
        "unique_handlers": {binary: len(handlers) for binary, handlers in classification["unique_handlers"].items()},
        "modified_handlers": {key: len(handlers) for key, handlers in classification["modified_handlers"].items()}
    }
    
    # 3. 分类详情
    report["classification_details"] = {
        "common_handlers": [
            {
                "canonical_name": h["canonical_name"],
                "reference_binary": h["reference_binary"],
                "address": h["address"],
                "names_in_binaries": h.get("names_in_binaries", {})
            } for h in classification["common_handlers"]
        ],
        "partially_shared": [
            {
                "canonical_name": h["canonical_name"],
                "reference_binary": h["reference_binary"],
                "address": h["address"],
                "shared_across": h["shared_across"],
                "names_in_binaries": h.get("names_in_binaries", {})
            } for h in classification["partially_shared"]
        ],
        "unique_handlers": {
            binary: [
                {
                    "canonical_name": h["canonical_name"],
                    "orig_name": h["orig_name"],
                    "address": h["address"]
                } for h in handlers
            ] for binary, handlers in classification["unique_handlers"].items()
        },
        "modified_handlers": {
            key: [
                {
                    "canonical_name": h["canonical_name"],
                    "original_names": h["original_names"],
                    "old": h["old"],
                    "new": h["new"],
                    "reason": h.get("reason", "")
                } for h in handlers
            ] for key, handlers in classification["modified_handlers"].items()
        }
    }
    
    # 4. LLM分析结果（包含被判定为不显著的）
    if "analysis_results" in classification:
        report["llm_analysis_results"] = classification["analysis_results"]
    
    # 5. 修改函数的优化测试策略
    report["modified_handler_strategy"] = {}
    for canonical_name, strategy in handler_test_strategy.items():
        report["modified_handler_strategy"][canonical_name] = {
            "version_groups": strategy["version_groups"],
            "modified_pairs": strategy["modified_pairs"],
            "binary_info": strategy["binary_info"],
            "description": strategy["description"]
        }
    
    # 6. 优化统计
    naive_test_count = sum(len(info["binary_info"]) for info in handler_test_strategy.values())
    optimized_test_count = sum(len(info["version_groups"]) for info in handler_test_strategy.values())
    
    total_tests = len(test_plan)
    total_all_handlers = sum(
        len(binary_extracts[b].get("handler_functions", [])) for b in binaries if b in binary_extracts
    )
    
    report["optimization_stats"] = {
        "modified_functions": {
            "total_modified_handlers": len(handler_test_strategy),
            "naive_test_count": naive_test_count,
            "optimized_test_count": optimized_test_count,
            "saved_percent": round((naive_test_count - optimized_test_count) / naive_test_count * 100, 1) if naive_test_count > 0 else 0
        },
        "overall": {
            "total_all_handlers": total_all_handlers,
            "total_tests": total_tests,
            "common_tests": len([t for t in test_plan if t["type"] == "common"]),
            "partially_shared_tests": len([t for t in test_plan if t["type"] == "partially_shared"]),
            "unique_tests": len([t for t in test_plan if t["type"] == "unique"]),
            "modified_tests": len([t for t in test_plan if t["type"] == "modified"]),
            "optimization_rate": round((total_all_handlers - total_tests) / total_all_handlers * 100, 2) if total_all_handlers > 0 else 0
        },
        "per_binary_tests": {}
    }
    
    # 按二进制文件统计测试项
    for test in test_plan:
        binary = test.get("binary")
        if binary not in report["optimization_stats"]["per_binary_tests"]:
            report["optimization_stats"]["per_binary_tests"][binary] = 0
        report["optimization_stats"]["per_binary_tests"][binary] += 1
    
    # 保存报告
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"分析报告已保存到: {output_file}")
    except Exception as e:
        print(f"保存分析报告失败: {e}")

def generate_test_plan(classification, binaries, binary_extracts, output_file=None):
    """
    根据分类结果生成测试计划
    
    Args:
        classification: 分类结果字典
        binaries: 二进制文件列表
        binary_extracts: 每个二进制文件的提取结果
        output_file: 输出文件路径（可选）
    """
    test_plan = []
    
    # 辅助函数：去重+验证
    # 1. 确保不重复添加同一个(binary, address)
    # 2. 确保添加的函数确实存在于binary_extracts中 (用户要求: "直接将不在extract里面有的去掉")
    added_keys = set()
    
    # 构建有效目标集合 {(binary, address)}
    valid_targets = set()
    for binary, data in binary_extracts.items():
        for func in data.get("handler_functions", []):
            valid_targets.add((binary, func.get("address")))
            
    def add_test(test_dict):
        key = (test_dict["binary"], test_dict["address"])
        
        # 检查是否存在于提取结果中
        if key not in valid_targets:
            # print(f"跳过: {test_dict['function_name']} 不在 {test_dict['binary']} 的提取结果中")
            return
            
        # 检查是否重复添加
        if key not in added_keys:
            test_plan.append(test_dict)
            added_keys.add(key)

    # 1. 公共函数测试计划 - 只在参考固件上测试一次
    for handler in classification["common_handlers"]:
        add_test({
            "function_name": handler["orig_name"],
            "canonical_name": handler["canonical_name"],
            "binary": handler["reference_binary"],
            "address": handler["address"],
            "type": "common",
            "reason": "存在于所有固件中且完全相同",
            "names_in_binaries": handler.get("names_in_binaries", {})
        })
    
    # 2. 部分共享函数测试计划 - 只在参考固件上测试一次
    for handler in classification["partially_shared"]:
        shared_list = ", ".join(handler["shared_across"])
        add_test({
            "function_name": handler["orig_name"],
            "canonical_name": handler["canonical_name"],
            "binary": handler["reference_binary"],
            "address": handler["address"],
            "type": "partially_shared",
            "reason": f"在部分固件中共享且完全相同: {shared_list}",
            "names_in_binaries": handler.get("names_in_binaries", {})
        })
    
    # 3. 独有函数测试计划
    for binary, handlers in classification["unique_handlers"].items():
        for handler in handlers:
            add_test({
                "function_name": handler["orig_name"],
                "canonical_name": handler["canonical_name"],
                "binary": binary,
                "address": handler["address"],
                "type": "unique",
                "reason": f"仅存在于 {binary} 中"
            })
    
    # 4. 修改函数测试计划 - 进行优化分析
    # 分析修改过的handler函数，确定最优测试策略
    handler_test_strategy = analyze_modified_handlers(classification, binaries)
    
    # 根据分析结果生成测试项
    for canonical_name, strategy in handler_test_strategy.items():
        # 为每个不同的版本组创建一个测试
        for version_group in strategy["version_groups"]:
            # 从每组中选择一个代表性版本进行测试
            representative_binary = version_group[0]
            
            # 获取该函数在此二进制文件中的详细信息
            binary_info = strategy["binary_info"].get(representative_binary)
            if not binary_info:
                continue
                
            add_test({
                "function_name": binary_info["name"],
                "canonical_name": canonical_name,
                "binary": representative_binary,
                "address": binary_info["address"],
                "type": "modified",
                "reason": f"修改的函数 - {strategy['description']}",
                "version_group": version_group,
                "modified_pairs": strategy["modified_pairs"]
            })
    
    # 如果指定了输出文件，保存测试计划
    organize_test_plan_by_binary(test_plan, output_file)
    
    # 打印测试计划统计信息
    total_tests = len(test_plan)
    common_tests = len([t for t in test_plan if t["type"] == "common"])
    partially_shared_tests = len([t for t in test_plan if t["type"] == "partially_shared"])
    unique_tests = len([t for t in test_plan if t["type"] == "unique"])
    modified_tests = len([t for t in test_plan if t["type"] == "modified"])
    
    print(f"\n===== 测试计划统计 =====")
    print(f"总测试数量: {total_tests}")
    print(f"公共函数测试: {common_tests}")
    print(f"部分共享函数测试: {partially_shared_tests}")
    print(f"独有函数测试: {unique_tests}")
    print(f"修改函数测试: {modified_tests}")
    
    # 计算测试优化效率
    # 计算总handler函数
    total_all_handlers = 0
    for binary, extract_data in binary_extracts.items():
        total_all_handlers += len(extract_data.get("handler_functions", []))
        
    # 计算优化比例
    if total_all_handlers > 0:
        optimization_ratio = (total_all_handlers - total_tests) / total_all_handlers * 100
        print(f"测试优化率: {optimization_ratio:.2f}% (从 {total_all_handlers} 减少到 {total_tests})")
    
    # 保存分析报告到output目录
    if output_file:
        if output_file.endswith('.json'):
            report_file = output_file[:-5] + '_analysis_report.json'
        else:
            report_file = output_file + '_analysis_report.json'
        save_analysis_report(classification, binaries, binary_extracts, handler_test_strategy, test_plan, report_file)
    
    return test_plan
# 读取JSON文件
def parse_functions_changes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # 获取meta信息中的Program Name
        old_program_name = data.get('old_meta', {}).get('Program Name', 'Unknown')
        new_program_name = data.get('new_meta', {}).get('Program Name', 'Unknown')
        
        # 获取functions元素
        functions = data.get('functions', {})
        
        # 获取added元素中的name和address (new独有的)
        added_functions = []
        for func in functions.get('added', []):
            added_functions.append({
                'name': func.get('name'),
                'address': func.get('address')
            })
        
        # 获取deleted元素中的name和address (old独有的)
        deleted_functions = []
        for func in functions.get('deleted', []):
            deleted_functions.append({
                'name': func.get('name'),
                'address': func.get('address')
            })
        
        # 获取modified中old和new的name和address以及diff内容 (只包含有差异的)
        modified_functions = []
        for func in functions.get('modified', []):
            # 只有当diff存在且不为空时才添加
            if func.get('diff'):
                modified_functions.append({
                    'old': {
                        'name': func.get('old', {}).get('name'),
                        'address': func.get('old', {}).get('address')
                    },
                    'new': {
                        'name': func.get('new', {}).get('name'),
                        'address': func.get('new', {}).get('address')
                    },
                    'diff': func.get('diff')
                })
        
        #获取比较的matches结果，分别是address和name匹配
        matches=data.get('matches', [])
        # address_matches=matches.get('address_matches', [])
        # name_matches=matches.get('name_matches', [])
        return {
            'old_program_name': old_program_name,
            'new_program_name': new_program_name,
            'added': added_functions,
            'deleted': deleted_functions,
            'modified': modified_functions,
            'matches':matches
        }
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"JSON格式错误: {file_path}")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

def extract_info(json_file):
    """
    从JSON文件中提取handler
    
    Args:
        json_file: JSON文件路径
    
    Returns:
        提取的信息字典
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # 提取程序路径
        program_path = data.get("program_path", "未找到程序路径")
        
        # 使用字典来跟踪已处理的调用者，避免重复
        processed_callers = {}
        
        callers = []
        for func in data.get("extract_functions", []):            
            # 提取调用者信息
            for caller in func.get("callers", []):
                caller_name = caller.get("name", "未命名调用者")
                caller_addr = caller.get("address", "无地址")
                
                # 使用地址作为唯一标识符来去重
                caller_key = f"{caller_name}_{caller_addr}"
                
                if caller_key not in processed_callers:
                    processed_callers[caller_key] = {
                        "name": caller_name,
                        "address": caller_addr
                    }
                    callers.append(processed_callers[caller_key])            
        
        # 提取需要排除的函数
        remove_functions = []
        for func in data.get("remove_functions", []):
            if isinstance(func, str):
                remove_functions.append(func)  # 简单的函数名
            elif isinstance(func, dict):
                func_name = func.get("name", "")
                if func_name:
                    remove_functions.append(func_name)
            
        return {
            "program_path": program_path,
            "handler_functions": callers,
            "remove_functions": remove_functions
        }
        
    except Exception as e:
        print(f"处理JSON文件时出错: {e}")
        return None

# 使用示例
if __name__ == "__main__":
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='分析二进制文件之间的差异')
    parser.add_argument('binaries', nargs='+', help='二进制程序名称列表，例如 AC6_httpd AC9_httpd AC12_httpd')
    parser.add_argument('--json_dir', required=True, help='包含JSON文件的目录')
    parser.add_argument('--output', help='输出测试计划的JSON文件路径')
    parser.add_argument('--model', default='all', help='使用的语言模型，默认为all (运行claude, gpt, deepseek)，也可以指定单个模型')
    # 解析命令行参数
    args = parser.parse_args()
    
    binaries = args.binaries
    json_dir = args.json_dir
    
    # determine models to run
    available_models = ['claude', 'gpt', 'deepseek']
    
    # 兼容旧参数 gpt4 -> gpt
    arg_model = args.model
    if arg_model == 'gpt4':
        arg_model = 'gpt'
        
    models_to_run = []
    if arg_model == 'all':
        models_to_run = available_models
    elif arg_model in available_models:
        models_to_run = [arg_model]
    elif ',' in arg_model:
        requested = arg_model.split(',')
        for m in requested:
            m = m.strip()
            if m == 'gpt4': m = 'gpt'
            if m in available_models:
                models_to_run.append(m)
    
    if not models_to_run:
        print(f"警告: 未知模型 '{args.model}'，将使用默认模型列表: {available_models}")
        models_to_run = available_models
        
    # 验证目录是否存在
    if not os.path.isdir(json_dir):
        print(f"错误: 目录 '{json_dir}' 不存在")
        sys.exit(1)
    
    # 确定输出目录
    if args.output:
        output_dir = os.path.dirname(args.output)
        if not output_dir:
            output_dir = "output"
    else:
        output_dir = "output"
        
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
            print(f"创建输出目录: {output_dir}")
        except Exception as e:
            print(f"创建目录失败: {e}")
            output_dir = "." # fallback to current directory
            
    print(f"将分析以下二进制文件: {', '.join(binaries)}")
    print(f"使用JSON目录: {json_dir}")
    print(f"将使用以下模型进行分析: {', '.join(models_to_run)}")
    
    print(f"loading extract results....")
    binary_extracts = {}
    for binary in binaries:
        extract_path= os.path.join(json_dir, f"extract_{binary}_results.json")
        if os.path.exists(extract_path):
            print(f"loading extract results from {extract_path}")
            extract_data=extract_info(extract_path)
            if extract_data:
                binary_extracts[binary] = extract_data
                print(f"successfully loaded extract results for {binary}")
                print(f"提取的函数: {len(extract_data['handler_functions'])}")
            else:
                print(f"failed to load extract results for {binary}")
        else:
            print(f"警告: 提取结果文件 '{extract_path}' 不存在")
            
    print(f"loading diff info....")
    # 预加载所有可能的diff文件
    diff_results = {}
    for binary1, binary2 in combinations(binaries, 2):
        # 尝试查找两种可能顺序的ghidriff文件
        ghidriff_filename1 = f"{binary1}-{binary2}.ghidriff.json"
        ghidriff_path1 = os.path.join(json_dir, ghidriff_filename1)
        
        ghidriff_filename2 = f"{binary2}-{binary1}.ghidriff.json"
        ghidriff_path2 = os.path.join(json_dir, ghidriff_filename2)
        
        # 确定使用哪一个文件路径并加载
        if os.path.exists(ghidriff_path1):
            print(f"加载差异文件: {ghidriff_path1}")
            diff_data = parse_functions_changes(ghidriff_path1)
            if diff_data:
                diff_results[f"{binary1}-{binary2}"] = diff_data
        elif os.path.exists(ghidriff_path2):
            print(f"加载差异文件: {ghidriff_path2}")
            diff_data = parse_functions_changes(ghidriff_path2)
            if diff_data:
                # 注意：我们仍然以请求的顺序存储键
                diff_results[f"{binary1}-{binary2}"] = diff_data
        else:
            print(f"警告: 未找到 {binary1} 和 {binary2} 之间的差异文件")

    print(f"成功加载了 {len(diff_results)} 个差异文件")
    
    all_model_classifications = {}
    
    for model_name in models_to_run:
        print(f"\n==========================================")
        print(f"正在使用模型进行分析: {model_name}")
        print(f"==========================================")
        
        # 初始化统计收集器
        stats_collector = StatsCollector(model_name)
        
        # 运行分类分析
        classification = classify_handler_functions(
            binaries, 
            binary_extracts, 
            diff_results, 
            model_type=model_name,
            stats_collector=stats_collector
        )
        
        all_model_classifications[model_name] = classification
        
        # 确定前缀
        log_prefix = None
        if args.output:
            # 从输出文件路径中提取文件名作为前缀
            filename = os.path.basename(args.output)
            if filename.endswith('.json'):
                log_prefix = filename[:-5]
            else:
                log_prefix = filename
        
        # 保存统计日志
        stats_collector.save_log(output_dir, prefix=log_prefix)
        
        # 生成测试计划文件名
        if args.output:
            if args.output.endswith('.json'):
                base_name = args.output[:-5]
                output_file = f"{base_name}_{model_name}.json"
            else:
                output_file = f"{args.output}_{model_name}.json"
        else:
            output_file = os.path.join(output_dir, f"test_plan_{model_name}.json")
            
        print(f"生成测试计划: {output_file}")
        generate_test_plan(classification, binaries, binary_extracts, output_file)
        
    # 如果运行了多个模型，生成对比报告
    if len(all_model_classifications) > 1:
        # 确定对比报告文件名
        comparison_file = None
        if args.output:
            if args.output.endswith('.json'):
                base_name = args.output[:-5]
                comparison_file = f"{base_name}_comparison.json"
            else:
                comparison_file = f"{args.output}_comparison.json"
        
        if not comparison_file:
            comparison_file = os.path.join(output_dir, "model_comparison.json")
            
        compare_model_results(all_model_classifications, diff_results, comparison_file)
        
    print("\n所有模型分析完成！")