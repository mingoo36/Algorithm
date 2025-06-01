n, m = map(int, input().split())
x, y, z = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

way = {
    0: (-1, 0),  
    1: (0, 1),   
    2: (1, 0),   
    3: (0, -1)   
}

count = 0

while True:

    if map[x][y] == 0:
        map[x][y] = 2  
        count += 1

    cleaned = False

  
    for _ in range(4):
        z = (z + 3) % 4  
        dx, dy = way[z]
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
            x, y = nx, ny  
            cleaned = True
            break

    if cleaned:
        continue  

    bx, by = way[(z + 2) % 4]  
    nx, ny = x + bx, y + by

    if 0 <= nx < n and 0 <= ny < m and map[nx][ny] != 1:
        x, y = nx, ny  
    else:
        break  
print(count)
