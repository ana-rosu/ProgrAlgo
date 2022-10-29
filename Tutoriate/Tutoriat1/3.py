'''Se citesc un număr natural n și apoi n numere întregi. Să se afișeze cele
mai mari două numere distincte din șir.'''

n = int(input('Dati n: '))
print(f'Introduceti {n} valori: ')

max1 = int(input())
max2 = max1

for i in range(n - 1):
    x = int(input())
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x
print(max1, max2)
