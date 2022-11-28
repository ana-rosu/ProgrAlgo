linie = input ('Lista: ')
L = [int(x) for x in linie.split()]
nr=0
s = set(L)
unica = list(s)

print('[', end='')
for el in unica:
    perechi = L.count(el)//2
    if perechi !=0:
        nr += perechi
        while perechi!=0:
            print(f'{(el,el)}', end=', ')
            perechi-=1
print(']')

print(nr)