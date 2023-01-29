# a) Norocel a moștenit G kilograme de aur. Deoarece Norocel este și mărinimos, el s-a
# gândit să împartă cele G kilograme de aur în 𝑛 saci cu proprietatea că valoarea absolută
# a diferenței dintre greutățile oricăror doi saci să fie cel mult egală cu o valoare i și apoi
# să doneze 𝑛 − 1 dintre sacii obținuți unor cazuri sociale. Ajutați-l pe Norocel să-și
# împartă aurul conform dorințelor sale scriind un program Python care să citească de la
# tastatură numerele G, n și i, după care să afișeze toate modalitățile în care Norocel poate
# să-și împartă aurul moștenit în saci. Dacă nu esolistă nicio modalitate de împărțire a
# aurului care să respecte cerințele lui Norocel, atunci programul va afișa mesajul
# “Imposibil”.
# Esolemplu: Pentru G = 10, n = 3 și i = 4 trebuie afișate următoarele 22 de variante pentru
# împărțirea aurului (nu neapărat în această ordine):
# 1 + 4 + 5
# 1 + 5 + 4
# 2 + 2 + 6
# 2 + 3 + 5
# 2 + 4 + 4
# 2 + 5 + 3
# 2 + 6 + 2
# 3 + 2 + 5
# 3 + 3 + 4
# 3 + 4 + 3
# 3 + 5 + 2
# 3 + 6 + 1
# 4 + 1 + 5
# 4 + 2 + 4
# 4 + 3 + 3
# 4 + 4 + 2
# 4 + 5 + 1
# 5 + 1 + 4
# 5 + 2 + 3
# 5 + 3 + 2
# 5 + 4 + 1
# 6 + 2 + 2
# b) Modificați o singură instrucțiune din program astfel încât să fie afișate doar soluțiile
# care conțin un sac cu greutatea de 1 kg. Pentru esolemplul anterior, aceste soluții sunt
# cele scrise cu roșu. (0.5 p.)

def bkt(k):
    global g, s, n, i, cnt

    for v in range(1, g):
        s[k]=v
        scrt = sum(s[1:k+1])

        if scrt <= g and abs(s[k]-s[k-1])<=i:
            if k == n:
                if scrt == g:
                    cnt+=1
                    print(*s[1:k+1], sep='+')
            else:
                bkt(k+1)

cnt =0
g = 10
i = 4
n = 3
s = [0] * (g+1)
bkt(1)
print(cnt)

# def back(l):
#     global verif,s,n,g,k
#     if l == n+1:
#         if sum(sol[1:]) == g:
#             verif = 1
#             print(*sol[1:], sep = "+")
#     else:
#         for i in range (1, g):
#             sol[l] = i
#             scrt = sum(sol[1:l+1])
#             if scrt <= g:
#                 ok = 1
#                 for i in range(1, l):
#                     if abs(sol[i]-sol[l]) > k:
#                         ok = 0
#                         break
#                 if ok == 1:
#                     back(l+1)
#
#
# g = 10
# n = 3
# k = 4
# sol = [0] *(n+1)
#
# verif = 0
#
# back(1)
#
# if verif == 0:
#     print("Nu exista")