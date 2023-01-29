'''
Analizând enunțul problemei, observăm faptul că orice număr care este soluție a
problemei are cel mult 10 cifre, deoarece acestea trebuie să fie distincte, și problema are
soluție doar în cazul în care 𝑐 ∈ {0,1, … ,45}, deoarece cea mai mare sumă care se poate
obține din cifre distincte este egală cu 1 + 2 + ⋯ + 9 = 45

!!! Implementând algoritmul Backtracking corespunzător, nu vom
obține toate soluțiile, ci doar o parte dintre ele! De exemplu, pentru 𝑐 = 3, nu vom obține
numerele 120,210,30 din solutia completa 102, 12, 120, 201, 21, 210, 3 și 30.
Acelea le vom obtine din solutiile care nu contin cifra 0. In momentul afișării unei soluții, verificăm dacă ea conține deja o cifră egală cu 0,
iar în caz negativ o afișăm încă o dată și-i adăugăm un 0 la sfârșit.
'''
import sys

def bkt(k):
    global c

    for v in range(1 if k == 1 else 0, 10):
        s[k]=v
        scrt = sum(s[1:k+1])
        if s[k] not in s[1:k] and scrt <=c:
            if scrt == c:
                print(*s[1:k+1], sep ='')
                if 0 not in s[1:k+1]:
                    print(*s[1:k+1],0,sep='')
            else:
                bkt(k+1)
c = int(input('c = '))
if c < 0 or c > 45:
     print("Problema nu are soluție!")
     sys.exit()
s = [0] * 11
print('Toate nr cerute: ')
bkt(1)