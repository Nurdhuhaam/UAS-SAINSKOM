import math

def bisection_method(f, a, b, tolerance=0.001, max_iterations=100):
    """
    Metode Biseksi untuk mencari akar persamaan dengan output seperti tabel.

    Parameter:
    f : function - Fungsi yang akan dicari akarnya
    a : float - Batas bawah interval
    b : float - Batas atas interval
    tolerance : float - Toleransi error (default 0.001)
    max_iterations : int - Maksimum iterasi (default 100)

    Return:
    None - Hasil ditampilkan dalam format tabel.
    """
    # Cek kondisi awal
    if f(a) * f(b) >= 0:
        print("Metode biseksi gagal: tidak ada akar dalam interval ini.")
        return None

    # Header tabel
    print(f"{'Iterasi':<10}{'a':<12}{'b':<12}{'x':<12}{'f(x)':<12}{'f(a)':<12}{'Keterangan':<20}")
    print("-" * 80)

    iterations = 0

    while iterations < max_iterations:
        # Hitung titik tengah
        x = (a + b) / 2
        
        
        fx = f(x)
        fa = f(a)

        
        if fa * fx < 0:
            keterangan = "berlawanan tanda"
        else:
            keterangan = "sama tanda"

        
        print(f"{iterations + 1:<10}{a:<12.6f}{b:<12.6f}{x:<12.6f}{fx:<12.6f}{fa:<12.6f}{keterangan:<20}")

        
        if abs(fx) < tolerance:
            return x

        
        if fa * fx < 0:
            b = x
        else:
            a = x

        iterations += 1

    print("Metode biseksi mencapai iterasi maksimum.")
    return None

# Fungsi untuk persamaan xe^(-x) + 1 = 0
def fungsi(x):
    return x * math.exp(-x) + 1

a = -1  
b = 0   
toleransi = 0.0001
iterasi_maks = 10

# Jalankan metode biseksi
akar = bisection_method(fungsi, a, b, toleransi, iterasi_maks)

# Tampilkan hasil akhir jika ditemukan
if akar is not None:
    print(f"\nAkar persamaan: {akar:.6f}")
    print(f"Nilai fungsi di titik akar: {fungsi(akar):.6f}")
