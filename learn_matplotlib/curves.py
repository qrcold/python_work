import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from typing import List, Tuple


def compute_alpha(R1: float, t1: float, R2: float, t2: float) -> float:
    """Compute alpha using formula: (R2-R1)/(R1*t2 - R2*t1)

    R in ohm, t in degC
    """
    return (R2 - R1) / (R1 * t2 - R2 * t1)


def alphas_from_pairs(R_list: List[float], t_list: List[float]) -> List[float]:
    """Compute alphas using pairs (n, n-5) for n=6..10 (1-based indexing).
    Expects len>=10.
    """
    if len(R_list) < 10:
        raise ValueError("Need at least 10 measurements")
    alphas = []
    # convert to 0-based indices; pairs (5,0),(6,1),(7,2),(8,3),(9,4)
    for n in range(5, 10):
        i1 = n  # n (0-based)
        i0 = n - 5
        R1 = R_list[i1]
        t1 = t_list[i1]
        R0 = R_list[i0]
        t0 = t_list[i0]
        a = compute_alpha(R0, t0, R1, t1)
        alphas.append(a)
    return alphas


def fit_alpha(R_list: List[float], t_list: List[float]) -> Tuple[float, float, float]:
    """Linear fit R = A + B*t, return A, B, alpha_fit = B/A"""
    coeffs = np.polyfit(t_list, R_list, 1)
    B, A = coeffs[0], coeffs[1]
    alpha = B / A
    return A, B, alpha


def main() -> None:
    # Given data
    t = [30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0]
    R_milli = [4.880, 4.965, 5.067, 5.160, 5.245, 5.330, 5.425, 5.515, 5.610, 5.705]
    # convert to ohm
    R = [x * 1e-3 for x in R_milli]

    # 1) compute 5 alphas from n and n-5 pairs
    alphas = alphas_from_pairs(R, t)
    alpha_mean = mean(alphas)

    print("Alphas from pairs (n and n-5):")
    for i, a in enumerate(alphas, start=1):
        print(f"alpha_{i} = {a:.6e}")
    print(f"Mean alpha = {alpha_mean:.6e}\n")

    # 2) linear fit and alpha from fit
    A, B, alpha_fit = fit_alpha(R, t)
    print("Linear fit R = A + B*t")
    print(f"Intercept A = {A:.6e} ohm")
    print(f"Slope B = {B:.6e} ohm/degC")
    print(f"Alpha from fit = B/A = {alpha_fit:.6e}\n")

    # 3) plot
    ts = np.linspace(min(t) - 5, max(t) + 5, 200)
    Rs_fit = A + B * ts

    plt.figure(figsize=(6, 4))
    plt.plot(t, R, 'o', label='data')
    plt.plot(ts, Rs_fit, '-', label=f'fit: R={A:.4e}+{B:.4e}t')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Resistance (Ω)')
    plt.title('R vs T and linear fit')
    plt.legend()
    plt.grid(True)
    plt.annotate(f"alpha_mean={alpha_mean:.3e}\nalpha_fit={alpha_fit:.3e}", xy=(0.02, 0.95), xycoords='axes fraction',
                 va='top')
    plt.tight_layout()
    plt.savefig('R_vs_T_fit.png', dpi=200)
    print("Plot saved to R_vs_T_fit.png")


if __name__ == '__main__':
    main()
