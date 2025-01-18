from sympy import symbols, summation, KroneckerDelta, oo

# Definisi fungsi Z-transform manual
def manual_z_transform(f, n, z):
    return summation(f * z**(-n), (n, 0, oo))

# Fungsi utama untuk contoh Z-transform
def z_transform_examples():
    # Definisi variabel simbolik
    n, z = symbols('n z')
    
    # Fungsi-fungsi yang akan dihitung Z-transformnya
    f = 1**n
    f1 = 2**n
    f2 = KroneckerDelta(n, 0)
    f3 = 5 * KroneckerDelta(n, 0)
    
    # Menghitung Z-transform manual dari masing-masing fungsi
    result1 = manual_z_transform(f, n, z)
    result2 = manual_z_transform(f1, n, z)
    result3 = manual_z_transform(f2, n, z)
    result4 = manual_z_transform(f3, n, z)
    
    # Menampilkan hasil Z-transform
    print("Z-Transform of 1^n:", result1)
    print("Z-Transform of 2^n:", result2)
    print("Z-Transform of KroneckerDelta:", result3)
    print("Z-Transform of 5 * KroneckerDelta:", result4)

# Menjalankan fungsi utama
z_transform_examples()
