n, d, k, c = map(int, input().split())

belt = [int(input()) for _ in range(n)]

belt += belt

result = 0
for i in range(n):
    window = belt[i:i+k]
    distinct = len(set(window))
    curr = distinct + (1 if c not in window else 0)

    if curr > result:
        result = curr
        
print(result)