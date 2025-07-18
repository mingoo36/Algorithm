n = int(input())


cookie = [list(input()) for _ in range(n)]

found = False
heart_x = 0
heart_y = 0

a,b,c,d,e = 0,0,0,0,0

for i in range(len(cookie)):
    for j in range(len(cookie[i])):
        if cookie[i][j] == '*':
            heart_x = i + 2 # 높이
            heart_y = j + 1 # 너비
            found = True
            break
    if found:
        break
        
for i in range(len(cookie)):
    for j in range(len(cookie[i])):
        if i == heart_x -1 and cookie[i][j] == '*':
            if j < (heart_y -1):
                a += 1
            elif j > (heart_y -1):
                b += 1
        
        if i > heart_x - 1 and cookie[i][j] == '*':
            if j == heart_y -1:
                c += 1
            elif j == heart_y -2:
                d += 1
            elif j == heart_y:
                e += 1
        
    
print(heart_x, heart_y)
print(a,b,c,d,e)