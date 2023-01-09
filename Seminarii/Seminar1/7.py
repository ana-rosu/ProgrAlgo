'''Sa se calculeze nr obtinut prin aplicarea operatorului XOR intre toate elementele tuturor submultimilor
unei multimi nevide A = {a1, a2, a3,..., an} inclusa in N, mai putin multimea vida.
Exemplu:  pt multimea A = {2,7,4} trebuie afisata valoarea
v = (2) ^ (7) ^ (4) ^ (2^7) ^ (2^4) ^ (7^4) ^ (2^4^7) = 0, unde am folosit parantezele pt a evidentia submultimile lui A'''

n = int(input('Dati cardinalul multimii A: '))

if n == 1:
    print(int(input('Dati elementul lui A: ')))
else:
    print(0)