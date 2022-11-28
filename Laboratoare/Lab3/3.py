'''
s: 23,47, 57, 23, 23, 47
l = [23,47,57]
duplicate=[23,23,47]

print(dir(list))
print(help(list.pop))
print(help(sorted))
'''

s = [int(x) for x in input('s: ').split()]
l = []
duplicate=[]
for x in s:
    if x not in l:
        l.append(x)
        duplicate.extend([x]*(l.count(x)-1))