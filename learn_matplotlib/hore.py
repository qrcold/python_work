import numpy as np
import matplotlib.pyplot as plt

# ========== 设置中文字体及负号显示 ==========
plt.rcParams['font.sans-serif'] = ['SimHei']   # 使用黑体
plt.rcParams['axes.unicode_minus'] = False     # 正常显示负号

# ========== 径向数据（合并正负侧） ==========
x = np.array([-5.00, -4.00, -3.00, -2.00, -1.00, 0.00, 1.00, 2.00, 3.00, 4.00, 5.00])
B_avg = np.array([1199, 1109, 1047, 1010, 991, 986, 998, 1024, 1071, 1140, 1248])

# ========== 绘图 ==========
plt.figure(figsize=(8, 6))
plt.plot(x, B_avg, 'bo-', linewidth=2, markersize=6, label='实验平均值')

# 可选：添加对称辅助线（x=0 竖线）
plt.axvline(0, color='gray', linestyle='--', linewidth=1, alpha=0.7)

plt.xlabel('径向距离 x (cm)', fontsize=12)
plt.ylabel('磁感应强度 (μT)', fontsize=12)
plt.title('圆形线圈径向磁场分布', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

# 可选：打印数据表格
print("径向距离(cm)\t磁感应强度(μT)")
for xi, Bi in zip(x, B_avg):
    print(f"{xi:8.2f}\t{Bi:8.0f}")