MAX = 100

def luDecomposition(mat, n):
    lower = [[0 for x in range(n)] for y in range(n)]
    upper = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        
        for k in range(i, n):
            
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            
            upper[i][k] = mat[i][k] - sum

        
        for k in range(i, n):
            if i == k:
                lower[i][i] = 1  
            else:
                
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])

                
                lower[k][i] = (mat[k][i] - sum) / upper[i][i]

    
    print("Lower Triangular\t\tUpper Triangular")
    for i in range(n):
        
        for j in range(n):
            print(f"{lower[i][j]:.2f}", end="\t")
        print("", end="\t")

        
        for j in range(n):
            print(f"{upper[i][j]:.2f}", end="\t")
        print("")


mat = [
    [2, 1, 2],
    [3, 4, 1],
    [5, 2, 9]
]
luDecomposition(mat, 3)