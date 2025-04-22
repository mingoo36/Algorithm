h1 = []
h2 = []
result = []


n, m = map(int, input().split())
for _ in range(n):
    h1.append(list(map(int, input().split())))


p, k = map(int, input().split())
for _ in range(p):
    h2.append(list(map(int, input().split())))


for _ in range(n):
    result.append([0] * k)


for i in range(n):
    for j in range(k):
        for x in range(m):
            result[i][j] += h1[i][x] * h2[x][j]

for row in result:
    print(*row)