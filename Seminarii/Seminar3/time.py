import time

nr_elemente = 100000

start = time.time()
lista = [x for x in range(nr_elemente)]
stop = time.time()
print(" Initializare: ", stop - start, "secunde")

start = time.time()
lista = []
for x in range(nr_elemente):
    lista.append(x)
stop = time.time()
print(" Metoda append(): ", stop - start, "secunde")

start = time.time()
lista = []
for x in range(nr_elemente):
    lista += [x]
stop = time.time()
print(" Operatorul +=: ", stop - start, "secunde")

start = time.time()
lista = [0] * nr_elemente
for x in range(nr_elemente):
    lista[x] = x
stop = time.time()
print(" Index: ", stop - start, "secunde")

start = time.time()
lista = []
for x in range(nr_elemente):
    lista = lista + [x]
stop = time.time()
print(" Operatorul +: ", stop - start, "secunde")


'''
Rezultatele sunt:
 Initializare:  0.0010383129119873047 secunde
 Metoda append():  0.01862335205078125 secunde
 Operatorul +=:  0.015999794006347656 secunde
 Index:  0.00919795036315918 secunde
 Operatorul +:  36.313913106918335 secunde
 
Se observă faptul că primele 4 variante au timpi de executare aproximativi egali, iar
ultima variantă are un timp de executare mult mai mare din cauza faptului că la fiecare
operație de concatenare a listei [x] la lista curentă se creează în memorie o copie a listei
curente, se adaugă la sfârșitul copiei noua valoare x și apoi referința listei curente se
înlocuiește cu referința copiei.
'''