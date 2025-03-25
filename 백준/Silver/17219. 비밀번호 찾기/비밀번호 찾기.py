n, m = map(int, input().split())
x={}
for _ in range(n):
  site, password = input().split()
  x[site] = password

for _ in range(m):
  print(x[input()])