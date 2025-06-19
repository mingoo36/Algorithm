from collections import deque

n = int(input())
x = list(map(int, input().split()))

queue = deque()

for idx, value in enumerate(x, start=1):
    queue.append((idx,value))


result = []
while queue:
    idx, value = queue.popleft()
    result.append(idx)
    if value >0:
        queue.rotate(-(value-1))
    else:
        queue.rotate(-value)


print(' '.join(map(str, result)))