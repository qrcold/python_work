import numpy as np
import matplotlib.pyplot as plt


R0 = 50.0  # ohm at 0 degC


def format_sigfig(value, digits=3):
	if value == 0:
		return "0." + "0" * (digits - 1)
	magnitude = int(np.floor(np.log10(abs(value))))
	decimals = max(digits - magnitude - 1, 0)
	return f"{value:.{decimals}f}"

def fit_alpha_with_known_r0(temperature_c, resistance_ohm, r0_ohm):
	temperature_c = np.asarray(temperature_c, dtype=float)
	resistance_ohm = np.asarray(resistance_ohm, dtype=float)
	slope = float(np.sum(temperature_c * (resistance_ohm - r0_ohm)) / np.sum(temperature_c * temperature_c))
	alpha = slope / r0_ohm
	return alpha, slope


def fit_alpha_by_linear_regression(temperature_c, resistance_ohm):
	coeffs = np.polyfit(temperature_c, resistance_ohm, 1)
	slope, intercept = float(coeffs[0]), float(coeffs[1])
	alpha = slope / intercept
	return alpha, slope, intercept


def main():
	temperature_c = np.array([17.2, 22.2, 27.2, 32.2, 37.2, 42.2, 47.2, 52.2], dtype=float)
	resistance_ohm = np.array([54.72, 55.78, 56.85, 57.42, 58.54, 59.63, 60.75, 61.82], dtype=float)

	alpha_each = (resistance_ohm - R0) / (R0 * temperature_c)
	alpha_avg = float(np.mean(alpha_each))
	alpha_fixed, slope_fixed = fit_alpha_with_known_r0(temperature_c, resistance_ohm, R0)
	alpha_unconstrained, slope_unconstrained, intercept_unconstrained = fit_alpha_by_linear_regression(temperature_c, resistance_ohm)

	fit_line_fixed = R0 + slope_fixed * temperature_c
	fit_line_unconstrained = slope_unconstrained * temperature_c + intercept_unconstrained
	r_squared_fixed = 1.0 - np.sum((resistance_ohm - fit_line_fixed) ** 2) / np.sum((resistance_ohm - np.mean(resistance_ohm)) ** 2)
	r_squared_unconstrained = 1.0 - np.sum((resistance_ohm - fit_line_unconstrained) ** 2) / np.sum((resistance_ohm - np.mean(resistance_ohm)) ** 2)
	max_residual_fixed = float(np.max(np.abs(resistance_ohm - fit_line_fixed)))

	fig, ax = plt.subplots(figsize=(8.4, 5.6), dpi=140)
	ax.scatter(temperature_c, resistance_ohm, s=48, color="#1f77b4", label="Measured data")
	t_dense = np.linspace(temperature_c.min(), temperature_c.max(), 300)
	ax.plot(t_dense, R0 + slope_fixed * t_dense, color="#d62728", lw=2.2, label="Fit with R0=50 ohm")
	ax.plot(t_dense, slope_unconstrained * t_dense + intercept_unconstrained, color="#2ca02c", lw=1.8, ls="--", label="Unconstrained fit")
	ax.set_xlabel("Temperature t (degC)")
	ax.set_ylabel("Resistance R_t (ohm)")
	ax.set_title("Balanced Bridge Data Validation")
	ax.grid(alpha=0.28)
	ax.legend()
	text = (
		f"fixed R0 = {format_sigfig(R0)} ohm\n"
		f"alpha_fixed = {format_sigfig(alpha_fixed * 1e3)} x 10^-3 /degC\n"
		f"alpha_avg = {format_sigfig(alpha_avg * 1e3)} x 10^-3 /degC"
	)
	ax.text(
		0.03,
		0.97,
		text,
		transform=ax.transAxes,
		va="top",
		ha="left",
		bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.9, edgecolor="#999999"),
	)
	fig.tight_layout()
	fig.savefig("balanced_bridge_linear_regression.png", bbox_inches="tight")

	print("Balanced bridge validation result:")
	print(f"  assumed R0 = {format_sigfig(R0)} ohm at 0 degC")
	print("  pointwise alpha values (x10^-3 /degC):")
	for index, value in enumerate(alpha_each * 1e3, start=1):
		print(f"    alpha_{index} = {format_sigfig(value)}")
	print(f"  average alpha = {format_sigfig(alpha_avg * 1e3)} x 10^-3 /degC")
	print(f"  fixed-R0 regression alpha = {format_sigfig(alpha_fixed * 1e3)} x 10^-3 /degC")
	print(f"  unconstrained regression alpha = {format_sigfig(alpha_unconstrained * 1e3)} x 10^-3 /degC")
	print(f"  unconstrained intercept = {format_sigfig(intercept_unconstrained)} ohm")
	print(f"  fixed-R0 R^2 = {format_sigfig(r_squared_fixed)}")
	print(f"  unconstrained R^2 = {format_sigfig(r_squared_unconstrained)}")
	print(f"  max residual with R0=50 ohm = {format_sigfig(max_residual_fixed)} ohm")
	print("Saved figure: balanced_bridge_linear_regression.png")


if __name__ == "__main__":
	main()