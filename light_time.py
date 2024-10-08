import os
from pydub import AudioSegment
import pandas as pd

def get_audio_duration(file_path):
    """返回音频文件的时长，单位为秒"""
    audio = AudioSegment.from_file(file_path)
    return len(audio) / 1000  # 返回时长，单位为秒

def collect_audio_durations(directory):
    """遍历目录，统计所有 .wav 文件的时长"""
    audio_data = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".wav"):
                file_path = os.path.join(root, file)
                duration = get_audio_duration(file_path)
                audio_data.append({"File Path": file_path, "Duration (seconds)": duration})
    
    return audio_data

def save_to_csv(audio_data, output_file):
    """将音频时长数据保存为 CSV 文件"""
    df = pd.DataFrame(audio_data)
    df.to_csv(output_file, index=False)

# 设置 large 文件夹路径
large_folder_path = '/mnt/data/user/fan_xiaoran/librilight/seg_large'

# 统计音频时长
audio_data = collect_audio_durations(large_folder_path)

# 保存为 CSV 表格
output_csv = '/mnt/data/user/fan_xiaoran/xjf/dit_tokenizer/datasets/libri-light/xjf/librilight_large_durations.csv'
save_to_csv(audio_data, output_csv)

print(f"Audio durations saved to {output_csv}")
