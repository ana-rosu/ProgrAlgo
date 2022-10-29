'''Se citește un număr natural n. Să se verifice dacă este pătrat perfect.'''
# v1
import math
n = int(input("Dati n: "))
print(math.sqrt(n) == int(math.sqrt(n)))

# v2
n = int(input("Dati n: "))
print(n ** (1 / 2) == int(n ** (1 / 2)))
