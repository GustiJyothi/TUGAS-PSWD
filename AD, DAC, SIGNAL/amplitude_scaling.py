import numpy as np
import matplotlib.pyplot as plt

# Meminta input sinyal dari pengguna
x_in = input('Masukkan nilai-nilai sinyal diskrit x, dipisahkan dengan spasi (misalnya -1 0 1 2 3): ')
x = np.array(list(map(float, x_in.split())))  # Mengonversi input string menjadi array numerik

# Indeks sampel untuk sinyal asli
n = np.arange(len(x))  # Indeks waktu/sampel sinyal asli

# Meminta scaling factor dari pengguna
scaling_factor = float(input('Masukkan faktor skala amplitudo (misalnya 2): '))

# Mengalikan sinyal dengan faktor skala amplitudo
y_amplitude_scaled = scaling_factor * x

# Plot Sinyal
plt.figure()

# Plot Sinyal Asli
plt.subplot(2, 1, 1)
plt.stem(n, x, basefmt=" ")  # 'basefmt' menghapus garis dasar
plt.title('Sinyal Asli')
plt.xlabel('Indeks Sampel')
plt.ylabel('Amplitudo')
plt.grid()

# Plot Sinyal dengan Amplitude Scaling
plt.subplot(2, 1, 2)
plt.stem(n, y_amplitude_scaled, basefmt=" ")  # 'basefmt' menghapus garis dasar
plt.title('Sinyal dengan Amplitude Scaling')
plt.xlabel('Indeks Sampel')
plt.ylabel('Amplitudo')
plt.grid()

plt.tight_layout()  # Mengatur layout agar tidak tumpang tindih
plt.show()
