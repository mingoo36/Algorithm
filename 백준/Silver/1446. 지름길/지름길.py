import sys
input = sys.stdin.readline

n, d = map(int, input().split())
dt = [tuple(map(int, input().split())) for _ in range(n)] ## 값을 수정할 필요가 없으면 튜플이 더 메모리 측면에서 효율적임

dp = [float('inf')] * (d+1)
dp[0] = 0

for i in range(1,d+1):
    dp[i] = dp[i-1] + 1
    for start, end, length in dt:
        if i == end:
            dp[i] = min(dp[i], dp[start] + length)

print(dp[d])