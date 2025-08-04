import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    result = 0
    max_prices = 0

    for price in reversed(prices):
        if price > max_prices:
            max_prices = price
        else:
            result += max_prices - price
        
    print(result)