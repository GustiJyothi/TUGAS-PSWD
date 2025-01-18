import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan sinyal x1 dan x2
x1_in = input('Masukkan nilai-nilai sinyal diskrit x1, dipisahkan dengan spasi (misalnya -1 0 1 2 3): ')
x2_in = input('Masukkan nilai-nilai sinyal diskrit x2, dipisahkan dengan spasi (misalnya -1 0 1 2 3): ')

# Mengubah input string menjadi array NumPy
x1 = np.array([float(i) for i in x1_in.split()])
x2 = np.array([float(i) for i in x2_in.split()])

# Mendefinisikan indeks n dari x1 dan x2
n1 = np.arange(len(x1))
n2 = np.arange(len(x2))

# Mengurangi sinyal x1 dan x2
# Menyesuaikan panjang sinyal untuk pengurangan
min_length = min(len(x1), len(x2))
x_sub = x1[:min_length] - x2[:min_length]

# Plot sinyal x1, x2, dan hasil pengurangannya
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(n1, x1, 'b', markerfmt='bo', basefmt=" ")
plt.title('Sinyal x1(n)')
plt.xlabel('n')
plt.ylabel('x1(n)')

plt.subplot(3, 1, 2)
plt.stem(n2, x2, 'r', markerfmt='ro', basefmt=" ")
plt.title('Sinyal x2(n)')
plt.xlabel('n')
plt.ylabel('x2(n)')

plt.subplot(3, 1, 3)
plt.stem(n1[:min_length], x_sub, 'g', markerfmt='go', basefmt=" ")
plt.title('Hasil Pengurangan x1(n) - x2(n)')
plt.xlabel('n')
plt.ylabel('x1(n) - x2(n)')

plt.tight_layout()
plt.show()
