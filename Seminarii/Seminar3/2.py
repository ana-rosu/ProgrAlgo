'''Fișierul text numere.txt conține numere naturale despărțite prin spații și scrise pe mai
multe linii. Să se scrie în fișierul text numere_comune.txt numerele care apar pe toate
liniile din fișier.
Exemplu: Dacă fișierul numere.txt are următorul conținut:
2 1 5 1 3
1 4 2 2
2 1 1 6 8
atunci fișierul numere_comune.txt trebuie să conțină numerele 1 2, nu neapărat în această
ordine.'''
f = open('numere.txt')
for linie in f:
