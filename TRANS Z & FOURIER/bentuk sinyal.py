import numpy as np
from scipy.signal import freqz
import matplotlib.pyplot as plt

# Meminta input bentuk sinyal dari pengguna
hn = input("Masukkan bentuk sinyal (gunakan tanda kurung siku untuk nilai ganda, misalnya [1, 0.5, 0.25]): ")
hn = np.array(eval(hn))  # Mengonversi input string menjadi array numpy

# Menentukan rentang nilai n
n = np.arange(len(hn))

# Menghitung respons frekuensi
w, h = freqz(hn)

# Plot respons frekuensi
plt.figure()
plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.title('Respons Frekuensi')
plt.xlabel('Frekuensi (rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.show()
