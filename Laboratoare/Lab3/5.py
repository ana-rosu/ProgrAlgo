'''Fie un text literar (cu semne de punctuatie, propozitii etc)
a) sa se afiseze nr cuvv care se incheie cu o vocala
b) sa se afiseze nr cuv care se incheie cu o vocala din fiecare propozitie
Ex: s='Ana, ai plecat?...Maria e acasa!'
a) 5
b) 2 (pt prima prop)
   3 (pt a 2 a prop)

Solutie: convertim semnele de punctuatie cu spatii si utilizam split()'''
# s = input('s: ')
sir = "test"
for c in sir:
 print(c, sep="1")
#Se va afișa: t e s t
