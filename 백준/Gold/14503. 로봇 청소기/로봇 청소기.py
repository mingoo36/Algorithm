n, m = map(int, input().split())
x,y,z = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

count = 0

way = {
    0 : (-1, 0), # 북
    1 : (0, 1), # 동
    2 : (1, 0), # 남
    3 : (0, -1)  # 서
}



while True:
    if maps[x][y] == 0:
        maps[x][y] = 2
        count += 1

    
    cleaned = False

    for _ in range(4):
        z = (z+3)% 4
        dx, dy = way[z]
        nx, ny = dx + x , dy + y
        if maps[nx][ny]== 0 and 0<= nx <n and 0<= ny < m:
            x,y = nx, ny
            cleaned = True
            break
    
    if cleaned:
        continue

    bx, by = way[(z+2)%4]
    nx, ny = bx+x, by+y

    if maps[nx][ny]!= 1 and 0<= nx <n and 0<= ny < m:
        x,y = nx, ny
    else:
        break

print(count)