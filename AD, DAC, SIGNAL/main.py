import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# INPUT SINYAL DISKRIT
def input_sinyal(prompt):
    while True:
        sinyal_in = input(prompt)
        if sinyal_in.strip():  
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

# Fungsi untuk melakukan time shifting
def time_shift(sinyal, k):
    shift = abs(k)
    if shift > len(sinyal):
        shift = len(sinyal)  # Pastikan pergeseran tidak melebihi panjang sinyal
    
    if k >= 0:
        return np.concatenate((np.zeros(shift), sinyal))[:len(sinyal)]  # Pergeseran ke kanan
    else:
        return np.concatenate((sinyal, np.zeros(shift)))[:len(sinyal)]  # Pergeseran ke kiri

# Input sinyal dari pengguna
x1 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x1, dipisahkan dengan spasi: ")
x2 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x2, dipisahkan dengan spasi: ")

# Menentukan panjang sinyal terpanjang untuk penanganan sinyal dengan panjang berbeda
max_len = max(len(x1), len(x2))
x1 = np.pad(x1, (0, max_len - len(x1)), mode='constant')
x2 = np.pad(x2, (0, max_len - len(x2)), mode='constant')
n = np.arange(0, max_len)

# Loop untuk menu pilihan
while True:
    print("\nPilih operasi yang ingin dilakukan:")
    print("1. Normalisasi Sinyal")
    print("2. Penjumlahan Sinyal")
    print("3. Pengurangan Sinyal")
    print("4. Perkalian Sinyal")
    print("5. Time Reversal")
    print("6. Time Scaling")
    print("7. Amplitude Scaling")
    print("8. Time Shifting")
    print("9. Keluar")

    choice = input("Masukkan nomor pilihan: ")

    if choice == "1":
        # Normalisasi sinyal
        x1_norm = normalisasi(x1)
        x2_norm = normalisasi(x2)

        # Plot hasil normalisasi
        plt.figure()
        ax = plt.gca()
        plt.stem(n, x1_norm, markerfmt='bo', linefmt='b--', basefmt='r-')
        label_batang(ax, n, x1_norm)
        plt.title('Sinyal x1(n) Normalisasi')
        plt.xlabel('n')
        plt.ylabel('x1(n)')
        plt.grid()
        plt.show()

    elif choice == "2":
        # Penjumlahan sinyal
        x_sum_norm = normalisasi(x1) + normalisasi(x2)
        
        # Plot hasil penjumlahan
        plt.figure()
        ax = plt.gca()
        plt.stem(n, x_sum_norm, markerfmt='gd', linefmt='g:', basefmt='b-')
        label_batang(ax, n, x_sum_norm)
        plt.title('Penjumlahan Normalisasi x1(n) + x2(n)')
        plt.xlabel('n')
        plt.ylabel('x1(n) + x2(n)')
        plt.grid()
        plt.show()

    elif choice == "3":
        # Pengurangan sinyal
        x_sub = x1 - x2
        
        # Plot hasil pengurangan
        plt.figure()
        ax = plt.gca()
        plt.stem(n, x_sub, markerfmt='mo', linefmt='m--', basefmt='k-')
        label_batang(ax, n, x_sub)
        plt.title('Pengurangan x1(n) - x2(n)')
        plt.xlabel('n')
        plt.ylabel('x1(n) - x2(n)')
        plt.grid()
        plt.show()

    elif choice == "4":
        # Perkalian sinyal
        x_product = x1 * x2
        
        # Plot hasil perkalian
        plt.figure()
        ax = plt.gca()
        plt.stem(n, x_product, markerfmt='co', linefmt='c--', basefmt='k-')
        label_batang(ax, n, x_product)
        plt.title('Perkalian x1(n) * x2(n)')
        plt.xlabel('n')
        plt.ylabel('x1(n) * x2(n)')
        plt.grid()
        plt.show()

    elif choice == "5":
        # Time reversal pada sinyal
        x1_reversed = time_reversal(normalisasi(x1))
        
        # Plot hasil time reversal
        plt.figure()
        ax = plt.gca()
        plt.stem(n, x1_reversed, markerfmt='bo', linefmt='b--', basefmt='r-')
        label_batang(ax, n, x1_reversed)
        plt.title('Time Reversal x1(n)')
        plt.xlabel('n')
        plt.ylabel('x1(-n)')
        plt.grid()
        plt.show()

    elif choice == "6":
        # Time scaling
        scaling_factor_time = float(input('Masukkan faktor skala waktu (contoh: 0.5 untuk upscaling, 2 untuk downscaling): '))
        n_scaled = n * (1 / scaling_factor_time)
        n_interp = np.linspace(np.min(n_scaled), np.max(n_scaled), num=len(n_scaled))
        interp_function = interp1d(n_scaled, normalisasi(x1), kind='linear', fill_value=0, bounds_error=False)
        x1_scaled_time = interp_function(n_interp)

        # Plot hasil time scaling
        plt.figure()
        ax = plt.gca()
        plt.stem(n_interp, x1_scaled_time, markerfmt='gs', linefmt='g-.', basefmt='k-')
        label_batang(ax, n_interp, x1_scaled_time)
        plt.title(f'Time Scaling x1(n) dengan faktor {scaling_factor_time}')
        plt.xlabel('n')
        plt.ylabel('x1(scaled)')
        plt.grid()
        plt.show()

    elif choice == "7":
        # Amplitude scaling
        scaling_factor_amp = float(input('Masukkan faktor skala amplitudo (misalnya 2): '))
        y_amplitude_scaled_x1 = scaling_factor_amp * x1

        # Plot hasil amplitude scaling
        plt.figure()
        ax = plt.gca()
        plt.stem(n, y_amplitude_scaled_x1, markerfmt='bo', linefmt='b--', basefmt='r-')
        label_batang(ax, n, y_amplitude_scaled_x1)
        plt.title(f'Amplitude Scaling x1(n) * {scaling_factor_amp}')
        plt.xlabel('n')
        plt.ylabel(f'x1(n) * {scaling_factor_amp}')
        plt.grid()
        plt.show()

    elif choice == "8":
        # Time shifting
        k = int(input('Masukkan Nilai k untuk pergeseran waktu: '))
        y1_shifted = time_shift(x1, k)

        # Plot hasil time shifting
        plt.figure()
        ax = plt.gca()
        plt.stem(n, y1_shifted, markerfmt='co', linefmt='c--', basefmt='k-')
        label_batang(ax, n, y1_shifted)
        plt.title(f'Pergeseran Waktu x1(n) dengan k = {k}')
        plt.xlabel('n')
        plt.ylabel('y1(n)')
        plt.grid()
        plt.show()

    elif choice == "9":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
