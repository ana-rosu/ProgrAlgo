'''Fie x si y 2 nr naturale.
Calculati numarul bitilor din reprezentarea binara interna a nr x a caror valoare
trebuie comutata pt a obtine nr y'''

x = int(input('x: '))
y = int(input('y: '))

print(bin(x).replace('0b', ''))
print(bin(y).replace('0b', ''))

dif = x ^ y

print(bin(dif).replace('0b', '').count('1'))

