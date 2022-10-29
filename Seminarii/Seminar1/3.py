'''Sa se determine in mod eficient nr de biti nenuli din repr binara a unui nr nat'''
'''Solutia 1'''
x = int(input('x: '))
# print(bin(x).replace('0b', '').count('1'))
cnt = 0
while x:
    if x & 1 == 1:
        cnt += 1
    x = x >> 1
print(cnt)

'''Solutia mai eficienta'''
n = int(input('n: '))
k = 0
while n:
    n = n & (n - 1)
    k += 1
print(k)

'''
n =         100010000100
n-1 =       100010000011
n & (n-1) = 100010000000 
Asadar n & (n-1) elimina ultimul 1 din scrierea binara a lui n
'''