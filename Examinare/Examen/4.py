# Să se afișeze toate permutările mulțimii A = {1,2, ..., n}, unde n este un număr natural nenul
def bkt(k):
    global s, n

    for v in range(1,n+1):
        s[k] = v
        if s[k] not in s[:k]:
            if k == n:
                print(*s[1:])
            else:
                bkt(k+1)

n = 5
s = [0] * (n+1)
bkt(1)