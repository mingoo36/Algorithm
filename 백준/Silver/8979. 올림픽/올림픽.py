n, t = map(int, input().split())

result = []

for _ in range(n):
    country = list(map(int, input().split()))
    result.append(country)

result.sort(key=lambda x: (x[1], x[2], x[3]),  reverse=True)

rank = 1
first = result[0][1:]

for i in range(n):
    if i>0:
        if result[i][1:] != first:
            rank += 1
            first = result[i][1:]
        
    if result[i][0] == t:
        print(rank)
        break