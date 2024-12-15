import numpy as np
import re

def parse_equation(equation):
    # Menghilangkan spasi dari persamaan
    equation = equation.replace(" ", "")
    
    # Menemukan semua koefisien (positif dan negatif) dan konstanta
    coefficients = re.findall(r'[+-]?\d*\.?\d*[xyz]', equation)
    constant = re.findall(r'[+-]?\d*\.?\d*$', equation)
    
    # Mengubah koefisien menjadi float dan memetakan ke x, y, z
    coeff_dict = {'x': 0, 'y': 0, 'z': 0}
    for coeff in coefficients:
        var = coeff[-1]
        value = coeff[:-1]
        if value in ['+', ''] or value == '-':
            value += '1'
        coeff_dict[var] = float(value)
    
    # Mengubah konstanta menjadi float
    if constant:
        constant = float(constant[0])
    else:
        constant = 0.0
    
    return [coeff_dict['x'], coeff_dict['y'], coeff_dict['z'], constant]

def gauss_elimination(A, b):
    # Menggabungkan matriks A dan vektor b menjadi matriks augment
    A = np.hstack([A, b.reshape(-1, 1)])
    n = len(b)
    
    # Proses triangularisasi
    for i in range(n):
        # Mencari elemen utama
        max_row = i + np.argmax(np.abs(A[i:, i]))
        if A[max_row, i] == 0:
            raise ValueError("Matriks tidak dapat diselesaikan karena terdapat elemen utama yang bernilai nol.")
        # Menukar baris jika diperlukan
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
        
        # Menghilangkan x_i dari baris berikutnya
        for j in range(i+1, n):
            m = A[j][i] / A[i][i]
            A[j, i:] -= m * A[i, i:]
            print(f"Eliminasi baris {j+1} menggunakan baris {i+1}:")
            print(A)
    
    print("\nMatriks Setelah Proses Triangularisasi:")
    print(A)
    
    # Proses substitusi mundur
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (A[i, -1] - np.sum(A[i, i+1:n] * X[i+1:n])) / A[i, i]
    
    return X

# Input manual berupa 3 persamaan linear dalam format string
print("Masukkan persamaan linear pertama (misalnya 2x + 3y + 5z = 6):")
eq1 = input()
print("Masukkan persamaan linear kedua (misalnya 3x + 2y + 4z = 8):")
eq2 = input()
print("Masukkan persamaan linear ketiga (misalnya x + y + z = 2):")                                                                
eq3 = input()

# Parsing persamaan menjadi koefisien
a1 = parse_equation(eq1)
a2 = parse_equation(eq2)
a3 = parse_equation(eq3)

# Membentuk matriks koefisien A dan vektor b
A = np.array([a1[:3], a2[:3], a3[:3]], dtype=float)
b = np.array([a1[3], a2[3], a3[3]], dtype=float)

print("\nMatriks Augment Awal:")
print(np.hstack([A, b.reshape(-1, 1)]))

# Melakukan eliminasi Gauss
X = gauss_elimination(A, b)

# Menampilkan hasil akhir
print("\nHasil Akhir:")
for i, var in enumerate(['x', 'y', 'z']):
    print(f"{var} = {X[i]}")
