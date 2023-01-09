'''.Se citește un șir de caractere s.
Să se verifice dacă există un șir t, diferit de s, astfel încât șirul s
să se poată obține prin concatenarea de un număr arbitrar de ori k a șirului t.
De exemplu, pentru s="abcabc" avem t="abc" și k=2'''

s = input('Dati sir: ')
n = len(s)

for d in range(1, n // 2 + 1):
    if n % d == 0:
        t = s[:d] * (n // d)
        if t == s:
            print('t = ', s[:d], '\nk = ', n // d)
            break
else:
    print('Imposibil!')
