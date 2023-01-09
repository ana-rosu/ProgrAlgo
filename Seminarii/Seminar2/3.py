'''Se citeste o propozitie in care cuvintele sunt despartite intre ele prin spatii si semne de punctuatie uzuale.
Sa se afiseze toate cuvintele distincte de lungime maxima din propozitia data.
Ex: Se da propozitia: "Ana are prune si gutui verzi, dar mai multe prune decat gutui!"
Cuvintele distincte de lungimea maxima 5 sunt "prune", "gutui", "verzi", "multe", "decat" '''

s = input('Propozitia sau fraza: ')

separatori = ',.:;?!'

for x in separatori:
    s = s.replace(x, '')

sol = ''
lmax = 0

for cuv in s.split():
    if len(cuv) > lmax:
        lmax = len(cuv)
        sol = ' ' + cuv + ' '
    elif len(cuv) == lmax:
        if ' ' + cuv + ' ' not in sol:
            sol += cuv + ' '

sol = sol.strip()
print(sol)

