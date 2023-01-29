with open('spectacole.txt') as f:
    crt = 1
    # lsp = lista spectacolelor, fiecare spectacol fiind memorat sub forma unui tuplu (ID, ora de început, ora de sfârșit)
    lsp = []
    for line in f:
        aux = line.split('-')
        # aux[0] = ora de început a spectacolului curent
        # aux[1] = ora de sfârșit a spectacolului curent
        lsp.append((crt, aux[0].strip(), aux[1].strip()))
        crt += 1

# sortam spectacolele crescator dupa ora de sfarsit
lsp.sort(key = lambda t:t[2])

# stocam planificarea optima a spectacolelor intr-o lista
# pe care o initializam cu spectacolul care se termina cel mai repede
posp = [lsp[0]]

# parcurgem restul spectacolelor
for sp in lsp[1:]:
    # daca spectacolul curent incepe dupa ultimul spectacol programat, atunci il programam si pe el
    if sp[1] > posp[len(posp)-1][2]:
        posp.append(sp)

with open('programare.txt', 'w') as f:
    f.write(f'Numarul maxim de spectacole: {len(posp)}\n\nSpectacolele programate:\n')
    for sp in posp:
        f.write(f'{sp[1]}-{sp[2]} Spectacol {sp[0]}\n')

