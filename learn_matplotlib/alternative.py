from pathlib import Path

import matplotlib as mpl
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import numpy as np


mpl.rcParams.update(
	{
		"axes.unicode_minus": False,
	}
)

CHINESE_FONT = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf")


def main() -> None:
	# Basic magnetization curve data.
	voltage_v = np.array([0.5, 1.0, 1.2, 1.5, 1.8, 2.0, 2.5, 2.8, 3.0])
	h_am = np.array([42.25, 76.72, 87.66, 108.7, 136.1, 156.4, 214.3, 251.8, 280.0])
	b_mt = np.array([94.20, 188.62, 227.70, 278.25, 342.75, 385.75, 494.25, 537.25, 576.50])

	# Convert B from mT to T before computing mu = B / H.
	mu_h_per_m = (b_mt * 1e-3) / h_am

	print("基本磁化曲线表")
	print(f"{'U/V':>6} {'H(A/m)':>12} {'B(mT)':>12} {'μ(H/m)':>14}")
	print("-" * 48)
	for u, h, b, mu in zip(voltage_v, h_am, b_mt, mu_h_per_m):
		print(f"{u:6.1f} {h:12.2f} {b:12.2f} {mu:14.6e}")

	# Plot the basic magnetization curve B-H.
	fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
	ax.plot(h_am, b_mt, marker="o", linewidth=2.2, color="#1f77b4")
	ax.set_xlabel("H (A/m)", fontproperties=CHINESE_FONT)
	ax.set_ylabel("B (mT)", fontproperties=CHINESE_FONT)
	ax.set_title("基本磁化曲线", fontproperties=CHINESE_FONT)
	ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)

	# Annotate each point with its excitation voltage for easier reading.
	for u, h, b in zip(voltage_v, h_am, b_mt):
		ax.annotate(
			f"{u:.1f}V",
			(h, b),
			textcoords="offset points",
			xytext=(0, 8),
			ha="center",
			fontsize=9,
		)

	output_path = Path(__file__).with_name("basic_magnetization_curve.png")
	fig.savefig(output_path, dpi=300, bbox_inches="tight")
	print(f"\n图像已保存到: {output_path}")

	plt.show()


if __name__ == "__main__":
	main()
