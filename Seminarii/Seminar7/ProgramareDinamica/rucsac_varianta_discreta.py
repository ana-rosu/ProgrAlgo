'''
Pentru a rezolva problema utilizând tehnica programării dinamice, trebuie
să cunoaștem toate câștigurile maxime care se pot obține folosind primele 𝑖 obiecte (𝑖 ∈
{0,1, . . . , 𝑛}), în limita oricărei capacități 𝑗 cuprinse între 0 și 𝐺.
Aplicând tehnica memoizării, vom considera un tablou bidimensional 𝑐𝑚𝑎𝑥 cu 𝑛 + 1 linii și 𝐺 + 1 coloane
în care un element 𝑐𝑚𝑎𝑥[𝑖][𝑗] va memora câștigul maxim care se poate obține folosind
primele 𝑖 obiecte în limita a 𝑗 kilograme. Astfel, relația de recurență care caracterizează
substructura optimală a problemei este următoarea:
𝑐𝑚𝑎𝑥[𝑖][𝑗] = {
                0,                                              dacă i = 0 sau 𝑗 = 0
                𝑐𝑚𝑎𝑥[𝑖 − 1][𝑗],                                  dacă 𝑔𝑖 > 𝑗
                𝑚𝑎𝑥{𝑐𝑚𝑎𝑥[𝑖 − 1][𝑗], 𝑐[𝑖] + 𝑐𝑚𝑎𝑥[𝑖 − 1][𝑗 − 𝑔[𝑖]]}, dacă 𝑔𝑖 ≤ j
            }
Câștigul maxim care se poate obține folosind toate cele 𝑛 obiecte este dat de valoarea
elementului 𝑐𝑚𝑎𝑥[𝑛][𝐺] n-nr de obicte, G - greutatea ghiozdanului.

Pentru a reconstitui o modalitate optimă de încărcare a
rucsacului vom utiliza informațiile din matricea 𝑐𝑚𝑎𝑥, astfel:
-> considerăm doi indici 𝑖 = 𝑛 și 𝑗 = 𝐺;
-> dacă 𝑐𝑚𝑎𝑥[𝑖][𝑗] = 𝑐𝑚𝑎𝑥[𝑖 − 1][𝑗], înseamnă fie că obiectul 𝑂𝑖 nu încape în rucsac,
fie încape, dar nu ar fi fost rentabil să-l încărcăm. Indiferent de motiv, obiectul 𝑂𝑖
nu a fost încărcat în rucsac (nu face parte din soluția optimă), deci trecem la
următorul obiect 𝑂𝑖−1, decrementând valoarea indicelui i
-> dacă 𝑐𝑚𝑎𝑥[𝑖][𝑗] ≠ 𝑐𝑚𝑎𝑥[𝑖 − 1][𝑗], înseamnă că a fost rentabil să încărcăm
obiectul 𝑂𝑖 în limita a 𝑗 kg, deci îl afișăm și trecem la reconstituirea soluției optime
pentru restul de 𝑗 − 𝑔[𝑖] kg folosind obiectele 𝑂1,𝑂2, … ,𝑂𝑖−1, scăzând din indicele
𝑗 valoarea 𝑔[𝑖] și decrementând indicele 𝑖.

Complexitate: 𝒪(𝑛𝐺) ≈ 𝒪(𝑛*2^[log2𝐺]).
'''
# Presupunem ca se citesc de la tastatura/din fisier urm valori:
# capacitatea G a rucsacului
G = 10
# greuatile obiectelor se vor memora intr-o lista g (g[i] = greutatea obiectului i)
# castigurile obiectelor se vor memora intr-o lista c (c[i] = castigul obiectului i)

# ambele liste trebuie sa fie indexate de la 1, deci adaugam in fiecare
# cate o valoare "inexistenta" pe pozitia 0 egala cu 0
g = [0, 5, 2, 20, 3, 4]
c = [0, 80, 50, 400, 60, 70]

# n = nr de obiecte
n = len(g) - 1

# initializam toate elementele matricei cmax cu 0
cmax = [[0 for i in range(G + 1)] for i in range(G + 1)]

# calculam elementele matricei cmax folosind relatia de recurenta
for i in range(1, n + 1):
    for j in range(1, G + 1):
        cmax[i][j] = cmax[i - 1][j]
        if g[i] <= j and c[i] + cmax[i - 1][j - g[i]] > cmax[i - 1][j]:
            cmax[i][j] = c[i] + cmax[i - 1][j - g[i]]

# scriem o modalitate optima de incarcare a rucsacului
print('Castigul maxim: ' + str(cmax[n][G]) + '\n')
i, j = n, G
while i != 0:
    if cmax[i][j] != cmax[i - 1][j]:
        print(i, end=' ')
        j = j - g[i]
    i = i - 1
