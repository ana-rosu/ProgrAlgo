'''Se citesc un număr natural n și o cifră k. Afișați numărul format prin
eliminarea tuturor aparițiilor cifrei k din numărul n'''

n = int(input("Dati n: "))
k = int(input("Dati o cifra a lui n: "))

#v1
nou = 0
p = 1
while n:
    if n % 10 != k:
        nou = n % 10 * p + nou
        p *= 10
    n //= 10

n = nou
print(n)

#v2

x = input('Dati n: ').replace(input('Dati o cifra a lui n: '), '')
print(x or 0)
