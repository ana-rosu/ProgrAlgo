# def citire_matrice():
#     m = []
#     with open('matrice.in') as f:
#         for line in f:
#             aux = [int(x) for x in line.split()]
#             m.append(aux)
#     return m

def citire_matrice():
    with open('matrice.in') as f:
        m = [[int(x) for x in line.split()] for line in f]
    return m


def bordare_matrice(matrice):
    for line in matrice:
        line.append(sum(line))
    matrice.append([sum([matrice[i][j] for i in range(len(matrice))]) for j in range(len(matrice) + 1)])
    return m


m = citire_matrice()
m = bordare_matrice(m)
print(m)

with open('matrice.out', 'w') as f:
    n = len(m)
    for i in range(n):
        f.write(f'{m[i][i]} ')
    for i in range(n):
        f.write(f'{m[i][n - i - 1]} ')
    for i in range(n):
        for j in range(n):
            if i != j and i + j != n - 1:
                f.write(f'{m[i][j]} ')
