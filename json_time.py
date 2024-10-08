import os
from pydub import AudioSegment
import pandas as pd
import json
from tqdm import tqdm

def get_audio_duration(file_path):
    """返回音频文件的时长，单位为秒"""
    with open(file_path, "r") as f:
        js = json.loads(f.read())
        duration = js['voice_activity'][-1][-1]
    return duration

def collect_audio_durations(directory):
    """遍历目录，统计所有 .json 文件的时长"""
    audio_data = []
    total_files = sum([len(files) for _, _, files in os.walk(directory) if any(file.endswith(".json") for file in files)])/2
    print(total_files)
    
    with tqdm(total=total_files, desc="Processing files") as pbar:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    duration = get_audio_duration(file_path)
                    audio_data.append({"File Path": file_path, "Duration (seconds)": duration})
                    pbar.update(1)
    
    return audio_data

def save_to_csv(audio_data, output_file):
    """将音频时长数据保存为 CSV 文件"""
    df = pd.DataFrame(audio_data)
    df.to_csv(output_file, index=False)

# 设置 large 文件夹路径
large_folder_path = '/mnt/data/user/fan_xiaoran/librilight/large/large'

# 统计音频时长
print("Collecting audio durations...")
audio_data = collect_audio_durations(large_folder_path)

# 保存为 CSV 表格
output_csv = '/mnt/data/user/fan_xiaoran/xjf/dit_tokenizer/datasets/libri-light/xjf/librilight_large_durations.csv'
print(f"Saving data to CSV file: {output_csv}")
save_to_csv(audio_data, output_csv)

print(f"Audio durations saved to {output_csv}")