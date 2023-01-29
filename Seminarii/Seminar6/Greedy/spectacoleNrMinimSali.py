# Complexitate O(n^2)
with open('spectacole.txt') as f:
    crt = 1
    lsp = []
    for line in f:
        aux = line.split('-')
        lsp.append((crt, aux[0].strip(), aux[1].strip()))
        crt += 1

# sortam spectacolele in ordinea crescatoare a orelor de inceput
lsp.sort(key = lambda t: t[1])

# stocam datele intr-o lista de liste, fiecare lista reprezentand o sala
psop = [[lsp[0]]]

for sp in lsp[1:]:
    # pentru spectacolul curent, verificam daca se poate programa intr-una dintre sali
    for sala in psop:
        if sp[1] >= sala[len(sala)-1][2]:
            sala.append(sp)
            break
    # in cazul in care spectacolul curent nu a fost programat in niciuna dintre salile curente,
    # deci instructiunea break nu s-a executat, atunci il programam intr-o sala(lista) noua
    else:
        psop.append([sp])

print('Numarul minim de sali: ' + str(len(psop)))
print()
crt = 1
for sala in psop:
    print(f'Sala {crt}:')
    for sp in sala:
        print(f'{sp[1]}-{sp[2]} Spectacolul {sp[0]}')
    crt+=1