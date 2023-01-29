# k reprezinta indicele componentei curente s[k] dintr-o lista indexata de la 1
def bkt(k):
    global s
    # parcurgem toate valorile posibile v pentru s[k]
    for v in range(mink,maxk+1):
        # atribuim componentei curente s[k] valoarea v
        s[k] = v

        # daca s[1],...,s[k] este solutie partiala
        if s[1],..., s[k] este soluție parțială:
            # dacă s[1],…,s[k] este o soluție
            if s[1],..., s[k] este soluție:
                # prelucrăm soluția curentă s[1],…,s[k]
            else:
                # s[1],…,s[k] este soluție parțială, dar nu este
                # soluție, deci adăugăm o nouă componentă s[k + 1]
                bkt(k + 1)