import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk input sinyal diskrit
def input_sinyal(prompt):
    while True:
        sinyal_in = input(prompt)
        if sinyal_in.strip():  # Memastikan input tidak kosong
            try:
                return np.array([float(i) for i in sinyal_in.split()])
            except ValueError:
                print("Input tidak valid, coba lagi.")
        else:
            print("Input tidak boleh kosong, coba lagi.")

# Mendapatkan input dari pengguna untuk sinyal x1 dan x2
x1 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x1, dipisahkan dengan spasi (misalnya -1 0 1 2 3): ")
x2 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x2, dipisahkan dengan spasi (misalnya -1 0 1 2 3): ")

# Mendefinisikan indeks n dari 0 hingga panjang sinyal x1
n = np.arange(0, len(x1))

# Melakukan perkalian sinyal x1 dan x2
x_product = x1 * x2  # Perkalian elemen-wise

# Plot sinyal x1, x2, dan hasil perkaliannya
plt.figure(figsize=(15, 5))

# Plot sinyal x1
plt.subplot(1, 3, 1)
plt.stem(n, x1, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Sinyal x1(n)')
plt.xlabel('n')
plt.ylabel('x1(n)')
plt.grid()

# Plot sinyal x2
plt.subplot(1, 3, 2)
plt.stem(n, x2, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('Sinyal x2(n)')
plt.xlabel('n')
plt.ylabel('x2(n)')
plt.grid()

# Plot hasil perkalian sinyal
plt.subplot(1, 3, 3)
plt.stem(n, x_product, linefmt='g-', markerfmt='go', basefmt='b-')
plt.title('Hasil Perkalian x1(n) . x2(n)')
plt.xlabel('n')
plt.ylabel('x1(n) . x2(n)')
plt.grid()

# Menampilkan plot
plt.tight_layout()
plt.show()
