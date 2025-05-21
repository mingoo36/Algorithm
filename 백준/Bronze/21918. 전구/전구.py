n, m = map(int, input().split())
x = list(map(int, input().split()))

for _ in range(m):
    a,b,c = map(int, input().split())
    if a==1:
        x[b-1] = c
    elif a==2:
        for i in range(b-1,c):
            if x[i] == 0:
                x[i] = 1
            else:
                x[i] = 0
    elif a==3:
        for i in range(b-1,c):
            x[i] = 0
    elif a==4:
        for i in range(b-1,c):
            x[i] = 1
print(*x)