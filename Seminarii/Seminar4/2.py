def cauta(x, *args):
    lista = []
    for list in args:
        if x in list:
            lista.append(list)
    return lista


x = 7
r = cauta(x, [5, 1, 7, 3, 7], [2, 3], [-3, 7, 1])

if r == []:
    print("Valoarea", x, "nu se gaseste in nicio lista!\n")
else:
    print("Valoarea", x, "se gaseste in listele urmatoare:")
print(*r, sep="\n")
