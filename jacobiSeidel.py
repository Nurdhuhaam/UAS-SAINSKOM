import numpy as np
import os

def jacobi_iteration(A, b, x, tolerance, max_iter):
    """
    A         : numpy array, matriks koefisien
    b         : numpy array, vektor konstanta
    x         : numpy array, tebakan awal
    tolerance : float, batas konvergensi
    max_iter  : int, jumlah iterasi maksimum
    """
    n = len(A)

    # Header tabel
    print(f"{'Iterasi':<25}{'x':<30}{'Error':<10}")
    print("=" * 80)

    for k in range(max_iter):
        x_new = np.zeros_like(x)
        
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]

        # Hitung error (norm infinity)
        error = np.linalg.norm(x_new - x, ord=np.inf)

        # Tampilkan hasil iterasi
        print(f"{k + 1:<10}{str(x_new):<40}     {error:<10.6f}")

        # Cek konvergensi
        if error < tolerance:
            print("Konvergen pada iterasi ke-", k + 1)
            print("=" * 80)
            return x_new

        x = x_new

    print("Tidak konvergen setelah iterasi maksimum")
    print("=" * 80)
    return x

def gauss_seidel_iteration(A, b, x, tolerance, max_iter):
    """
    A         : numpy array, matriks koefisien
    b         : numpy array, vektor konstanta
    x         : numpy array, tebakan awal
    tolerance : float, batas konvergensi
    max_iter  : int, jumlah iterasi maksimum
    """
    n = len(A)

    # Header tabel
    print(f"{'Iterasi':<25}{'x':<30}{'Error':<10}")
    print("=" * 80)

    for k in range(max_iter):
        x_new = np.copy(x)
        
        for i in range(n):
            sum_ax = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]

        # Hitung error (norm infinity)
        error = np.linalg.norm(x_new - x, ord=np.inf)

        # Tampilkan hasil iterasi
        print(f"{k + 1:<10}{str(x_new):<40}     {error:<10.6f}")

        # Cek konvergensi
        if error < tolerance:
            print("Konvergen pada iterasi ke-", k + 1, "(Gauss-Seidel)")
            print("=" * 80)
            return x_new

        x = x_new

    print("Tidak konvergen setelah iterasi maksimum (Gauss-Seidel)")
    print("=" * 80)
    return x

def is_diagonally_dominant(A):
    """Memeriksa apakah matriks A adalah dominan diagonal."""
    n = len(A)
    for i in range(n):
        sum_row = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= sum_row:
            return False
    return True

def input_matrixA():
    while True:
        n = int(input("Masukkan jumlah variabel (n): "))
        print("Masukkan elemen matriks A (baris per baris):")
        A = []
        for i in range(n):
            row = list(map(float, input(f"Baris {i + 1}: ").split()))
            A.append(row)
        A = np.array(A, dtype=float)
        
        if is_diagonally_dominant(A):
            return A
        else:
            print("Matriks A tidak dominan diagonal. clsSilakan masukkan matriks yang memenuhi syarat.")

def input_matrixB():
    while True:
        n = int(input("Masukkan jumlah variabel (n): "))
        print("Masukkan elemen vektor b:")
        b = []
        for i in range(n):
            b.append(float(input(f"b[{i + 1}]: ")))
        b = np.array(b, dtype=float)
        return b
def mainiterasi():
    os.system("cls")
    print(""" 
          =====================================
          ===iterasi Jacobi dan Gauss-Seidel===
          =====================================
          """)
    # Input matriks dan vektor
    A = input_matrixA()
    b = input_matrixB()

    # Tebakan awal x
    x_initial = np.zeros(len(b))

    # Parameter iterasi
    tolerance = 1e-6
    max_iter = 100

    # Jalankan iterasi Jacobi
    print("\nIterasi Jacobi:")
    result_jacobi = jacobi_iteration(A, b, x_initial, tolerance, max_iter)

    # Cetak hasil Jacobi
    print("Hasil akhir (Jacobi):")
    for i, x in enumerate(result_jacobi):
        print(f"x{i + 1} = {x:.6f}")

    # Jalankan iterasi Gauss-Seidel
    print("\nIterasi Gauss-Seidel:")
    result_gauss_seidel = gauss_seidel_iteration(A, b, x_initial, tolerance, max_iter)

    # Cetak hasil Gauss-Seidel
    print("Hasil akhir (Gauss-Seidel):")
    for i, x in enumerate(result_gauss_seidel):
        print(f"x{i + 1} = {x:.6f}")
        
    os.system("pause")
    os.system("cls")
        
mainiterasi()
