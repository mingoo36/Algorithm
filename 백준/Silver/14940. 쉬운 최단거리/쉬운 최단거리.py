from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]  

dx = [1,-1,0,0] 
dy = [0,0,-1,1] 

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start_x, start_y = i,j

result[start_x][start_y] = 0
queue = deque()
queue.append((start_x, start_y))

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and result[nx][ny]==-1:
                result[nx][ny] = result[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result[i][j] = 0


for row in result:
    print(' '.join(map(str, row)))