# Se consideră 𝑛 șiruri de numere sortate crescător. Știind faptul că interclasarea a două
# șiruri de lungimi 𝑝 și 𝑞 are complexitatea 𝒪(𝑝 + 𝑞), să se determine o modalitate de
# interclasare a celor 𝑛 șiruri astfel încât complexitatea totală să fie minima
# Exemplu :
# Fie 4 siruri avand lungimile 30,20,10,25.
# Interclasarea primelor 2 necesita 50 de operatii elementare si obtinem un nou sir de lungime 50
# Mai avem de interclasat 3 siruri de lungimi 50,10,25
# Analog, mai avem de interclasat 2 siruri de lungimi 60,25
# Interclasarea celor 2 siruri mai necesita 85 de operatii
# => nr total de operatii elementare este 50+60+85 = 195
# => obtinem un sir final de lungime 85

# Numarul minim de operatii elementare se obtine interclasand de fiecare data cele mai mici 2 siruri dpdv al lungimilor
# Pt sirurile cu lungimi 30,20,10,25:
# 20+10 = 30
# 30+25 = 55
# 55+30 = 85
# 30+55+85=170
import queue

# functie pt interclasare a 2 siruri sortate crescator
def interclasare(a,b):
    i = j = 0
    rez = []
    while i < len(a) and j < len(b):
        if a[i]<=b[j]:
            rez.append(a[i])
            i+=1
        else:
            rez.append(b[j])
            j+=1
    rez.extend(a[i:])
    rez.extend(b[j:])

    return rez

# fiecare linie din fișierul text de intrare siruri.txt
# conține câte un șir ordonat crescător
f = open('siruri.txt')
siruri = queue.PriorityQueue()
for linie in f:
    aux = [int(x) for x in linie.split()]
    siruri.put((len(aux), aux))
f.close()

# t = nr total de operatii elementare efectuate
t = 0
while siruri.qsize()!=1:
    # extragem primele două șiruri a și b cu lungimi minime
    a = siruri.get()
    b = siruri.get()
    # interclasăm șirurile a și b
    r = interclasare(a[1], b[1])
    # actualizăm numărul total de operații elementare
    t = t + len(r)
    # introducem în coada cu priorități șirul r rezultat
    # prin interclasarea șirurilor a și b
    siruri.put((len(r), r))

# afisam rezultatele
print("Numar minim de operații elementare:", t)
r = siruri.get()[1]
print("Șirul obținut prin interclasarea tuturor șirurilor:", *r)