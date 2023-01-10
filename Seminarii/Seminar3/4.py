'''Scrieti un program care construieste o matrice patratica M de dimensiune n,
avand forma urmatoare:
- pe prima linie si ultima coloana toate elementele sunt egale cu 1
- restul elementelor se calculeaza ca suma a elementelor vecine de la est si sud

Exemplu: pt n = 4 matricea M ceruta este:
20 10 4 1
10 6 3 1
4 3 2 1
1 1 1 1
'''

n = int(input('n= '))
M = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    M[n-1][i] = 1
    M[i][n-1] = 1

for i in range(n-2,-1, -1):
    for j in range(n-2, -1, -1):
        M[i][j] = M[i+1][j] + M[i][j+1]

for linie in M:
    for el in linie:
        print(el, end = " ")
    print()
