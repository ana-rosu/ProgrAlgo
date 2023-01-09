'''Fie x si y 2 nr naturale.
Calculati numarul bitilor din reprezentarea binara interna a nr x a caror valoare
trebuie comutata pt a obtine nr y'''

x = int(input('x: '))
y = int(input('y: '))

# raspunsul este nr de biti nenuli din repr binara a x ^ y
dif = x ^ y

nr = 0
while dif:
    dif = dif & (dif-1)
    nr += 1
print(nr)

'''
x = 12 = 01100
y = 20 = 10100
x ^ y  = 11000
R: 2
'''