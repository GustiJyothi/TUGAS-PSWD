import numpy as np
from scipy.signal import freqz, convolve2d
import matplotlib.pyplot as plt
from scipy.io import loadmat, wavfile
from sympy import symbols, summation, KroneckerDelta, oo
from scipy import signal
from scipy.io.wavfile import write
import sounddevice as sd
import streamlit as st

# **1. Bentuk Sinyal**
def plot_frequency_response(hn):
    hn = np.array(hn)  # Mengonversi input menjadi array numpy
    w, h = freqz(hn)

    # Membuat plot
    fig, ax = plt.subplots()
    ax.plot(w, 20 * np.log10(abs(h)), 'b')
    ax.set_title('Respons Frekuensi')
    ax.set_xlabel('Frekuensi (rad/sample)')
    ax.set_ylabel('Magnitude (dB)')
    ax.grid()

    # Menampilkan plot di Streamlit
    st.pyplot(fig)  # Menggunakan objek 'fig' yang sudah dibuat

# **2. ECG Processing**
def process_ecg(file_path, fs, G, fft_fs):
    data = loadmat(file_path)
    if 'ecg' in data:
        ecg = data['ecg'].flatten()
    else:
        raise ValueError(f"File {file_path} tidak mengandung variabel 'ecg'.")
    
    # Normalisasi dan pemrosesan sinyal ECG
    ecg = ecg / G
    ecg = (ecg - np.mean(ecg)) / np.std(ecg)

    # Waktu untuk plotting
    t = np.arange(0, len(ecg) / fs, 1 / fs)

    # Membuat plot ECG dalam domain waktu
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, ecg)
    ax.set_xlim([0, 4])
    ax.set_xlabel('Waktu (s)')
    ax.set_ylabel('Amplitudo (mV)')
    ax.set_title('ECG dalam Domain Waktu')
    ax.grid(True)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

    # FFT untuk domain frekuensi
    F = np.fft.fft(ecg)
    F = np.abs(F[:len(F)//2]) / np.max(F)
    f = np.linspace(0, fft_fs / 2, len(F))

    # Membuat plot ECG dalam domain frekuensi
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.plot(f, F)
    ax2.set_xlabel('Frekuensi (Hz)')
    ax2.set_ylabel('Magnitude Normalisasi')
    ax2.set_title('ECG dalam Domain Frekuensi')
    ax2.grid(True)

    # Menampilkan plot frekuensi di Streamlit
    st.pyplot(fig2)

# **3. Membuat dan Memutar Lagu**
def create_song(output_path, fs=8000):
    t1 = np.arange(0, 0.70, 1/fs)
    t5 = np.arange(0, 1, 1/fs)
    g1 = np.sin(2 * np.pi * 392.0 * t1)
    e1 = np.sin(2 * np.pi * 659.3 * t1)
    d1 = np.sin(2 * np.pi * 587.3 * t1)
    c2 = np.sin(2 * np.pi * 523.3 * t5)
    nol = np.zeros_like(t1)
    lagu = np.concatenate((g1, e1, d1, c2, nol))
    bintangkecil = np.int16(lagu * 32767)
    write(output_path, fs, bintangkecil)
    sd.play(bintangkecil, fs)
    sd.wait()

# **4. Fourier Transform for Audio**
def plot_audio_fft(audio_path):
    Fs, audio = wavfile.read(audio_path)
    
    # Memastikan audio dalam bentuk mono
    if len(audio.shape) > 1:
        audio = audio[:, 0]
    
    # Hitung FFT
    F = np.fft.fft(audio)
    F = np.abs(F[:len(F)//2]) / np.max(F)  # Ambil separuh dari hasil FFT (dari 0 ke Nyquist)
    f = np.linspace(0, Fs/2, len(F))  # Rentang frekuensi untuk plot

    # Membuat plot FFT
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(f, F)
    ax.set_xlabel('Frekuensi (Hz)')
    ax.set_ylabel('Magnitude Normalisasi')
    ax.set_title('Spektrum Frekuensi Audio')
    ax.grid(True)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# **5. Penyesuaian Sinyal**
def zplane(b):
    # Hitung zeros dan poles menggunakan tf2zpk
    zeros, poles, _ = signal.tf2zpk(b, [1])

    # Membuat plot
    fig, ax = plt.subplots()
    ax.scatter(np.real(zeros), np.imag(zeros), marker='o', color='b', label='Zeros')
    ax.scatter(np.real(poles), np.imag(poles), marker='x', color='r', label='Poles')
    
    # Menambahkan lingkaran satuan
    unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='dashed')
    ax.add_artist(unit_circle)

    # Menyempurnakan tampilan plot
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    ax.legend()
    ax.set_title("Zero-Pole Plot")
    ax.grid(True)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

# **6. Z-Transform**
def manual_z_transform(f, n, z):
    return summation(f * z**(-n), (n, 0, oo))

def z_transform_examples():
    n, z = symbols('n z')
    f = 1**n
    f1 = 2**n
    f2 = KroneckerDelta(n, 0)
    f3 = 5 * KroneckerDelta(n, 0)
    
    result1 = manual_z_transform(f, n, z)
    result2 = manual_z_transform(f1, n, z)
    result3 = manual_z_transform(f2, n, z)
    result4 = manual_z_transform(f3, n, z)
    
    st.write("Z-Transform of 1^n:", result1)
    st.write("Z-Transform of 2^n:", result2)
    st.write("Z-Transform of KroneckerDelta:", result3)
    st.write("Z-Transform of 5 * KroneckerDelta:", result4)

# **7. Plotting**
def plot_song_frequencies(signals, fs, frequencies, titles):
    fig, axes = plt.subplots(len(signals), 1, figsize=(10, 10))
    
    # Loop untuk setiap sinyal dan menghitung frekuensi
    for i in range(len(signals)):
        N = len(signals[i])
        t_total = np.arange(0, N) / fs
        freq_count = np.zeros_like(frequencies)

        for j, freq in enumerate(frequencies):
            wave = np.sin(2 * np.pi * freq * t_total)
            freq_count[j] = np.abs(np.sum(signals[i] * wave))  # Hitung kontribusi frekuensi

        axes[i].stem(frequencies, freq_count)
        axes[i].set_xlabel('Frekuensi (Hz)')
        axes[i].set_ylabel('Magnitude')
        axes[i].set_title(f'Frekuensi Dominan untuk {titles[i]}')
        axes[i].grid(True)
    
    plt.tight_layout()
    st.pyplot(fig)
