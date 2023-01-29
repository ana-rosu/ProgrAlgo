def suma(t, st, dr):
    if st == dr:
        return t[st]

    mij = (st+dr)//2
    sol_st = suma(t, st, mij)
    sol_dr = suma(t, mij+1, dr)

    return sol_st+sol_dr

print(suma([11,1,5,0,2],0,4))
