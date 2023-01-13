def faraSemne(sir):
    semne = ',.?!;'
    for s in semne:
        sir = sir.replace(s, '')
    return sir

with open('teatru.in') as f:
    d = {}
    for line in f:
        line = faraSemne(line).lower()
        personaj = line[:line.find(':')]
        cuvinte = line[line.find(':')+1:].strip()
        for cuv in cuvinte.split():
            if cuv not in d:
                d[cuv] = {personaj}
            else:
                d[cuv].add(personaj)

l = sorted(list(d.items()), key = lambda t: (-len(t[1]), t[0]))

with open('teatru.out', 'w') as f:
    for t in l:
        f.write(f'{t[0]} : ' + ', '.join([nume[0].upper()+nume[1:] for nume in t[1]]) + '\n')