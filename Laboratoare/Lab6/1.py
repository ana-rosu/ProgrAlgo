# n = 4
# di, l1
# 7, 2
# 3, 2
# 3, 2
# 6, 5
# activitatea i se desfasoare in intervalul ( , ) si are intarziere de ... secunde
# scriere in fisier
n = int(input('Dati n: '))

L = []
for i in range(n):
    l = [int(x) for x in input().split()]
    L.append(l)
print(L)

l = sorted(L, key=lambda x: int(x[0]))
for i, subl in enumerate(l):
    print(f'Activitatea {i} se desfasoara in intervalul')

