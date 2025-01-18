import numpy as np
from scipy.io.wavfile import write

# Meminta input frekuensi sampling dari pengguna, default 8000 Hz
fs = int(input('Frekuensi Sampling (Hz): ') or 8000)

# Waktu untuk masing-masing nada
t1 = np.arange(0, 0.70, 1/fs)
t2 = np.arange(0, 0.75, 1/fs)
t3 = np.arange(0, 0.25, 1/fs)
t4 = np.arange(0, 2, 1/fs)
t5 = np.arange(0, 1, 1/fs)

# Membuat gelombang sinus untuk masing-masing nada
c1 = np.sin(2 * np.pi * 523.3 * t1)
c2 = np.sin(2 * np.pi * 523.3 * t5)
d1 = np.sin(2 * np.pi * 587.3 * t1)
d2 = np.sin(2 * np.pi * 587.3 * t5)
e1 = np.sin(2 * np.pi * 659.3 * t1)
f1 = np.sin(2 * np.pi * 698.5 * t1)
g1 = np.sin(2 * np.pi * 392.0 * t1)
g2 = np.sin(2 * np.pi * 392.0 * t5)
g3 = np.sin(2 * np.pi * 785.0 * t1)
a = np.sin(2 * np.pi * 440.0 * t1)
a3 = np.sin(2 * np.pi * 440.0 * t5)
b = np.sin(2 * np.pi * 493.9 * t1)

# Membuat nol (array dengan semua nilai nol)
nol = np.zeros_like(t1)

# Menggabungkan nada menjadi lagu
lagu1 = np.concatenate((g1, e1, d1, c2, nol, b, d1, c1, b, a, g2, nol))
lagu2 = np.concatenate((a, b, c1, g2, nol, c1, e1, g3, d1, c2, d2, nol))
lagu3 = np.concatenate((g3, e1, d1, c2, nol, e1, g3, e1, d1, c1, a3, nol))
lagu4 = np.concatenate((a, c1, a, g2, nol, g1, e1, f1, d1, a, b, c1))

# Menggabungkan semua lagu
bintangkecil = np.concatenate((lagu1, lagu2, lagu3, lagu4))

# Mengubah ke format 16-bit integer
bintangkecil_int16 = np.int16(bintangkecil * 32767)

# Menyimpan file audio
filename = 'TRANS Z & FOURIER\Bintang Kecil.wav'
write(filename, fs, bintangkecil_int16)

# Memutar suara (hanya di Jupyter Notebook atau lingkungan lain yang mendukung)
import sounddevice as sd
sd.play(bintangkecil, fs)
sd.wait()  # Tunggu sampai suara selesai diputar
