'''
Un grup format din 𝑛𝑛 excursioniști (1 ≤ 𝑛𝑛 ≤ 100) au 𝑚𝑚 corturi (1 ≤ 𝑚𝑚 ≤ 100) cu
capacitățile 𝑐𝑐1, 𝑐𝑐2, … , 𝑐𝑐𝑚𝑚 astfel încât 𝑐𝑐1 + 𝑐𝑐2 + ⋯ + 𝑐𝑐𝑚𝑚 ≥ 𝑛𝑛. Capacitatea unui cort
reprezintă numărul maxim de excursioniști care pot sta în cortul respectiv. Scrieți un
program Python care să citească de la tastatură numerele naturale 𝑛𝑛, 𝑚𝑚, 𝑐𝑐1, 𝑐𝑐2, … , 𝑐𝑐𝑚𝑚 și
afișează toate posibilitățile de a repartiza cei 𝑛𝑛 excursioniști în cele 𝑚𝑚 corturi astfel încât
niciun cort să nu rămână gol, precum și numărul acestora. (2.5 p.)
Exemplu:
Pentru 𝑛𝑛 = 9, 𝑚𝑚 = 3, 𝑐𝑐1 = 5, 𝑐𝑐2 = 2, 𝑐𝑐3 = 4 există 5 modalități corecte de repartizare a
excursioniștilor în corturi:
3, 2, 4
4, 1, 4
4, 2, 3
5, 1, 3
5, 2, 2
'''

def bkt(k):
    global n, m, c

    for v in range(1, c[k]+1):
        s[k] = v

        scrt = sum(s[1:k + 1])
        if scrt <= n:
            if k == m:
                if scrt == n:
                    print(*s[1:], sep=',')
            else:
                bkt(k+1)

n = 9
m = 3
c = [0,5,2,4]
s = [0] * (m+1)
bkt(1)