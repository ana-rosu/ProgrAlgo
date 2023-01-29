'''
Această problemă apare destul de des în practică, în diverse forme: împărțirea unui
produs dintr-un depozit între mai multe magazine de desfacere, distribuirea unui sume
de bani (un buget) între mai multe firme sau persoane fizice, partiționarea unui teren
între mai mulți cumpărători etc
'''

'''
De exemplu, numărul natural n=4 poate fi descompus ca sumă de numere naturale
nenule, astfel: 1+1+1+1, 1+1+2, 1+2+1, 1+3, 2+1+1, 2+2, 3+1 și 4. 

! Restricția ca termenii sumei să fie numere naturale nenule este esențială, altfel problema ar avea o infinitate de soluții!
'''


def bkt(k):
    global s, n

    for v in range(1, n-k+1+1):
        s[k] = v
        scrt = sum(s[:k+1])
        # - to see what happens behind the scenes
        # print(s[1:])
        if scrt <=n:
            if scrt == n:
                print(*s[1:k+1], sep="+")
            else:
                bkt(k+1)

n = 4
s = [0] * (n+1)
bkt(1)
