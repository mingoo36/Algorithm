from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque([1])
    visited[1] = True
    distance = [0] * (n+1)
    
    while queue:
        x = queue.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                distance[i] = distance[x] + 1
    
        max_dist = max(distance)

    return distance.count(max_dist)