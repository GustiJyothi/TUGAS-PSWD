import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Input sinyal
hn = input("Masukan Sinyal (pisahkan nilai dengan koma): ")
hn = [float(x) for x in hn.split(",")]

# Range n
n = np.arange(len(hn))

# Fungsi untuk plotting zero-pole diagram (zplane)
def zplane(b):
    zeros, poles, _ = signal.tf2zpk(b, [1])  # Menghitung zero-pole untuk sistem FIR
    plt.figure()
    plt.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
    plt.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
    unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='dashed')
    plt.gca().add_artist(unit_circle)
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.legend()
    plt.title("Zero-Pole Plot")
    plt.grid()
    plt.show()

# Plot zplane untuk hn
zplane(hn)
