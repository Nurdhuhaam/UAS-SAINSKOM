def beda_pembeda(x, y):
    n = len(x)
    tabel = [y.copy()]
    
    
    for i in range(1, n):
        baris_baru = []
        for j in range(n - i):
            beda = (tabel[i-1][j+1] - tabel[i-1][j]) / (x[j+i] - x[j])
            baris_baru.append(beda)
        tabel.append(baris_baru)
    
    return tabel

def polinom_newton(x, y, titik):
    tabel = beda_pembeda(x, y)
    
    n = len(x)
    hasil = y[0]
    produk = 1
    
    
    for i in range(1, n):
        produk *= (titik - x[i-1])
        hasil += tabel[i][0] * produk
    
    return hasil

def cetak_tabel_beda_pembeda(x, y):
    tabel = beda_pembeda(x, y)
    header = "x\t\t" + "\t\t".join([f"ST-{i}" for i in range(len(tabel))])
    print(header)
    
    for i in range(len(x)):
        baris = f"{x[i]:.4f}\t\t{tabel[0][i]:.4f}"
        for j in range(1, len(tabel)):
            if i < len(tabel[j]):
                baris += f"\t\t{tabel[j][i]:.4f}"
            else:
                baris += "\t\t-"
        print(baris)


def main():
    x = [0, 1, 2, 3, 4]
    y = [1, 0.5403, -0.4161, -0.99, -0.6536]
    
    cetak_tabel_beda_pembeda(x, y)
    
    titik_interpolasi = 2.5
    nilai = polinom_newton(x, y, titik_interpolasi)
    print(f"\nNilai polinom Newton pada x = {titik_interpolasi}: {nilai:.4f}")

if __name__ == "__main__":
    main()
