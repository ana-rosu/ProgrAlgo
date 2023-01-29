# Complexitate O(nlog2n) -> priority queue

# In Python, clasa PriorityQueue implementează o coadă cu priorități în care un element trebuie să fie un tuplu de forma (𝑝𝑟𝑖𝑜𝑟𝑖𝑡𝑎𝑡𝑒, 𝑣𝑎𝑙𝑜𝑎𝑟𝑒)

# get(): furnizează elementul din coadă care are prioritatea minimă sau, dacă există mai multe elemente cu prioritate minimă, pe primul inserat - 𝒪(log2 𝑛)
# put(element): inserează în coadă un element de forma indicată mai sus - 𝒪(log2 𝑛)
# empty(): returnează True în cazul în care coada nu mai conține niciun element sau False în caz contrar -  𝒪(1)
# qsize(): returnează numărul de elemente din coadă -  𝒪(1)

'''
Vom folosi o coadă cu priorități pentru a memora sălile utilizate,
prioritatea unei săli fiind dată de ora de terminare a ultimului spectacol planificat în ea,
iar spectacolele planificate într-o sală vor fi păstrate folosind o listă

Astfel, vom extrage sala cu timpul minim de terminare al ultimului
spectacol planificat în ea și vom verifica dacă spectacolul curent poate fi planificat în sala
respectivă sau nu (dacă spectacolul curent nu poate fi planificat în această sală, atunci el
nu poate fi planificat în nicio altă sală!).

În caz afirmativ, vom planifica spectacolul curent
în sala respectivă și îi vom actualiza prioritatea la ora de terminare a spectacolului
adăugat.

Altfel vom insera în coadă o sală nouă în care vom planifica spectacolul curent și
prioritatea sălii va fi egală cu ora de terminare a spectacolului respectiv.
'''

import queue

# citim datele de intrare din fișierul text "spectacole.txt"
with open('spectacole.txt') as f:
    lsp = []
    crt = 1
    for line in f:
        aux = line.split('-')
        lsp.append((crt, aux[0].strip(), aux[1].strip()))
        crt += 1

# sortăm spectacolele crescător după orele de început
lsp.sort(key=lambda t: t[1])

# sălile vor fi stocate într-o coadă cu priorități
sali = queue.PriorityQueue()

# planificam primul spectacol in prima sala
sali.put((lsp[0][2], list((lsp[0],))))

# parcurgem restul spectacolelor
for k in range(1, len(lsp)):
    # extragem sala cu ora minima de terminare a ultimului spectacol planificat in ea
    min_timp_final = sali.get()

    # daca spectacolul curent lsp[k] poate fi planificat in sala extrasa, atunci il adaugam in lista
    # spectacolelor planificate in ea si reintroducem sala in coada cu prioritati, dar cu
    # prioritatea actualizata la ora de terminare a spectacolului adaugat
    if lsp[k][1] >= min_timp_final[0]:
        min_timp_final[1].append(lsp[k])
        sali.put((lsp[k][2], min_timp_final[1]))

    # daca spectacolul curent nu poate fi planificat in sala extrasa, atunci
    # reintroducem sala extrasa fara a-i modifica prioritatea si
    # adaugam o sala noua in care planificam spectacolul curent
    else:
        sali.put(min_timp_final)
        sali.put((lsp[k][2], list((lsp[k],))))

# scriem datele de ieșire în fișierul text "programare.txt"
with open('programareNrMinimSali.txt','w') as f:
    f.write(f'Numarul minim de sali: {sali.qsize()}\n')
    scrt = 1
    while not sali.empty():
        sala = sali.get()
        f.write('\n Sala'+ str(scrt) + ':\n')
        for sp in sala[1]:
            f.write(f'\t{sp[1]}-{sp[2]} Spectacol {sp[0]} \n')
        scrt += 1

# în fișierul de ieșire sălile vor fi scrise în ordinea priorităților, nu în ordinea în care au fost inserate!