'''Se citeste un cuvant w, un nr nat nenul p si un sir format din n cuvinte. Sa se afiseze
toate cuvintele care sunt p-rime cu w (ultimele p caractere ale sale coincid cu
ultimele p caractere ale lui w).
Ex: Se citesc w="mere", p=2, n=3, cuvintele "pere", "teste", "programare". Se afiseaza
"pere" si "programare" '''

w = input("Dati cuvant: ")
p = int(input("p: "))
n = int(input("n: "))
sol = ""
for i in range(n):
    cuv = input("Cuvant: ")
    # if cuv[-p:] == w[-p:]:
    if cuv.endswith(w[-p:]):
        sol = sol + cuv + " "

print(sol)