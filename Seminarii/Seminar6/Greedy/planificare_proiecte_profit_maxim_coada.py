# Complexitate 𝒪(𝑛 log2 𝑛) - coada cu prioritati
# fiecare termen limită strict mai mare decât numărul 𝑛 de proiecte îl vom înlocui cu 𝑛
# sortam proiectele descrescator dupa termenul limita
# pentru fiecare zi 𝑧𝑐𝑟𝑡 de la 𝑛 la 1 procedăm în următorul mod:
#     ▪ introducem într-o coadă cu priorități toate proiectele care au termenul limită 𝑧𝑐𝑟𝑡, considerând prioritatea unui proiect ca fiind dată de profitul său;
#     ▪ extragem proiectul cu profit maxim și îl planificăm în ziua 𝑧𝑐𝑟t

# !! Deoarece clasa PriorityQueue din pachetul queue implementează o coadă cu priorități
# care permite extragerea minimului, vom considera prioritatea unui proiect ca fiind egală
# cu –profit.

import queue

with open('proiecte.in') as f:
    toate_liniile = f.readlines()

n = len(toate_liniile)

lp = [] #lista cu toate proiectele
for linie in toate_liniile:
    aux = linie.split()
    lp.append((-float(aux[2]), min(int(aux[1]), n), aux[0]))

# sortăm proiectele descrescător după termenul limită
lp.sort(key = lambda t:-t[1])
# planificarea optimă o vom memora într-un dicționar
# cu intrări de forma zi:proiect
planificare = {k: None for k in range(1, n + 1)}
# coada cu priorități (prioritatea = -profit)
coada = queue.PriorityQueue()
k = 0
profitmax = 0
for zcrt in range(n, 0, -1):
    # încărcăm în coadă toate proiectele care au
    # termenul limită egal cu zcrt
    while k <= n - 1 and lp[k][1] == zcrt:
        coada.put(lp[k])
        k += 1
        # extragem din coadă proiectul cu profit maxim și
        # îl planificăm în ziua zcrt
        if coada.qsize() > 0:
            planificare[zcrt] = coada.get()
        profitmax += abs(planificare[zcrt][0])
# scriem o planificare optimă în fișierul text proiecte.out
fout = open("proiecte.out", "w")
for z in planificare:
    if planificare[z] != None:
        fout.write("Ziua " + str(z) + ": " + planificare[z][2] + " " + str(abs(planificare[z][0])) + "\n")
fout.write("\nProfit maxim: " + str(profitmax))
fout.close()