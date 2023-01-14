def citire_numere(numef):
    with open (numef) as f:
        M = [[int(nr) for nr in line.split()] for line in f]
    return M

def prelucrare_lista(lista):
    l = []
    l_final = []
    for sublista in lista:
        sublista = [x for x in sublista if x != min(sublista)]
        l.append(sublista)

    lmin = len(l[0])
    for sublista in l[1:]:
        lmin = min(lmin, len(sublista))

    for sublista in l:
        sublista = sublista[:lmin]
        l_final.append(sublista)
    return l_final


m = citire_numere('numere.in')
m = prelucrare_lista(m)

for linie in m:
    for el in linie:
        print(el, end=' ')
    print()

L = citire_numere('numere.in')
k = int(input('Dati k: '))

with open('cifre.out', 'w') as f:
    rez = []
    ok = 0
    for sublista in L:
        for el in sublista:
            if len(str(el)) == k:
                rez.append(el)
                ok = 1
    if ok == 0:
        f.write('Imposibil')
    else:
        rez = list(set(rez))
        rez.sort(key = lambda nr: -nr)
        for el in rez:
            f.write(f'{el} ')