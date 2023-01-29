'''
Fiind dată o tablă de șah de dimensiune 𝑛 × 𝑛, 𝑛 ≥ 4 (pentru 𝑛 ≤3 problema nu are soluții) problema cere să se determine toate
modurile în care pot fi plasate 𝑛 regine pe tablă astfel încât oricare două să nu se atace
între ele.
'''
# s[k] - coloana pe care este poziționată regina de pe linia k
# reginele trebuie sa nu se afle pe aceeasi linie, pe aceeasi coloana, sau pe aceeasi diagonala
# conditia referitoare la linii si coloane se reduce la generarea permutarilor de ordin n
# 2 regine se ataca pe diagonala daca dreapta formata de ele este paralela cu una dintre cele 2 diagonale ale tablei de sah
# adica daca au pantele egale cu 1 sau cu -1, deci daca modulul pantei dreptei = 1. |(s[k]-s[i])/k-i| != 1 sau, echivalent |s[k] - s[i]| != |k-i|

def bkt(k):
    global s,n

    for v in range(1,n+1):
        s[k] = v
        if s[k] not in s[:k] and True not in [abs(k-i) == abs(s[k]-s[i]) for i in range(1,k)]:
            if k == n:
                print(*s[1:], sep =",")
            else:
                bkt(k+1)

n = 4
# index de la 1 la n
s = [0] * (n+1)
bkt(1)