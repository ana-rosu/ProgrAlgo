'''Sa se determine in mod eficient nr de biti nenuli din repr binara a unui nr nat'''
'''Solutia 1'''
print('Solutia 1')
n = int(input('n: '))
cnt = 0
while n:
    if n & 1 == 1:
        cnt += 1
    n = n >> 1
print(cnt)

'''Solutia 2'''
print('Solutia 2')
n = int(input('n: '))
cnt = 0
while n:
    n = n & (n - 1)
    cnt += 1
print(cnt)

'''
n & (n-1) elimina ultimul 1 din scrierea binara a lui n

Enemplu:
n         = 100110000
n-1       = 100101111
n & (n-1) = 100100000
'''