import pandas as pd
import numpy as np
import os

def read_csv(file_path):
    return pd.read_csv(file_path)

def analyze_durations(df, n_bins=5):
    durations = df['Duration (seconds)']
    
    # 使用 Sturges' formula 来确定理想的区间数量
    n_bins = int(np.ceil(np.log2(len(durations)) + 1))
    
    # 使用 numpy 的 histogram 函数来智能划分区间
    counts, bins = np.histogram(durations, bins=n_bins)
    
    # 创建区间标签
    labels = [f'{bins[i]:.1f}-{bins[i+1]:.1f}s' for i in range(len(bins)-1)]
    
    return labels, counts

def create_table(labels, counts):
    total = sum(counts)
    percentages = [(count / total) * 100 for count in counts]
    
    # 创建一个新的 DataFrame
    table_data = {
        'Interval': labels,
        'Count': counts,
        'Percentage': [f"{percentage:.1f}%" for percentage in percentages]
    }
    
    df_table = pd.DataFrame(table_data)
    
    # 添加总计行
    total_row = pd.DataFrame({
        'Interval': ['Total'], 
        'Count': [total], 
        'Percentage': ['100.0%']
    })
    
    df_table = pd.concat([df_table, total_row], ignore_index=True)
    
    return df_table

def main(input_file_path, output_file_path):
    df = read_csv(input_file_path)
    labels, counts = analyze_durations(df)
    table = create_table(labels, counts)
    
    # 保存表格为CSV文件
    table.to_csv(output_file_path, index=False)
    print(f"分析结果已保存到: {output_file_path}")

if __name__ == "__main__":
    input_csv_file_path = '/mnt/data/user/fan_xiaoran/xjf/dit_tokenizer/datasets/libri-light/xjf/librilight_small_durations.csv'  # 请替换为您的输入CSV文件路径
    output_csv_file_path = '/mnt/data/user/fan_xiaoran/xjf/dit_tokenizer/datasets/libri-light/xjf/small_dur_distri.csv'  # 请替换为您想要保存输出的CSV文件路径
    
    main(input_csv_file_path, output_csv_file_path)