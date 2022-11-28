'''
a = 9
b = 17
10, 10, 9, 16, 15, 10, 13
'''

ora1 = int(input('Dati ora de incepere a programului: '))
ora2 = int(input('Dati ora de incheiere a programului: '))
l = [int(x) for x in input('Dati orele sedintelor angajatilor: ').split()]

for i in range(ora1, ora2):
    if i not in l:
        print(i)