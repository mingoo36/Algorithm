import heapq, sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())

min_heap = []
max_heap = []
solved = defaultdict(int)

for _ in range(n):
    num , level = map(int, input().split())
    heapq.heappush(min_heap,(level, num))
    heapq.heappush(max_heap,(-level, -num))

m = int(input())

for _ in range(m):
    x = list(input().split())
    cmd = x[0]

    if cmd == 'add':
        num , level = int(x[1]), int(x[2])
        heapq.heappush(min_heap,(level, num))
        heapq.heappush(max_heap,(-level, -num))
    
    elif cmd == 'recommend':
        if x[1] == '1':
            while solved[abs(max_heap[0][1])] != 0:
                solved[abs(max_heap[0][1])] -= 1
                heapq.heappop(max_heap)
            print(-max_heap[0][1])
        
        else:
            while solved[abs(min_heap[0][1])] != 0:
                solved[abs(min_heap[0][1])] -= 1
                heapq.heappop(min_heap)
            print(min_heap[0][1])


    elif cmd == 'solved':
        solved[int(x[1])] += 1