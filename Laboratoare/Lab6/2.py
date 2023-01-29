# primim dimensiunile unor liste ordonate. vrem sa stim in ce ordine le interclasam a.i nr de operatii pe care le facem in procesul interclasarii sa fie minim
# 20 30 20 35
# heap sau maxheap!!!
l = [int(x) for x in input('').split()]
while len(l) != 1:
    l.sort()
    s = 0
    min1 = min(l)
    l.remove(min1)
    min2 = min(l)
    l.remove(min2)
    s = min1 + min2
    l.append(s)

print(*l)

#heapul generat de python este o lista -> functia heapify
# cream el de tip tuplu in care salvam ordinea initiala (20, "1) , (30, "2") , (20, "3") , (35, "4")
# import heapq
# h = []
# heapq.heappush(h, arg2)
# heapq.heappop(h)
# 10 20 30 70 40
# 10
# 20 | 30
# 70 40 |
# dintr-un heap elimini numai capul prin pop (decapitare)
# FA PROBLEMA CU HEAPSORT
