n = int(input())
result = 0
p = []

for _ in range(n):
    l,h = map(int, input().split())
    p.append((l,h))

p.sort()

tmp = 0 
for (l,h) in p:
    if h > result:
        result = h
        idx = tmp
    tmp += 1

height = p[0][1]

for i in range(idx):
    if height < p[i+1][1]:
        result += height * (p[i+1][0] - p[i][0])
        height = p[i+1][1]
    else:
        result += height * (p[i+1][0] - p[i][0])

height = p[-1][1]

for i in range(n-1, idx, -1):
    if height < p[i-1][1]:
        result += height * (p[i][0] - p[i-1][0])
        height = p[i-1][1]
    else:
        result += height * (p[i][0] - p[i-1][0])

print(result)