# Problema plății unei sume folosind monede cu valori date
'''
Considerând faptul că avem la dispoziție 𝑛 monede cu valorile 𝑣1, 𝑣2, … , 𝑣𝑛 pe care
putem să le folosim pentru a plăti o sumă 𝑃, trebuie să determinăm toate modalitățile în
care putem realiza acest lucru (vom presupune faptul că avem la dispoziție un număr
suficient de monede de fiecare tip).

Exemplu:
Dacă avem la dispoziție 𝑛 = 3 tipuri de monede cu valorile 𝑣 = (2$, 3$, 5$),
atunci putem să plătim suma 𝑃 = 12$ în următoarele 5 moduri:
4 × 3$, 1 × 2$ + 2 × 5$, 2 × 2$ + 1 × 3$ + 1 × 5$, 3 × 2$ + 2 × 3$ și 6 × 2$

!!! deoarece problema nu are întotdeauna soluție (de exemplu, dacă toate monedele date
au valori pare și suma de plată este impară), vom adăuga o variabila nrs care să
contorizeze numărul soluțiilor găsite, iar după terminarea algoritmului vom verifica
dacă problema a avut cel puțin o soluție sau nu.

!!! Pentru ca mink = 0, vom efectua apelul recursiv bkt(k+1) doar în cazul în care k<n!
'''
'''
s[k] - numărul de monede cu valoarea v[k] utilizate pentru plata sumei P,
deci obținem mink=0 și maxk=P/v[k]
'''


def bkt(k):
    global s, P, v, n

    for i in range(0, P // v[k] + 1):
        s[k] = i
        scrt = sum([s[i] * v[i] for i in range(k + 1)])
        if scrt <= P:
            if scrt == P and k == n:
                for i in range(1, n + 1):
                    if s[i] != 0:
                        print(s[i], "x", v[i], "$ + ", end="")
                print()
        else:
            if k < len(v[1:]):
                bkt(k + 1)

P = 12
# pt valori de monede citite de la tastatura:
# aux = [int(x) for x in input("Valorile monedelor: ").split()]
# v = [0]
# v.extend(aux)
# n = len(v[1:])
v = [2, 3, 5]
n = len(v)
s = [0] * (n + 1)
bkt(1)
