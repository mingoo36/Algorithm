j_money = int(input())
s_money = j_money
price = list(map(int, input().split()))

j_stock= 0
for i in price:
    j_stock += j_money // i
    j_money = j_money % i
j_total = j_stock * price[-1] + j_money

s_stock = 0
up = 0
down = 0

for i in range(1, len(price)):
    if price[i] > price[i-1]:
        up += 1
        down = 0
    elif price[i] < price[i-1]:
        up = 0
        down += 1
    else:
        up = 0
        down = 0 
    
    if down >=3:
        buy = s_money // price[i]
        s_stock += buy
        s_money -= buy * price[i]

    elif up >=3:
        s_money += s_stock * price[i]
        s_stock = 0
    else:
        continue
s_total = s_stock * price[-1] + s_money

if j_total > s_total:
    print("BNP")
elif j_total == s_total:
    print("SAMESAME")
else:
    print("TIMING")