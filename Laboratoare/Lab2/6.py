prop = input("propozitie:")
s = input("Cuvant de inlocuit:")
t = input("cuvanta cu care inlocuim :")
prop = " " + prop
s = "  " + s
t = " " + t
for semn in ";.,!?":
    x = s + semn
    y = t + semn
    prop = prop.replace(x, y)
print(prop)
