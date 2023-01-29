# Problema mulțimii de acoperire / Problema cuielor
'''
Fie 𝑛 intervale închise 𝐼1 = [𝑎1, 𝑏1], … ,𝐼𝑛 = [𝑎𝑛, 𝑏𝑛]. Să se determine o mulțime 𝑀 cu
număr minim de elemente astfel încât oricare ar fi intervalul Ik ∃𝑥 ∈ 𝑀 astfel încat 𝑥 ∈ 𝐼𝑘 = [𝑎𝑘, 𝑏𝑘
].
Mulțimea 𝑀 se numește mulțime de acoperire a șirului de intervale respectiv.

Observatie:
Problema mai este cunoscută și sub numele de problema cuielor: "Se consideră 𝑛
scânduri, fiecare fiind dată printr-un interval închis de pe axa reală. Să se determine
numărul minim de cuie pe care trebuie să le batem astfel încât în fiecare scândură să fie
bătut cel puțin un cui. Se consideră faptul că orice cui are o lungime suficient de mare
pentru a trece prin oricâte scânduri este nevoie.".
'''
# 𝒪(𝑛log2 𝑛)
with open('intervale.txt') as fin:
    intervale = []
    for linie in fin:
        aux = linie.split()
        intervale.append((int(aux[0]), int(aux[1])))

# sortez intervalele dupa extremitatea din dreapta
intervale.sort(key = lambda t: t[1])

# primul cui trebuie batut in extremitatea dreapta a primei scanduri
M = [intervale[0][1]]
# pentru fiecare dintre scandurile ramase verificam daca exista deja un cui batut in ea
# adica daca extremitatea sa din stanga este strict mai mica decat valorea ultimului cui batut
for icrt in intervale[1:]:
    if icrt[0] > M[len(M)-1]:
        M.append(icrt[1])

with open('acoperire.txt', 'w') as fout:
    fout.write('\n'.join([str(x) for x in M]))


