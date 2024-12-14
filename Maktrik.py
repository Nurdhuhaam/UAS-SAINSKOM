import numpy as mtrix

def input_matrix(rows, cols, matrix):
    print(f"Masukkan elemen-elemen untuk {matrix} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Baris {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Baris harus memiliki {cols} elemen. Coba lagi.")
            row = list(map(float, input(f"Baris {i + 1}: ").split()))
        matrix.append(row)
    return mtrix.array(matrix)

def main():
    # Input ukuran matriks
    M = int(input("Masukkan jumlah baris matriks: "))
    N = int(input("Masukkan jumlah kolom matriks: "))

    # Input elemen matriks
    matrix1 = input_matrix(M, N, matrix="Matrix 1")
    print("Matrix 1 berhasil dimasukkan:\n", matrix1)
    
    operation = input(
        "\nPilih operasi:\n"
        "1. Perkalian skalar\n"
        "2. Penjumlahan matriks\n"
        "3. Pengurangan matriks\n"
        "4. Perkalian matriks\n"
        "Masukkan pilihan (1/2/3/4): "
    )

    if operation == "1":
        scalar = float(input("Masukkan nilai skalar: "))
        result = scalar * matrix1
        print(f"Hasil perkalian skalar:\n{result}")

    elif operation in ["2", "3"]:
        matrix2 = input_matrix(M, N, matrix="Matrix 2")
        print("Matrix 2 berhasil dimasukkan:\n", matrix2)

        if operation == "2":
            result = matrix1 + matrix2
            print(f"Hasil penjumlahan matriks:\n{result}")
        elif operation == "3":
            result = matrix1 - matrix2
            print(f"Hasil pengurangan matriks:\n{result}")

    elif operation == "4":
        P = int(input("Masukkan jumlah baris matriks kedua: "))
        matrix2 = input_matrix(P, M, matrix="Matrix 2")
        print("Matrix 2 berhasil dimasukkan:\n", matrix2)
        result = mtrix.dot(matrix1, matrix2)
        print(f"Hasil perkalian matriks:\n{result}")

    else:
        print("Pilihan tidak valid. Program selesai.")

if __name__ == "__main__":
    main()
