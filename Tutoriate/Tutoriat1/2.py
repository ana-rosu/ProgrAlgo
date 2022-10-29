'''Se citește un număr natural n. Să se verifice dacă este palindrom.'''

# v1
n = int(input("n= "))
c = n
o = 0
while n:
    o = o * 10 + n % 10
    n //= 10

print(c == o)

# v2
x = input("x= ")
print(x[::-1] == x)
