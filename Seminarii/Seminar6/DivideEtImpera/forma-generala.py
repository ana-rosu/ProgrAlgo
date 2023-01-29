# functie care furnizeaza solutia unei probleme combinand solutiile
# subproblemelor in care ea a fost descompusa
def combinare(sol_st, sol_dr):
    pass

def divimp(t, st, dr):
    # daca subproblema curenta este direct rezolvabila
    if dr-st <= k: # k este, de obicei, 0 sau 1
        return solutie_problema_directa

    # etapa Divide
    mij = (st+dr)//2
    sol_st = divimp(t, st, mij)
    sol_dr = divimp(t, mij+1, dr)

    # etapa Impera
    return combinare(sol_st, sol_dr)