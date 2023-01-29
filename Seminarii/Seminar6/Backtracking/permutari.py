def bkt(k):
    global s,n

    for v in range(1,n+1):
        s[k] = v
        # conditie necesara (nu si suficienta): s[1],..,s[k-1],s[k] este solutie partiala daca s[k] != s[i] pt orice i ∈ {1,..,k-1}
        if s[k] not in s[:k]:
            # pentru a fi si solutie (conditia suplimentara pt suficienta), trebuie sa formam o permutare de ordin n
            if k == n:
                print(*s[1:], sep =",")
            else:
                bkt(k+1)

n = 6
# index de la 1 la n
s = [0] * (n+1)
bkt(1)