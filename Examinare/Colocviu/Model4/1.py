def fara_semne(sir):
    semne = ',.:;!?'
    for semn in semne:
        sir = sir.replace(semn, '')
    return sir

with open('text.in') as f:
    s = f.read().lower()
    aux = [x for x in fara_semne(s).split()]

d = dict()
multime = set(aux)
for cuv in multime:
    nr = aux.count(cuv)
    if nr not in d:
        d[nr] = [cuv]
    else:
        d[nr].append(cuv)


with open('text.out', 'w') as f:
    for i in sorted(d.keys(), reverse=True):
        f.write(f'Frecventa {i}: ' + '\n')
        l = sorted(d[i])
        for el in l:
            f.write(f'{el}' + '\n')
