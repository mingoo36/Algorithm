n = int(input())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def count_bombs(x,y):
    count = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if bomb[nx][ny] == '*':
                count += 1
    return count

bomb = [list(input()) for _ in range(n)]
status = [list(input()) for _ in range(n)]
result = [['.' for _ in range(n)] for _ in range(n)]

game_over = False

for i in range(n):
    for j in range(n):
        if status[i][j] == 'x':
            if bomb[i][j] == '*':
                game_over = True
            else:
                result[i][j] = count_bombs(i,j)

if game_over:
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == '*':
                result[i][j] = '*'


for row in result:
    print(*row, sep='')
