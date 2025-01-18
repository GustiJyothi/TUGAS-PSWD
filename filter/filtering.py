import numpy as np
import sounddevice as sd
import soundfile as sf
from scipy.signal import firwin, lfilter, convolve2d, freqz
import matplotlib.pyplot as plt
import streamlit as st

class Equalizer:
    def __init__(self, fs, audio):
        self.fs = fs
        self.audio = audio

    def apply_equalizer(self, gains, volume):
        N = 16
        fc1, fc2 = 1500, 5000
        wc1, wc2 = fc1 / (self.fs / 2), fc2 / (self.fs / 2)

        b_low = firwin(N + 1, wc1)
        b_band = firwin(N + 1, [wc1, wc2], pass_zero=False)
        b_high = firwin(N + 1, wc2, pass_zero=False)

        y_low = gains[0] * lfilter(b_low, 1.0, self.audio)
        y_band = gains[1] * lfilter(b_band, 1.0, self.audio)
        y_high = gains[2] * lfilter(b_high, 1.0, self.audio)

        return (y_low + y_band + y_high) * volume

    @staticmethod
    def normalize_audio(audio):
        max_amplitude = np.max(np.abs(audio))
        if max_amplitude > 0:
            return audio / max_amplitude
        return audio

    def play_audio(self, audio):
        normalized_audio = self.normalize_audio(audio).astype(np.float32)
        with sd.OutputStream(samplerate=self.fs, channels=1) as stream:
            stream.write(normalized_audio)

class HighPassFilter:
    @staticmethod
    def apply_hpf(image, kernel):
        return convolve2d(image, kernel, mode='same', boundary='symm')

class LowPassFilter:
    @staticmethod
    def apply_lpf(image, kernel):
        return convolve2d(image.astype(float), kernel, mode='same')
    
class ResponseSystem:
    @staticmethod
    def compute_frequency_response(hn):
        """
        Menghitung respons frekuensi dari sinyal diskrit.
        :param hn: Koefisien filter atau sinyal diskrit (array 1D)
        :return: w (frekuensi angular), h (respons frekuensi)
        """
        w, h = freqz(hn, worN=8000)  # worN menentukan resolusi frekuensi
        return w, h

    @staticmethod
    def plot_frequency_response(w, h):
        """
        Memplot respons frekuensi menggunakan Streamlit.
        :param w: Frekuensi angular
        :param h: Respons frekuensi
        """
        plt.figure(figsize=(10, 6))

        # Amplitudo dalam dB
        plt.subplot(2, 1, 1)
        plt.plot(w, 20 * np.log10(abs(h)), 'b')
        plt.title('Frequency Response')
        plt.ylabel('Amplitude (dB)')
        plt.xlabel('Frequency (rad/sample)')
        plt.grid()

        # Fase
        plt.subplot(2, 1, 2)
        plt.plot(w, np.angle(h), 'r')
        plt.ylabel('Phase (radians)')
        plt.xlabel('Frequency (rad/sample)')
        plt.grid()

        # Render plot di Streamlit
        st.pyplot(plt.gcf())
