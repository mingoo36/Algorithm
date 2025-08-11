import sys
input = sys.stdin.readline

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
p.sort()

result = 0

for i, (l,h) in enumerate(p):
    if h > result:
        result = h
        idx = i

height = p[0][1]

for i in range(idx):
    if p[i+1][1] > height:
        result += height * (p[i+1][0] - p[i][0])
        height = p[i+1][1]
    else:
        result += height * (p[i+1][0] - p[i][0])

height = p[-1][1]

for i in range(n-1, idx, -1):
    if p[i-1][1] > height:
        result += height * (p[i][0] - p[i-1][0])
        height = p[i-1][1]
    else:
        result += height * (p[i][0] - p[i-1][0])

print(result)