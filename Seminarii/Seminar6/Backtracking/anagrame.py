'''
Pentru a genera toate anagramele distincte ale unui cuvânt, vom genera
toate permutările de lungime egală cu lungimea cuvântului, pentru fiecare permutare
vom reconstitui cuvântul asociat și îl vom salva într-un set
'''
def bkt(k):
    global s, n, cuv, cuv_dist

    for v in range(1, n+1):
        s[k] = v
        if s[k] not in s[:k]:
            if k == n:
                aux = ''.join([cuv[i-1] for i in s[1:]])
                cuv_dist.add(aux)
            else:
                bkt(k+1)

cuv = 'rau'
n = len(cuv)
cuv_dist = set()
s = [0] * (n+1)
bkt(1)
print(*cuv_dist)