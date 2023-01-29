# sortarea prin interclasare -> permite obținerea unei liste sortate crescător din
# două liste care sunt, de asemenea, sortate crescător

# complexitate O(nlog2n)
# relatia de recurenta: T(n) = 2T(n/2) + n

# functia interclasare are complexitatea 0(n)
def interclasare(t,st,mij,dr):
    i = st
    j = mij + 1
    aux = []
    while i <= mij and j <= dr:
        if t[i] <= t[j]:
            aux.append(t[i])
            i += 1
        else:
            aux.append(t[j])
            j += 1

    aux.extend(t[i:mij+1])
    aux.extend(t[j:dr+1])

    t[st:dr+1] = aux[:]

def mergesort(t,st,dr):
    if st < dr:
        mij = (st+dr)//2
        mergesort(t,st,mij)
        mergesort(t,mij+1,dr)
        interclasare(t,st,mij,dr)

a = [38,27,43,3,9,82,10]
mergesort(a, 0,len(a)-1)
print(a)