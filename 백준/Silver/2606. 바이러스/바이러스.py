import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global result
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            result += 1
            dfs(i)
dfs(1)

print(result)