def bkt(i):
    global s, n, k, cnt

    for v in range(1, n+1):
        s[i] = v
        if s[i] not in s[:i]:
            if i == k:
                cnt+=1
                print(*s[1:], sep=",")
            else:
                bkt(i+1)

n = 5
k = 3
cnt = 0
s = [0] * (k+1)
bkt(1)

print(f'\nNumarul aranjamentelor de {n} luate cate {k} este {cnt}')