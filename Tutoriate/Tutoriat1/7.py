'''Se citește un număr natural n. Să se calculeze media aritmetică a tuturor
divizorilor săi.'''

n = int(input("Dati n: "))
s = 0
nrdiv = 0
for d in range(1, int(n ** (1 / 2)) + 1):
    if n % d == 0:
        s += d
        nrdiv += 1
        if d != n ** (1 / 2):
            s += n / d
            nrdiv += 1

print(s / nrdiv)
