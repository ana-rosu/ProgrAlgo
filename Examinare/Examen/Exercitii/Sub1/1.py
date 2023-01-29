# a) Scrieţi o funcţie numere care primeşte un număr variabil de numere naturale şi
# returnează informaţii despre numere sub forma unui dicţionar de perechi {medie: lista
# de numere}. Lista de numere este formată din numerele naturale primite ca parametru
# care au aceeași medie aritmetică a cifrelor, iar cheia medie este un număr real având
# valoarea respectivei medii aritmetice. Listele de numere nu conţin elemente duplicate şi
# sunt sortate în ordine descrescătoare.
# De exemplu, pentru apelul numere (82375, 201, 51, 73, 3456, 2855, 1021, 90, 153)
# funcţia va returna dicţionarul {1.0: [1021, 201], 3.0: [153, 51], 4.5: [3456, 90], 5.0: [82375,
# 2855, 73]}.

def numere(*numere):
    d = {}
    for nr in numere:
        medie = sum([int(x) for x in str(nr)])/len(str(nr))
        if medie not in d:
            d[medie] = {nr}
        else:
            d[medie].add(nr)

    for m in d:
        l = sorted(d[m], reverse = True)
        d[m] = l
    print(d)

numere(82375, 201, 51, 73, 3456, 2855, 1021, 90, 153)

# b) Înlocuiți punctele de suspensie din instrucțiunea L = [...] cu o secvență de
# inițializare (list comprehension) astfel încât, după executarea sa, lista L să conțină
# numerele naturale formate din exact 3 cifre aflate în ordine strict crescătoare

L = [x for x in range(100,1000)]