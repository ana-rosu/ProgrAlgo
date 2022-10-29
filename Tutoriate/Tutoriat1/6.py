'''Se citește un număr natural n. Să se verifice dacă este putere a lui 2.'''

n = int(input('Dati n: '))
print(n & (n - 1) == 0)
