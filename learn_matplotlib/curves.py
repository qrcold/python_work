import numpy as np
import matplotlib.pyplot as plt


def generate_input_waveform(frequency_hz: float = 50.0, cycles: float = 4.0, points: int = 4000):
    """Generate a normalized sine-wave input signal."""
    period = 1.0 / frequency_hz
    time = np.linspace(0.0, cycles * period, points)
    input_signal = np.sin(2.0 * np.pi * frequency_hz * time)
    return time, input_signal


def half_wave_rectify(signal: np.ndarray) -> np.ndarray:
    return np.maximum(signal, 0.0)


def full_wave_rectify(signal: np.ndarray) -> np.ndarray:
    return np.abs(signal)


def bridge_rectify(signal: np.ndarray) -> np.ndarray:
    return np.abs(signal)


def capacitor_filter(rectified_signal: np.ndarray, dt: float, tau: float) -> np.ndarray:
    """Ideal-diode capacitor filter with exponential discharge between peaks."""
    output = np.empty_like(rectified_signal)
    output[0] = rectified_signal[0]

    for index in range(1, len(rectified_signal)):
        discharge_value = output[index - 1] * np.exp(-dt / tau)
        output[index] = rectified_signal[index] if rectified_signal[index] >= discharge_value else discharge_value

    return output


def plot_rectification_curves() -> None:
    time, input_signal = generate_input_waveform()
    dt = time[1] - time[0]

    half_output = half_wave_rectify(input_signal)
    full_output = full_wave_rectify(input_signal)
    bridge_output = bridge_rectify(input_signal)

    capacitor_values_uF = [47.0, 100.0, 470.0]
    load_resistance_ohm = 1000.0
    filtered_outputs = []
    for capacitor_uF in capacitor_values_uF:
        tau = load_resistance_ohm * capacitor_uF * 1e-6
        filtered_outputs.append(capacitor_filter(bridge_output, dt, tau))

    fig, axes = plt.subplots(2, 3, figsize=(15, 8), layout='constrained')

    top_row = [
        ('Half-wave rectifier', half_output),
        ('Full-wave rectifier', full_output),
        ('Bridge rectifier', bridge_output),
    ]

    for axis, (title, output_signal) in zip(axes[0], top_row):
        axis.plot(time * 1000.0, input_signal, color='0.75', linewidth=1.2, label='Input')
        axis.plot(time * 1000.0, output_signal, color='#1f77b4', linewidth=2.0, label='Output')
        axis.set_title(title)
        axis.axis('off')
        axis.legend(fontsize=8)

    for axis, capacitor_uF, filtered_signal in zip(axes[1], capacitor_values_uF, filtered_outputs):
        axis.plot(time * 1000.0, bridge_output, color='0.75', linewidth=1.2, label='Rectified input')
        axis.plot(time * 1000.0, filtered_signal, color='#d62728', linewidth=2.0, label=f'Output with C = {capacitor_uF:g} μF')
        axis.set_title(f'Bridge rectifier + capacitor filter ({capacitor_uF:g} μF)')
        axis.axis('off')
        axis.legend(fontsize=8)

    fig.suptitle('Rectification Input and Output Waveforms', fontsize=14)
    plt.savefig('rectifier_waveforms.png', dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    plot_rectification_curves()
