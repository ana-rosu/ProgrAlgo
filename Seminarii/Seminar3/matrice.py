# sol1
m = int(input("Numarul de linii: "))
n = int(input("Numarul de coloane: "))
T = []
for i in range(m):
    linie = []
    for j in range(n):
        x = int(input(f"T[{i}][{j}] = "))
        linie.append(x)
    T.append(linie)
print(f"Tabloul bidimensional: {T}")

# sol2
m = int(input("Numarul de linii: "))
n = int(input("Numarul de coloane: "))
T = [[0 for x in range(n)] for y in range(m)]
for i in range(m):
    for j in range(n):
        T[i][j] = int(input(f"T[{i}][{j}] = "))

# sol3
T = []
while True:
    linie = input(f"Elementele de pe linia {len(T)}: ")
    if len(linie) != 0:
        T.append([int(x) for x in linie.split()])
    else:
        break

print("Tabloul bidimensional:")
for linie in T:
    for el in linie:
        print(el, end=' ')
    print()
