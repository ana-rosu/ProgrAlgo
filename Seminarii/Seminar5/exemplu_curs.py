'''
La un ghișeu, stau la coadă 𝑛 persoane 𝑝1, 𝑝2, … , 𝑝𝑛 și pentru fiecare persoană 𝑝𝑖 se
cunoaște timpul său de servire 𝑡𝑖. Să se determine o modalitate de reașezare a celor 𝑛
persoane la coadă, astfel încât timpul mediu de așteptare să fie minim.
'''
# funcția afișează, într-un format tabelar, timpii de servire
# și timpii de așteptare ai persoanelor
# ts = o lista cu timpii individuali de servire
def afisare_timpi(ts):
    print("Persoana\tTimp de servire\tTimp de asteptare")
    # timpul de asteptare al persoanei curente
    tcrt = 0
    ttotal = 0
    for t in ts:
        tcrt += t[1]
        ttotal += tcrt
        print(str(t[0]).center(len("Persoana")),
              str(t[1]).center(len("Timp de servire")),
              str(tcrt).center(len("Timp de asteptare")),
              sep = "\t")
    print('Timpul mediu de asteptare:', round(ttotal/len(ts), 2))

# CITIRE DATE
# timpii de servire ai persoanelor
# ex = 7 6 3 10 6 3
aux = [int(x) for x in input("Timpii de servire: ").split()]
# asociem fiecărui timp de servire numărul de ordine al persoanei
tis = [(i+1, aux[i]) for i in range(len(aux))]

# AFISARE DATE
print('Varianta initiala: ')
afisare_timpi(tis)

# SOLUTIA
tis.sort(key = lambda t: t[1])

# AFISARE SOLUTIE
print('\nVarianta optima:')
afisare_timpi(tis)

