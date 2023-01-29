def bkt(i):
    global s, n, k, cnt

    for v in range(1,n+1):
        s[i] = v
        if s[i] not in s[:i] and s[i] > s[i-1]:
            if i == k:
                cnt +=1
                print(*s[1:], sep =',')
            else:
                bkt(i+1)
cnt = 0
n = 5
k = 3
s = [0] * (k+1)
bkt(1)
print(f'\nNumarul combinarilor de {n} luate cate {k} este {cnt}')