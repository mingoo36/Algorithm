from collections import deque

n,m = map(int,input().split())

graph = [list(map(int, input())) for _ in range(n)]

result = [[False]* m for _ in range(n)]
# 목표 지점은 (n-1 ,m-1)

queue = deque([(0,0)])
result[0][0] = 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny <m:
            if graph[nx][ny] == 1 and not result[nx][ny]:
                result[nx][ny] = result[x][y] + 1
                queue.append((nx,ny))

print(result[n-1][m-1])
