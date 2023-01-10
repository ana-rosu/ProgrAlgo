'''
Scrieți o funcție care să se verifice dacă două șiruri de caractere formate doar din litere
mici sunt anagrame sau nu. Două șiruri sunt anagrame dacă sunt formate din aceleași
litere, dar așezate în altă ordine (sau, echivalent, unul dintre șiruri se poate obține din
celălalt printr-o permutare a caracterelor sale). De exemplu, șirurile emerit și treime
sunt anagrame, dar șirurile emerit și treimi nu sunt!
'''
def anagrame1(s, t):
    if set(s) != set(t):
        return False
    for litera in set(s):
        if s.count(litera) != t.count(litera):
            return False
    return True

# Complexitate O(n^2)
def anagrame2(s, t):
    if len(s) != len(t):
        return False
    for litera in s:
        if litera not in t:
            return False
        t = t.replace(litera, "", 1)

    return True



# Complexitate 0(nlogn)
def anagrame3(s, t):
    return sorted(s) == sorted(t)


# Solutii folosind dictionare

# Complexitate O(n^2) ( metoda count are complexitate O(n) )
def anagrame1v1(sir1, sir2):
    d = {litera: sir1.count(litera) for litera in sir1}
    s = {litera: sir2.count(litera) for litera in sir2}
    return d == s


# Complexitatea 𝒪(𝑛) dacă se utilizează o funcție de dispersie bună
# Dictionar creat fara a folosi metoda count; testarea apartenentei unei chei este de O(1)
def anagrame1v2(s, t):
    ds = {}
    for lit in s:
        if lit not in ds:
            ds[lit] = 1
        else:
            ds[lit] += 1
    dt = {}
    for lit in t:
        if lit not in dt:
            dt[lit] = 1
        else:
            dt[lit] += 1
    return ds == dt

# Complexitatea acestei funcții este tot 𝒪(𝑛), dar, spre deosebire de varianta cu dicționare,
# este stabilă (nu depinde de performanțele unei funcții de dispersie)!
def anagrame(s, t):
    fs = [0] * 26
    ft = [0] * 26
    for litera in s:
        fs[ord(litera) - ord("a")] += 1
    for litera in t:
        ft[ord(litera) - ord("a")] += 1
    return fs == ft
