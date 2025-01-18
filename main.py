import streamlit as st
import numpy as np
from addac.operations import normalisasi, time_reversal, time_shift, penjumlahan, pengurangan, perkalian, time_scaling, amplitude_scaling, plot_sinyal
from SWD.convolution import konvolusi  # Import the convolution function
from filter.filtering import Equalizer, HighPassFilter, LowPassFilter, ResponseSystem
import cv2
from PIL import Image
from scipy.signal import convolve2d
import soundfile as sf
from tranz.TransZ import (
    plot_frequency_response,
    process_ecg,
    create_song,
    plot_audio_fft,
    zplane,
    z_transform_examples,
    plot_song_frequencies,
    manual_z_transform
)
from scipy.io import wavfile
from sympy import symbols, KroneckerDelta, oo


# Input sinyal
def input_sinyal(prompt):
    sinyal_in = st.text_input(prompt)
    if sinyal_in:
        try:
            return np.array([float(i) for i in sinyal_in.split()])
        except ValueError:
            st.error("Input tidak valid. Pastikan hanya angka dipisahkan oleh spasi.")
    return None

# Menentukan panjang sinyal terpanjang
def prepare_sinyal(x1, x2):
    max_len = max(len(x1), len(x2))
    x1 = np.pad(x1, (0, max_len - len(x1)), mode='constant')
    x2 = np.pad(x2, (0, max_len - len(x2)), mode='constant')
    n = np.arange(0, max_len)
    return x1, x2, n

# Streamlit interface
st.title("Operasi Sinyal Diskrit")

# Pilihan menu halaman
page = st.selectbox("Pilih Halaman", ["Operasi Sinyal", "Konvolusi", "Equalizer", "Image Filters", "Frequency Response", "Plot Frequency Response", "ECG Processing", "Create and Play Song", "Plot Audio FFT", "Zero-Pole Plot", "Plot Song Frequencies", "Z-Transform"])

# Halaman Operasi Sinyal
if page == "Operasi Sinyal":
    # Input sinyal x1 dan x2
    x1 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x1 (misalnya 1 2 3): ")
    x2 = input_sinyal("Masukkan nilai-nilai sinyal diskrit x2 (misalnya 4 5 6): ")

    if x1 is not None and x2 is not None:
        x1, x2, n = prepare_sinyal(x1, x2)

        # Menu pilihan operasi
        operation = st.selectbox(
            "Pilih operasi:",
            ["Normalisasi", "Penjumlahan", "Pengurangan", "Perkalian", "Time Reversal", "Time Scaling", "Amplitude Scaling", "Time Shifting"]
        )

        if operation == "Normalisasi":
            x1_norm = normalisasi(x1)
            x2_norm = normalisasi(x2)
            plot_sinyal(x1_norm, n, 'Normalisasi x1(n)', 'n', 'x1(n)')
            plot_sinyal(x2_norm, n, 'Normalisasi x2(n)', 'n', 'x2(n)')

        elif operation == "Penjumlahan":
            x_sum = penjumlahan(x1, x2)
            plot_sinyal(x_sum, n, 'Penjumlahan x1(n) + x2(n)', 'n', 'x1(n) + x2(n)')

        elif operation == "Pengurangan":
            x_sub = pengurangan(x1, x2)
            plot_sinyal(x_sub, n, 'Pengurangan x1(n) - x2(n)', 'n', 'x1(n) - x2(n)')

        elif operation == "Perkalian":
            x_product = perkalian(x1, x2)
            plot_sinyal(x_product, n, 'Perkalian x1(n) * x2(n)', 'n', 'x1(n) * x2(n)')

        elif operation == "Time Reversal":
            x1_reversed = time_reversal(x1)
            plot_sinyal(x1_reversed, n, 'Time Reversal x1(n)', 'n', 'x1(-n)')

        elif operation == "Time Scaling":
            scaling_factor_time = st.number_input('Masukkan faktor skala waktu', value=1.0, min_value=0.1, max_value=10.0)
            x1_scaled = time_scaling(x1, n, scaling_factor_time)
            plot_sinyal(x1_scaled, n, f'Time Scaling x1(n) dengan faktor {scaling_factor_time}', 'n', 'x1(scaled)')

        elif operation == "Amplitude Scaling":
            scaling_factor_amp = st.number_input('Masukkan faktor skala amplitudo', value=1.0, min_value=0.1, max_value=10.0)
            x1_scaled_amp = amplitude_scaling(x1, scaling_factor_amp)
            plot_sinyal(x1_scaled_amp, n, f'Amplitude Scaling x1(n) * {scaling_factor_amp}', 'n', 'x1(n) * factor')

        elif operation == "Time Shifting":
            k = st.number_input('Masukkan nilai k untuk pergeseran waktu', value=0, min_value=-len(x1), max_value=len(x1))
            x1_shifted = time_shift(x1, k)
            plot_sinyal(x1_shifted, n, f'Pergeseran Waktu x1(n) dengan k={k}', 'n', 'x1(n) shifted')

    else:
        st.warning("Silakan masukkan sinyal terlebih dahulu untuk melanjutkan operasi.")

# Halaman Konvolusi
elif page == "Konvolusi":
    # Input sinyal
    xn = input_sinyal("Masukkan nilai-nilai sinyal pertama (misalnya 1 -1): ")
    hn = input_sinyal("Masukkan nilai-nilai sinyal kedua (misalnya 1 -2 3): ")

    if xn is not None and hn is not None:
        konvolusi(xn, hn)
    else:
        st.warning("Silakan masukkan kedua sinyal terlebih dahulu untuk melanjutkan konvolusi.")

if page == "Equalizer":
    st.header("3-Band Equalizer")
    file = st.file_uploader("Upload a WAV File", type=["wav"])

    if file:
        audio, fs = sf.read(file)
        equalizer = Equalizer(fs, audio)

        gains = [st.slider(f"Gain for Band {i+1}", 0.0, 1.0, 0.5) for i in range(3)]
        volume = st.slider("Volume", 0.0, 1.0, 1.0)

        if st.button("Play Equalized Audio"):
            processed_audio = equalizer.apply_equalizer(gains, volume)
            equalizer.play_audio(processed_audio)

if page == "Image Filters":
    st.header("Image High-Pass and Low-Pass Filters")
    file = st.file_uploader("Upload an Image", type=["jpg", "png", "bmp"])

    if file:
        image = Image.open(file)
        image_np = np.array(image)
        gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

        filter_type = st.radio("Filter Type", ["High-Pass", "Low-Pass"])
        kernel = np.array([[st.number_input(f"Kernel Row {i+1}, Col {j+1}", value=0.0) for j in range(3)] for i in range(3)])

        if filter_type == "High-Pass":
            result = HighPassFilter.apply_hpf(gray, kernel)
        else:
            result = LowPassFilter.apply_lpf(gray, kernel)

        st.image(gray, caption="Original Grayscale Image", use_column_width=True, clamp=True)
        st.image(result, caption=f"{filter_type} Filtered Image", use_column_width=True, clamp=True)

if page == "Frequency Response":
    st.header("Frequency Response of Discrete Signals")

    # Input koefisien sinyal diskrit
    hn_input = st.text_input("Masukkan koefisien sinyal diskrit (pisahkan dengan koma)", value="0.5, -0.5, 0.5")
    
    try:
        hn = np.array([float(x.strip()) for x in hn_input.split(",")])  # Parsing input menjadi array
        if len(hn) > 0:
            # Hitung respons frekuensi menggunakan ResponseSystem
            w, h = ResponseSystem.compute_frequency_response(hn)

            # Plot respons frekuensi menggunakan Streamlit
            ResponseSystem.plot_frequency_response(w, h)
        else:
            st.warning("Masukkan setidaknya satu koefisien untuk sinyal.")
    except ValueError:
        st.error("Input tidak valid. Pastikan hanya angka dipisahkan oleh koma.")

if page == "Plot Frequency Response":
    st.header("Plot Frequency Response")
    hn = st.text_input("Enter Filter Coefficients (comma-separated)", "1, -1, 0.5, 0.3")
    hn = [float(i) for i in hn.split(',')]
    
    if st.button("Plot Response"):
        plot_frequency_response(hn)

# **4. ECG Processing**
elif page == "ECG Processing":
    st.header("ECG Processing")
    file = st.file_uploader("Upload ECG .mat File", type=["mat"])
    
    if file is not None:
        fs = st.number_input("Sampling Frequency (Hz)", value=500)
        G = st.number_input("Gain", value=10)
        fft_fs = st.number_input("FFT Sampling Frequency (Hz)", value=500)
        
        if st.button("Process and Plot ECG"):
            process_ecg(file, fs, G, fft_fs)

# **5. Create and Play Song**
elif page == "Create and Play Song":
    st.header("Create and Play Song")
    fs = st.number_input("Sampling Frequency (Hz)", value=8000)
    
    if st.button("Generate and Play Song"):
        output_path = "output_song.wav"
        create_song(output_path, fs)
        st.audio(output_path, format="audio/wav")

# **6. Plot Audio FFT**
elif page == "Plot Audio FFT":
    st.header("Plot Audio FFT")
    audio_file = st.file_uploader("Upload Audio File", type=["wav"])
    
    if audio_file is not None:
        audio_path = audio_file.name
        with open(audio_path, "wb") as f:
            f.write(audio_file.getbuffer())
        
        if st.button("Plot FFT"):
            plot_audio_fft(audio_path)

# **7. Zero-Pole Plot**
elif page == "Zero-Pole Plot":
    st.header("Zero-Pole Plot")
    b = st.text_input("Enter Filter Coefficients (comma-separated)", "0.1, 0.2, 0.3")
    b = [float(i) for i in b.split(',')]
    
    if st.button("Plot Zero-Pole"):
        zplane(b)

# **8. Plot Song Frequencies**
elif page == "Plot Song Frequencies":
    st.header("Plot Song Frequencies")
    signals = []
    signal1_freq = st.number_input("Frequency for Signal 1 (Hz)", value=440)
    signal2_freq = st.number_input("Frequency for Signal 2 (Hz)", value=880)
    
    fs = st.number_input("Sampling Frequency (Hz)", value=8000)
    frequencies = [signal1_freq, signal2_freq]
    signals.append(np.sin(2 * np.pi * signal1_freq * np.arange(0, 1, 1/fs)))
    signals.append(np.sin(2 * np.pi * signal2_freq * np.arange(0, 1, 1/fs)))
    
    if st.button("Plot Frequencies"):
        plot_song_frequencies(signals, fs, frequencies, ["Signal 1", "Signal 2"])

elif page == "Z-Transform":
    st.header("Z-Transform Examples")
    
    n, z = symbols('n z')
    
    # Define functions for Z-Transform
    f = 1**n
    f1 = 2**n
    f2 = KroneckerDelta(n, 0)
    f3 = 5 * KroneckerDelta(n, 0)
    
    # Perform Z-Transform
    result1 = manual_z_transform(f, n, z)
    result2 = manual_z_transform(f1, n, z)
    result3 = manual_z_transform(f2, n, z)
    result4 = manual_z_transform(f3, n, z)
    
    st.subheader("Results")
    st.write(f"Z-Transform of 1^n: {result1}")
    st.write(f"Z-Transform of 2^n: {result2}")
    st.write(f"Z-Transform of KroneckerDelta: {result3}")
    st.write(f"Z-Transform of 5 * KroneckerDelta: {result4}")
