'''Se citește o listă de numere naturale sortată strict crescător și un număr natural 𝑆. Să
se afișeze toate perechile distincte formate din valori distincte din lista dată cu
proprietatea că suma lor este egală cu 𝑆. '''

l = [2, 5, 7, 8, 10, 12, 15, 17, 25]
s = 20

# VARIANTA OPTIMA de rezolvare, având complexitatea 𝒪(𝑛) și neutilizând memorie
# suplimentară, se bazează pe metoda arderii lumânării la două capete (two pointers).
def perechi(L, S):
    st = 0
    dr = len(L) - 1
    rez = []
    while st < dr:
        if L[st] + L[dr] < S:
            st += 1
        elif L[st] + L[dr] > S:
            dr -= 1
        else:
            rez.append((L[st], L[dr]))
            st += 1
            dr -= 1
    return rez

# SOL1 - complexitate O(n^2)
def perechi(L, S):
    rez = []
    for i in range(len(L)):
        if L[i] >= S // 2:
            break
        if S - L[i] in L[i + 1:]:
            rez.append((L[i], S - L[i]))
    return rez


# SOL2 - reducem complexitatea la 𝒪(𝑛log2𝑛) cautand elementul S-L[i] folosind cautarea binara
# Deoarece căutarea binară a valorii S-L[i] în sublista L[i+1:] are complexitatea
# maximă 𝒪(log2 𝑛), această funcție va avea complexitatea 𝒪(𝑛log2 𝑛).
def perechi2(L, S):
    rez = []
    for i in range(len(L)):
        if L[i] >= S // 2:
            break
        st = i + 1
        dr = len(L) - 1
        while st <= dr:
            mij = (st + dr) // 2
            if S - L[i] == L[mij]:
                rez.append((L[i], S - L[i]))
                break
            elif S - L[i] < L[mij]:
                dr = mij - 1
            else:
                st = mij + 1
    return rez


# SOL3 - si mai eficienta - O(n) dar foloseste memorie suplimentara
# crearea setului are complex O(n) iar testarea apartenentei in set, in general, O(1)
def perechi(L, S):
    M = set(L)
    rez = []
    for x in L:
        if x >= S // 2:
            break
    if S - x in M:
        rez.append((x, S - x))
    return rez


