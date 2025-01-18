import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Gunakan backend TkAgg
matplotlib.use('TkAgg')

# Definisikan sinyal asli x(n)
n = np.arange(-5, 6)  # Rentang n
x = np.array([0, 0, 0, 1, 5, 2, 4, 3, 0, 0, 0])  # Nilai dari x(n)

# Definisikan nilai pergeseran waktu k
k = int(input('Masukkan Nilai k: '))

# Lakukan operasi pergeseran waktu
# Pergeseran ke kanan
y1 = np.concatenate((np.zeros(k), x[:len(x)-k]))
# Pergeseran ke kiri
y2 = np.concatenate((x[k:], np.zeros(k)))

# Plot sinyal asli x(n)
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.stem(n, x, 'b', markerfmt='bo', basefmt='k-')
plt.title('x(n)')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.xticks(n)
plt.axis([-5, 5, 0, 6])
plt.grid(True)

# Plot sinyal yang digeser y1(n)
plt.subplot(1, 3, 2)
plt.stem(n, y1, 'r', markerfmt='ro', basefmt='k-')
plt.title(f'y1(n) = x(n - {k})')
plt.xlabel('n')
plt.ylabel('y1(n)')
plt.xticks(n)
plt.axis([-5, 5, 0, 6])
plt.grid(True)

# Plot sinyal yang digeser y2(n)
plt.subplot(1, 3, 3)
plt.stem(n, y2, 'g', markerfmt='go', basefmt='k-')
plt.title(f'y2(n) = x(n + {k})')
plt.xlabel('n')
plt.ylabel('y2(n)')
plt.xticks(n)
plt.axis([-5, 5, 0, 6])
plt.grid(True)

plt.tight_layout()

# Tampilkan plot
try:
    plt.show()
except KeyboardInterrupt:
    print("Plot display interrupted. Saving figure to file instead.")
    plt.savefig("timeshift_plot.png")
    print("Figure saved as 'timeshift_plot.png'")
