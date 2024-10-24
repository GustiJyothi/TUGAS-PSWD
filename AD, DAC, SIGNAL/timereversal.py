import numpy as np
import matplotlib.pyplot as plt

# Meminta input sinyal dari pengguna dalam bentuk string
x_str = input('Masukkan nilai-nilai sinyal diskrit x, dipisahkan dengan spasi (misalnya -1 0 1 2 3): ')

# Mengonversi string input menjadi array numerik
x = np.array([float(i) for i in x_str.split()])  # Menggunakan list comprehension

# Operasi time reversal y(n) = x(-n)
y = np.flip(x)  # Menggunakan fungsi flip dari NumPy untuk mencerminkan sinyal

# Indeks waktu untuk sinyal asli
n = np.arange(len(x))  # Array dari 0 sampai panjang sinyal x
n_reversed = -np.flip(n)  # Indeks waktu untuk sinyal pencerminan

# Membuat plot
plt.figure(figsize=(10, 6))

# Plot sinyal asli
plt.subplot(2, 1, 1)
plt.stem(n, x, basefmt=" ")  # Menggunakan stem plot tanpa use_line_collection
plt.title('Sinyal Asli x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.grid()

# Plot sinyal hasil pencerminan
plt.subplot(2, 1, 1)
plt.stem(n_reversed, y, basefmt=" ")  # Menggunakan stem plot tanpa use_line_collection
plt.title('Sinyal Hasil Pencerminan y(n) = x(-n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid()

# Menampilkan plot
plt.tight_layout()
plt.show()

