# citim triunghiul de numere din fișierul text "triunghi.txt"
with open("triunghi.txt") as f:
    t = []
    for line in f:
        aux = [int(x) for x in line.split()]
        t.append(aux)
    f.close()

# creăm un triunghi smax de aceeași dimensiune cu triunghiul t
# smax[i][j] reprezinta suma maxima care SE TERMINA cu elementul t[i][j]
n = len(t)
smax = [[0] * (i + 1) for i in range(n)]

# copiem prima linie din t in smax
smax[0][0] = t[0][0]

# completez restul de smax
# smax[i][j] = t[i][j] + smax[i-1][j] daca sunt pe prima coloana
# smax[i][j] = t[i][j] + smax[i-1][j-1] daca sunt pe diagonala
# smax[i][j] = t[i][j] + max(smax[i-1][j], smax[i-1][j-1]) in rest

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            smax[i][j] = t[i][j] + smax[i - 1][j]
        elif j == i:
            smax[i][j] = t[i][j] + smax[i - 1][j - 1]
        else:
            smax[i][j] = t[i][j] + max(smax[i - 1][j], smax[i - 1][j - 1])

# afisam valoarea maxima din ultima linie a triunghiului, ea este smax din triunghi
suma = max(smax[n - 1])
pmax = smax[n - 1].index(suma)
# print(smax)

# afisam traseul
# pt fiecare linie stocam indicii coloanelor lui t[i][j] folositi pt smax intr-un vector
# dupa care facem reverse la vectorul de indici ca sa afisam traseul din varf spre baza
sol = []
sol.append(pmax)
j = pmax
for i in range(n - 2, 0, -1):
    x = max(smax[i][j], smax[i][j - 1])
    index = smax[i].index(x)
    sol.append(index)
    j = index

sol.append(0)
sol.reverse()

print("\nTraseul cu suma maxima:")
for i in range(n - 1):
    print("{}({}, {}) -> ".format(t[i][sol[i]], i, sol[i]), end="")
print("{}({}, {})".format(t[n - 1][sol[n - 1]], n - 1, sol[n - 1]))
