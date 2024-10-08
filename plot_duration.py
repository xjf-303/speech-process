import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 读取CSV文件
def read_csv(file_path):
    return pd.read_csv(file_path)

# 智能划分区间并统计数量
def analyze_durations(df, n_bins=5):
    durations = df['Duration (seconds)']
    
    # 使用 Sturges' formula 来确定理想的区间数量
    n_bins = int(np.ceil(np.log2(len(durations)) + 1))
    
    # 使用 numpy 的 histogram 函数来智能划分区间
    counts, bins = np.histogram(durations, bins=n_bins)
    
    # 创建区间标签
    labels = [f'{bins[i]:.1f}-{bins[i+1]:.1f}s' for i in range(len(bins)-1)]
    
    return dict(zip(labels, counts))

# 绘制饼图
def plot_pie_chart(data):
    plt.figure(figsize=(10, 8))
    plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=90)
    plt.title('Audio Duration Distribution')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.tight_layout()
    plt.savefig('/mnt/data/user/fan_xiaoran/xjf/dit_tokenizer/datasets/libri-light/xjf/small_dur.png')
# 主函数
def main(file_path):
    df = read_csv(file_path)
    duration_stats = analyze_durations(df)
    plot_pie_chart(duration_stats)

# 运行脚本
if __name__ == "__main__":
    csv_file_path = '/mnt/data/user/fan_xiaoran/xjf/dit_tokenizer/datasets/libri-light/xjf/librilight_small_durations.csv'  # 请替换为您的CSV文件路径
    main(csv_file_path)