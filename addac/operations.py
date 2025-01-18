import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import streamlit as st  # Impor Streamlit

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

# Fungsi untuk menambahkan sinyal
def penjumlahan(x1, x2):
    return x1 + x2

# Fungsi untuk mengurangi sinyal
def pengurangan(x1, x2):
    return x1 - x2

# Fungsi untuk mengalikan sinyal
def perkalian(x1, x2):
    return x1 * x2

# Fungsi untuk time scaling
def time_scaling(x1, n, scaling_factor_time):
    n_scaled = n * (1 / scaling_factor_time)
    n_interp = np.linspace(np.min(n_scaled), np.max(n_scaled), num=len(n_scaled))
    interp_function = interp1d(n_scaled, normalisasi(x1), kind='linear', fill_value=0, bounds_error=False)
    return interp_function(n_interp)

# Fungsi untuk amplitude scaling
def amplitude_scaling(x1, scaling_factor_amp):
    return scaling_factor_amp * x1

# Fungsi untuk membuat plot dari operasi sinyal dan menampilkannya di Streamlit
def plot_sinyal(x, n, title, xlabel, ylabel):
    plt.figure()
    ax = plt.gca()
    plt.stem(n, x, markerfmt='bo', linefmt='b--', basefmt='r-')
    label_batang(ax, n, x)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    
    # Tampilkan plot di Streamlit
    st.pyplot(plt)
    plt.close()  # Tutup plot setelah ditampilkan di Streamlit
