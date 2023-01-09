'''Sa se gaseasca lungimea maxima a unei secvente de biti egali cu 1 din repr binara a unui nr nat dat'''
n = int(input("n = "))


def decimalToBinary(nr):
    print(nr % 2, end='')
    nr = nr // 2
    if nr >= 1:
        decimalToBinary(nr)


decimalToBinary(n)
print()

k = 0
while n:
    n = n & (n << 1)
    k += 1
print(k)
