def cautare_binara(t,x,st,dr):
    if st > dr:
        return -1

    mij = (st+dr)//2
    if x > t[mij]:
        return cautare_binara(t,x,mij+1,dr)
    elif x < t[mij]:
       return cautare_binara(t,x,st,mij-1)
    else:
        return mij

print(cautare_binara([1,2,5,7,9,10],2, 0, 5))