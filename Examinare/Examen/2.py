'''
Considerăm n spectacole S1, S2, ..., Sn pentru care cunoaștem intervalele lor de desfășurare
[s1, f1), ..., [sn, fn), toate dintr-o singură zi. Având la dispoziție o singură sală, în care putem
să planificăm un singur spectacol la un moment dat, să se determine numărul maxim de
spectacole care pot fi planificate fără suprapuneri. Un spectacol Sj poate fi programat
după spectacolul Si dacă sj ≥ fi. Justificați corectitudinea programului și complexitatea sa.
'''
# Solutia 1
with open('spectacole.txt') as f:
    lsp = [] # lista spectacole
    crt = 1
    for line in f:
        aux = line.split('-')
        lsp.append((crt, aux[0].strip(), aux[1].strip()))
        crt+=1

# le sortez crescator dupa ora de final a unui spectacol
lsp.sort(key = lambda t: t[2])
psp = [lsp[0]] # lista cu planificare spectacole
for sp in lsp[1:]:
    if sp[1]>=psp[len(psp)-1][2]:
        psp.append(sp)

print(len(psp))

# Solutia implementata cu ajutorul unei cozi cu prioritati
# import queue
#
# with open('spectacole.txt') as f:
#     lsp = []
#     crt = 1
#     for line in f:
#         aux = line.split('-')
#         lsp.append((crt, aux[0].strip(), aux[1].strip()))
#         crt += 1
#
# # sortăm spectacolele crescător după orele de final
# lsp.sort(key=lambda t: t[2])
#
# # sălile vor fi stocate într-o coadă cu priorități
# plan = queue.PriorityQueue()
#
# # planificam primul spectacol
# # (prioritate = ora de terminare a spectacolului, valoare = lista de spectacole planificate)
# plan.put((lsp[0][2], list((lsp[0],))))
#
# # parcurgem restul spectacolelor
# for k in range(1, len(lsp)):
#     # extragem spectacolul cu ora minima de terminare
#     ora_de_terminare, spectacole_planificate = plan.get()
#
#     # daca spectacolul curent lsp[k] poate fi planificat dupa el, atunci il adaugam in list reintroducem planul in coada cu prioritati, dar cu
#     # prioritatea actualizata la ora de terminare a spectacolului adaugat
#     if lsp[k][1] >= ora_de_terminare:
#         spectacole_planificate.append(lsp[k])
#         plan.put((lsp[k][2], spectacole_planificate))
#
#     # daca spectacolul curent nu poate fi planificat, atunci reintroducem planul fara a-i modifica prioritatea si
#     else:
#         plan.put((ora_de_terminare, spectacole_planificate))
#
# while not plan.empty():
#     ultima_ora, spectacole = plan.get()
#     print(len(spectacole))

# SOLUTIA MEA
# import queue
#
# with open('spectacole.txt') as f:
#     lsp = []
#     crt = 1
#     for line in f:
#         aux = line.split('-')
#         lsp.append((crt, aux[0].strip(), aux[1].strip()))
#         crt += 1
#
# # sortăm spectacolele crescător după orele de final
# lsp.sort(key=lambda t: t[2])
#
# # sălile vor fi stocate într-o coadă cu priorități
# plan = queue.PriorityQueue()
#
# # planificam primul spectacol
# # (prioritate = ora de terminare a spectacolului, valoare = spectacolul)
# plan.put((lsp[0][2], lsp[0]))
#
# # parcurgem restul spectacolelor
# for k in range(1, len(lsp)):
#     ora_de_terminare, spectacol = plan.get()
#
#     if lsp[k][1] >= ora_de_terminare:
#         plan.put((lsp[k][2], lsp[k]))
#     plan.put((ora_de_terminare, spectacol))
#
# while not plan.empty():
#     ora, sp = plan.get()
#     print(sp)