d = {}
with open('drumuri.in') as f:
    for linie in f:
        linie = linie.split("-")
        linie = [x.split() for x in linie]
        oras1 = " ".join(linie[0])
        oras2 = " ".join(linie[1][:-2])
        dist = int(linie[1][-2])
        stare = int(linie[1][-1])
        d[(oras1, oras2)] = (dist, stare)


def modifica_stare(d, s, o1, o2=''):
    cnt = 0
    if o2 != '' and (o1, o2) in date.keys():
        d[(o1, o2)] = (d[(o1, o2)][0], s)
        cnt += 1
    else:
        chei = [x for x in d.keys() if x[0] == o1]
        for cheie in chei:
            d[cheie] = ( d[cheie][0], s)
            cnt += 1
    return cnt

def accesibil(d, *nume_orase):
    l = []
    for key in d.keys():
        if key[0] in nume_orase:
            l.append(key[1])
        elif key[1] in nume_orase:
            l.append(key[0])
    return set(l)

print(d)
modifica_stare(d, 4, 'Oraselul Mic')
print(d)
orase = accesibil(d, 'Oraselul Mic', 'Capitala')
print(orase)

