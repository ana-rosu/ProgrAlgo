'''Verificam daca un sir este periodic sau nu.
ex: abcdabcd sir periodic cu perioada abcd
ex: abcdabcda sir neperiodic

abcabcdabcabcd perioada abcabcd
abaaba perioada aba
'''

s = input('Dati sir: ')
n = len(s)

for d in range(1, n // 2 + 1):
    if n % d == 0:
        subsir = s[:d]
        repetitie = n // d
        if subsir * repetitie == s:
            print(subsir)
            break
else:
    print('neperiodic')
