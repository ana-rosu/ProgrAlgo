'''Sa se verifice daca un sir de caractere t apare ca subsir intr-un sir s,
iar in caz afirmativ sa se afiseze toate pozitiile la care incepe t in s(nesuprapuse).
Epoz1: t="abc" apare ca subsir in s="abccabcababcc" incepand cu pozitiile 0,4,9
Epoz2: t="aa" apare ca subsir in s="aaaaaa" incepand cu pozitiile 0,2,4'''

s = input("Dati sir1: ")
t = input("Dati sir2: ")

poz = s.find(t)
if poz == -1:
    print("Șirul '" + t + "' nu apare în șirul '" + s + "'!")
else:
    print("Pozitiile pe care incepe sirul '" + t +
          "' în șirul '" + s + "':")
    while poz != -1:
        print(poz, end =' ')
        poz = s.find(t, poz + len(t))
