'''Sa se verifice daca un nr nat nenul n este de forma 2^k sau nu. In caz afirmativ sa se afiseze valoarea k'''
'''n=2^k => n = 100.....00(2)'''

# Solutia 1
n = int(input("Dati n: "))

k = 0
while n & 1 == 0:
    n = n >> 1
    k += 1

if n == 1:
    print(k)
else:
    print('nu')
'''
Ultimul bit este cel care indica paritatea( 1 - impar, 0 - par )
x & 1 = 1, daca x impar
      = 0, daca x par
      
Exemple:
x = 157 = 10011101
      1 = 00000001
x & 1 =   00000001 = 1

x = 2 = 10
    1 = 01
x & 1 = 00 = 0

Operatori de deplasare
x << b -> se insereaza b biti egali cu 0 la sfarsitul reprezentarii binare a lui x
x << b <=> x * 2**b

x >> b -> se elimina ultimii b biti din reprezentarea binara a lui x
x >> b <=> x // 2**b

Exemple:

x = 157 = 10011101
x << 3  = 10011101000 = 1256 = 157 * 2**3

x = 157 = 10011101
x >> 3 =  10011 = 19 = 157 // 2**3 
'''

# Solutia 2

import math
n = int(input('Dati n: '))

if n & (n-1) == 0:
    k = int(math.log2(n))
    print(k)
else:
    print('nu')