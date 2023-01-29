with open('rucsac.in') as f:
    g = float(f.readline())
    # fiecare dintre urmatoarele linii contine
    # greutatea si castigul unui obiect
    obiecte = []
    crt = 1
    for linie in f:
        aux = linie.split()
        # aux[0] -  greutatea obiectului
        # aux[1] - castigul obiectului
        obiecte.append((crt, float(aux[0]), float(aux[1])))
        crt += 1

# sortam obiectele in functie de castigul unitar
# (vrem in ordine crescatoare obiectele cu greutate mica si castig mare)
obiecte.sort(key=lambda t: -t[2] / t[1])

print(obiecte)
n = len(obiecte)
solutie = [0] * n

spatiu_liber_rucsac = g
for i in range(n):
    if spatiu_liber_rucsac - obiecte[i][1] >= 0:
        spatiu_liber_rucsac -= obiecte[i][1]
        solutie[i] = 1
    else:
        solutie[i] = spatiu_liber_rucsac / obiecte[i][1]
        break

# calculam castigul
castig = sum([solutie[i] * obiecte[i][2] for i in range(n)])

# scriem datele de ieșire în fișierul text "rucsac.out"
with open('rucsac.out', 'w') as f:
    f.write(f'Castig maxim: {castig}\n\n')
    for i in range(n):
        if solutie[i]!=0:
            procent = format(solutie[i]*100,'.2f')
            f.write(f'Obiect {obiecte[i][0]}: {procent}%\n')