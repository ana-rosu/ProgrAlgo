# a)
def prim(nr):
    if nr <= 1:
        return False
    if nr % 2 == 0 and nr != 2:
        return False
    for i in range(3, nr//2+1):
        if nr % i == 0:
            return False
    return True

def lista_divizori(nr):
    l = []
    for i in range(2, nr//2+1):
        if nr%i==0:
            if prim(i):
                l.append(i)
    return l

def divizori(*numere):
    d = {}
    for nr in numere:
        d[nr] = lista_divizori(nr)
    return d

d = divizori(50,21)
print(d)

# b)
litere_10 = [chr(i+97) for i in range(10)]
print(litere_10)