import numpy as np
import os

def gauss_elimination(A, b):
    """
    Menyelesaikan sistem persamaan linier Ax = b menggunakan eliminasi Gauss.
    """
    n = len(b)
    # Forward elimination
    for i in range(n):
        # Partial pivoting (optional)
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if i != max_row:
            A[[i, max_row]] = A[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x

def quadratic_interpolation():
    """
    Melakukan interpolasi kuadrat dengan inputan titik dari pengguna.
    """
    print("Masukkan tiga titik untuk interpolasi kuadrat.")
    points = []
    for i in range(3):
        x = float(input(f"Masukkan nilai x{i+1}: "))
        y = float(input(f"Masukkan nilai y{i+1}: "))
        points.append((x, y))
    
    # Ekstraksi koordinat
    x_values = np.array([p[0] for p in points])
    y_values = np.array([p[1] for p in points])

    # Membentuk matriks A dan vektor b
    A = np.array([[x**2, x, 1] for x in x_values], dtype=float)
    b = np.array(y_values, dtype=float)

    # Menyelesaikan sistem persamaan
    coefficients = gauss_elimination(A, b)
    return coefficients

# Main program
def maininterpolkuadrat():
    coefficients = quadratic_interpolation()
    print("\nKoefisien polinomial kuadrat (a, b, c):")
    print(f"a = {coefficients[0]:.4f}, b = {coefficients[1]:.4f}, c = {coefficients[2]:.4f}")

    # Menampilkan persamaan polinomial
    print("\nPersamaan polinomial kuadrat:")
    print(f"y = {coefficients[0]:.4f}x^2 + {coefficients[1]:.4f}x + {coefficients[2]:.4f}")

    # Input nilai x dan menghitung y
    while True:
        try:
            x_input = float(input("\nMasukkan nilai x untuk menghitung y (atau ketik 'exit' untuk keluar): "))
            y_result = coefficients[0] * x_input**2 + coefficients[1] * x_input + coefficients[2]
            print(f"Untuk x = {x_input:.4f}, y = {y_result:.4f}")
        except ValueError:
            print("Program selesai.")
            break
        
    os.system("pause")
    os.system("cls")
    
maininterpolkuadrat()
        
