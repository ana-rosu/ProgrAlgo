# SUB 1

def citire_matrice(numef):
    f = open(numef)
    matrice = []
    cnt = 0
    for line in f:
        aux = [int(nr) for nr in line.split()]
        matrice.append(aux)
        if cnt == 0:
            l = len(aux)
        else:
            if len(aux) != l:
                return None
        cnt += 1
    return matrice

def prima_cifra(x):
    cx = x
    p = 1
    while cx > 9:
        p *= 10
        cx //= 10
    return x // p

def multimi(matrice, *indici):
    multimea2 = set()
    ok = 1
    for i in range(len(matrice)):
            if i in indici:
                A = set(x for x in matrice[i] if x < 0)
                B = set(x for x in matrice[i] if x > 0 and prima_cifra(x) == x % 10)
                if ok == 1:
                    multimea1 = A
                    ok = 0
                multimea1 = multimea1 & A
                multimea2 = multimea2 | B
    return multimea1, multimea2

m = citire_matrice('matrice.in')

n = len(m)
_, rasp1 = multimi(m, n-1, n-2, n-3)
rasp1 = sorted(rasp1)
rasp2,_ = multimi(m, 0, n-1)

with open('matrice.out', 'w') as f:
    for el in rasp1:
        f.write(str(el) + ' ')
    f.write('\n')
    for el in rasp2:
        f.write(str(el) + ' ')
