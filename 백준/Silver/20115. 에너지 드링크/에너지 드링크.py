n = int(input())

drinks = sorted(list(map(int, input().split())), reverse=True)

result = drinks[0]
for drink in drinks[1:]:
    result += drink/2

print(result)


