import os 
def linear_interpolation(x1, y1, x2, y2, x):
    """
    Fungsi untuk melakukan interpolasi linier.
    :param x1: Titik x pertama
    :param y1: Titik y pertama
    :param x2: Titik x kedua
    :param y2: Titik y kedua
    :param x: Titik x yang ingin diinterpolasi
    :return: Nilai y pada titik x
    """
    if x1 == x2:
        raise ValueError("x1 dan x2 tidak boleh sama (tidak dapat dihitung interpolasi linier).")
    y = y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
    return y


def maininterpolasi():
    print("=== Program Interpolasi Linier ===")
    print("Masukkan dua titik data (x1, y1) dan (x2, y2):")
    
    try:
        # Input dua titik data
        x1 = float(input("Masukkan x1: "))
        y1 = float(input("Masukkan y1: "))
        x2 = float(input("Masukkan x2: "))
        y2 = float(input("Masukkan y2: "))
        
        # Validasi input
        if x1 == x2:
            print("Error: x1 dan x2 tidak boleh sama.")
            return
        
        print("\nMasukkan nilai x yang ingin diinterpolasi:")
        x_values = input("Masukkan nilai x (pisahkan dengan spasi jika lebih dari satu): ")
        x_values = list(map(float, x_values.split()))
        
        # Hitung interpolasi untuk setiap nilai x
        results = {}
        for x in x_values:
            y = linear_interpolation(x1, y1, x2, y2, x)
            results[x] = y
        
        # Tampilkan hasil interpolasi
        print("\n=== Hasil Interpolasi ===")
        for x, y in results.items():
            print(f"x = {x:.2f}, y = {y:.2f}")
    
    except ValueError as e:
        print(f"Input tidak valid: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    os.system("pause")
    os.system("cls")


    maininterpolasi()
