city = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = distance[0] * price[0]

min_price = price[0]

for i in range(1, len(distance)):
    if min_price > price[i]:
        min_price = price[i]
    result += distance[i] * min_price

print(result)