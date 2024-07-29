import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parámetros
sampling_rate = 200*3  # Tasa de muestreo en Hz
duration = 1.0  # Duración en segundos
num_samples = int(sampling_rate * duration)  # Número de muestras

# Array de tiempo
t = np.linspace(0, duration, num_samples, endpoint=False)
print(f"{t}")

# Señal sinusoidal
frequency = 100  # Frecuencia de la señal en Hz
signal = np.sin(2 * np.pi * frequency * t)

# Realizar la FFT
signal_fft = fft(signal)

# Obtener las frecuencias correspondientes
freqs = fftfreq(len(signal), 1 / sampling_rate)

# Graficar la señal original
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title('Señal Sinusoidal de 100 Hz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.grid(True)

# Graficar la FFT
plt.subplot(1, 2, 2)
plt.plot(freqs, np.abs(signal_fft) / num_samples)  # Normalizar por el número de muestras
plt.title('Transformada de Fourier')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')
plt.grid(True)

# Limitar el eje x para mejor visualización
plt.xlim(0, 150)
plt.show()
##ALGO NUEVOasdasd