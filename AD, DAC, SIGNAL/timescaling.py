import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Meminta input sinyal diskrit
x_in = input('Masukkan nilai-nilai sinyal diskrit x, dipisahkan dengan spasi (misalnya -1 0 1 2 3): ')
x = np.array([float(i) for i in x_in.split()])
n = np.arange(len(x))  # Indeks waktu diskrit

# Meminta input scaling factor dari pengguna
scaling_factor = float(input('Masukkan nilai penskalaan (contoh: 0.5 untuk upscaling, 2 untuk downscaling): '))

# Time Scaling
n_scaled = n * (1 / scaling_factor)
n_interp = np.linspace(np.min(n_scaled), np.max(n_scaled), num=len(n_scaled))
interpolation_function = interp1d(n_scaled, x, kind='linear', fill_value=0, bounds_error=False)
x_scaled = interpolation_function(n_interp)

# Plot sinyal asli dan sinyal hasil scaling
fig, axs = plt.subplots(2, 1, figsize=(8, 6))

# Plot sinyal asli
axs[0].stem(n, x, markerfmt='o')
axs[0].set_title('Original Discrete Signal')
axs[0].set_xlabel('n')
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)

# Plot sinyal hasil scaling
axs[1].stem(n_interp, x_scaled, markerfmt='o')
axs[1].set_title(f'Time-Scale Sinyal Diskrit (Scaling Factor: {scaling_factor})')
axs[1].set_xlabel('n')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)

plt.tight_layout()
plt.show()
