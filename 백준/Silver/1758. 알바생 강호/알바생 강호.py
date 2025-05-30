n = int(input())

tips = [int(input()) for _ in range(n)]

tips.sort()
tips.reverse()
result  = tips

for i in range(1,n+1):
    result[i-1] = tips[i-1] - (i-1)

money = 0

for i in result:
    if i > 0:
        money += i

print(money)