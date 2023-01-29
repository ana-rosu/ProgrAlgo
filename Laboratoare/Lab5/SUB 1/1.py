# SUBIECTUL 1

#a)
def citire_numere(numef):
    f = open(numef)
    s = f.readline()
    l = []
    while s != '':
        l.append([int(x) for x in s.split()])
        s = f.readline()
    return l

#b)
def prelucrare_lista(lista_de_liste):
    minim = len(lista_de_liste[0])
    for lista in lista_de_liste:
        x = min(lista)
        while lista.count(x) != 0:
            lista.remove(x)

        # if len(lista) < minim:
        #     minim = len(lista)

    minim = min([len(lista) for lista in lista_de_liste])
    # lista_de_liste[:] = [lista[:minim] for lista in lista_de_liste]
    for lista in lista_de_liste:
        lista[minim:] = []
    return lista_de_liste


#c)
# l = citire_numere('numere.in')
# l = prelucrare_lista(l)
# for sublista in l:
#     for el in sublista:
#         print(el, end=' ')
#     print()

#d)
l = citire_numere('numere.in')
k = int(input('Introduceti un nr nat nenul: '))
f = open('cifre.out', 'w')

lista_despachetata = []
for sublista in l:
    lista_despachetata.extend(sublista)

lista_despachetata = list(set(lista_despachetata))
lista_despachetata.sort(reverse=True)

for nr in lista_despachetata:
        if len(str(nr)) == k:
            f.write(str(nr) + ' ')

