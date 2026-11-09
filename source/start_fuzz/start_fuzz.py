#!/usr/bin/env python3
# filepath: /root/FHFuzz/fuzz/start_fuzz.py

import os
import json
import argparse
import subprocess
import time
import signal
import threading
import psutil
import queue
from pathlib import Path

class AFLMonitor:
    """监视所有 AFL++ 模糊测试实例的状态，并管理目标函数队列"""
    def __init__(self, target_queue, firmware_root, binary_name, 
                 interval=300, timeout=None, inactive_timeout=300,
                 parallel_count=1, report_path=None,handler_folder=None,max_cycle=20):
        self.target_queue = target_queue  # 目标函数队列
        self.firmware_root = firmware_root
        self.binary_name = binary_name
        self.interval = interval  # 检查间隔（秒）
        self.timeout = timeout    # 总超时时间（秒）或 None 表示无限
        self.inactive_timeout = inactive_timeout  # 无新发现的超时时间（秒，默认30分钟）
        self.parallel_count = parallel_count  # 并行运行的模糊器数量
        self.report_path = report_path  # 报告输出路径
        
        self.running = True
        self.output_dirs = []  # 活跃的输出目录列表
        self.handler_folder =handler_folder
        self.report_path = report_path  # 报告输出路径
        
        self.max_cycle = max_cycle
        
        self.running = True
        self.output_dirs = []  # 活跃的AFL输出目录列表
        self.processes = {}    # 使用字典存储进程，键为AFL输出目录
        self.instance_start_time = {}  # 存储每个实例最后发现的时间
        self.start_time = time.time()
        self.active_targets = {}  # 当前活跃的目标函数 {output_dir: target_func}
        self.instance_status = {}  # {output_dir: {last_edges_found: 0}} 存储上次检查的边缘覆盖
        
        self.total_targets = self.target_queue.qsize()
        self.completed_targets = 0
        self.completed_results = {}  # 存储已完成目标的结果 {target_func: {stats}
        
        self.skipped_targets = {
        'no_seeds': set(),  # 没有种子文件的目标
        'no_binary': set()  # 没有二进制文件的目标
    }
        
        
    def add_process(self, process, output_dir, target_func):
        """添加要监控的进程，以AFL输出文件夹来区分进程"""
        self.processes[output_dir] = process
        self.instance_start_time[output_dir] = time.time()  # 初始化进程启动时间
        self.output_dirs.append(output_dir)
        self.active_targets[output_dir] = target_func
        self.instance_status[output_dir] = {
        'last_edges_found': 0,
        'last_check_time': time.time()
    }
        
    def kill_process(self, output_dir):
        """终止特定的AFL进程"""
        proc = self.processes.get(output_dir)
        if not proc:
            target = self.active_targets.get(output_dir, "unknown")
            print(f"进程引用不存在: {target}")
            return True
            
        # 检查进程是否已经结束
        if proc.poll() is not None:
            target = self.active_targets.get(output_dir, "unknown")
            print(f"进程已经自行结束: {target} (返回码: {proc.poll()})")
            return True
            
        # 进程仍在运行，尝试终止它
        try:
            parent = psutil.Process(proc.pid)
            for child in parent.children(recursive=True):
                try:
                    child.kill()
                except:
                    pass
            try:
                parent.kill()
            except:
                pass
            target = self.active_targets.get(output_dir, "unknown")
            print(f"已终止模糊测试: {target}")
            return True
        except psutil.NoSuchProcess:
            target = self.active_targets.get(output_dir, "unknown")
            print(f"进程已经不存在: {target}")
            return True
        except Exception as e:
            print(f"终止进程失败: {e}")
        return False
    
    def kill_all_processes(self):
        """终止所有 AFL 进程"""
        for output_dir in list(self.processes.keys()):
            self.kill_process(output_dir)
    
    def generate_final_report(self):
        """生成最终的模糊测试报告"""
        if not self.report_path:
            return
            
        try:
            total_run_time = int(time.time() - self.start_time)
            total_crashes = sum(result.get('saved_crashes', 0) for result in self.completed_results.values())
            
            with open(self.report_path, 'w') as f:
                # 写入报告标题和概述
                f.write(f"# AFL++ 批量模糊测试报告\n\n")
                f.write(f"生成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"总运行时间: {total_run_time//3600}小时 {(total_run_time%3600)//60}分钟 {total_run_time%60}秒\n")
                total_fuzzing_time = sum(result.get('run_time', 0) for result in self.completed_results.values())
                f.write(f"累计模糊测试时间(线程累计): {total_fuzzing_time//3600}小时 {(total_fuzzing_time%3600)//60}分钟 {total_fuzzing_time%60}秒\n")
                f.write(f"测试目标总数: {self.total_targets}\n")
                f.write(f"已完成目标: {self.completed_targets}\n")
                f.write(f"发现的崩溃总数: {total_crashes}\n\n")
                
                # 写入目标函数结果表格
                f.write("## 目标函数测试结果\n\n")
                f.write("| 目标函数 | 运行时间 | 执行/秒 | 周期数 | 覆盖率 | 路径 | 崩溃 | 挂起 | 状态 |\n")
                f.write("|---------|---------|---------|-------|-------|------|------|------|------|\n")
                
                for func, result in sorted(self.completed_results.items()):
                    run_time = result.get('run_time', 0)
                    run_time_str = f"{run_time//3600}:{(run_time%3600)//60:02d}:{run_time%60:02d}"
                    
                    f.write(f"| {func} | {run_time_str} | {result.get('execs_per_sec', 0):.1f} | ")
                    f.write(f"{result.get('cycles_done', 0)} | {result.get('bitmap_cvg', '0%')} | ")
                    f.write(f"{result.get('paths_total', 0)} | {result.get('saved_crashes', 0)} | ")
                    f.write(f"{result.get('saved_hangs', 0)} | {result.get('status', 'Unknown')} |\n")
                
                # 添加跳过目标的信息
                f.write("\n## 跳过的目标函数\n\n")
                
                # 缺少种子文件的目标
                if self.skipped_targets['no_seeds']:
                    f.write("### 缺少种子文件的目标函数\n\n")
                    f.write("以下函数因为缺少种子文件而被跳过:\n\n```\n")
                    for func in sorted(self.skipped_targets['no_seeds']):
                        f.write(f"- {func}\n")
                    f.write("```\n\n")
                
                # 缺少二进制文件的目标
                if self.skipped_targets['no_binary']:
                    f.write("### 缺少二进制文件的目标函数\n\n")
                    f.write("以下函数因为缺少目标二进制文件而被跳过:\n\n```\n")
                    for func in sorted(self.skipped_targets['no_binary']):
                        f.write(f"- {func}\n")
                    f.write("```\n\n")
                
                # 如果没有跳过的目标
                if not self.skipped_targets['no_seeds'] and not self.skipped_targets['no_binary']:
                    f.write("没有目标函数被跳过。\n\n")
                
                # 崩溃摘要
                f.write("\n## 崩溃摘要\n\n")
                has_crashes = False
                
                for func, result in sorted(self.completed_results.items()):
                    if result.get('saved_crashes', 0) > 0:
                        has_crashes = True
                        crashes_dir = os.path.join(self.firmware_root, self.handler_folder, func, "output", "default", "crashes")
                        crashes_count = 0
                        crash_files = []
                        
                        if os.path.exists(crashes_dir):
                            crash_files = [f for f in os.listdir(crashes_dir) if f.startswith('id:')]
                            crashes_count = len(crash_files)
                        
                        f.write(f"### {func}: {crashes_count} 崩溃\n\n")
                        f.write(f"崩溃文件路径: {crashes_dir}\n\n")
                        
                        # 列出前5个崩溃文件
                        if crash_files:
                            f.write("崩溃文件示例:\n```\n")
                            for crash_file in sorted(crash_files)[:5]:
                                f.write(f"- {crash_file}\n")
                            if len(crash_files) > 5:
                                f.write(f"... 以及 {len(crash_files) - 5} 个其他崩溃文件\n")
                            f.write("```\n\n")
                
                if not has_crashes:
                    f.write("没有发现崩溃。\n")
                
            print(f"已生成模糊测试报告: {self.report_path}")
        except Exception as e:
            print(f"生成报告时出错: {str(e)}")
        
    def check_status(self):
        """检查所有 AFL 实例的状态，并展示详细指标"""
        all_crashes = 0
        instances_info = []
        inactive_dirs = []
        current_time = time.time()
        
        # 准备表格标题
        print("\n" + "="*120)
        print(f"AFL Status Report - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Progress: {self.completed_targets}/{self.total_targets} targets completed | {len(self.output_dirs)} active")
        print("="*120)
        
        # 打印表头
        header = f"{'Target Function':<20} {'Run Time':<10} {'Exec/sec':<10} {'Cycles':<8} {'Coverage':<12} {'Edges':<8} {'Crashes':<6} {'Hangs':<6} {'Status':<20}"
        print(header)
        print("-"*120)
        
        for output_dir in list(self.output_dirs):
            target_func = self.active_targets.get(output_dir, "unknown")
            
            process_start_time = self.instance_start_time.get(output_dir, current_time)
            process_run_time = current_time - process_start_time
            stats_file = os.path.join(output_dir, 'default','fuzzer_stats')
            if not os.path.exists(stats_file):
                if process_run_time<self.interval:
                    row = f"{target_func:<20} {'00:00:00':<10} {0:<10.1f} {0:<8} {'0.00%':<12} {0:<8} {0:<6} {0:<6} "
                    row += f"\033[93mStarting ({process_run_time:.1f}s)...\033[0m"  # 黄色显示启动中状态
                    print(row)
                    continue
                
                print(f"Warning: stats file not found for {target_func}, terminating fuzzer...")
                # 将该实例添加到需要终止的列表
                inactive_dirs.append(output_dir)
                
                # 保存结果数据用于报告
                result = {
                    'run_time': 0,
                    'execs_per_sec': 0,
                    'cycles_done': 0,
                    'bitmap_cvg': '0.00%',
                    'edges_found': 0,
                    'saved_crashes': 0,
                    'saved_hangs': 0,
                    'status': 'afl start failed',
                    'end_time': time.time()
                }
                self.completed_results[target_func] = result
                
                # 显示表格行
                row = f"{target_func:<20} {'00:00:00':<10} {0:<10.1f} {0:<8} {'0.00%':<12} {0:<8} {0:<6} {0:<6} "
                row += f"\033[91mTerminating: stats file not found\033[0m"  # 红色显示错误信息
                print(row)
                continue
                
            with open(stats_file, 'r') as f:
                stats = {}
                for line in f:
                    if ':' in line:
                        key, value = line.strip().split(':', 1)
                        stats[key.strip()] = value.strip()
            
            # 获取各项指标
            run_time = int(stats.get('run_time', 0))
            run_time_str = f"{run_time//3600:02d}:{(run_time%3600)//60:02d}:{run_time%60:02d}"
            
            execs_per_sec = float(stats.get('execs_per_sec', 0))
            cycles_done = int(stats.get('cycles_done', 0))
            edges_found = int(stats.get('edges_found', 0))
            bitmap_cvg = stats.get('bitmap_cvg', '0.00%')
            
            saved_crashes = int(stats.get('saved_crashes', 0))
            saved_hangs = int(stats.get('saved_hangs', 0))
            
            
            all_crashes += saved_crashes
            
            target_func = self.active_targets.get(output_dir, "unknown")
            
            
            # 检查是否应该停止这个实例
            should_stop = False
            status = "Active"
            edge_time_str = "N/A"
        
            if output_dir in self.instance_status:
                status_info = self.instance_status[output_dir]
                last_edges = status_info.get('last_edges_found', 0)
                last_update_time = status_info.get('last_check_time', current_time)
                
                # 检查边缘覆盖是否有变化
                if edges_found > last_edges:
                    # 边缘数量有增长，更新时间戳
                    status_info['last_check_time'] = current_time
                    status_info['last_edges_found'] = edges_found
                    edge_time_str = "updated"
                else:
                    # 计算边缘无增长的时间（分钟）
                    edge_stagnation_time = (current_time - last_update_time)
                    edge_time_str = f"{edge_stagnation_time:.1f}"
                    
                    # 如果超过5分钟无新边缘发现，终止该实例
                    if edge_stagnation_time >= self.inactive_timeout:
                        should_stop = True
                        status = f"Edges stagnant for {edge_time_str}"
                
                # 暂时禁用达到最大 cycle 次数后自动结束的判断
                # if cycles_done > self.max_cycle:
                #     should_stop = True
                #     status = f"Reached {cycles_done} cycles limit"
                
            # 格式化为表格行
            row = f"{target_func:<20} {run_time_str:<10} {execs_per_sec:<10.1f} {cycles_done:<8} {bitmap_cvg:<12} {edges_found:<8} {saved_crashes:<6} {saved_hangs:<6} "
            
            if should_stop:
                row += f"\033[91m{'Terminating: ' + status}\033[0m"  # 红色显示即将终止的实例
                inactive_dirs.append(output_dir)
                
                # 保存结果数据用于报告
                if target_func not in self.completed_results:
                    result = {
                        'run_time': run_time,
                        'execs_per_sec': execs_per_sec,
                        'cycles_done': cycles_done,
                        'bitmap_cvg': bitmap_cvg,
                        'edges_found': edges_found,
                        'saved_crashes': saved_crashes,
                        'saved_hangs': saved_hangs,
                        'status': status,
                        'end_time': time.time()
                    }
                    self.completed_results[target_func] = result
            else:
                row += f"\033[92m{status}\033[0m"  # 绿色显示活跃的实例
            
            print(row)
            instances_info.append((target_func, run_time, execs_per_sec, edges_found, saved_crashes, status))
        
        print("-"*120)
        print(f"Running: {len(self.output_dirs)}  |  Total crashes: {all_crashes}  |  Runtime: {int(current_time - self.start_time)//3600}h {(int(current_time - self.start_time)%3600)//60}m")
        print("="*120 + "\n")
        
        # 终止不活跃的模糊器
        new_slots = 0
        for output_dir in inactive_dirs:
            target_func = self.active_targets.get(output_dir, "unknown")
            print(f"Terminating fuzzer for: {target_func}")
            if self.kill_process(output_dir):
                self.output_dirs.remove(output_dir)
                self.completed_targets += 1
                if output_dir in self.processes:
                    del self.processes[output_dir]
                if output_dir in self.instance_start_time:
                    del self.instance_start_time[output_dir]
                if output_dir in self.active_targets:
                    del self.active_targets[output_dir]
                if output_dir in self.instance_status:
                    del self.instance_status[output_dir]
                new_slots += 1
        
        # 启动新的模糊测试以填补空闲位置
        if new_slots > 0:
            self.start_new_fuzzers(new_slots)
        
        # 检查是否应该停止全部
        if self.timeout and (current_time - self.start_time) > self.timeout:
            print("Total timeout reached, stopping all fuzzers...")
            self.running = False
            return True
        
        # 如果所有模糊器都被终止且没有更多目标，则停止监视器
        if not self.output_dirs and self.target_queue.empty():
            print("All fuzzing instances completed and no more targets in queue")
            self.running = False
            
            # 生成最终报告
            if self.report_path:
                self.generate_final_report()
                
            return True
            
        return False
    
    def start_fuzzing(self, target_func, fuzzer_index=0):
        """
        启动单个AFL++实例
        
        Args:
            target_func: 目标函数名称
            fuzzer_index: 当前模糊器索引
        """
        # 创建输出目录
        output_dir = os.path.join(self.firmware_root, self.handler_folder, target_func, "output")
        
        # 清理输出目录下的default文件夹，确保开始新的测试
        default_dir = os.path.join(output_dir, 'default')
        if os.path.exists(default_dir):
            import shutil
            print(f"清理目标目录: {default_dir}")
            try:
                shutil.rmtree(default_dir)
            except Exception as e:
                print(f"清理目录失败: {e}")
        
        # 设置环境变量
        env, input_dir = setup_environment(self.firmware_root, target_func, self.handler_folder,output_dir)
        
        # 如果setup_environment返回None，说明没有种子文件，跳过该目标
        if env is None or input_dir is None:
            self.skipped_targets['no_seeds'].add(target_func)
            return None, None
        
        # 目标二进制
        binary = os.path.join(self.firmware_root, self.handler_folder, target_func, self.binary_name)
        if not os.path.exists(binary):
            print(f"错误: 未找到目标二进制 {binary}")
            self.skipped_targets['no_binary'].add(target_func)
            return None, None
        
        # 构建AFL命令
        cmd = [
        # 先执行 ulimit -c 0 关闭 core 文件生成，然后启动 AFL
        "bash", "-c", 
        "ulimit -c 0 && exec /root/AFLplusplus/afl-fuzz "
        f'-i "{input_dir}" '
        f'-o "{output_dir}" '
        "-m none -Q -- "
        f'"{binary}" @@'
    ]
        
        
        print(f"启动模糊测试 针对函数: {target_func}")
        print(f"命令: {' '.join(cmd)}")
        
        # 创建日志文件
        log_file = open(os.path.join(output_dir, f"afl-{fuzzer_index}.log"), "w")
        
        # 启动进程
        process = subprocess.Popen(
            cmd,
            env=env,
            stdout=log_file,
            stderr=log_file,
            start_new_session=True  # 创建新会话，使进程组能够独立终止
        )
        
        return process, output_dir
    
    def start_new_fuzzers(self, count=None):
        """启动新的模糊器填补空闲位置"""
        if count is None:
            # 确定需要启动的模糊器数量
            count = self.parallel_count - len(self.output_dirs)
        
        if count <= 0 or self.target_queue.empty():
            return
        
        print(f"Starting {count} new fuzzing instances...")
        
        # 跟踪实际成功启动的实例数量
        successful_starts = 0
        
        # 继续尝试启动实例，直到成功启动count个或队列为空
        while successful_starts < count and not self.target_queue.empty():
            try:
                target_func = self.target_queue.get_nowait()
                process, output_dir = self.start_fuzzing(
                    target_func,
                    successful_starts,  # 使用成功启动的索引作为fuzzer_index
                )
                
                if process and output_dir:
                    self.add_process(process, output_dir, target_func)
                    print(f"Started fuzzer for: {target_func} - PID: {process.pid}")
                    successful_starts += 1  # 只有在成功启动时才增加计数
                else:
                    # 如果启动失败，标记为已完成并继续
                    self.completed_targets += 1
                    print(f"Failed to start fuzzer for: {target_func}")
                    # 注意：这里不增加successful_starts，允许尝试下一个目标
            except queue.Empty:
                break
            
            # 稍作延时，避免实例同时启动引起资源争用
            time.sleep(1)
        
        print(f"Successfully started {successful_starts} new fuzzing instances")
            
    def monitor(self):
        """监视器主循环"""
        try:
            # 先启动初始批次的模糊器
            self.start_new_fuzzers(self.parallel_count)
            while self.running:
                should_stop = self.check_status()
                if should_stop:
                    self.kill_all_processes()
                    # 确保在所有进程终止后生成报告
                    if self.report_path:
                        self.generate_final_report()
                    break
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("用户中断，正在停止所有模糊测试...")
            self.kill_all_processes()
            self.running = False
            # 即使在中断情况下也生成报告
            if self.report_path:
                self.generate_final_report()

def extract_callers(json_path):
    """从JSON文件提取所有调用者函数并去重"""
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    callers = set()
    for func in data.get("extract_functions", []):
        for caller in func.get("callers", []):
            if "name" in caller:
                callers.add(caller["name"])
    
    return sorted(list(callers))

def extract_test_plan(json_path,target):
    """从测试计划JSON文件中提取目标函数列表"""
    if not os.path.exists(json_path):
        print(f"错误: 测试计划文件 {json_path} 不存在")
        return []
    
    with open(json_path, 'r') as f:
        data = json.load(f)
    for group in data["test_group"]:
        if group["binary"] == target:
            return [item["func_name"] for item in group["test_plan"]]
    return []

def setup_environment(firmware_root, target_func, handler_folder,output_dir):
    """设置AFL++环境变量，如果没有种子则返回None"""
    env = os.environ.copy()
    
    # 基本环境变量
    env["QEMU_LD_PREFIX"] = firmware_root
    env["QEMU_SET_ENV"] = f"LD_PRELOAD=/lib/libdl.so.0:/lib/{target_func}_hooks.so"
    
    # 设置目标配置
    taint_config = os.path.join(firmware_root, handler_folder, target_func, "config", "taint.txt")
    env["AFL_TAINT_CONFIG_FILE"] = taint_config
    
    # 设置变异器
    env["AFL_CUSTOM_MUTATOR_LIBRARY"] = "/root/AFLplusplus/custom_mutators/key_value_mutator/key_value_mutator.so"
    env["AFL_DISABLE_TRIM"] = "1"
    env["AFL_CUSTOM_MUTATOR_ONLY"] = "1"
    
    # 检查并创建输入输出目录
    input_dir = os.path.join(firmware_root, handler_folder, target_func, "input")
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    
    # 检查种子文件，如果不存在则跳过该目标
    seed_files = list(Path(input_dir).glob("*"))
    if len(seed_files) == 0:
        print(f"目标 {target_func} 无输入种子，跳过该目标的模糊测试")
        return None, None
    
    return env, input_dir

def main():
    parser = argparse.ArgumentParser(description="批量启动AFL++模糊测试")
    parser.add_argument("json_path", help="提取结果的JSON文件路径")
    parser.add_argument("firmware_root", help="固件根目录")
    parser.add_argument("--test_plan", default=None, help="测试计划JSON文件路径 (例如: test_plan.json)")
    parser.add_argument("--test_target", default=None, help="测试目标函数")
    parser.add_argument("--handler_folder", default="result_test", help="目标函数污点信息和输入文件名 (默认: result_test)")
    parser.add_argument("--binary", default="httpd", help="目标二进制文件名称 (默认: httpd)")
    parser.add_argument("--parallel", type=int, default=10, help="并行运行的模糊器数量 (默认: 10)")
    parser.add_argument("--max_targets", type=int, default=None, help="最多测试多少个目标函数 (默认: 全部)")
    parser.add_argument("--filter", help="按函数名称过滤目标 (可使用逗号分隔多个)")
    parser.add_argument("--timeout", type=int, default=24*3600, help="总运行时间限制(秒) (默认: 24小时)")
    parser.add_argument("--interval", type=int, default=300, help="状态检查间隔(秒) (默认: 5分钟)")
    parser.add_argument("--inactive", type=int, default=300, help="无新发现超时时间(秒) (默认: 5分钟)")
    parser.add_argument("--report", help="模糊测试结果报告输出文件路径")
    
    args = parser.parse_args()
    
    # 提取目标函数列表
    all_callers = extract_callers(args.json_path)
    print(f"从 {args.json_path} 文件中提取到 {len(all_callers)} 个目标函数")
    
    #如果存在测试计划文件且指定了目标函数，则从测试计划中提取目标函数
    if args.test_plan and args.test_target:
        print(f"使用测试计划文件: {args.test_plan},target: {args.test_target}")
        all_callers = extract_test_plan(args.test_plan, args.test_target)
        if not all_callers:
            print(f"未在测试计划中找到目标函数 {args.test_target}，退出程序")
            return
    
    # 过滤目标函数
    target_funcs = all_callers
    if args.filter:
        filter_funcs = [f.strip() for f in args.filter.split(",")]
        target_funcs = [f for f in all_callers if f in filter_funcs]
        print(f"根据过滤条件选择了 {len(target_funcs)} 个目标函数")
    
    # 限制目标函数数量
    if args.max_targets and args.max_targets < len(target_funcs):
        target_funcs = target_funcs[:args.max_targets]
        print(f"限制为 {len(target_funcs)} 个目标函数")
    
    # 创建目标函数队列
    target_queue = queue.Queue()
    for func in target_funcs:
        target_queue.put(func)
    
    print(f"创建目标队列，共 {target_queue.qsize()} 个目标函数")
    print(f"将以 {args.parallel} 个并行实例运行模糊测试")
    
    # 创建并启动监视器
    monitor = AFLMonitor(
        target_queue=target_queue,
        firmware_root=args.firmware_root,
        binary_name=args.binary,
        interval=args.interval,
        timeout=args.timeout,
        inactive_timeout=args.inactive,
        parallel_count=args.parallel,
        handler_folder=args.handler_folder,
        report_path=args.report
    )
    
    # 启动监视线程
    monitor_thread = threading.Thread(target=monitor.monitor)
    monitor_thread.daemon = True
    monitor_thread.start()
    
    try:
        # 等待监视器线程结束
        monitor_thread.join()
    except KeyboardInterrupt:
        print("接收到中断信号，正在停止所有模糊测试...")
        monitor.running = False
        monitor.kill_all_processes()
        
        # 即使被中断，也生成报告
        if args.report:
            monitor.generate_final_report()
            
    print("所有模糊测试实例已结束")

if __name__ == "__main__":
    main()
