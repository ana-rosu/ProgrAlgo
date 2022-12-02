'''Considerăm un șir de caractere reprezentând un titlu în limba engleză.
 Să se formateze titlul respectiv conform următoarelor reguli:
 a)primul și ultimul cuvânt se vor scrie întotdeauna cu majusculă;
 b)toate cuvintele formate din cel puțin 5 litere se vor scrie cu majusculă;
 c)toate cuvintele formate din cel mult 4 litere care nu fac parte dintr-o listă de cuvinte exceptate (articole, prepoziții, conjuncții etc.)se vor scrie cu majusculă.

 Titlul poate să conțină și alte caractere în afară de litere mari sau mici (i.e., cifre sau semne de punctuație), iar cuvintele sunt despărțite între ele printr-un spațiu sau printr-un semn de punctuație și un spațiu.
 Lista cuvintelor exceptate poate conține, de exemplu, cuvintele "a", "an", "by", "on", "in", "at", "to", "for", "ago", "the", "past", "over", "into" și "onto".
 Exemple:
 •"where are WE GOING to?" -> "Where Are We Going To?"
 •"GOING To California By My Car" -> "Going to California by My Car"
 •"by my SIDE, at The SeaSide" -> "By My Side, at the Seaside"
 •"walking over the rainbow" -> "Walking over the Rainbow"
 '''

s = input('Titlul: ')
# eliminăm spațiile de la începutul și sfârșitul șirului, după care transformăm toate literele în minuscule
s = s.strip().lower()
# a)
# transformăm prima literă în majusculă
s = s[0].upper() + s[1:]
# căutăm ultimul cuvânt din titlu (începe după ultimul spațiu)
# și îi transformăm prima literă în majusculă
p = s.rfind(' ')
if p != -1:
    s = s[:p + 1] + s[p + 1].upper() + s[p + 2:]

exceptii = ' a an by on in at to for ago the past over into onto '

# cautam primul spatiu
p = s.find(' ')
while p != -1:
   # cautam urmatorul spatiu
    q = s.find(' ', p+1)
    if q != -1:
        cuv = s[p+1:q].strip(' ,.:;!?')
        if len(cuv) >=5 or (len(cuv) < 5 and ' ' + cuv + ' ' not in exceptii):
            s = s[:p+1] + s[p+1].upper() + s[p+2:]
    p = q

print(s)