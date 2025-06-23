import sys, heapq

input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
            continue
        else:
            print(0)
            continue
    
    heapq.heappush(heap, (abs(x),x))