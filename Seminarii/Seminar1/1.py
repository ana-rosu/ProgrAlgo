''' Sa se interschimbe valorile a 2 variabile de tip intreg folosind operatorul ^ '''

x = int(input('Dati x: '))
y = int(input('Dati y: '))
print(bin(x), bin(y))

x = x ^ y
y = x ^ y
x = x ^ y

print(f'''x este {x},
y este {y}''')

'''
1) x ^ x = 0
2) x ^ 0 = x
3) ^ comutativa
4) ^ asociativa

x = x ^ y
y = x ^ y // y = (x ^ y) ^ y = x ^ (y ^ y) = x ^ 0 = x
x = x ^ y // x = (x ^ y) ^ x = (x ^ x) ^ y = 0 ^ y = y
'''

