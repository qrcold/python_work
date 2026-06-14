from pathlib import Path

import matplotlib as mpl
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
import numpy as np


mpl.rcParams.update(
	{
		"font.sans-serif": ["SimHei", "DejaVu Sans"],
		"axes.unicode_minus": False,
	}
)

CHINESE_FONT = font_manager.FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf")


def format_value(value: float, digits: int = 3) -> str:
	if value == 0:
		return "0"
	magnitude = int(np.floor(np.log10(abs(value))))
	decimals = max(digits - magnitude - 1, 0)
	return f"{value:.{decimals}f}"


def find_linear_crossing(x_values: np.ndarray, y_values: np.ndarray, target: float = 0.0) -> float:
	x_values = np.asarray(x_values, dtype=float)
	y_values = np.asarray(y_values, dtype=float)
	delta = y_values - target

	for index in range(len(delta) - 1):
		left_delta = delta[index]
		right_delta = delta[index + 1]
		if np.isclose(left_delta, 0.0):
			return float(x_values[index])
		if left_delta == 0.0:
			return float(x_values[index])
		if left_delta * right_delta <= 0.0:
			if np.isclose(left_delta, right_delta):
				return float(x_values[index])
			fraction = (target - y_values[index]) / (y_values[index + 1] - y_values[index])
			return float(x_values[index] + fraction * (x_values[index + 1] - x_values[index]))

	raise ValueError("No crossing found for the requested target value.")


def polygon_area(x_values: np.ndarray, y_values: np.ndarray) -> float:
	x_values = np.asarray(x_values, dtype=float)
	y_values = np.asarray(y_values, dtype=float)
	return 0.5 * float(np.abs(np.dot(x_values, np.roll(y_values, -1)) - np.dot(y_values, np.roll(x_values, -1))))


def interpolate_value_at_x(x_values: np.ndarray, y_values: np.ndarray, target_x: float) -> float:
	x_values = np.asarray(x_values, dtype=float)
	y_values = np.asarray(y_values, dtype=float)
	return float(np.interp(target_x, x_values, y_values))


def main() -> None:
	# The 4th B value in the left branch appears to be missing a minus sign in the source table.
	# Without this correction the curve is physically inconsistent and the loop area is distorted.
	number_0 = np.arange(1, 13, dtype=int)
	left_h_am = np.array([-242.1, -179.6, -159.3, -139.0, -101.5, -65.62, -32.81, 7.812, 75.0, 137.5, 196.8, 285.9], dtype=float)
	left_b_mt = np.array([-568.00, -435.00, -384.25, -325.75, -185.20, -21.14, 113.28, 246.08, 378.75, 460.75, 519.50, 578.00], dtype=float)
	right_h_am = np.array([-242.1, -167.1, -76.56, -7.812, 32.81, 64.06, 95.31, 121.8, 154.6, 189.0, 220.3, 285.9], dtype=float)
	right_b_mt = np.array([-568.00, -521.00, -479.50, -282.75, -157.85, -28.95, 109.38, 222.66, 320.25, 410.00, 472.50, 578.00], dtype=float)

	left_br_mt = interpolate_value_at_x(left_h_am, left_b_mt, 0.0)
	right_br_mt = interpolate_value_at_x(right_h_am, right_b_mt, 0.0)
	left_hc_am = find_linear_crossing(left_h_am, left_b_mt, 0.0)
	right_hc_am = find_linear_crossing(right_h_am, right_b_mt, 0.0)

	loop_h = np.concatenate([left_h_am, right_h_am[::-1]])
	loop_b_mt = np.concatenate([left_b_mt, right_b_mt[::-1]])
	loop_area_mt_amp = polygon_area(loop_h, loop_b_mt)
	loop_area_j_m3 = loop_area_mt_amp * 1e-3

	common_h = np.linspace(max(left_h_am.min(), right_h_am.min()), min(left_h_am.max(), right_h_am.max()), 500)
	left_interp = np.interp(common_h, left_h_am, left_b_mt)
	right_interp = np.interp(common_h, right_h_am, right_b_mt)
	max_vertical_gap = float(np.max(np.abs(left_interp - right_interp)))
	max_gap_h = float(common_h[np.argmax(np.abs(left_interp - right_interp))])

	fig, ax = plt.subplots(figsize=(8.6, 6.0), layout="constrained")
	ax.plot(left_h_am, left_b_mt, marker="o", linewidth=2.1, color="#1f77b4", label="支路 1")
	ax.plot(right_h_am, right_b_mt, marker="s", linewidth=2.1, color="#d62728", label="支路 2")
	ax.scatter([0.0, 0.0], [left_br_mt, right_br_mt], color=["#1f77b4", "#d62728"], zorder=5)
	ax.scatter([left_hc_am, right_hc_am], [0.0, 0.0], color=["#1f77b4", "#d62728"], zorder=5, marker="x", s=90)
	ax.set_xlabel("H (A/m)")
	ax.set_ylabel("B (mT)")
	ax.set_title("磁滞回线")
	ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
	ax.legend(prop=CHINESE_FONT)

	ax.annotate(
		f"Br1 = {format_value(left_br_mt)} mT",
		(0.0, left_br_mt),
		textcoords="offset points",
		xytext=(10, 10),
		fontsize=9,
	)
	ax.annotate(
		f"Br2 = {format_value(right_br_mt)} mT",
		(0.0, right_br_mt),
		textcoords="offset points",
		xytext=(10, -18),
		fontsize=9,
	)
	ax.annotate(
		f"Hc1 = {format_value(left_hc_am)} A/m",
		(left_hc_am, 0.0),
		textcoords="offset points",
		xytext=(-42, 10),
		fontsize=9,
	)
	ax.annotate(
		f"Hc2 = {format_value(right_hc_am)} A/m",
		(right_hc_am, 0.0),
		textcoords="offset points",
		xytext=(8, -18),
		fontsize=9,
	)

	output_path = Path(__file__).with_name("hysteresis_curve.png")
	fig.savefig(output_path, dpi=300, bbox_inches="tight")

	print("磁滞回线分析结果")
	print("-" * 58)
	print(f"图像已保存到: {output_path}")
	print(f"回线面积 = {format_value(loop_area_mt_amp)} mT·A/m")
	print(f"回线面积 = {format_value(loop_area_j_m3)} J/m^3")
	print()
	print("特殊交点")
	print(f"  支路1: B=0 时的 Hc1 = {format_value(left_hc_am)} A/m")
	print(f"  支路2: B=0 时的 Hc2 = {format_value(right_hc_am)} A/m")
	print(f"  支路1: H=0 时的 Br1 = {format_value(left_br_mt)} mT")
	print(f"  支路2: H=0 时的 Br2 = {format_value(right_br_mt)} mT")
	print()
	print("相关参数")
	print(f"  左支路最大 B = {format_value(left_b_mt.max())} mT, 对应 H = {format_value(left_h_am[np.argmax(left_b_mt)])} A/m")
	print(f"  右支路最大 B = {format_value(right_b_mt.max())} mT, 对应 H = {format_value(right_h_am[np.argmax(right_b_mt)])} A/m")
	print(f"  左支路最小 B = {format_value(left_b_mt.min())} mT, 对应 H = {format_value(left_h_am[np.argmin(left_b_mt)])} A/m")
	print(f"  右支路最小 B = {format_value(right_b_mt.min())} mT, 对应 H = {format_value(right_h_am[np.argmin(right_b_mt)])} A/m")
	print(f"  两支路在同一 H 位置的最大磁感应强度差 = {format_value(max_vertical_gap)} mT, 发生在 H = {format_value(max_gap_h)} A/m")

	plt.show()


if __name__ == "__main__":
	main()