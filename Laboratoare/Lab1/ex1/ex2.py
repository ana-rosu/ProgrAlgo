'''
p1,p2,p3 prime
n-nat
afisati cate nr<=n sunt div cu p1,p2,p3
'''

p1 = int(input('p1: '))
p2 = int(input('p2: '))
p3 = int(input('p3: '))
n = int(input('n: '))

print(n // p1 + n // p2 + n // p3 - (n // (p1 * p2) + n // (p1 * p3) + n // (p2 * p3) + n // (p1 * p2 * p3)))
