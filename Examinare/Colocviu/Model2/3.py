with open('autori.in') as f:
    aux = [int(nr) for nr in f.readline().split()]
    d ={}
    date = f.readlines()
    for linie in date[:aux[0]]:
        linie = linie.split()
        cod_autor = int(linie[0])
        nume_autor = ' '.join(linie[1:])
        cheie = (cod_autor, nume_autor)
        d[cheie] = {}
    for linie in date[aux[0]:]:
        linie = linie.split()
        for key in d.keys():
            if int(linie[0]) == key[0]:
                d[key][int(linie[1])] = (linie[2], linie[3], ' '.join(linie[4:]))

    print(d)

def sterge_carte(dict, cod_carte):
    for key, value in dict.items():
        for k in value.keys():
            if cod_carte == k:
                del dict[key][k]
                return key[1]
    return None

autor = sterge_carte(d, int(input()))
if autor != None:
    print(f'Cartea a fost scrisa de {autor}')
    print(d)
else:
    print('Cartea nu exista')

def carti_autor(dict,cod_autor):
    lista = []
    autor = None
    for key, value in dict.items():
        if cod_autor == key[0]:
            autor = key[1]
            for v in value.values():
                lista.append((v[2], v[0], v[1]))
    if autor:
        return autor, lista
    else:
        return []

cod = int(input('Dati codul autorului: '))
if carti_autor(d,cod) != []:
    autor, lista = carti_autor(d,cod )
    print(autor)
    for t in lista:
        print(*t)
else:
    print('Cod incorect')