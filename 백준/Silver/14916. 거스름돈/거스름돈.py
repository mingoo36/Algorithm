money = int(input())

dp = [0] + [float('inf')] * money

for coin in [2,5]:
    for i in range(coin, money+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[money] if dp[money] != float('inf') else -1)