import sys
input = sys.stdin.readline

t = int(input())

dp = [1] * 10001

for i in [2,3]:
    for j in range(i,10001):
        dp[j] += dp[j-i]

for _ in range(t):
    n = int(input())
    print(dp[n])