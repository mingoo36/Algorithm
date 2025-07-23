n = int(input())
cities = list(map(int, input().split()))
total_money = int(input())

start = 0
end = max(cities)
result = 0 



while start <= end:

    mid = (start + end) // 2

    total = 0

    for i in cities:
        total += min(i,mid)
    
    if total > total_money:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

