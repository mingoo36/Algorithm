x = list(range(1,31))
for i in range(28):
    a = int(input())
    x.remove(a)

print(min(x))
print(max(x))