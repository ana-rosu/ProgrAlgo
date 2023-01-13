def faraSemne(s):
    return "".join([x for x in s if x.isalnum() or x == '-'])

with open("text.in", 'r') as f:
    cuv = faraSemne(f.readline().lower())
    aux = [faraSemne(x) for x in f.read().lower().split()]


multime = set(cuv + '-')
d = dict()

for cuvant in aux:
    if set(cuvant) & multime == set(cuvant):
        aux = list(set(cuvant) - set('-'))
        aux.sort()
        cheie = tuple(aux)
        if cheie in d.keys():
            d[cheie].append(cuvant)
        else:
            d[cheie] = [cuvant]

chei = list(d.keys())
chei.sort(key=lambda x: (-len(x), str(x)) )

with open("text.out", 'w') as g:
    for cheie in chei:
        g.write(f'Literele {list(cheie)}:\n')
        d[cheie] = list(set(d[cheie]))
        d[cheie].sort(key=lambda x: (-len(x), x) )
        g.write('\n'.join(d[cheie]))
        g.write('\n')
    if chei == []:
        g.write("Imposibil")
