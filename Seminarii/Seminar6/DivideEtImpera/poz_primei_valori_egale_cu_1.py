'''
Se consideră o listă 𝑙𝑠𝑏 formată din valori egale cu 0, urmate de valori egale cu 1 (este
posibil ca în șir să nu existe nicio valoare egală cu 0 sau nicio valoare egală cu 1). Scrieți
o funcție cu complexitate minimă care să furnizeze poziția primei valori egale cu 1 din
lista 𝑙𝑠𝑏 sau -1 dacă în listă nu există nicio valoare egală cu 1.
Exemple:
lsb = [0, 0, 0, 0, 1, 1, 1] => poziția = 4
lsb = [0, 0, 0] => poziția = -1
lsb = [1, 1, 1] => poziția = 0
'''
def cbin(lsb, st, dr):
    mij = (st+dr)//2
    if lsb[mij]==1:
        if lsb[mij-1]==0:
            return mij
        else:
            return cbin(lsb, st,mij-1)
    else:
        return cbin(lsb, mij+1, dr)

def pozitie_1(lsb):
     # toate valorile din lista sunt egale cu 1
     if lsb[0] == 1:
        return 0
     # toate valorile din lista sunt egale cu 0
     if lsb[len(lsb) - 1] == 0:
        return -1
     # lista conține și valori egale cu 0 și valori egale cu 1
     return cbin(lsb,0,len(lsb)-1)