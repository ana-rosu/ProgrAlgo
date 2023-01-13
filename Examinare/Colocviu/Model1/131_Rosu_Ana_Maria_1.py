# Rosu Ana Maria, grupa 131
# SUB

f = open('text.in')
sir = f.read()
sir = sir.lower()
f.close()
semne = ',.:;!? '
for s in semne:
    sir = sir.replace(s, '')
sir = sir.replace('\n', '')

f = open('text.out', 'w')
l = len(sir)
L = []
for litera in set(sir):
    value = round((sir.count(litera) / l),3)
    L.append((litera, value))
L.sort(key=lambda t: (-t[1], t[0]))
for pereche in L:
    f.write(f"{pereche[0]} : {pereche[1]:.3f}" + '\n')



# nr = 2.25
# res = f'{nr:3f}'
# print(res)