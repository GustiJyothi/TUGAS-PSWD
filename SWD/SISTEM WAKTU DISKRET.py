import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi variabel
xn = list(map(int, input("Respon Impuls h(n) : ").split()))  # Sinyal pertama [contoh: 1 -1]
hn = list(map(int, input("Sinyal Kedua x(n) : ").split()))   # Sinyal kedua [contoh: 1 -2 3]

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

# Menampilkan plot
plt.tight_layout()
plt.show()