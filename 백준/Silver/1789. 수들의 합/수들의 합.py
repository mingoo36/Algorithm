n = int(input())
i = 1
count = 0

while n >= i:
    n -= i
    i += 1
    count += 1

print(count)