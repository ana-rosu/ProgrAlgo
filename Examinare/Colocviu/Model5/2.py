def citire(numef):
    with open(numef) as f:
        m = [[int(nr) for nr in line.split()] for line in f]
    return m


def modifica_matr(m, *indici):
    l = []
    n = len(m)
    for j in range(n):
        if j in indici:
            s = 0
            for i in range(n):
                if i < j:
                    s += m[i][j]
        else:
            s = -1
        l.append(s)
    m.append(l)

    for i in range(n + 1):
        if i in indici:
            s = 0
            for j in range(n):
                if i + j >= n - 1:
                    s = max(s, m[i][j])
        else:
            s = -1
        m[i] = [s] + m[i]
    return m


m = citire('date.in')
m = modifica_matr(m, 0, 1, 3, len(m) - 1)
for linie in m:
    for el in linie:
        if el < 0:
            print(' ' + str(el), end = ' ')
        else:
            print('  '+ str(el), end=' ')
    print()
