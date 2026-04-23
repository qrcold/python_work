import numpy as np
import matplotlib.pyplot as plt


def find_inflection_tc(t, u, grid_step=0.05, smooth_window=11):
	"""
	Inflection-point method:
	1) Interpolate to dense grid;
	2) Smooth curve with moving average;
	3) Compute first/second derivatives;
	4) Find d2U/dT2 = 0 nearest the steepest slope position.
	"""
	t = np.asarray(t, dtype=float)
	u = np.asarray(u, dtype=float)

	order = np.argsort(t)
	t = t[order]
	u = u[order]

	t_dense = np.arange(t.min(), t.max() + grid_step, grid_step)
	u_dense = np.interp(t_dense, t, u)

	if smooth_window % 2 == 0:
		smooth_window += 1
	smooth_window = max(5, smooth_window)

	kernel = np.ones(smooth_window) / smooth_window
	pad = smooth_window // 2
	u_pad = np.pad(u_dense, (pad, pad), mode="edge")
	u_smooth = np.convolve(u_pad, kernel, mode="valid")

	d1 = np.gradient(u_smooth, t_dense)
	d2 = np.gradient(d1, t_dense)

	sign = np.sign(d2)
	cross_idx = np.where(sign[:-1] * sign[1:] < 0)[0]

	if len(cross_idx) == 0:
		idx_use = np.argmin(d1[pad:-pad]) + pad if len(d1) > 2 * pad else np.argmin(d1)
		tc = t_dense[idx_use]
		best_idx = int(idx_use)
	else:
		# Among all inflection candidates, choose the one with the steepest slope.
		slope_strength = np.abs(d1[cross_idx])
		best_idx = int(cross_idx[np.argmax(slope_strength)])
		x0, x1 = t_dense[best_idx], t_dense[best_idx + 1]
		y0, y1 = d2[best_idx], d2[best_idx + 1]
		if y1 == y0:
			tc = (x0 + x1) / 2
		else:
			tc = x0 - y0 * (x1 - x0) / (y1 - y0)

	u_tc = np.interp(tc, t_dense, u_smooth)

	return {
		"tc": float(tc),
		"u_tc": float(u_tc),
		"t_dense": t_dense,
		"u_smooth": u_smooth,
		"d1": d1,
		"d2": d2,
		"best_idx": best_idx,
	}


def main():
	# Heating data
	t_heat = np.array([
		20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0,
		52.0, 54.0, 56.0, 58.0, 60.0, 62.0, 64.0, 66.0, 68.0, 70.0,
		70.5, 71.0, 71.5, 72.0, 72.5, 73.0, 73.5, 74.0, 74.5, 75.0,
		75.5, 76.0, 76.5, 77.0, 77.5, 78.0, 78.5, 79.0, 79.5, 80.0,
		80.5, 81.0, 81.5, 82.0, 82.5, 83.0, 83.5, 84.0, 84.5, 85.0,
		85.5, 86.0, 86.5, 87.0, 87.5, 88.0, 88.5, 89.0, 89.5, 90.0,
		92.0, 94.0, 96.0, 98.0, 100.0, 102.0, 104.0, 106.0, 108.0, 110.0,
	])
	u_heat = np.array([
		100.3, 100.8, 101.0, 101.4, 101.8, 102.3, 102.7,
		102.9, 103.0, 103.2, 103.4, 103.4, 103.3, 103.5, 103.5, 103.2, 102.8,
		102.8, 103.2, 103.2, 103.0, 102.7, 102.2, 101.5, 100.5, 99.6, 98.5,
		96.5, 94.5, 91.5, 86.4, 83.6, 79.9, 76.1, 72.2, 68.7, 65.2,
		61.7, 58.8, 56.4, 54.5, 52.3, 50.5, 48.5, 47.0, 45.3, 43.8,
		42.2, 40.6, 39.2, 38.1, 37.0, 36.0, 34.8, 33.7, 33.2, 32.3,
		29.1, 26.3, 23.9, 21.8, 19.5, 18.0, 15.4, 13.8, 10.8, 9.3,
	])

	# Cooling data
	t_cool = np.array([
		110.0, 108.0, 106.0, 104.0, 102.0, 100.0, 98.0, 96.0, 94.0, 92.0,
		90.0, 89.5, 89.0, 88.5, 88.0, 87.5, 87.0, 86.5, 86.0, 85.5,
		85.0, 84.5, 84.0, 83.5, 83.0, 82.5, 82.0, 81.5, 81.0, 80.5,
		80.0, 79.5, 79.0, 78.5, 78.0, 77.5, 77.0, 76.5, 76.0, 75.5,
		75.0, 74.5, 74.0, 73.5, 73.0, 72.5, 72.0, 71.5, 71.0, 70.5,
		70.0, 68.0, 66.0, 64.0, 62.0, 60.0, 58.0, 56.0,
	])
	u_cool = np.array([
		9.3, 10.1, 13.1, 15.0, 16.4, 18.8, 21.7, 24.1, 26.7, 29.2,
		32.4, 32.7, 33.7, 34.5, 35.6, 36.7, 37.5, 38.4, 40.3, 41.8,
		43.5, 45.0, 46.8, 48.4, 50.2, 51.7, 54.4, 57.8, 60.6, 63.1,
		66.9, 71.1, 75.5, 79.1, 83.2, 87.0, 90.3, 93.0, 95.7, 96.0,
		97.5, 97.7, 98.3, 98.9, 100.4, 99.7, 100.3, 100.4, 101.3, 101.4,
		101.4, 103.9, 103.9, 103.4, 102.8, 102.5, 101.4, 100.8,
	])

	heat_res = find_inflection_tc(t_heat, u_heat)
	cool_res = find_inflection_tc(t_cool, u_cool)

	tc_heat = heat_res["tc"]
	tc_cool = cool_res["tc"]

	# Figure 1: heating/cooling overlay for direct comparison
	fig_cmp, ax_cmp = plt.subplots(figsize=(8.8, 5.4), dpi=140)
	ax_cmp.scatter(t_heat, u_heat, s=16, color="#1f77b4", alpha=0.55, label="Heating raw")
	ax_cmp.scatter(t_cool, u_cool, s=16, color="#2ca02c", alpha=0.55, label="Cooling raw")
	ax_cmp.plot(heat_res["t_dense"], heat_res["u_smooth"], color="#1f77b4", lw=2.2, label="Heating smooth")
	ax_cmp.plot(cool_res["t_dense"], cool_res["u_smooth"], color="#2ca02c", lw=2.2, label="Cooling smooth")
	ax_cmp.axvline(tc_heat, color="#1f77b4", ls="--", lw=1.8, label=f"Heating Tc={tc_heat:.2f} degC")
	ax_cmp.axvline(tc_cool, color="#2ca02c", ls="--", lw=1.8, label=f"Cooling Tc={tc_cool:.2f} degC")
	ax_cmp.plot(tc_heat, heat_res["u_tc"], "o", color="#1f77b4")
	ax_cmp.plot(tc_cool, cool_res["u_tc"], "o", color="#2ca02c")
	ax_cmp.set_title("Heating vs Cooling Comparison")
	ax_cmp.set_xlabel("T (degC)")
	ax_cmp.set_ylabel("U (mV)")
	ax_cmp.grid(alpha=0.25)
	ax_cmp.legend(fontsize=9)
	fig_cmp.tight_layout()
	fig_cmp.savefig("curie_compare_overlay.png", bbox_inches="tight")
	plt.close(fig_cmp)

	# Figure 2: inflection-method diagnostics (curve + derivatives)
	fig_inflect, axes = plt.subplots(2, 2, figsize=(12.6, 8.5), dpi=140)

	axes[0, 0].scatter(t_heat, u_heat, s=14, color="#1f77b4", alpha=0.6, label="Raw")
	axes[0, 0].plot(heat_res["t_dense"], heat_res["u_smooth"], color="#ff7f0e", lw=2.0, label="Smoothed")
	axes[0, 0].axvline(tc_heat, color="crimson", ls="--", lw=1.7, label=f"Tc={tc_heat:.2f}")
	axes[0, 0].set_title("Heating U-T")
	axes[0, 0].set_xlabel("T (degC)")
	axes[0, 0].set_ylabel("U (mV)")
	axes[0, 0].grid(alpha=0.25)
	axes[0, 0].legend()

	axes[0, 1].plot(heat_res["t_dense"], heat_res["d1"], color="#d62728", lw=1.8, label="dU/dT")
	axes[0, 1].plot(heat_res["t_dense"], heat_res["d2"], color="#9467bd", lw=1.5, label="d2U/dT2")
	axes[0, 1].axhline(0, color="gray", ls=":", lw=1)
	axes[0, 1].axvline(tc_heat, color="crimson", ls="--", lw=1.7, label="Tc from inflection")
	axes[0, 1].set_title("Heating Derivatives")
	axes[0, 1].set_xlabel("T (degC)")
	axes[0, 1].set_ylabel("Derivative")
	axes[0, 1].grid(alpha=0.25)
	axes[0, 1].legend()

	axes[1, 0].scatter(t_cool, u_cool, s=14, color="#2ca02c", alpha=0.6, label="Raw")
	axes[1, 0].plot(cool_res["t_dense"], cool_res["u_smooth"], color="#ff7f0e", lw=2.0, label="Smoothed")
	axes[1, 0].axvline(tc_cool, color="crimson", ls="--", lw=1.7, label=f"Tc={tc_cool:.2f}")
	axes[1, 0].set_title("Cooling U-T")
	axes[1, 0].set_xlabel("T (degC)")
	axes[1, 0].set_ylabel("U (mV)")
	axes[1, 0].grid(alpha=0.25)
	axes[1, 0].legend()

	axes[1, 1].plot(cool_res["t_dense"], cool_res["d1"], color="#d62728", lw=1.8, label="dU/dT")
	axes[1, 1].plot(cool_res["t_dense"], cool_res["d2"], color="#9467bd", lw=1.5, label="d2U/dT2")
	axes[1, 1].axhline(0, color="gray", ls=":", lw=1)
	axes[1, 1].axvline(tc_cool, color="crimson", ls="--", lw=1.7, label="Tc from inflection")
	axes[1, 1].set_title("Cooling Derivatives")
	axes[1, 1].set_xlabel("T (degC)")
	axes[1, 1].set_ylabel("Derivative")
	axes[1, 1].grid(alpha=0.25)
	axes[1, 1].legend()

	fig_inflect.suptitle("Inflection-Point Method Diagnostics")
	fig_inflect.tight_layout()
	fig_inflect.savefig("curie_inflection_method.png", bbox_inches="tight")
	plt.close(fig_inflect)

	print(f"Heating Curie temperature Tc = {tc_heat:.2f} degC")
	print(f"Cooling Curie temperature Tc = {tc_cool:.2f} degC")
	print("Saved figure: curie_compare_overlay.png")
	print("Saved figure: curie_inflection_method.png")


if __name__ == "__main__":
	main()
