# În vitrina magazinului CheapLuxury bijuteriile din aur sunt așezate pe 𝑚 ≥ 3 rânduri, iar
# pe fiecare rând sunt câte 𝑛 ≥ 3 bijuterii. Hoțul Gicuță vrea să spargă vitrina magazinului
# și să fure bijuteriile, dar, deoarece sistemul de alarmă al magazinului este foarte
# performant, el își dă seama că are nevoie de un plan bine pus la punct. În acest scop, Gicuță
# se gândește să fure de pe fiecare din cele 𝑚 rânduri câte o singură bijuterie astfel încât
# valoarea totală a acestora să fie maximă și, fiind lacom, vrea ca valoarea fiecărei bijuterii
# să fie strict mai mare decât valoarea bijuteriei furate de pe rândul precedent.

# Scrieți un program Python care citește de la tastatură două numere naturale nenule m și
# n, o matrice cu m linii și n coloane care conține pe linia 𝑖 valorile bijuteriilor de pe rândul
# 𝑖 exprimate în euro, după care afișează pe ecran, în forma indicată în exemplu, valoarea
# totală a bijuteriilor pe care trebuie să le fure Gicuță, precum și pozițiile acestora
# (rândurile sunt considerate ca fiind numerotate de la 1, la fel și pozițiile bijuteriilor în
# cadrul unui rând). Dacă nu există nicio modalitate de a fura bijuteriile conform
# restricțiilor indicate, atunci programul va afișa mesajul “Imposibil”
with open('1.in') as f:
    aux = f.readline().split()
    m, n = int(aux[0]), int(aux[1])

    M=[]
    for line in f:
        aux = [float(x) for x in line.split()]
        M.append(aux)

for i in range(len(M)):
    M[i].sort(reverse=True)

s = 0
ult_bij = M[m-1][0]
s+=ult_bij

for i in range(m-2,-1,-1):
    for j in range(n):
        if M[i][j] < ult_bij:
            s+=M[i][j]
            ult_bij = M[i][j]
            break
    else:
        print('Imposibil')

print(round(s,2))





