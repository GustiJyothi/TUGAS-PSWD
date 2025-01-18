import numpy as np
import matplotlib.pyplot as plt

# Parameter
fs = float(input('Frekuensi Sampling (Hz): '))  # default Sampling frequency is 8000
t1 = np.arange(0, 0.70, 1/fs)
t2 = np.arange(0, 0.75, 1/fs)
t3 = np.arange(0, 0.25, 1/fs)
t4 = np.arange(0, 2, 1/fs)
t5 = np.arange(0, 1, 1/fs)

# Nada dengan amplitudo 0.5
c1 = 0.5 * np.sin(2 * np.pi * 523.3 * t1)
c2 = 0.5 * np.sin(2 * np.pi * 523.3 * t5)
d1 = 0.5 * np.sin(2 * np.pi * 587.3 * t1)
d2 = 0.5 * np.sin(2 * np.pi * 587.3 * t5)
e1 = 0.5 * np.sin(2 * np.pi * 659.3 * t1)
f1 = 0.5 * np.sin(2 * np.pi * 698.5 * t1)
g1 = 0.5 * np.sin(2 * np.pi * 392.0 * t1)
g2 = 0.5 * np.sin(2 * np.pi * 392.0 * t5)
g3 = 0.5 * np.sin(2 * np.pi * 785 * t1)
a = 0.5 * np.sin(2 * np.pi * 440 * t1)
a3 = 0.5 * np.sin(2 * np.pi * 440 * t5)
b = 0.5 * np.sin(2 * np.pi * 493.9 * t1)
nol = np.zeros_like(t1)

# Sinyal lagu
lagu1 = np.concatenate([g1, e1, d1, c2, nol, b, d1, c1, b, a, g2, nol])
lagu2 = np.concatenate([a, b, c1, g2, nol, c1, e1, g3, d1, c2, d2, nol])
lagu3 = np.concatenate([g3, e1, d1, c2, nol, e1, g3, e1, d1, c1, a3, nol])
lagu4 = np.concatenate([a, c1, a, g2, nol, g1, e1, f1, d1, a, b, c1])

# Frekuensi masing-masing nada
frequencies = np.array([392, 440, 493.9, 523.3, 587.3, 659.3, 698.5, 785])

# Kombinasikan sinyal-sinyal lagu
signals = [lagu1, lagu2, lagu3, lagu4]
titles = ['Lagu 1', 'Lagu 2', 'Lagu 3', 'Lagu 4']

# Plot frekuensi untuk setiap lagu
plt.figure(figsize=(10, 10))
for i in range(4):
    plt.subplot(4, 1, i + 1)
    
    # Hitung durasi dan jumlah sampel
    N = len(signals[i])
    t_total = np.arange(0, N) / fs
    
    # Temukan frekuensi dominan untuk setiap lagu   
    freq_count = np.zeros_like(frequencies)
    for j in range(len(frequencies)):
        # Hitung amplitudo rata-rata pada frekuensi tertentu
        freq = frequencies[j]
        wave = np.sin(2 * np.pi * freq * t_total)
        correlation = np.abs(np.sum(signals[i] * wave))
        freq_count[j] = correlation
    
    # Plot menggunakan stem
    plt.stem(frequencies, freq_count,)
    plt.xlabel('Frekuensi (Hz)')
    plt.ylabel('Magnitude')
    plt.title(f'Frekuensi Dominan untuk {titles[i]}')
    plt.xlim([0, 800])  # Sesuaikan dengan rentang frekuensi yang relevan
    plt.grid(True)

plt.tight_layout()
plt.show()
