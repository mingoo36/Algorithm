n,k = map(int, input().split())

x = []

for i in range(1, n+1):
  if n%i ==0:
    x.append(i)

if len(x) < k:
  print(0)
else:
  print(x[k-1])