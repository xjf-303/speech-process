import os

def count_json_files(directory):
    json_count = 0
    for root, dirs, files in os.walk(directory):
        # 使用生成器表达式来快速过滤.json文件
        # 如果目录中有.json文件，则增加计数
        json_count += sum(1 for file in files if file.endswith('.json'))
    return json_count

directory = '/mnt/data/user/fan_xiaoran/librilight/large/large'
total_files = count_json_files(directory)
print(f"Total JSON files: {total_files}")