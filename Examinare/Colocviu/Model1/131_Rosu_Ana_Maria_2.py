# Rosu Ana Maria, grupa 131
# SUB 2

def citire_matrice(numef):
    M = []
    f = open(numef)
    for linie in f:
        l = [int(nr) for nr in linie.split()]
        M.append(l)
    return M


def modifica_matrice(matrice, ch, x=0, y=0):
    n = len(matrice)
    if ch == 'c':
        # interschimba coloana x cu coloana y
        for i in range(n):
            matrice[i][x], matrice[i][y] = matrice[i][y], matrice[i][x]
        return matrice
    else:
        # interschimba diag sec cu diag princ
        # dp=a[i][i] ds=a[i][n-i-1]
        for i in range(n):
            matrice[i][i], matrice[i][n -i - 1] = matrice[i][n - i - 1], matrice[i][i]
        return matrice


def scrie_matrice1(matrice, numef):
    f = open(numef, 'w')
    cnt = 0
    for linie in matrice:
        if cnt % 2 == 0:
            for el in linie:
                f.write(str(el) + ' ')
        else:
            l = linie[::-1]
            for el in l:
                f.write(str(el) + ' ')
        f.write('\n')
        cnt += 1


def scrie_matrice2(matrice, numef):
    f = open(numef, 'w')
    cnt = 0
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if cnt % 2 == 0:
                f.write(str(matrice[i][j]) + ' ')
            else:
                f.write(str(matrice[i][n - j - 1]) + ' ')
        f.write('\n')
        cnt += 1


m = citire_matrice('date.in')
n = len(m)
for i in range(n // 2):
    modifica_matrice(m, 'c', i, n - i - 1)

modifica_matrice(m, 'd')
# mat = modifica_matrice(m, 'd')
# modifica_matrice(matrice, 'd')

print(m)
scrie_matrice1(m, 'date.out')
