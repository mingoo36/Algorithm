e, s, m = map(int,  input().split())

x = 1
while True:
    if (x-e) % 15 == 0 and (x-s) % 28 == 0 and (x-m) % 19 == 0:
        break
    x += 1

print(x)