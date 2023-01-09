'''Fișierul text exemplu_fisiere.txt conține, pe mai multe linii, numere întregi separate
între ele prin spații. Scrieți un program care afișează pe ecran suma numerelor din
fișier.'''

# folosind metoda read -> furnizează tot conținutul fișierului text într-un singur șir de caractere
f1 = open('exemplu_fisiere.txt')
numere1 = [int(nr) for nr in f1.read().split()]
print('Varianta 1) Suma nr din fisier este', sum(numere1))
f1.close()

#folosind metoda readline -> furnizează conținutul liniei curente din fișierul text într-un șir de
#caractere sau un șir vid când se ajunge la sfârșitul fișierului
f2 = open('exemplu_fisiere.txt')
numere2 = []
linie = f2.readline()
while linie != '':
    numere2.extend(int(nr) for nr in linie.split())
    linie = f2.readline()

print('Varianta 2) Suma nr din fisier este', sum(numere2))
f2.close()

#folosind metoda readlines -> furnizează toate liniile din fișierul text într-o listă de șiruri de
#caractere

f3 = open("exemplu_fisiere.txt")
total = 0
for linie in f3.readlines():
    numere = [int(x) for x in linie.split()]
    total = total + sum(numere)
print("Varianta 3) Suma nr din fisier este", total)
f3.close()
