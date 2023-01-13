# Functii callback
'''
Vom prezenta o funcție generică pentru calculul unor sume. De exemplu,
să considerăm următoarele 3 sume:
𝑆1 = 1 + 1/2 + ⋯ + 1/𝑛
𝑆2 = 1^2 + 2^2 + ⋯ + 𝑛^2
𝑆3 = 𝑒^1 + e^2 + ⋯ + e^𝑛
Evident, putem să definim câte o funcție pentru calculul fiecărei sume, dar această soluție
nu este scalabilă. Putem observa cu ușurință faptul că toate cele 3 sume au următoarea
formă generală:
      𝑛
 𝑆𝑘 = ∑𝑓𝑘(𝑖)
     𝑖=1
unde 𝑓1(𝑖) = 1/𝑖, 𝑓2(𝑖) = 𝑖^2 și 𝑓3(𝑖) = 𝑒^i
'''
import math

def suma_generica(n, fk):
    s = 0
    for i in range(1, n + 1):
        s = s + fk(i)
    return s

def fk_1(i):
    return 1 / i

def fk_2(i):
    return i ** 2


n = 10
s = suma_generica(n, fk_1)
print("Suma 1:", s.__round__(2))  # Suma 1: 2.93
s = suma_generica(n, fk_2)
print("Suma 2:", s)  # Suma 2: 385
s = suma_generica(n, math.exp)
print("Suma 3:", s)  # Suma 3: 34843.77384533132

# Functii anonime
print((lambda x, y: x + y)(4, 3))
print((lambda x: x % 2 == 0)(5))
print((lambda x, y: False if y == 0 else x % y == 0)(45, 5))
print((lambda x: sum([int(cf) for cf in str(x)]))(45))
print((lambda sir: len([lit for lit in sir if lit in "aeiouAEIOU"]))('Andra'))
print((lambda L, v: len([x for x in L if x > v]))([23, 4, 52, 4], 4))


# Functii imbricate
def combinari(n, k):
    def factorial(x):
        p = 1
        for i in range(1, x + 1):
            p = p * i
        return p

    return factorial(n) // (factorial(k) * factorial(n - k))


print(combinari(5, 3))

# Sortari complexe
# Să se sorteze o listă de numere naturale astfel încât numerele pare sortate crescător
# să fie poziționate înaintea celor impare sortate descrescător
L = [10, 23, 13, 5, 15, 69, 22, 66]
print(sorted(L, key=lambda n: (0, n) if n % 2 == 0 else (1, -n)))

# Considerăm o listă care conține informații despre mai mulți studenți, respectiv pentru
# fiecare student se cunoaște numele, grupa și nota obținută la examenul de admitere.
# Să se sorteze studenții în ordinea crescătoare a grupelor, în fiecare grupă studenții să
# fie sortați descrescător după nota obținută la examenul de admitere, iar în cazul unor
# note egale studenții să fie sortați alfabetic.
# Vom considera faptul că informațiile despre fiecare student sunt memorate într-un
# tuplu, astfel:

L = [("Popescu Ion", 131, 9.25),
     ("Ionescu Ana", 133, 8.75),
     ("Popa Marian", 131, 9.85),
     ("David Maria", 132, 8.95),
     ("Gheorghe Ana", 131, 9.85),
     ("Popescu Anca", 132, 9.15),
     ("Corbu Florin", 133, 8.05),
     ("Gheorghe Dan", 132, 9.15)]

S = sorted(L, key=lambda t: (t[1], -t[2], t[0]))
print(*S, sep='\n')

# Să se sorteze șirurile de caractere dintr-o listă L în ordinea descrescătoare a
# lungimilor prefixelor maximale comune cu un șir dat s. De exemplu, dacă lista este
# L = ["apasator", "apartament", "exemplu", "ars", "test", "aparat", "amic"] și s = "aparator",
# atunci lista sortată va fi
# L = ["aparat", "apartament", "apasator", "ars", "amic", "exemplu", "test"].

L = ["apasator", "apartament", "exemplu", "ars", "test", "aparat", "amic"]
s = "aparator"

def prefixMaxim(s):
    def pmax(t):
        for i in range(len(s), 0, -1):
            if t.startswith(s[:i]):
                return i, t
        return 0, t

    return pmax


L.sort(key=prefixMaxim(s), reverse=True)
print(L)


# Generatori
def generator_numere_pare(n):
    x = 0
    while x <= n:
        yield x
        x += 2

nr_pare = generator_numere_pare(100)
for x in nr_pare:
    print(x, end=" ")

# functia next
x = next(nr_pare, -1)
print(x)

# generatori care ruleaza "la infinit"
def generator_numere_pare():
    x = 0
    while True:
        yield x
        x = x + 2

nr_pare = generator_numere_pare()

for x in nr_pare:
    print(x, end=" ")
    if x == 10:
        break

for x in nr_pare:
    print(x, end=" ")
    if x == 20:
        break

nr_pare.close()

for x in nr_pare:
    print(x, end=" ")
    if x == 30:
        break