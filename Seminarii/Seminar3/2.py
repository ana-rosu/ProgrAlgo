'''Fișierul text 2.in conține numere naturale despărțite prin spații și scrise pe mai
multe linii. Să se scrie în fișierul text 2.out numerele care apar pe toate
liniile din fișier.
Exemplu: Dacă fișierul 2.in are următorul conținut:
2 1 5 1 3
1 4 2 2
2 1 1 6 8
atunci fișierul 2.out trebuie să conțină numerele 1 2, nu neapărat în această
ordine.'''
f = open('2.in')
s = f.readline()
m = set([int(nr) for nr in s.split()])
while s != '':
    s = f.readline()
    if s != '':
        crt = set([int(nr) for nr in s.split()])
        m = m & crt  # sau m.intersection(crt)
        if m == set():
            break
f.close()

f = open('2.out', 'w')
if len(m) != 0:
    f.write(' '.join(str(x) for x in m))
else:
    f.write('Nu exista numere comune tuturor liniilor')
