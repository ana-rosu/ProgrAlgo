# SUBIECTUL 2
# a)
f = open('cinema.in')
l = f.read().split('\n')
L = []
for el in l:
    t = tuple(el.split(' % '))
    L.append(t)

date = {}
for t in L:
    if t[0] not in date:
        date[t[0]] = {t[1]: set(t[2].split())}
    else:
        date[t[0]][t[1]] = set(t[2].split())


print(date)
# b)
#returneaza o lista cu/fara filmul film
def sterge_ore(dict, cinema, film, ore):
    for ora in ore:
        dict[cinema][film].discard(ora)
    if dict[cinema][film] == set():
        del dict[cinema][film]
    return list(dict[cinema])

date_copie = date.copy()
d = sterge_ore(date,'Cinema 1', 'Minionii 2', {'12:30', '18:30'})
print(date)
print(d)

# c) lista de tupluri (nume_film, nume_cinema, lista_de_ore) cu filmele care încep la cel puțin unul dintre cinematografele primite ca parametru între orele ora_minima și ora_maxima
def cinema_film(dict, ora_minima, ora_maxima, *cinematografe):
    L = []
    for cinema in cinematografe:
        print()
        print(cinema)
        for film in dict[cinema]:
            print(film, end=" ")
            ore = []
            for ora in dict[cinema][film]:
                if ora_minima <= ora <= ora_maxima:
                    ore.append(ora)
            t = (film, cinema, ore)
            if len(ore) != 0:
                L.append(t)
    return L

