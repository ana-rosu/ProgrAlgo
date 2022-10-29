'''Sa se verifice daca un nr nat nenul n este de forma 2^k sau nu. In caz afirmativ sa se afiseze valoarea k'''
'''n=2^k => n = 100.....00(2)'''

n = int(input("Dati n: "))

k = 0
while n & 1 == 0:
    n = n >> 1
    k += 1

if n == 1:
    print(k)
else:
    print('nu')
