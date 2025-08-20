n, d  = map(int, input().split())

dp = [0] * 10001

info = []

for _ in range(n):
    a,b,c = map(int, input().split())
    info.append((a,b,c))

for i in range(1,d+1):
    dp[i] = dp[i-1] + 1
    for start, end, dt in info:
        if end == i:
            dp[i] = min(dp[i],dp[start] + dt)

print(dp[d])