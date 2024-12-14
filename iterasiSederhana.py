import math
import os


# Definisi fungsi g(x) untuk metode iterasi sederhana
def g(x):
    return math.sqrt(2*x+3) # Contoh fungsi iterasi

# Metode iterasi sederhana
def iterasi_sederhana(x0, toleransi, iterasi_maks):
    print(f"{'Iterasi':<10}{'x_n':<20}{'g(x_n)':<20}{'Error':<20}")
    print("-" * 70)

    for i in range(iterasi_maks):
        xn = g(x0)  # Menghitung nilai baru
        error = abs(xn - x0)  # Error absolut
        print(f"{i+1:<10}{x0:<20.10f}{xn:<20.10f}{error:<20.10f}")

        if error < toleransi:  # Cek konvergensi
            print("\nSolusi ditemukan!")
            return xn

        x0 = xn  # Update nilai untuk iterasi berikutnya

    print("\nIterasi maksimum tercapai, solusi mungkin tidak konvergen.")
    return None

def mainiterasiseder():
    os.system("cls")
    print("=== Metode Iterasi Sederhana ===\n")
    # Input parameter
    print(f"Persamaan: √(2*{'x'} + 3)")
    x0 = float(input("Masukkan nilai awal (x0): "))
    toleransi = float(input("Masukkan toleransi error: "))
    iterasi_maks = int(input("Masukkan jumlah iterasi maksimum: "))

    # Menjalankan metode iterasi sederhana
    hasil = iterasi_sederhana(x0, toleransi, iterasi_maks)

    if hasil is not None:
        print(f"\nAkar yang ditemukan: {hasil:.10f}")
    else:
        print("\nTidak ditemukan solusi dalam iterasi maksimum.")
    os.system("pause")  
    os.system("cls")
    
    
mainiterasiseder()