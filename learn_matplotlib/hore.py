import numpy as np
import matplotlib.pyplot as plt

# ========== 设置中文字体及负号显示 ==========
plt.rcParams['font.sans-serif'] = ['SimHei']   # 使用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False     # 正确显示负号

# ========== 物理常数与线圈参数 ==========
mu0 = 4 * np.pi * 1e-7      # 真空磁导率 (H/m)
I = 0.4                     # 电流 (A)，400 mA
N = 400                     # 线圈匝数
R = 0.10                    # 线圈半径 (m)，10.00 cm

# ========== 实验数据 ==========
x_cm = np.array([-10.00, -9.00, -8.00, -7.00, -6.00, -5.00, -4.00, -3.00, -2.00, -1.00,
                  0.00,  1.00,  2.00,  3.00,  4.00,  5.00,  6.00,  7.00,  8.00,  9.00, 10.00])
B_fwd = np.array([346, 398, 461, 536, 618, 696, 781, 858, 923, 974,
                  987, 980, 943, 882, 805, 731, 640, 564, 489, 426, 367])
B_rev = np.array([-341, -400, -463, -538, -610, -699, -778, -860, -929, -969,
                  -993, -980, -950, -883, -809, -713, -635, -557, -481, -412, -360])

# ========== 正确的实验磁感应强度 (μT) ==========
B_exp = (B_fwd - B_rev) / 2.0

# ========== 理论磁感应强度 (μT) ==========
x_m = x_cm / 100.0
B_th_T = (mu0 * N * I * R**2) / (2 * (R**2 + x_m**2)**(3/2))
B_th_uT = B_th_T * 1e6

# ========== 相对误差 (%) ==========
rel_error = (B_exp - B_th_uT) / B_th_uT * 100

# ========== 打印表格 ==========
print("="*80)
print(f"{'x (cm)':<8} {'B_exp (μT)':<12} {'B_theory (μT)':<15} {'相对误差 (%)':<12}")
print("-"*80)
for i in range(len(x_cm)):
    print(f"{x_cm[i]:<8.2f} {B_exp[i]:<12.2f} {B_th_uT[i]:<15.2f} {rel_error[i]:<12.2f}")
print("="*80)

# ========== 绘图：磁场分布对比 ==========
plt.figure(figsize=(10, 6))
plt.plot(x_cm, B_exp, 'bo-', label='实验值 (B_exp = (B_fwd - B_rev)/2)', markersize=4)
plt.plot(x_cm, B_th_uT, 'r^-', label='理论值 (B_theory)', markersize=4)
plt.xlabel('轴向距离 x (cm)', fontsize=12)
plt.ylabel('磁感应强度 (μT)', fontsize=12)
plt.title(f'圆形线圈轴线上磁场分布 (N={N}, R={R*100:.1f} cm, I={I*1000:.0f} mA)', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ========== 绘图：相对误差曲线 ==========
plt.figure(figsize=(10, 4))
plt.plot(x_cm, rel_error, 'go-', markersize=4)
plt.axhline(0, color='k', linestyle='--', linewidth=0.8)
plt.xlabel('轴向距离 x (cm)', fontsize=12)
plt.ylabel('相对误差 (%)', fontsize=12)
plt.title('实验值与理论值的相对误差', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()