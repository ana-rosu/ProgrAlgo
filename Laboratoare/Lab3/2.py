'''
2 siruri de numere
a) elementele comune
b) elementele comune si nr lor de aparitii comun
c) diferenta simetrica
'''
# s1 = input('sir1: ')
# s2 = input('sir2: ')
s1 = '2 -3 -100 2 3 7'
s2 = '-100 2 2 9 10 11 5 2 2'

l1=[int(x) for x in s1.split()]
l2=[int(x) for x in s2.split()]
l3=[]
l4=[]

s1 = set(l1)
for el in s1:
    if el in l2:
        l3.append(el)
        nrApComune = min(l1.count(el), l2.count(el))
        l4.extend([el]*nrApComune)
print(l3, l4)