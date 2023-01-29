def bkt(i):
    global n, k, s, cnt

    for v in range(s[i - 1] + 1, n + 1):
        s[i] = v
        if i == k:
            cnt += 1
            print(*s[1:], sep=',')
        else:
            bkt(i + 1)


n = 3
for k in range(1, n + 1):
    cnt = 0
    s = [0] * (k + 1)
    bkt(1)
    print(f'Nr submultimilor cu {k} elemente este {cnt}')
