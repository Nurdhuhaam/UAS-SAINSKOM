from scipy import linalg
import numpy as np

matrix = np.array([
    [4, 3, 2],
    [6, 3, -1],
    [-2, 5, 7]
])

P, L, U = linalg.lu(matrix)
invers = np.linalg.inv(matrix)

print(f"Matriks Asli:\n{matrix}")
print(f"\nMatriks Invers:\n {invers}")
print("\n### LU - Decomposition ###")
print("\nMatriks Permutasi P:\n", P)
print("\nLower Matrix L:\n", L)
print("\nUpper Matrix U:\n", U)