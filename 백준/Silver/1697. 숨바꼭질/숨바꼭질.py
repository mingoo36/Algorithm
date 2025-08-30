from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
Max = 100001
dist = [0] * Max

def dfs(n,k):
    if n >= k:
        return n - k
    
    queue = deque([n])

    while queue:
        x = queue.popleft()

        if x == k:
            return dist[x]
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < Max and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)
        
print(dfs(n,k))