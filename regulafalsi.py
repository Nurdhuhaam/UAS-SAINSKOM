import sympy as sp

def regula_falsi_with_input():
    expr = input("Masukkan fungsi f(x) (gunakan 'x' sebagai variabel): ")
    x = sp.symbols('x')
    func = sp.lambdify(x, sp.sympify(expr))

    a = float(input("Masukkan batas bawah (a): "))
    b = float(input("Masukkan batas atas (b): "))
    e = float(input("Masukkan toleransi error (e): "))
    n = int(input("Masukkan iterasi maksimum (n): "))

    Fa = func(a)
    Fb = func(b)
    
    print(f"{'Iterasi':<8}{'a':<15}{'b':<15}{'x':<15}{'f(x)':<15}{'f(a)':<15}{'f(b)':<15}")
    print("-" * 98)
    
    for i in range(1, n + 1):
        x = b - (Fb * (b - a)) / (Fb - Fa)
        Fx = func(x)
        error = abs(Fx)
        
        print(f"{i:<8}{a:<15.6f}{b:<15.6f}{x:<15.6f}{Fx:<15.6f}{Fa:<15.6f}{Fb:<15.6f}")
        
        if error < e:
            print(f"Akar ditemukan: {x}")
            return x
        
        if Fx * Fa < 0:
            b = x
            Fb = Fx
        else:
            a = x
            Fa = Fx

    print("Akar tidak ditemukan dalam iterasi maksimum")
    return None


regula_falsi_with_input()
