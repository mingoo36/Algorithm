# 백준에서 런타임에러 남
# 재귀함수 이슈

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

result = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            result[i] = v
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(result[i])