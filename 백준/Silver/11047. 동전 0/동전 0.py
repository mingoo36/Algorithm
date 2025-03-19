n,m = map(int, input().split())
count = 0
lst = [int(input()) for _ in range(n)][::-1]

for i in lst:
  count+= m//i
  m = m%i

print(count)