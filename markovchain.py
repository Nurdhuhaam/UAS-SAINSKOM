import numpy as np

def mchain():
    # Memilih ukuran matriks
    print("Pilih ukuran matriks (2, 3, atau 4):")
    size = int(input())
    if size not in [2, 3, 4]:
        print("Ukuran matriks tidak valid.")
        return

    print(f"Masukkan matrik perubahan status {size}x{size} (baris dipisahkan oleh koma, elemen dipisahkan oleh spasi):")
    user_input = input()
    state_changes = np.array([list(map(int, row.split())) for row in user_input.split(',')])

    # Menghitung jumlah total perubahan dari setiap status
    total_changes = state_changes.sum(axis=1, keepdims=True)

    # Menambahkan kolom jumlah pada tabel state_changes
    state_changes_with_totals = np.hstack((state_changes, total_changes))

    # Menampilkan matrik jumlah perubahan status dengan kolom jumlah
    print("Matrik Jumlah Perubahan Status:")
    print(state_changes_with_totals)

    # Menghitung matriks probabilitas transisi
    transition_matrix = state_changes / total_changes

    # Menampilkan matriks probabilitas transisi
    print("Matrik Probabilitas Transisi:")
    print(transition_matrix)

    def future_state_prob(initial_state, n_steps):
        state = initial_state
        for _ in range(n_steps):
            state = state.dot(transition_matrix)
        return state

    # Menghitung probabilitas untuk setiap kondisi awal
    n_steps = 5
    for i in range(size):
        initial_state = np.zeros(size)
        initial_state[i] = 1
        future_prob = future_state_prob(initial_state, n_steps)
        print(f"Probabilitas setelah {n_steps} iterasi dari kondisi awal {i + 1}:")
        print(future_prob)

    # Menentukan Steady State
    num_states = transition_matrix.shape[0]
    A = np.append(transition_matrix.T - np.eye(num_states), [np.ones(num_states)], axis=0)
    b = np.append(np.zeros(num_states), [1])

    steady_state = np.linalg.lstsq(A, b, rcond=None)[0]

    print("Steady State:")
    print(steady_state)

if __name__ == "__main__":
    mchain()
