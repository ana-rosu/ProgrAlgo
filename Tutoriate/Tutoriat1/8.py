'''Un număr se numește superprim dacă el și prefixele lui sunt prime. Să se
scrie un program care citește de la tastatură un număr n și verifică dacă este
superprim'''

n = int(input('Dati n: '))

ok = True
while n != 0 and ok is True:
    for d in range(2, int(n ** (1 / 2) + 1)):
        if n % d == 0:
            ok = False
    break
    n //= 10
print(ok)
