s = int(input())
status = [0] + list(map(int, input().split())) 

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:  
        for i in range(b, s + 1, b):
            status[i] = 1 - status[i]
    elif a == 2:  
        l = r = b
        while l > 0 and r <= s and status[l] == status[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        for i in range(l, r + 1):
            status[i] = 1 - status[i]

for i in range(1, s + 1):
    print(status[i], end=' ')
    if i % 20 == 0:
        print()
