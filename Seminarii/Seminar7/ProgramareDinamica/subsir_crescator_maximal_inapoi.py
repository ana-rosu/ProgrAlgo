t = [9,7,3,6,2,8,5,4,5,8,7,10,4]

# lmax[i] = lungimea maxima a unui subsir care se termina cu t[i]
# pred[i] = pozitia elementului in fata caruia a fost alipit t[i] sau -1 daca nu poate fi alipit
n = len(t)
lmax = [1] * n
pred = [-1 for i in range(n)]

for i in range(1,n):
    for j in range(i):
        if t[j] <= t[i] and lmax[i] < 1 + lmax[j]:
            lmax[i] = 1 + lmax[j]
            pred[i] = j

# pozitia elementului t[i] - elem cu care se termina cel mai lung subsir maximal
pmax = lmax.index(max(lmax))

# reconstituim sirul de la coada la cap, apoi il afisam reversed
sol = []
i = pmax
while i != -1:
    sol.append(t[i])
    i = pred[i]

sol.reverse()
print("Lungimea maxima a unui subsir crescator:", lmax[pmax])
print("Un subsir crescator maximal:")
print(sol)
