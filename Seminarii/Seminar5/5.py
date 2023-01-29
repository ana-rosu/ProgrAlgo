'''
Planificarea unor proiecte cu profit maxim
Se consideră 𝑛 proiecte, pentru fiecare proiect cunoscându-se profitul, un termen limită
(sub forma unei zi din lună) și faptul că implementarea sa durează exact o zi. Să se
găsească o modalitate de planificare a unor proiecte astfel încât profitul total să fie
maxim.
'''

with open('proiecte.in') as f:
    proiecte = []
    for line in f:
        aux = line.split()
        proiecte.append((aux[0], int(aux[1]), int(aux[2])))

proiecte.sort(key=lambda t: -t[2])

zile = max([proiect[1] for proiect in proiecte])
# planificarea optimă va fi construită folosind un dicționar
# cu intrări de forma zi: proiect
planificare = {k: None for k in range(1, zile + 1)}
profit = 0
for proiect in proiecte:
    for zi in range(proiect[1], 0, -1):
        if planificare[zi] is None:
            planificare[zi] = proiect
            profit += proiect[2]
            break

with open('proiecte.out', 'w') as f:
    for zi in planificare:
        if planificare[zi] != None:
            f.write('Ziua {}: {} {}\n'.format(zi, planificare[zi][0], planificare[zi][2]))
    f.write(f'\nProfit maxim: {profit}')
