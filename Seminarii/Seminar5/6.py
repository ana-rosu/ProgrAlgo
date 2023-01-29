'''
n fiecare zi, 𝑛 șoferi transmit către Compania Națională de Administrare a
Infrastructurii Rutiere informații referitoare la starea unei anumite autostrăzi, respectiv
intervale închise de forma [𝑥, 𝑦] având semnificația "asfaltul de pe autostradă este avariat
între kilometrii 𝑥 și 𝑦". Considerând faptul că toate informațiile transmise de către șoferi
sunt corecte și cunoscând lungimea autostrăzii respective, scrieți un program care, la
sfârșitul zilei respective, să furnizeze angajaților Companiei Naționale de Administrare a
Infrastructurii Rutiere următoarele informații:
a) porțiunile de autostradă care sunt avariate, sub forma unei reuniuni de intervale;
b) porțiunile de autostradă care nu sunt avariate, sub forma unei reuniuni de intervale
deschise;
c) gradul de uzură al autostrăzii, respectiv raportul dintre numărul total de kilometri
avariați de autostradă și lungimea autostrăzii.
autostrada.in
200
57 67
50 59
69 84
100 121
60 68
73 79
160 170
70 80
120 127
autostrada.out
[50, 68]
[69, 84]
[100, 127]
[160, 170]
(0, 50)
(68, 69)
(84, 100)
(127, 160)
(170, 200)
35%
Explicatii
Lungimea autostrăzii este 200 km.
Porțiunile avariate sunt [50, 68], [69, 84],
[100, 127] și [160, 170].
Porțiunile neavariate sunt (0, 50), (68, 69),
(84, 100), (127, 160) și (170, 200).
Gradul de uzură al autostrăzii este 35%,
deoarece numărul total de kilometri avariați
este 70.
'''