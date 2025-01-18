import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def konvolusi(xn, hn):
    """
    Fungsi untuk melakukan konvolusi antara dua sinyal xn dan hn.

    Parameters:
    xn (array): Sinyal pertama.
    hn (array): Sinyal kedua.

    Returns:
    yn (array): Hasil konvolusi xn dan hn.
    """
    # Operasi konvolusi antara hn dan xn
    yn = np.convolve(xn, hn)

    # Plot sinyal h(n)
    plt.subplot(1, 3, 1)
    plt.stem(hn)
    plt.title('h(n)')

    # Plot sinyal x(n)
    plt.subplot(1, 3, 2)
    plt.stem(xn)
    plt.title('x(n)')

    # Plot sinyal konvolusi h(n)*x(n)
    plt.subplot(1, 3, 3)
    plt.stem(yn)
    plt.title('h(n)*x(n)')

    # Menampilkan plot menggunakan st.pyplot
    plt.tight_layout()
    st.pyplot(plt)  # Use st.pyplot to display the plot in Streamlit

    return yn
