import matplotlib.pyplot as plt
import numpy as np

# 数据
N = np.array([100, 500, 1000, 2000, 4000, 6000, 8000, 10000])

# 单次操作时间 Duration (sec) —— 来自你之前计算的表格
iter_bin_dur = np.array([1.75e-8, 2.24e-8, 2.60e-8, 2.75e-8, 3.13e-8, 3.39e-8, 3.38e-8, 3.66e-8])
rec_bin_dur  = np.array([2.13e-8, 2.85e-8, 3.14e-8, 3.52e-8, 3.67e-8, 4.09e-8, 4.09e-8, 4.35e-8])
iter_seq_dur = np.array([7.50e-8, 3.80e-7, 6.60e-7, 1.42e-6, 3.12e-6, 4.02e-6, 5.36e-6, 8.10e-6])
rec_seq_dur  = np.array([1.33e-7, 6.75e-7, 1.51e-6, 2.98e-6, 6.04e-6, 9.96e-6, 1.19e-5, 1.53e-5])

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制折线，用不同颜色和标记区分
plt.plot(N, iter_bin_dur, 'o-', label='Iterative Binary Search', linewidth=2, markersize=6)
plt.plot(N, rec_bin_dur,  's-', label='Recursive Binary Search', linewidth=2, markersize=6)
plt.plot(N, iter_seq_dur, '^-', label='Iterative Sequential Search', linewidth=2, markersize=6)
plt.plot(N, rec_seq_dur,  'd-', label='Recursive Sequential Search', linewidth=2, markersize=6)

# 使用对数坐标（因为数值范围相差很大）
plt.yscale('log')
plt.xscale('log')  # N 本身跨度也大，可选对数或线性；这里用对数使趋势更明显

# 添加标签和标题
plt.xlabel('Array Size N', fontsize=12)
plt.ylabel('Average Time per Search (sec)', fontsize=12)
plt.title('Performance Comparison of Search Algorithms (Worst Case)', fontsize=14)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=10)

# 显示图形（如果是在脚本中运行）
plt.tight_layout()


plt.savefig('performance_comparison.pdf', format='pdf', bbox_inches='tight')