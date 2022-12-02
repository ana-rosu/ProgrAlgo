'''Într-o propoziție, Ana a sintetizat informațiile despre cumpărăturile
pe care le-a efectuat într-o anumită zi, pentru fiecare produs cumpărat
ea precizând cantitatea și prețul unitar.
(e.g., "Astăzi am cumpărat 5 kg de mere cu 2.30 RON kilogramul și 2 pâini a câte 5 lei bucata.").
Afișați totalul cheltuielilor Anei din ziua respectivă. '''

propozitie = input("Sirul: ")
total = 0.0
cantitate = pret = None
for cuvant in propozitie.split():
    try:
        numar = float(cuvant)
        if cantitate is None:
            cantitate = numar
        else:
            pret = numar
            total += cantitate * pret
            cantitate = None
    except ValueError:
        pass
print(f"Totalul chletuielilor Anei: {total}")