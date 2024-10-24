import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk input sinyal diskrit dengan penanganan input negatif atau kosong
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

# Fungsi untuk normalisasi sinyal
def normalisasi(sinyal):
    min_val = np.min(sinyal)
    max_val = np.max(sinyal)
    return (sinyal - min_val) / (max_val - min_val) if max_val != min_val else sinyal

# Fungsi untuk menambahkan label nilai di atas batang plot
def label_batang(ax, x, y):
    for i, val in enumerate(y):
        ax.text(i, val, f'{val:.2f}', ha='center', va='bottom')

# Fungsi untuk melakukan time reversal
def time_reversal(sinyal):
    return np.flip(sinyal)

# Mendapatkan input dari pengguna
x1 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x1, dipisahkan dengan spasi: ")
x2 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x2, dipisahkan dengan spasi: ")

# Menentukan panjang sinyal terpanjang untuk penanganan sinyal dengan panjang berbeda
max_len = max(len(x1), len(x2))

# Pad x1 dan x2 jika panjangnya berbeda
x1 = np.pad(x1, (0, max_len - len(x1)), mode='constant')
x2 = np.pad(x2, (0, max_len - len(x2)), mode='constant')

# Mendefinisikan indeks n dari 0 hingga panjang sinyal terpanjang-1
n = np.arange(0, max_len)

# Normalisasi sinyal x1 dan x2
x1_norm = normalisasi(x1)
x2_norm = normalisasi(x2)

# Menjumlahkan sinyal setelah normalisasi
x_sum_norm = x1_norm + x2_norm

# Melakukan perkalian sinyal
x_product = x1 * x2

# Melakukan time reversal pada sinyal yang dinormalisasi dan hasil perkalian
x1_reversed = time_reversal(x1_norm)
x2_reversed = time_reversal(x2_norm)
x_sum_reversed = time_reversal(x_sum_norm)
x_product_reversed = time_reversal(x_product)

# Plot sinyal x1, x2, hasil penjumlahan, dan hasil perkalian
plt.figure(figsize=(18, 8))

# Plot sinyal x1 yang dinormalisasi
plt.subplot(3, 3, 1)
ax = plt.gca()
plt.stem(n, x1_norm, markerfmt='bo', linefmt='b--', basefmt='r-')
label_batang(ax, n, x1_norm)
plt.title('Sinyal x1(n) Normalisasi')
plt.xlabel('n')
plt.ylabel('x1(n)')
plt.grid()

# Plot sinyal x2 yang dinormalisasi
plt.subplot(3, 3, 2)
ax = plt.gca()
plt.stem(n, x2_norm, markerfmt='rs', linefmt='r-.', basefmt='k-')
label_batang(ax, n, x2_norm)
plt.title('Sinyal x2(n) Normalisasi')
plt.xlabel('n')
plt.ylabel('x2(n)')
plt.grid()

# Plot hasil penjumlahan sinyal yang dinormalisasi
plt.subplot(3, 3, 3)
ax = plt.gca()
plt.stem(n, x_sum_norm, markerfmt='gd', linefmt='g:', basefmt='b-')
label_batang(ax, n, x_sum_norm)
plt.title('Penjumlahan Normalisasi x1(n) + x2(n)')
plt.xlabel('n')
plt.ylabel('x1(n) + x2(n)')
plt.grid()

# Plot hasil perkalian sinyal
plt.subplot(3, 3, 4)
ax = plt.gca()
plt.stem(n, x_product, markerfmt='mo', linefmt='m--', basefmt='k-')
label_batang(ax, n, x_product)
plt.title('Hasil Perkalian x1(n) . x2(n)')
plt.xlabel('n')
plt.ylabel('x1(n) * x2(n)')
plt.grid()

# Plot sinyal x1 setelah time reversal
plt.subplot(3, 3, 5)
ax = plt.gca()
plt.stem(n, x1_reversed, markerfmt='bo', linefmt='b--', basefmt='r-')
label_batang(ax, n, x1_reversed)
plt.title('Time Reversal x1(n)')
plt.xlabel('n')
plt.ylabel('x1(-n)')
plt.grid()

# Plot sinyal x2 setelah time reversal
plt.subplot(3, 3, 6)
ax = plt.gca()
plt.stem(n, x2_reversed, markerfmt='rs', linefmt='r-.', basefmt='k-')
label_batang(ax, n, x2_reversed)
plt.title('Time Reversal x2(n)')
plt.xlabel('n')
plt.ylabel('x2(-n)')
plt.grid()

# Plot hasil penjumlahan sinyal yang dinormalisasi setelah time reversal
plt.subplot(3, 3, 7)
ax = plt.gca()
plt.stem(n, x_sum_reversed, markerfmt='gd', linefmt='g:', basefmt='b-')
label_batang(ax, n, x_sum_reversed)
plt.title('Time Reversal Penjumlahan x1(n) + x2(n)')
plt.xlabel('n')
plt.ylabel('x1(-n) + x2(-n)')
plt.grid()

# Plot hasil perkalian sinyal setelah time reversal
plt.subplot(3, 3, 8)
ax = plt.gca()
plt.stem(n, x_product_reversed, markerfmt='mo', linefmt='m--', basefmt='k-')
label_batang(ax, n, x_product_reversed)
plt.title('Time Reversal Perkalian x1(n) . x2(n)')
plt.xlabel('n')
plt.ylabel('x1(-n) * x2(-n)')
plt.grid()

# Tampilkan plot
plt.tight_layout()
plt.show()
