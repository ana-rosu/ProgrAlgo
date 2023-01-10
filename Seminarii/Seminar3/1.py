'''În fișierul text 1.txt se găsesc pe prima linie 𝑛 − 1 numere naturale distincte
dintre primele 𝑛 numere naturale nenule. Să se afișeze numărul lipsă. De exemplu, dacă
prima linie din fișier este 2 1 5 4, numărul lipsă este 3.
'''
#Solutia 0 -> complexite timp & spatiu O(n)
try:
    f = open('1.txt')
    numere = [int(nr) for nr in f.read().split()]
    n = len(numere) + 1
    x = 0
    for i in range(1, n+1):
        x = x ^ numere[i-1] ^ i
    x = x ^ n
    print(x)
    f.close()
except FileNotFoundError:
    print('Fisier inexistent')


# Solutia 1 -> complexitate timp 𝒪(𝑛), spațiul de memorie utilizat 𝒪(𝑛)
# printam diferența dintre suma celor 𝑛 numere naturale și suma numerelor din fișier
try:
    f = open('1.txt')
    numere = [int(nr) for nr in f.read().split()]
    s = sum(numere)
    n = len(numere) + 1
    gauss = n * (n + 1) // 2
    print(gauss - s)
    f.close()
except FileNotFoundError:
    print('Fisier inexistent')

# Solutia 2 -> complexitate timp 𝒪(𝑛^2), spațiul de memorie utilizat O(n)
# citim numerele din fișier într-o listă și apoi căutăm în ea fiecare număr de la 1 la 𝑛
try:
    f = open('1.txt')
    numere = [int(nr) for nr in f.read().split()]
    n = len(numere) + 1
    for i in range(1, n + 1):
        if i not in numere:
            print(i)
            break
    f.close()
except FileNotFoundError:
    print('Fisier inexistent')

# Solutia 3 -> complexitate timp O(nlogn), spatiu de memorie utilizat O(n)
# citim numerele din fișier într-o listă 𝐿 pe care o sortăm crescător și apoi căutăm în ea
# primul indice pentru care 𝑖 + 1 ≠ 𝐿[𝑖], iar dacă nu există niciun indice având această
# proprietate, înseamnă că lipsește numărul n
try:
    f = open('1.txt')
    numere = [int(nr) for nr in f.read().split()]
    numere.sort()
    n = len(numere) + 1
    for i in range(n - 1):
        if numere[i] != i + 1:
            print(i + 1)
            break
    else:
        print(n)
except FileNotFoundError:
    print('Fisier inexistent')

# Solutia 4 -> complexitate timp mediu si spatiu O(n)
# determinăm numărului lipsă ca diferență dintre mulțimea formată din primele 𝑛
# numere naturale nenule și mulțimea numerelor din fișier:
try:
    f = open("1.txt")
    nr = {int(x) for x in f.read().split()}
    n = len(nr) + 1
    toate = {x for x in range(1, n + 1)}
    print(*(toate - nr))
    f.close()
except FileNotFoundError:
    print("Fișier inexistent!")
# Solutia 5 -> complexitate timp si spatiu O(n)
# marcăm cele 𝑛 − 1 numere din fișier într-un dicționar având cheile 1, 2, . . . , 𝑛
# inițializate cu False și apoi căutăm primul număr nemarcat

try:
    f = open("1.txt")
    lista = [int(nr) for nr in f.read().split()]
    n = len(lista) + 1
    d = {x: False for x in range(1, n + 1)}
    for nr in lista:
        d[nr] = True
    for nr in d:
        if d[nr] == False:
            print(nr)
    f.close()
except FileNotFoundError:
    print("Fișier inexistent!")
