'''
Vezi curs 14 pentru explicatii detaliate!
Avem triunghiul:
10
-2 15
13 -8 -10
-17 1 21 16
7 3 -11 14 1
'''
# Complexitate O(n^2)
# citim triunghiul de numere din fișierul text "triunghi.txt"
with open("triunghi.txt") as f:
    t = []
    for line in f:
        aux = [int(x) for x in line.split()]
        t.append(aux)
    f.close()

# creăm un triunghi smax de aceeași dimensiune cu triunghiul t
# smax[i][j] reprezinta suma maxima care INCEPE cu elementul t[i][j]
n = len(t)
smax = [[0] * (i + 1) for i in range(n)]

# copiem ultima linie a triunghiului t in triunghiul smax
n = len(t)
for i in range(n):
    smax[n - 1][i] = t[n - 1][i]

# completez smax de la penultima linie in sus, cu valoarea t[i][j] + max(t[i+1][j], t[i+1][j+1]
for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        smax[i][j] = t[i][j] + max(smax[i + 1][j + 1], smax[i + 1][j])

print(smax)
# afisam suma maxima
print(smax[0][0])

# afișăm un traseu pe care se poate obține suma maximă
print('\nTraseul cu suma maxima: ')
j = 0
for i in range(n - 1):
    print("{}({}, {}) -> ".format(t[i][j], i, j), end="")
    if smax[i + 1][j + 1] > smax[i + 1][j]:
        j += 1
print("{}({}, {})".format(t[n - 1][j], n - 1, j))
