import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Memuat sinyal ECG dari file .mat
data = loadmat('TRANS Z & FOURIER\ecg.mat')  # Memuat file ECG yang sesuai

# Pastikan bahwa data ECG terdapat pada variabel 'ecg' dalam file .mat
if 'ecg' in data:
    ecg = data['ecg'].flatten()  # Ambil data ECG dan ratakan (flatten)
else:
    raise ValueError("File 'ecg.mat' tidak mengandung variabel 'ecg'.")

# Input frekuensi sampling dan faktor skalabilitas amplitudo
Fs = float(input('Frekuensi Sampling: '))  # 250 Hz
G = float(input('Skala Amplitudo: '))  # Faktor skalabilitas amplitudo, misalnya 2000

# Penyesuaian sinyal ECG
ecg = ecg / G  # Sesuaikan amplitudo
ecg = (ecg - np.mean(ecg)) / np.std(ecg)  # Normalisasi sinyal ECG
t = np.arange(0, len(ecg) / Fs, 1 / Fs)  # Membuat vektor waktu dengan durasi sesuai panjang sinyal

# Plot sinyal ECG dalam domain waktu
plt.figure(figsize=(10, 6))
plt.plot(t, ecg)
plt.xlim([0, 4])  # Fokus pada 4 detik pertama
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo (mV)')
plt.title('ECG dalam Domain Waktu')
plt.grid(True)
plt.show()

# FFT - Transformasi Fourier
Fs_fft = float(input('Frekuensi Sampling FFT: '))  # Frekuensi sampling untuk FFT

F = np.fft.fft(ecg)  # Hitung FFT dari sinyal ECG
F = np.abs(F)  # Ambil nilai absolut dari FFT
F = F[:len(F)//2]  # Ambil hanya setengah spektrum positif
F = F / np.max(F)  # Normalisasi amplitudo antara 0 dan 1

L = len(F)  # Panjang sinyal dalam domain frekuensi
f = np.linspace(0, Fs_fft / 2, L)  # Membuat vektor frekuensi

# Plot hasil spektrum frekuensi
plt.figure(figsize=(10, 6))
plt.plot(f, F)
plt.xlabel('Frekuensi (Hz)')
plt.ylabel('Magnitude Normalisasi')
plt.title('ECG dalam Domain Frekuensi')
plt.grid(True)
plt.show()
