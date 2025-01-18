import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Membaca file audio
Fs, bintangkecil = wavfile.read('TRANS Z & FOURIER\Bintang Kecil.wav')  # Fs adalah frekuensi sampling

# Terapkan FFT pada data audio
F = np.fft.fft(bintangkecil)  # melakukan FFT pada data audio
F = np.abs(F)  # mengambil nilai absolut dari FFT

# Ambil hanya setengah bagian positif dari spektrum frekuensi
F = F[:len(F)//2]

# Normalisasi rentang amplitudo ke 0-1
F = F / np.max(F)

# Mendapatkan panjang sinyal
L = len(F)

# Membuat vektor frekuensi
f = np.linspace(0, Fs/2, L)

# Plot spektrum frekuensi
plt.figure(figsize=(10, 6))
plt.plot(f, F)
plt.xlabel('Frekuensi (Hz)')
plt.ylabel('Magnitude Normalisasi')
plt.title('Spektrum Frekuensi dari Bintang Kecil')
plt.grid(True)
plt.show()
