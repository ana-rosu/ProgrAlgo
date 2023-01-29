'''
Se consideră o placă de tablă de formă dreptunghiulară având colțul stânga-jos în punctul
(𝑥𝑠𝑡, 𝑦𝑠𝑡) și colțul dreapta-sus în punctul (𝑥𝑑𝑟, 𝑦𝑑𝑟). Placa are pe suprafața sa 𝑛 găuri cu
coordonate numere întregi. Știind că sunt permise doar tăieturi orizontale sau verticale
complete, se cere să se decupeze din placă o bucată de arie maximă fără găuri.
Explicație
placa.in
2 1 - coord coltului din stanga jos al dreptunghiului dat
8 5 - coord coltului din dreapta sus al dreptunghiului dat
3 2
4 4
5 3
7 4
placa.out
Dreptunghiul:
3 1
8 3
Aria maximă:
10
Placa de tablă este un dreptunghi având colțul stânga-jos de coordonate (2,1) și colțul dreapta-sus de coordonate (8,5).
În placă sunt date 4 găuri, având coordonatele (3,2), (4,4), (5,3) și (7,4).
Dreptunghiul cu aria maximă de 10 și care nu conține nicio gaură are coordonatele (3,1) pentru colțul stânga-jos și (8,3) pentru colțul dreapta-sus.
'''


# funcție care citește datele de intrare din fișierul text placa.in
# prima linie din fișier conține coordonatele colțului stânga-jos al
# dreptunghiului inițial, a doua linie pe cele ale colțului
# dreapta-sus, iar pe următoarele linii sunt coordonatele găurilor
def citireDate():
    f = open("placa.in")
    aux = f.readline().split()
    xst, yst = int(aux[0]), int(aux[1])
    aux = f.readline().split()
    xdr, ydr = int(aux[0]), int(aux[1])
    coordonateGauri = []
    for linie in f:
        aux = linie.split()
        coordonateGauri.append((int(aux[0]), int(aux[1])))
    f.close()
    return xst, yst, xdr, ydr, coordonateGauri


# funcția recursivă care prelucrează dreptunghiul curent
def dreptunghiArieMaxima(xst, yst, xdr, ydr):
    global arieMaxima, coordonateGauri, dMaxim
    # considerăm, pe rând, fiecare gaură
    for g in coordonateGauri:
        # dacă gaura curentă se găsește în interiorul dreptunghiului
        # curent, atunci reapelăm funcția pentru cele 4
        # dreptunghiuri care se formează aplicând o tăietură
        # orizontală și una verticală prin gaura curentă
        if xst < g[0] < xdr and yst < g[1] < ydr:
            # dreptunghiurile obținute după o tăietură orizontală
            dreptunghiArieMaxima(xst, yst, xdr, g[1])
            dreptunghiArieMaxima(xst, g[1], xdr, ydr)
            # dreptunghiurile obținute după o tăietură verticală
            dreptunghiArieMaxima(xst, yst, g[0], ydr)
            dreptunghiArieMaxima(g[0], yst, xdr, ydr)
            break
    # dacă dreptunghiul curent nu conține nicio gaură, atunci
    # comparăm aria sa cu aria maximă a unui dreptunghi fără găuri
    # determinată până în momentul respectiv
    else:
        if (xdr - xst) * (ydr - yst) > arieMaxima:
            arieMaxima = (xdr - xst) * (ydr - yst)
            dMaxim = (xst, yst, xdr, ydr)


# citirea datelor de intrare din fișierul text placa.in
xst, yst, xdr, ydr, coordonateGauri = citireDate()
# inițializăm aria maximă a unui dreptunghi fără găuri
arieMaxima = 0
# inițializăm coordonatele drepunghiul cu arie maximă fără găuri
dMaxim = (0, 0, 0, 0)
# apelăm funcția pentru drepunghiul inițial
dreptunghiArieMaxima(xst, yst, xdr, ydr)

# scriem datele de ieșire în fișierul text placa.out
f = open("placa.out", "w")
f.write("Dreptunghiul:\n" + str(dMaxim[0]) + " " + str(dMaxim[1]) + "\n" + str(dMaxim[2]) + " " + str(dMaxim[3]))
f.write("\nAria maxima:\n" + str(arieMaxima))
f.close()
