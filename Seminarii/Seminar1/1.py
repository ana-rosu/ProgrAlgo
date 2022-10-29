''' Sa se interschimbe valorile a 2 variabile de tip intreg folosind operatorul ^ '''

x = int(input('Dati x: '))
y = int(input('Dati y: '))
print(bin(x), bin(y))

x = x ^ y
y = x ^ y
x = x ^ y

print(f"x este {x}, y este {y}")
