import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


U_S = 1.3  # V
ALPHA_STD = 0.004280  # 1 / degC


def format_sigfig(value, digits=3):
	if value == 0:
		return "0." + "0" * (digits - 1)
	magnitude = int(np.floor(np.log10(abs(value))))
	decimals = max(digits - magnitude - 1, 0)
	return f"{value:.{decimals}f}"


def bridge_voltage(t, alpha):
	return U_S * alpha * t / (4.0 + 2.0 * alpha * t)


def fit_alpha_from_linearized_data(t, u_v):
	# Rearranged exact model: U / (U_S - 2U) = (alpha / 4) * t
	x = np.asarray(t, dtype=float)
	y = np.asarray(u_v / (U_S - 2.0 * u_v), dtype=float)
	denom = float(np.sum(x * x))
	m = float(np.sum(x * y) / denom)
	alpha = 4.0 * m
	return alpha, m


def fit_alpha_nonlinear(t, u_v):
	(alpha,) = curve_fit(bridge_voltage, t, u_v, p0=[0.003], maxfev=100000)[0]
	return float(alpha)


def main():
	t = np.array([17.2, 22.2, 27.2, 32.2, 37.2, 42.2, 47.2, 52.2], dtype=float)
	u_mv = np.array([25.8, 32.4, 39.3, 44.7, 50.7, 56.7, 62.5, 68.1], dtype=float)
	u_v = u_mv / 1000.0

	# Per-point alpha values from the given formula.
	alpha_each = 4.0 * u_v / (t * (U_S - 2.0 * u_v))
	alpha_avg = float(np.mean(alpha_each))

	# Fit alpha from the U-T characteristic curve.
	alpha_curve = fit_alpha_nonlinear(t, u_v)

	rel_err_avg = abs(alpha_avg - ALPHA_STD) / ALPHA_STD * 100.0
	rel_err_curve = abs(alpha_curve - ALPHA_STD) / ALPHA_STD * 100.0

	# Figure 1: U0-T characteristic curve and fitted alpha.
	fig1, ax1 = plt.subplots(figsize=(8.6, 5.6), dpi=140)
	ax1.scatter(t, u_mv, s=48, color="#1f77b4", label="Measured data")
	t_dense = np.linspace(t.min(), t.max(), 300)
	ax1.plot(t_dense, bridge_voltage(t_dense, alpha_curve) * 1000.0, color="#d62728", lw=2.2, label="Curve fit")
	ax1.set_xlabel("Temperature T (degC)")
	ax1.set_ylabel("U0 (mV)")
	ax1.set_title("U0-T Characteristic Curve")
	ax1.grid(alpha=0.28)
	ax1.legend()
	text1 = (
		f"alpha_curve = {format_sigfig(alpha_curve * 1e3)} x 10^-3 /degC\n"
		f"alpha_avg = {format_sigfig(alpha_avg * 1e3)} x 10^-3 /degC"
	)
	ax1.text(
		0.03,
		0.97,
		text1,
		transform=ax1.transAxes,
		va="top",
		ha="left",
		bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.88, edgecolor="#999999"),
	)
	fig1.tight_layout()
	fig1.savefig("u0_t_linear_fit.png", bbox_inches="tight")

	# Figure 2: alpha values for each data point.
	fig2, ax2 = plt.subplots(figsize=(8.6, 5.6), dpi=140)
	indices = np.arange(1, len(t) + 1)
	alpha_scaled = alpha_each * 1e3
	ax2.plot(indices, alpha_scaled, "o-", color="#9467bd", lw=2, label="alpha_i")
	ax2.axhline(alpha_avg * 1e3, color="#d62728", ls="--", lw=1.8, label="Average alpha")
	ax2.axhline(alpha_curve * 1e3, color="#1f77b4", ls="-.", lw=1.8, label="Curve-fit alpha")
	ax2.set_xticks(indices)
	ax2.set_xlabel("Index")
	ax2.set_ylabel("alpha x 10^-3 /degC")
	ax2.set_title("Eight Alpha Values")
	ax2.grid(alpha=0.28)
	ax2.legend(fontsize=9)
	fig2.tight_layout()
	fig2.savefig("alpha_values.png", bbox_inches="tight")

	print("1) U-T characteristic curve and alpha from curve fit:")
	print(f"   alpha_curve = {format_sigfig(alpha_curve * 1e3)} x 10^-3 /degC")
	print("2) Alpha at each temperature and the average:")
	for i, value in enumerate(alpha_scaled, start=1):
		print(f"   alpha_{i} = {format_sigfig(value)} x 10^-3 /degC")
	print(f"   average alpha = {format_sigfig(alpha_avg * 1e3)} x 10^-3 /degC")

	print("3) Relative error versus theory:")
	print(f"   alpha_curve error = {format_sigfig(rel_err_curve)} %")
	print(f"   average alpha error = {format_sigfig(rel_err_avg)} %")
	print(f"   reference alpha = {format_sigfig(ALPHA_STD * 1e3)} x 10^-3 /degC")



if __name__ == "__main__":
	main()