from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def dfs(n,k):
    if n >= k:
        return n - k
    
    Max = 100000
    visited = [False] * (Max + 1)
    visited[n] = True
    queue = deque([(n,0)])

    while queue:
        x, t = queue.popleft()

        if x == k:
            return t
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= Max and not visited[nx]:
                visited[nx] = True
                queue.append((nx, t+1))
        
print(dfs(n,k))