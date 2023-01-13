'''
a)Scrieți  o  funcție  generică  care  să  furnizeze  numărul  elementelor  dintr-o colecție iterabilă
care au o anumită proprietate, implementată sub forma unei funcții cu  un singur  parametru care returnează
True dacă acesta are  proprietatea  cerută  sau False în caz contrar.

b)Scrieți câte o funcție care să implementeze proprietatea necesară pentru ca funcția de numărare să furnizeze:
•numărul valorilor pare dintr-o listă/tuplu de numere întregi;
•numărul vocalelor dintr-un șir de caractere;
•numărul perechilor (x, y) cu proprietatea că x=y dintr-o listă de tupluri;
•numărul șirurilor de lungime k dintr-o listă de șiruri de caractere;
•numărul valorilor x dintr-o listă de numere întregi pentru care cmmdc(x, y) = t, unde y și t sunt date.
'''


def numarare(colectie, proprietate):
    cnt = 0
    for el in colectie:
        if proprietate(el) == True:
            cnt += 1
    return cnt


def pare(x):
    return x % 2 == 0


def vocale(ch):
    return ch in 'aeiouAEIOU'


def perechiEgale(tuplu):
    return tuplu[0] == tuplu[1]


def lungimeSir(k):
    def aux(sir):
        return len(sir) == k

    return aux


def cmmdcEsteT(y, t):
    def cmmdc(a, b):
        r = a % b
        while r != 0:
            a, b = b, r
            r = a % b
        return b

    def aux(x):
        return cmmdc(x,y) == t
    return aux

c = numarare([2, 3, 4, 6, 9], pare)
print('Numarul valorilor pare din lista este', c)

v = numarare('aeroport', vocale)
print('Numarul vocalelor din sir este', v)

n = 5
L = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1)]
np = numarare(L, perechiEgale)
print("Numarul perechilor cu componente egale:", np)

L = "Ana are mere si pere mai multe mere decat pere".split()
lmax = max([len(cuv) for cuv in L])
for k in range(1, lmax + 1):
    ncuv = numarare(L, lungimeSir(k))
    print("Numarul de cuvinte cu lungimea", k, "este", ncuv)

L = [10, 142, 24, 17, 18, 100, 13, 15]
print(numarare(L, cmmdcEsteT(4, 2)))
