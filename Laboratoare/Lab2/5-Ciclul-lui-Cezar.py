'''ex: pt s = laborator si k = 3 -> oderudwru
a->d
...
w->z
x->a
y->b
z->c!!'''

s = input('Dati sir: ')
k = int(input('Dati k: '))
t = ''
for i in range(len(s)):
    if s[i] == 'x':
        t = t + 'a'
    elif s[i] == 'y':
        t = t + 'b'
    elif s[i] == 'z':
        t = t + 'c'
    else:
        t = t + chr(ord(s[i]) + k)

s = t
print(s)
