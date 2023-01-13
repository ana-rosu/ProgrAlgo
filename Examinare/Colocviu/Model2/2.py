def modifica_prefix(x, y, prop):
    prop_modif = ''
    cnt = 0
    for cuv in prop.split():
        if cuv.startswith(x):
            prop_modif += cuv.replace(x, y, 1) + ' '
            cnt += 1
        else:
            prop_modif += cuv + ' '
    return prop_modif, cnt

def poz_max(lista):
    rez = [index for index, value in enumerate(lista, start=1) if value == max(lista)]
    return rez

with open('propozitii_modificate.out', 'w') as f:
    with open('propozitii.in') as g:
        aux = [' '.join(linie.split()) for linie in g.readlines()]
        l = []
        for prop in aux:
            prop_mod, cnt = modifica_prefix('cea', 'ca', prop)
            l.append(cnt)
            f.write(prop_mod + '\n')

        print(*poz_max(l))