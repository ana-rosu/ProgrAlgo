def mat_triunghiulara(n):
    M = [[0] * (i+1) for i in range(n)]
    for i in range(n):
        M[i][0] = i+1
        M[n-1][i] = n-i
    for i in range(n-2,0,-1):
        for j in range(1,i+1):
            M[i][j] = M[i][j-1] + M[i+1][j-1] + M[i+1][j]

    for l in M:
        for el in l:
            print(el, end=' ')
        print()

mat_triunghiulara(4)
