'''
Varianta recursiva:

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)

Pentru a evita calcularea repetată a unor termeni ai șirului, vom folosi tehnica
memoizării: vom utiliza o listă f pentru a memora termenii șirului, iar fiecare termen nou
f[i] va fi calculat ca sumă a celor doi termeni precedenți, respectiv f[i-2] și f[i-1]:
'''

def fib(n):
    f = [-1,0,1]
    for i in range(3, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fib(2))

# Se observă faptul că lista f este completată într-o maniera ascendentă (bottom-up),
# respectiv se începe cu subproblemele direct rezolvabile (cazurile 𝑛 = 0 și 𝑛 = 1) și apoi
# se calculează restul termenilor șirului, până la valoarea dorită f[n].