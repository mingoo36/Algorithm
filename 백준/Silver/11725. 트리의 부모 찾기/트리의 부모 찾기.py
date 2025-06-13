import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [[] for _ in range(n+1)]

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    x = queue.popleft()
    for i in graph[x]:
        if not visited[i]:
            result[i] = x
            visited[i] = True
            queue.append(i)

for i in result[2:]:
    print(i)


