'''
Inițializând componenta curentă s[k] cu prima valoare strict mai mare decât componenta
anterioară s[k-1] (mink = s[k-1]+1) – este cea mai eficientă variantă posibilă, deoarece
nu se generează și testează tupluri inutile și, mai mult, orice tuplu este soluție parțială
(elementele sale sunt generate direct în ordine strict crescătoare, deci sunt distincte),
ceea ce înseamnă că putem renunța la testarea condițiilor de continuare!
'''

def bkt(i):
    global n, k, s, cnt

    for v in range(s[i-1]+1, n+1):
        s[i] = v
        if i == k:
            cnt += 1
            print(*s[1:], sep=',')
        else:
            bkt(i+1)

n = 5
k = 3
cnt = 0
s = [0] * (k+1)
bkt(1)
print(f'\nNumarul submultimilor cu {k} elemente ale unei multimi cu {n} elemente este {cnt}')