def citireInformatiiStudenti(numef):
    f = open(numef)
    studenti = []
    for linie in f:
        aux = linie.split(',')
        studenti.append((aux[0], int(aux[1]), tuple(int(x) for x in aux[2:])))

    f.close()
    return studenti


studenti = citireInformatiiStudenti('3.in')


def promovat(lista_studenti, minc):
    for i in range(len(lista_studenti)):
        if 0 not in lista_studenti[i][2] and sum(lista_studenti[i][2]) >= minc:
            lista_studenti[i] += (True,)
        else:
            lista_studenti[i] += (False,)
    return lista_studenti

promovat(studenti, 15)

#crescător după grupă și în fiecare grupă în ordine alfabetică;
studenti.sort(key = lambda t: (t[1], t[0]))

# întâi studenții promovați,  apoi  cei  nepromovați  și  în  fiecare  categorie  în  ordine alfabetică

studenti.sort(key= lambda t: (-t[3],t[0]))

# descrescător  după  suma  creditelor,  iar  în  cazul  unor  sume  egale  în  ordinea crescătoare a grupei și în ordine alfabetică în cadrul grupei:
studenti.sort(key = lambda t: (-sum(t[2]), t[1], t[0]))

# în  ordinea  crescătoare  a  grupelor,
# în  cadrul  fiecărei  grupe  mai  întâi  studenții promovați, iar apoi cei nepromovați,
# în fiecare categorie (promovat/nepromovat) în ordinea descrescătoare a sumei creditelor și,
# în cazul unor sume egale,  în  ordine alfabetică:

studenti.sort(key = lambda t: (t[1], -t[3], -sum(t[2]), t[0] ))

for linie in studenti:
    print(linie)