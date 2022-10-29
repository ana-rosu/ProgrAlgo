'''Se da un sir de caractere de la tastatura. Sa se traduca in limba pasareasca:
p dupa fiecare vocala si inca o data vocala'''

s = input('Dati sir: ')
t = ""

#Solutia1
for ch in s:
    t = t + ch
    if ch in 'aeiouAEIOU':
        t = t + 'p' + ch
s = t
print(s)

#Solutia2
i = 0
while i < len(s):
    if s[i] in 'aeiouAEIOU':
        s = s[:i + 1] + 'p' + s[i:]
        i += 2
    i += 1
print(s)
