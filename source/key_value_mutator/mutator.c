#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "custom_mutator_helpers.h"

#define MAX_TAINT_KEYS 64
#define MAX_KEY_LEN 256
#define MAX_LINE_LEN 2048
#define CONFIG_ENV_VAR "AFL_TAINT_CONFIG_FILE"

// 变异类型选择相关概率参数
#define PROB_HAVOC       50    // surgical_havoc_mutate 的概率
#define PROB_DELETE      10    // 删除操作的概率
#define PROB_INSERT      40    // 插入操作的概率

// 随机操作的长度范围
#define MIN_RANDOM_LEN   512
#define MAX_RANDOM_LEN   1024

#define MAX_EXTEND_LEN   2048

typedef struct {
    afl_t *afl;
    char *taint_keys[MAX_TAINT_KEYS];
    int taint_key_count;
    
    // 输入/输出缓冲区
    BUF_VAR(u8, fuzz);
    BUF_VAR(u8, data);
    
    // 分析用的临时缓冲区
    BUF_VAR(u8, tmp);
    
} my_mutator_t;

// 去除字符串首尾空白字符
static char *trim(char *str) {
  if (!str) return NULL;
  
  // 跳过开头的空白字符
  while (isspace((unsigned char)*str)) str++;
  
  if (*str == 0) return str;  // 全是空白字符
  
  // 从末尾往前移除空白字符
  char *end = str + strlen(str) - 1;
  while (end > str && isspace((unsigned char)*end)) end--;
  
  // 在末尾放置终止符
  *(end + 1) = '\0';
  
  return str;
}

// 从配置文件中读取污点键信息 - 每行一个键名
static void read_taint_config(my_mutator_t *data) {
    const char *config_path = getenv(CONFIG_ENV_VAR);
    if (!config_path) {
      fprintf(stderr, "警告: 未设置 %s 环境变量，默认所有键都可变异\n", CONFIG_ENV_VAR);
      return;
    }
    
    FILE *config_file = fopen(config_path, "r");
    if (!config_file) {
      fprintf(stderr, "错误: 无法打开配置文件 %s\n", config_path);
      return;
    }
    
    char line[MAX_LINE_LEN];
    while (fgets(line, sizeof(line), config_file) && data->taint_key_count < MAX_TAINT_KEYS) {
      // 去除行首尾空白字符
      char *key = trim(line);
      
      // 跳过空行和注释行(以#开头)
      if (*key == '\0' || *key == '#') continue;
      
      // 直接添加到污点列表
      if (*key) {
        data->taint_keys[data->taint_key_count] = strdup(key);
        data->taint_key_count++;
      }
    }
    
    fclose(config_file);
    
    if (data->taint_key_count > 0) {
      fprintf(stderr, "已从 %s 加载 %d 个污点键: ", config_path, data->taint_key_count);
      for (int i = 0; i < data->taint_key_count; i++) {
        fprintf(stderr, "%s%s", data->taint_keys[i], (i < data->taint_key_count - 1) ? ", " : "\n");
      }
    } else {
      fprintf(stderr, "警告: 在配置文件 %s 中未找到任何污点键\n", config_path);
    }
  }
// 检查键是否在污点列表中
static int is_tainted_key(const my_mutator_t *data, const char *key) {
  // 如果没有指定污点键，则所有键都视为可变异
  if (data->taint_key_count == 0) return 1;
  
  for (int i = 0; i < data->taint_key_count; i++) {
    if (strcmp(data->taint_keys[i], key) == 0) {
      return 1;
    }
  }
  
  return 0;
}

// 删除一段字节
static void delete_bytes(u8 *buf, s32 value_start, s32 value_end) {
    s32 value_len = value_end - value_start;//本行value的长度
    if (value_len <= 1) return;  // 至少保留一个字节
    
    // 确定删除的范围
    s32 del_start = value_start + RAND_BELOW(value_len);
    s32 del_len = 1 + RAND_BELOW(value_len - (del_start - value_start));
    
    // 确保至少保留一个字节
    if (del_len >= value_len) del_len = value_len - 1;
    
    // 删除操作
    s32 del_end = del_start + del_len;
    if(del_end>value_end) del_end=value_end;
    
    memmove(buf + del_start, buf + del_end, strlen((char*)buf) - del_end + 1);
    
  }

// 插入一段字节
static void insert_bytes(my_mutator_t *state, u8 *buf, s32 value_start, s32 value_end, size_t max_value_size, size_t max_total_size) {
  s32 value_len = value_end - value_start;
  
  // 确定插入位置
  s32 ins_pos = value_start + RAND_BELOW(value_len + 1);
  
  // 确定插入长度
  s32 ins_len = MIN_RANDOM_LEN + RAND_BELOW(MAX_RANDOM_LEN - MIN_RANDOM_LEN + 1);
  
  // 确保不超过当前value的最大长度限制(2048)
  size_t current_value_len = value_len;
  if (current_value_len + ins_len > max_value_size) {
    ins_len = max_value_size - current_value_len;
    if (ins_len <= 0) return;  // value已经达到最大长度
  }
  
  // 确保不超过总体最大长度
  size_t current_total_len = strlen((char*)buf);
  if (current_total_len + ins_len >= max_total_size) {
    ins_len = max_total_size - current_total_len - 1;
    if (ins_len <= 0) return;  // 没有空间插入
  }
  
  // 分配插入数据的缓冲区
  u8 *ins_data = malloc(ins_len);
  if (!ins_data) return;
  
  // 生成安全的随机数据 - 避免 \0 和 \n
  for (s32 i = 0; i < ins_len; i++) {
      // 生成1-255范围内的随机字符(避开0)
      u8 random_byte = 1 + RAND_BELOW(254);
      
      // 避开换行符(10)
      if (random_byte == '\n') {
        random_byte = 255; // 用255替代换行符
      }else if (random_byte == '=') {
        random_byte = 254; // 用254替代等号
      }
      
      ins_data[i] = random_byte;
  }
  
  // 为插入腾出空间
  memmove(buf + ins_pos + ins_len, buf + ins_pos, current_total_len - ins_pos + 1);
  
  // 插入新数据
  memcpy(buf + ins_pos, ins_data, ins_len);
  
  free(ins_data);
}

// 定位并变异所有符合条件的值
static void mutate_tainted_values(my_mutator_t *state, size_t max_size) {
    const char *data = (const char *)state->data_buf;
    size_t data_len = state->data_size;
    size_t mutator_size = data_len;
    if (data_len+MAX_EXTEND_LEN > max_size) {
        mutator_size = max_size;
    } else {
        mutator_size = data_len + MAX_EXTEND_LEN;
    }
    
    // 确保缓冲区足够大
    maybe_grow(BUF_PARAMS(state, fuzz), mutator_size);
    memcpy(state->fuzz_buf, state->data_buf, data_len);
    state->fuzz_buf[data_len] = '\0';
    
    // 判断是否有污点键以及是否应该只针对污点键进行变异
    int has_taint_keys = (state->taint_key_count > 0);
    int only_taint_keys = has_taint_keys && (RAND_BELOW(100) < 80);  // 有污点键时，80%概率只对污点键变异
    
    const char *line_start = (const char *)state->fuzz_buf;
    while (line_start < (const char *)state->fuzz_buf + data_len) {
        // 查找行尾
        const char *line_end = strchr(line_start, '\n');
        if (!line_end) line_end = (const char *)state->fuzz_buf + data_len;
        
        // 查找等号分隔符
        const char *separator = strchr(line_start, '=');
        if (separator && separator < line_end) {
            // 提取键名
            char key[MAX_KEY_LEN] = {0};
            size_t key_len = separator - line_start;
            if (key_len < MAX_KEY_LEN) {
                memcpy(key, line_start, key_len);
                key[key_len] = '\0';
                
                // 去除键名中的空白字符
                char *trimmed_key = trim(key);
                
                // 根据规则决定是否变异此键
                int should_mutate = !only_taint_keys || is_tainted_key(state, trimmed_key);
                
                if (should_mutate) {
                    // 计算值的起始位置和长度
                    s32 value_start = separator + 1 - (const char *)state->fuzz_buf;
                    s32 value_end = line_end - (const char *)state->fuzz_buf;
                    s32 value_len = value_end - value_start;

                    const int MAX_VALUE_LEN = 2048;
                    // 对值进行变异
                    if (value_end > value_start) {
                        // 随机选择变异类型
                        int mutation_type = RAND_BELOW(100);
                        
                        if (mutation_type < PROB_HAVOC) {
                            // 使用原始的 surgical_havoc_mutate
                            surgical_havoc_mutate(state->fuzz_buf, value_start, value_end);
                        }
                        else if (mutation_type < PROB_HAVOC + PROB_DELETE) {
                            // 删除变异
                            delete_bytes(state->fuzz_buf, value_start, value_end);
                        }
                        else {
                            // 插入变异
                            insert_bytes(state, state->fuzz_buf, value_start, value_end, MAX_VALUE_LEN,mutator_size);
                        }
                        // 更新数据长度
                        data_len = strlen((char*)state->fuzz_buf);
                        line_end = strchr(line_start, '\n');
                        if (!line_end) line_end = (const char *)state->fuzz_buf + data_len;
                    }
                    else if(value_end==value_start) {
                        insert_bytes(state, state->fuzz_buf, value_start, value_end, MAX_VALUE_LEN,mutator_size);
                        // 更新数据长度
                        data_len = strlen((char*)state->fuzz_buf);
                        line_end = strchr(line_start, '\n');
                        if (!line_end) line_end = (const char *)state->fuzz_buf + data_len;
                    }
                }
            }
            else {
                fprintf(stderr, "键名过长: %s\n", key);
            }
        }
        // 移动到下一行
        if(line_end<(const char *)state->fuzz_buf + data_len) {
            line_start = line_end + 1;
        }
        else {
            break;
        }
        state->fuzz_size = strlen((char*)state->fuzz_buf);
    }
}


// 自定义变异器初始化
my_mutator_t *afl_custom_init(afl_t *afl, unsigned int seed) {
    
    srand(seed);
    my_mutator_t *state = calloc(1, sizeof(my_mutator_t));
    if (!state)
    {
        perror("afl_custom_init alloc");
        return NULL;
    }
    
    // 从配置文件读取污点键列表
    read_taint_config(state);
    state->afl = afl;     
    return state;
}

// 自定义变异器清理
void afl_custom_deinit(my_mutator_t *data) {
  my_mutator_t *state = (my_mutator_t *)data;
  if (!state) return;
  
  // 释放污点键列表
  for (int i = 0; i < state->taint_key_count; i++) {
    free(state->taint_keys[i]);
  }
  
  // 释放缓冲区
  free(state->fuzz_buf);
  free(state->data_buf);
  free(state->tmp_buf);
  
  // 释放状态结构
  free(state);
}

// 自定义变异器变异函数
size_t afl_custom_fuzz(my_mutator_t *data, u8 *buf, size_t buf_size, u8 **out_buf,
                      u8 *add_buf, size_t add_buf_size, size_t max_size) {
  my_mutator_t *state = (my_mutator_t *)data;
  
  // 将输入数据复制到内部缓冲区
  maybe_grow(BUF_PARAMS(state, data), buf_size);
  if(!state->data_buf) {
    perror("custom mutator allocation (maybe_grow)");
    return 0;
  }
  memcpy(state->data_buf, buf, buf_size);
  state->data_size = buf_size;
  
  // 执行针对污点值的变异
  mutate_tainted_values(state,max_size);
  
  // 设置输出指针
  *out_buf = state->fuzz_buf;
  
  return state->fuzz_size;
}