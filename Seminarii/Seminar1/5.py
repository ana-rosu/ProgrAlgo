'''Se citeste un sir format din nr nat cu proprietatea ca fiecare valoare distincta apare de exact 2 ori in sir,
mai putin una care apare o singura data. Sa se afiseze valoarea care apare o singura data in sir.'''

n = int(input('n = '))
rez = 0
for i in range(0,n):
    x = int(input('x = '))
    rez = rez ^ x

print(rez)