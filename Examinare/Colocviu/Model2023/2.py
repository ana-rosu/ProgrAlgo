def citire_date():
    d = {}
    with open('cinema.in') as f:
        for line in f:
            aux = [x for x in line.split(' % ')]
            cinema = aux[0]
            film = aux[1]
            ore = [x for x in aux[2].split()]
            if cinema not in d:
                d[cinema] = {film: ore}
            else:
                d[cinema][film] = ore
    return d

def sterge_ore(date, cinema, film, ore):
    ore_ramase = []
    for ora in date[cinema][film]:
        if ora not in ore:
            ore_ramase.append(ora)
    date[cinema][film] = ore_ramase

    l = []
    for film, ore in date[cinema].items():
        if ore != []:
            l.append(film)
    return l

def cinema_film(date, ora_minima, ora_maxima, *cinemas):
    l = []
    for cinema in cinemas:
        for film, ore in date[cinema].items():
            lista_ore = []
            for ora in ore:
                if ora_minima <= ora <= ora_maxima:
                    lista_ore.append(ora)
            if lista_ore != []:
                l.append((film, cinema, lista_ore))
    l.sort(key = lambda t:(t[0], -len(t[2])))
    return l

#a)
d = citire_date()
print(d)
#b)
l = sterge_ore(d, 'Cinema 1', 'Minionii 2', {'12:30', '18:30'})
print(d)
print(l)

#c)
d = citire_date()
l = cinema_film(d, '14:00', '22:00', 'Cinema 1', 'Cinema 2')
print(l)

