v = [2,5,3]
p = 12

# initializam listele nrmin si pred
nrmin = [p+1] * (p+1)
nrmin[0] = 0
pred  = [-1] * (p+1)
# calculăm valorile nrmin[1],..., nrmin[P]
# folosind relația de recurență 𝑛𝑟𝑚𝑖𝑛[𝑖] = {1 + min{𝑛𝑟𝑚𝑖𝑛[𝑖 − 𝑣[𝑗]]|𝑣[𝑗] ≤ 𝑖}, pentru 1 ≤ 𝑖 ≤ p
for suma in range(1,p+1):
    for moneda in v:
        if moneda <= suma and 1 + nrmin[suma-moneda] < nrmin[suma]:
            nrmin[suma] = 1 + nrmin[suma-moneda]
            pred[suma] = moneda

# afisam datele de iesire
if nrmin[p] == p+1:
    print(f'Suma {p} nu poate fi platita cu monedele {v}')
else:
    print(f'Numarul minim de monede necesare pt a plati suma {p} este {nrmin[p]}')
    print('O modalitate de plata: ')
    suma = p
    while pred[suma] != -1:
        print(pred[suma], end = ' ')
        suma = suma - pred[suma]
