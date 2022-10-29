'''Se citesc de la tastatura un cuvant, un nr n, pe cate o linie alte n cuvinte. Sa se afiseze cate dintre cele n cuvinte
sunt p rime cu primul cuvant(au ultimele p caractere egale cu ultimele p caractere ale primului cuvant)'''

primul = input('Dati cuvant: ')
n = int(input('Dati n: '))
p = int(input('Dati p: '))

cnt = 0
for i in range(n):
    cuvant = input("Dati urmatorul cuvant: ")
    if primul[-p:] == cuvant[-p:]:
        cnt += 1
print(cnt)