'''Afisati cel mai mic nr prim din intervalul [a,b]
Instructiunea else pt structurile repetitive se executa in cazul in care break nu s-a intamplat si tine locul unei variabile de tip bool.
'''
a = int(input('Dati a: '))
b = int(input('Dati b: '))
for i in range(a, b + 1):
    for d in range(2, i // 2 + 1):
        if i % d == 0:
            break
    else:
        print(i)
        break
else:
    print('nu exista nr prime')
