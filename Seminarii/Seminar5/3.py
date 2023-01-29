'''
Reuniunea a n intervale.
'''
# funcție care furnizează cheia necesară sortării intervalelor
# crescător în raport de capetele din stânga și, în cazul unora
# egale, descrescător după capetele din dreapta
def cheieIntervale(t):
    return t[0], -t[1]

with open('intervale.txt') as fin:
    intervale = []
    for linie in fin:
        aux = linie.split()
        intervale.append((int(aux[0]), int(aux[1])))

intervale.sort(key = cheieIntervale)
print(intervale)

minr = intervale[0][0]
maxr = intervale[0][1]

reuniune = []

lungime = maxr - minr

for i in range(1, len(intervale)):
    # Caz 1: intervalul curent este inclus in reuniunea curenta
    # suntem siguri de asta pentru ca intervale[i][0] - capatul din stanga este sigur mai mare decat minr (din sortare)
    # deci daca si capatul din dreapta (intervale[i][1]) este mai mic decat maxr, inseamna ca tot intervalul curent este inclus in reuniunea curenta
    if intervale[i][1] <= maxr:
        continue
    # Caz 2: intervalul curent nu este disjunct cu reuniunea curenta
    # daca capatul din stanga este inclus in reuniunea curenta, stim de la if ul anterior ca capatul din dreapta este mai mare decat maxr
    # deci actualizam maxr
    elif intervale[i][0] < maxr:
        lungime += intervale[i][1] - maxr
        maxr = intervale[i][1]
    # Caz 3: intervalul curent este disjunct cu reuniunea curenta
    # reinitializam reuniunea curenta cu intervalul curent
    else:
        lungime+= intervale[i][1] - intervale[i][0]
        reuniune.append((minr, maxr))
        minr = intervale[i][0]
        maxr = intervale[i][1]

# adaugam ultima reuniune curenta
reuniune.append((minr, maxr))

with open('reuniune.txt', 'w') as fout:
    for icrt in reuniune:
        fout.write("[{}, {}]\n".format(icrt[0], icrt[1]))
    fout.write("\nLungimea reuniunii: " + str(lungime))
