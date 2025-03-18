n = int(input())
x = list(map(int, input().split()))
result = 0
x.sort()
for i in range(len(x)):
  result += sum(x[0:i+1])
print(result)