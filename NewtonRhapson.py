import numpy as np
import sympy as sp

def newton_raphson(f, f_inverse, x0, e, n):
    """
    Metode Newton-Raphson untuk mencari akar sebuah fungsi, dengan turunan sebagai invers fungsi.

    Parameter:
        f         : Fungsi yang akarnya akan dicari.
        f_inverse : Invers dari fungsi tersebut.
        x0        : Pendekatan awal.
        e         : Toleransi kesalahan.
        n         : Jumlah iterasi maksimum.

    Mengembalikan:
        Akar dari fungsi jika ditemukan dalam batas toleransi dan iterasi, jika tidak maka None.
    """
    print("Iter\txi\tf(xi)\t|f(xi)|")
    for i in range(1, n + 1):
        fx = f(x0)
        f_inv = f_inverse(x0)
        print(f"{i}\t{x0:.6f}\t{fx:.6f}\t{abs(fx):.6f}")

        # Periksa apakah |f(xi)| berada dalam toleransi
        if abs(fx) <= e:
            print(f"\nAkar ditemukan: {x0:.6f} setelah {i} iterasi.")
            return x0

        # Hindari pembagian dengan nol
        if f_inv == 0:
            print("\nInvers bernilai nol. Solusi tidak ditemukan.")
            return None

        # Perbarui pendekatan
        x0 = x0 - fx * f_inv

    print("\nJumlah iterasi maksimum tercapai. Solusi tidak ditemukan dalam toleransi yang diberikan.")
    return None

def input_fungsi():
    print("Masukkan fungsi f(x):")
    fungsi_input = input("f(x) = ")

    x = sp.symbols('x')
    fungsi = sp.sympify(fungsi_input)
    fungsi_turunan = sp.diff(fungsi, x)

    def f(x_val):
        return float(fungsi.evalf(subs={x: x_val}))

    def f_inverse(x_val):
        turunan_val = fungsi_turunan.evalf(subs={x: x_val})
        if turunan_val == 0:
            raise ZeroDivisionError("Turunan bernilai nol, tidak dapat menghitung invers.")
        return 1 / float(turunan_val)

    return f, f_inverse

# Input parameter dari pengguna
try:
    toleransi = float(input("Masukkan toleransi (contoh: 1e-6): "))
    iterasi_maks = int(input("Masukkan jumlah iterasi maksimum: "))
    tebakan_awal = float(input("Masukkan tebakan awal: "))

    # Masukkan fungsi secara manual
    f, f_inverse = input_fungsi()

    # Jalankan metode Newton-Raphson
    newton_raphson(f, f_inverse, tebakan_awal, toleransi, iterasi_maks)
except Exception as e:
    print(f"Kesalahan: {e}")
