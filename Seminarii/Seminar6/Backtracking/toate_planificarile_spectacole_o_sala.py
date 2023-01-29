'''
Problema poate fi rezolvată folosind doar metoda Backtracking, respectiv generând toate
planificările posibile ale celor 𝑛 spectacole date și păstrându-le pe cele care sunt corecte
și au lungimea maximă. Deoarece ordinea în care sunt planificate spectacolele contează,
trebuie utilizată o variantă modificată a generării tuturor aranjamentelor de lungime 𝑚
ale unei mulțimi cu 𝑛 elemente. Din cauza faptului că numărul maxim de spectacole care
se pot planifica fără suprapuneri poate varia între 1 (dacă toate cele 𝑛 spectacole se
suprapun) și 𝑛 (dacă niciun spectacol nu se suprapune cu toate celelalte 𝑛 − 1), va trebui
să considerăm și valoarea lui 𝑚 ca fiind cuprinsă între 1 și 𝑛, deci numărul total de
planificări generate va fi aproximativ 𝐴𝑛1 + 𝐴𝑛2 + ⋯ + 𝐴𝑛n ≫ 𝐴𝑛𝑛 = 𝑛!, deci complexitatea acestui algoritm va fi MULT mai mare decât 𝒪(𝑛!).

O variantă mai eficientă de rezolvare a acestei probleme o constituie utilizarea metodei
Greedy pentru a afla numărul maxim de spectacole 𝑛𝑚𝑠 care se pot programa fără suprapuneri, cu o complexitate 𝒪(𝑛 log2 𝑛) și generarea doar a aranjamentelor cu 𝑛𝑚𝑠 elemente ale unei mulțimi cu 𝑛 elemente:
'''
# funcție care determina numărul maxim de spectacole care pot fi
# programate fără suprapuneri folosind metoda Greedy
def numarMaximSpectacole(lsp):
    # sortăm spectacolele în ordinea crescătoare a orelor de sfârșit
    lsp.sort(key=lambda s: s[2])
    # ora de sfârșit a ultimului spectacol programat
    ult = "00:00"
    # cnt = numărul maxim de spectacole care se pot programa corect
    cnt = 0
    for sp in lsp:
        if sp[1] >= ult:
            cnt += 1
    ult = sp[2]
    return cnt
# generarea tuturor programărilor cu număr maxim de spectacole
# folosind metoda backtracking, respectiv generarea aranjamentelor
# cu nms elemente ale celor n spectacole



for linie in fin:
     aux = linie.split()
     # ora de inceput si ora de sfarsit pentru spectacolul curent
     tsp = aux[0].split("-")
     lsp.append((" ".join(aux[1:]), tsp[0], tsp[1]))

fin.close()

# n = numărul de spectacole
n = len(lsp)
fout = open("spectacole.out", "w")
# nms = numărul maxim de spectacole care se pot programa corect
# = lungimea soluțiilor care vor fi generate cu backtracking
nms = numarMaximSpectacole(lsp)
s = [0] * nms
bkt(0)
fout.close()