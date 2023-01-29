t = [9, 7, 3, 6, 2, 8, 5, 4, 5, 8, 7, 10, 4]
n = len(t)

# lmax[i] = lungimea maxima a unui subsir crescator maximal care incepe cu t[i]
lmax = [1] * n
# succ[i] = pozitia elementului in fata caruia va fi alipit t[i] pt a forma un subsir crescator maximal sau -1 daca nu poate fi alipit
succ = [-1] * n

lmax[n - 1] = 1
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if t[i] <= t[j] and lmax[i] < 1 + lmax[j]:
            lmax[i] = 1 + lmax[j]
            succ[i] = j

pmax = lmax.index(max(lmax))
i = pmax
while i != -1:
    print(t[i], end=' ')
    i = succ[i]
