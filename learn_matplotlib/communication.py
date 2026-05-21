import matplotlib.pyplot as plt
import numpy as np

# 电容数据（单位：μF）
C = np.array([0, 1, 2, 3, 4, 5, 6, 7])

# 功率因数 cosϕ
cos_phi = np.array([0.370, 0.473, 0.586, 0.760, 0.862, 0.836, 0.698, 0.541])

fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')

ax.plot(C, cos_phi, marker='o', linewidth=2, markersize=6, color='#1f77b4')
ax.set_xlabel('C / μF')
ax.set_ylabel('cosϕ')
ax.set_title('cosϕ - C Curve')
ax.set_xticks(C)
ax.set_ylim(0, 1)
ax.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

plt.savefig('cosphi_C_curve.png', dpi=300, bbox_inches='tight')
plt.show()



