'''Sa se verifice daca un sir de caractere t apare ca subsir intr-un sir s,
iar in caz afirmativ sa se afiseze toate pozitiile la care incepe t in s(nesuprapuse).
Ex1: t="abc" apare ca subsir in s="abccabcababcc" incepand cu pozitiile 0,4,9
Ex2: t="aa" apare ca subsir in s="aaaaaa" incepand cu pozitiile 0,2,4'''

s = input("Dati sir1: ")
t = input("Dati sir2: ")

x = s.find(t)

if x != -1:
    while x != -1:
        print(x)
        x = s.find(t, x + len(t))
else:
    print('Nu exista')
