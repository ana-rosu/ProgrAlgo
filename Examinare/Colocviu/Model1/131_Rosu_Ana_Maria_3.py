# Rosu Ana Maria grupa 131
# SUB 3

with open('legaturi.in', 'r') as f:
    aux = [linie.split() for linie in f.readlines()]
    print(aux)
d = {}
for linie in aux:
    p1 = tuple([int(x) for x in linie[0][1:-1].split(',')])
    p2 = tuple([int(x) for x in linie[1][1:-1].split(',')])
    culoare = linie[2]
    eticheta = ' '.join(linie[3:])
    d[(p1, p2)] = (culoare, eticheta)

def insereaza_legatura(date, x, y, culoare, eticheta):
    if (x,y) in date.keys() or (y,x) in date.keys():
        return False
    else:
        date[(x,y)] = (culoare, eticheta)
    return date

d = insereaza_legatura(d, (1,3), (2,7), 'negru', 'legatura noua')

# for key, value in d.items():
#     print(list(key[0]), list(key[1]), value[0], value[1])

def vecini(date, *tupluri):
    v = []
    for tuplu in tupluri:
        vec = []
        for key in date.keys():
            if key[0] == tuplu:
                vec.append(key[1])
            elif key[1] == tuplu:
                vec.append(key[0])
        v.append(set(vec))
    # intersectie multimi v[i]
    aux = v[0]
    for multime in v[1:]:
        aux = aux & multime

    aux = sorted(aux, key = lambda t: -t[1])
    return aux


print(vecini(d, (2,7), (1,2)))