'''
Să se determine un subșir crescător de lungime maximă al unui șir t format din n numere
întregi.
'''
t = [5,7,-13,4,9,7,3,15,6,20,2]
n = len(t)
# lmax[i] - subsir maximal care incepe cu t[i]
lmax = [1] * (n+1)
succ = [-1] * (n+1)

for i in range(n-2, -1,-1):
    for j in range(i+1,n):
        if t[i] <= t[j] and lmax[i] < 1 + lmax[j]:
            lmax[i] = 1+lmax[j]
            succ[i]=j

l = max(lmax)
pmax = lmax.index(l)

i = pmax
while i!=-1:
    print(t[i], end=' ')
    i = succ[i]

