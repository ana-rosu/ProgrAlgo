'''Sa se elimine prima vocala dintr-un sir'''

s = input('Dati sir: ')

for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        s = s[:i] + s[i + 1:]
        break

print(s)
