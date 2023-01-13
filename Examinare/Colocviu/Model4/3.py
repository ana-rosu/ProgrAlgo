# Am stocat datele intr-un dictionar de tipul
# {'Ana Maria Pop': {'Matematica': [10, 9, 9, 10, 10], 'Limba romana': [8, 9, 9, 8], 'Fizica': [10, 9, 7, 10, 10]}
def citire_date():
    with open('catalog.in') as f:
        nr_elevi = int(f.readline())
        d = {}
        for line in f:
            nume_elev = ''.join([x for x in line[:-3]])
            nr_materii = int(line[-2])
            for i in range(nr_materii):
                line = f.readline()
                line = line.replace('\n', '')
                aux = [el for el in line.split(',')]
                materie = aux[0]
                note = [int(nr) for nr in aux[1:]]
                if nume_elev not in d:
                    d[nume_elev] = {materie:note}
                else:
                    d[nume_elev][materie] = note
        return d

def detalii_elev(date, nume_elev):
    l = []
    for materie, note in date[nume_elev].items():
        medie = sum(note)/len(note)
        if len(note) == 1 or medie < 5:
            medie = 0
        l.append((materie, round(medie, 2)))
    return l

def clasament(date, *nume_elevi):
    lista = []
    for nume_elev in nume_elevi:
        situatie = detalii_elev(date, nume_elev)
        medie = 0
        for el in situatie:
            medie+=el[1]
            if el[1] ==0:
                medie = 0
                break
        if medie:
            medie /= len(situatie)
        lista.append((nume_elev, medie))
    lista.sort(key = lambda t: -t[1])
    return lista

date = citire_date()
print(date)

note = detalii_elev(date, 'Ana Maria Pop')
note.sort(key = lambda t: t[0])
for el in note:
    print(f'{el[0]} {el[1]:.2f}')

print(clasament(date, 'Ioana Matei', 'Alin Enache', 'Ana Maria Pop'))


# Am stocat datele intr-un dictionar de tipul
# {'Ana Maria Pop': [('Matematica', [10, 9, 9, 10, 10]), ('Limba romana', [8, 9, 9, 8]), ('Fizica', [10, 9, 7, 10, 10])]}
# def citire_date():
#     with open('catalog.in') as f:
#         nr_elevi = int(f.readline())
#         d = {}
#         for line in f:
#             nume_elev = line[:-3]
#             nr_materii = int(line[-2:])
#             for i in range(nr_materii):
#                 line = f.readline()
#                 line = line.replace('\n', '')
#                 aux = [x for x in line.split(',')]
#                 t = (aux[0], [int(nr) for nr in aux[1:]])
#                 if nume_elev not in d:
#                     d[nume_elev] = [t]
#                 else:
#                     d[nume_elev].append(t)
#         return d
#
# def detalii_elev(date, nume_elev):
#     l = []
#     materii = d[nume_elev]
#     for t in materii:
#         medie = round((sum(t[1])/len(t[1])),2)
#         if len(t[1])==1 or medie < 5:
#             medie = 0
#         l.append((t[0],medie))
#     return l
#
# # def clasament(date, *nume_elevi): este exact la fel
#
# d = citire_date()
# print(d)
#
# note = detalii_elev(d, 'Ana Maria Pop')
# note.sort(key = lambda t: t[0])
# for el in note:
#     print(f'{el[0]} {el[1]:.2f}')