with open('text.in') as f:
    aux = set(f.readline())
    aux.remove('\n')

    rest = f.read().lower()
semne = '.,!?'
for s in semne:
    rest = rest.replace(s, '')

d = {}
for cuv in rest.split():
    s = set(cuv)
    s.discard('-')
    if s & aux == s:
        t = tuple(sorted(s))
        if t not in d:
            d[t] = [cuv]
        else:
            if cuv not in d[t]:
                d[t].append(cuv)

lista = sorted(d.items(), key = lambda key: key)

with open('text.out', 'w') as f:
    if lista == []:
        f.write('Imposibil')
    for tuplu in lista:
        f.write(f'Literele {list(tuplu[0])}:' + '\n')
        cuvinte = tuplu[1]
        cuvinte= sorted(cuvinte, key= lambda cuv : len(cuv))
        for cuv in tuplu[1]:
            f.write(cuv + '\n')
