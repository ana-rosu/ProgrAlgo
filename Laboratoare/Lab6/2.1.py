import heapq

l = [int(x) for x in input('').split()]

heap = []
heapq.heapify(heap)
for el in l:
    heapq.heappush(heap, el)

op = 0
while len(heap) >= 2:
    s = 0
    min1 = heapq.heappop(heap)
    min2 = heapq.heappop(heap)
    s = min1 + min2
    op += s
    heapq.heappush(heap, s)

print(heap[0], op)
