import numpy as np2
import sympy as sp

def secant_method(f, x0, x1, e, n):
    """
    Metode Secant untuk mencari akar sebuah fungsi.

    Parameter:
        f  : Fungsi yang akarnya akan dicari.
        x0 : Pendekatan awal pertama.
        x1 : Pendekatan awal kedua.
        e  : Toleransi kesalahan.
        n  : Jumlah iterasi maksimum.

    Mengembalikan:
        Akar dari fungsi jika ditemukan dalam batas toleransi dan iterasi, jika tidak maka None.
    """
    print("Iter\t\tx0\t\tx1\t\tf(x0)\t\tf(x1)\t\tx_next\t\t|f(x_next)|")
    for i in range(1, n + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Periksa apakah |f(x1)| berada dalam toleransi
        if abs(f_x1) <= e:
            print(f"\nAkar ditemukan: {x1:.6f} setelah {i} iterasi.")
            return x1

        # Hindari pembagian dengan nol
        if f_x1 - f_x0 == 0:
            print("\nPembagian dengan nol terjadi. Solusi tidak ditemukan.")
            return None

        # Hitung nilai berikutnya
        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(f"{i}\t\t{x0:.6f}\t{x1:.6f}\t{f_x0:.6f}\t{f_x1:.6f}\t{x_next:.6f}\t{abs(f(x_next)):.6f}")

        # Perbarui nilai
        x0, x1 = x1, x_next

    print("\nJumlah iterasi maksimum tercapai. Solusi tidak ditemukan dalam toleransi yang diberikan.")
    return None

def input_fungsi():
    print("Masukkan fungsi f(x):")
    fungsi_input = input("f(x) = ")

    x = sp.symbols('x')
    fungsi = sp.sympify(fungsi_input)

    def f(x_val):
        return float(fungsi.evalf(subs={x: x_val}))

    return f

# Input parameter dari pengguna
try:
    toleransi = float(input("Masukkan toleransi (contoh: 1e-6): "))
    iterasi_maks = int(input("Masukkan jumlah iterasi maksimum: "))
    x0 = float(input("Masukkan nilai pendekatan awal pertama (x0): "))
    x1 = float(input("Masukkan nilai pendekatan awal kedua (x1): "))

    # Masukkan fungsi secara manual
    f = input_fungsi()

    # Jalankan metode Secant
    secant_method(f, x0, x1, toleransi, iterasi_maks)
except Exception as e:
    print(f"Kesalahan: {e}")
