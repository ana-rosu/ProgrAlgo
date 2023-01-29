# Problema candidatului majoritar

# SOL 1
# În prima variantă de rezolvare vom calcula direct numărul de voturi primite de fiecare
# candidat distinct:
def castigator(voturi):
    for v in set(voturi):
        if voturi.count(v) > len(voturi) // 2:
            return v
    return 0


# Deoarece numărul candidaților distincți poate fi cel mult 𝑛, iar metoda count are
# complexitatea maximă 𝒪(𝑛), această funcție va avea complexitatea maximă 𝒪(𝑛^2)

# SOL 2
# În a doua variantă de rezolvare vom sorta crescător lista voturi și apoi vom verifica dacă
# ea conține o secvență de voturi egale având lungimea strict mai mare decât n//2:
def castigator(voturi):
    voturi.sort()
    candidat = voturi[0]
    nr_voturi = 1
    for vot in voturi[1:]:
        if vot == candidat:
            nr_voturi = nr_voturi + 1
            if nr_voturi > len(voturi) // 2:
                return candidat
        else:
            candidat = vot
            nr_voturi = 1
    return 0


# Sortarea listei voturi se realizează cu complexitatea 𝒪(𝑛 log2 𝑛), iar căutarea unei
# secvențe cu lungimea strict mai mare decât n//2 are complexitatea maximă 𝒪(𝑛), deci
# această funcție va avea complexitatea maximă 𝒪(𝑛 log2 𝑛)

# SOL3
# A treia variantă de rezolvare se obține observând faptul că în lista voturilor sortată
# crescător singurul posibil câștigător este elementul din mijlocul listei, pentru că orice
# secvență formată din cel puțin n//2+1 elemente egale trebuie să conțină și elementul de
# pe poziția n//2:
def castigator(voturi):
    voturi.sort()
    n = len(voturi)
    if voturi.count(voturi[n // 2]) > n // 2:
        return voturi[n // 2]
    return 0


# Sortarea listei voturi se realizează cu complexitatea 𝒪(𝑛 log2 𝑛), iar metoda count are
# complexitatea maximă 𝒪(𝑛), deci și această funcție va avea complexitatea maximă tot
# 𝒪(𝑛 log2 𝑛).

# SOL4
def castigator(voturi):
    d = {}
    for v in voturi:
        if v not in d:
            d[v] = 1
        else:
            d[v] += 1
    for v in d:
        if d[v] > len(voturi) // 2:
            return v
    return 0


# Complexitatea computațională a acestei funcții este 𝒪(𝑛), deci este optimă, dar are
# dezavantajul de a utiliza memorie suplimentară (dicționarul). Atenție, dicționarul
# nr_voturi ar putea fi creat și prin nr_voturi = {x: voturi.count(x) for x in
# set(voturi)}, dar complexitatea acestei operații ar fi 𝒪(𝑛^2)!

# ALGORITMUL BOYER-MOORE
def castigator(voturi):
    avantaj = 0
    majoritar = None
    for v in voturi:
        if avantaj == 0:
            avantaj = 1
            majoritar = v
        elif v == majoritar:
            avantaj += 1
        else:
            avantaj -= 1

    if avantaj == 0:
        return 0
    if voturi.count(majoritar) > len(voturi) // 2:
        return majoritar
    return 0
# Se observă faptul că algoritmul Boyer-Moore rezolvă această problemă în mod optim,
# deoarece are complexitatea computațională 𝒪(𝑛) și nu folosește memorie suplimentară!