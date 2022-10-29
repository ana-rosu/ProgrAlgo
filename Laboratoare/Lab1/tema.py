''' A={1,2,3,4,...,n}
Sa se afiseze toate submultimile lui A.
A={1,2,3,4,5}

{} ->    00000 ->  0
{1} ->   10000 ->  16
{2,3} -> 01100 ->  12
{3} ->   00100 ->  4
...
{1,2,3,...,n}->11111->2+2**1+2**2+...+2**n-1
Parcurgem numerele de la 0 la (2*n)-1 și transformăm fiecare număr în baza 2;
Obținem astfel pentru fiecare număr, un șir de biți care va fi transformat în submulțime '''

n = int(input('Dati n: '))
end = (1 << n) - 1
# end=2**n-1


i = 0
while i <= end:
    s = bin(i).replace("0b", "")
    s = s.rjust(n, '0')

    print('{', end='')
    for index, char in enumerate(s):
        if int(char) == 1:
            print(index + 1, end='')
    print('}')
    i += 1
