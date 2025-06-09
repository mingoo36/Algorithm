x = list(input().split('-'))
result = []

for i in range(len(x)):
    tmp = list(x[i].split('+'))
    plus = 0
    for k in tmp:
        plus += int(k)
    result.append(plus)

a = result[0]

for i in range(1, len(result)):
    a -= result[i]

print(a)
