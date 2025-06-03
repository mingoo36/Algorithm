n, money = map(int, input().split())

coins = sorted([int(input()) for _ in range(n)],reverse=True)

result = 0

for i in coins:
    if i > money:
        continue
    result += money // i
    money %= i

print(result)