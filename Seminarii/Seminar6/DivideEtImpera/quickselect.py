# selectia celui de-al k minim
# Considerăm o listă 𝐿 de lungime 𝑛 și dorim să determinăm al 𝑘-lea minim al său

'''De exemplu, pentru 𝐴 = [10, 7, 25, 4, 3, 4, 9, 12, 7] și 𝑘 = 5 vom obține
valoarea 7, deoarece lista A sortată crescător este [3, 4, 4, 7, 7, 9, 10, 12, 25]. Evident,
problema poate fi rezolvată sortând lista și apoi accesând elementul aflat pe poziția 𝑘 −
1, complexitatea acestei soluții fiind 𝒪(𝑛 log2 𝑛).'''

''' 
Un algoritm de tip Divide et Impera:
1) alegem aleatoriu un element din lista ca pivot
2) partitionam lista A in 3 liste in raport cu pivotul respectiv
    -> o lista L formata din elemente strict mai mici decat pivotul
    -> o lista E formata din elemente egale cu pivotul
    -> o lista G formata din elemente strict mai mari decat pivotul
3) comparam valoarea k cu lungimile celor 3 liste si
 fie furnizam valoarea cautata (daca a k a valoare se gaseste in lista E)
 fie reluam procedeul pt una dintre listele L sau G
'''
# Complexitate O(n), insa selectarea repetata a pivotului duce la complexitate O(n^2)!
import random

def quickselect(A, k, f_pivot = random.choice):
    pivot = f_pivot(A)

    L = [x for x in A if x < pivot]
    E = [x for x in A if x == pivot]
    G = [x for x in A if x > pivot]

    if k < len(L):
        return quickselect(L, k, f_pivot)
    elif k < len(L) + len(E)
        return E[0]
    else:
        return quickselect(G, k-len(L) - len(E), f_pivot)

'''
Teoretic, un pivot "bun" ar trebui să fie mediana listei respective, adică valoarea aflată
la mijlocul listei sortate crescător, sau, cel puțin, o valoare apropiată de aceasta.
 
În continuare, vom prezenta algoritmul mediana medianelor, tot de tip Divide et Impera,
care permite determinarea unui pivot "bun" pentru o listă. Algoritmul a fost creat în anul
1973 de către informaticienii M. Blum, R.W. Floyd, V. Pratt, R.L. Rivest și R. Tarjan, din
acest motiv fiind cunoscut și sub numele de algoritmul BFPRT.
 
Pașii algoritmului, pentru o listă 𝐴 formată din 𝑛 elemente, sunt următorii:
• se împarte lista 𝐴 în [n/5] liste de lungime 5 (dacă ultima listă nu are exact 5
elemente, atunci ea poate fi eliminată) 
• pentru fiecare dintre cele [𝑛/5] liste de lungime 5 se determină direct mediana sa
(e.g., se sortează lista și se returnează elementul aflat în mijlocul său);
• se reia procedeul pentru lista formată din medianele celor [𝑛/5] liste de lungime 5 
până când se obține mediana medianelor (i.e., lista medianelor are cel mult 5 elemente).

Exemplu:
Considerăm lista 𝐴 = [3, 14, 10, 2, 15, 10, 5, 51, 15, 20, 40, 4, 18, 13, 8,
40, 21, 61, 19, 50, 12, 35, 8, 7, 22, 100, 17] cu 𝑛 = 27 elemente.
După sortarea fiecărei liste de lungime 5 (am eliminat lista [100,17], deoarece este formată doar din două elemente)
și determinarea medianelor lor, reluăm procedeul pentru lista medianelor, respectiv
[10, 15, 13, 40, 12], și obținem pivotul 13.
'''

def BFPRT(A):
    if len(A) <= 5:
        return sorted(A)[len(A) // 2]
    grupuri = [sorted(A[i:i + 5]) for i in range(0, len(A), 5)]
    mediane = [grup[len(grup) // 2] for grup in grupuri]
    return BFPRT(mediane)

#  T(n) ∈ O(n), totusi complexitatea liniara se obtine pt constanta destul de mare (c=140, din Teorema Master)
#  In practică se preferă utilizarea variantei cu pivot ales aleatoriu deoarece are o complexitate medie mai bună