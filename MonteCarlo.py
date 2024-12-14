import numpy as np

def BilanganAcak(n_simulations):
    random_array = np.random.rand(n_simulations)
    return random_array

def Frekuensi(i, array, distribusi):
    jarak = array[i] * 100
    for j in range(len(distribusi) - 1):
        if jarak < distribusi[j]:
            return j
        elif distribusi[j] <= jarak < distribusi[j + 1]:
            return j + 1
    return len(distribusi) - 1

def tabelsimulasi(n, array, distribusi, variabel):
    print("Tabel Simulasi")
    print("Hari ke\t\tBilangan Acak\t\tFrekuensi")
    for i in range(n):
        indeks_frekuensi = Frekuensi(i, array, distribusi)
        print(i + 1, "\t\t", round(array[i], 4), "\t\t", variabel[indeks_frekuensi])
        
    ratarata = np.sum(variabel[indeks_frekuensi]) / n
    print ("\nRata-rata:", ratarata)
    
if __name__ == "__main__":
    # Langkah 1: Membuat distribusi kemungkinan
    variabel = []  # Variabel penting
    frekuensi = []  # Frekuensi untuk tiap nilai variabel

    # Input data variabel dan frekuensi
    n = int(input("Masukkan jumlah variabel: "))
    for i in range(n):
        nilai = float(input(f"Masukkan nilai variabel ke-{i + 1}: "))
        freq = int(input(f"Masukkan frekuensi untuk variabel {nilai}: "))
        variabel.append(nilai)
        frekuensi.append(freq)

    # Hitung probabilities berdasarkan frekuensi
    jumlah_frekuensi = sum(frekuensi)
    distribusi_probabilitas = [freq / jumlah_frekuensi for freq in frekuensi]
    print("\nDistribusi Probabilitas:")
    print(distribusi_probabilitas)

    distribusi_komulatif = np.cumsum(distribusi_probabilitas) * 100
    print("\nDistribusi Komulatif:")
    print(distribusi_komulatif)

    n_simulations = int(input("Masukkan jumlah simulasi: "))
    random_array = BilanganAcak(n_simulations)
    print("\nArray Random:")
    print(random_array)

    tabelsimulasi(n_simulations, random_array, distribusi_komulatif, variabel)