from itertools import combinations

n,m = map(int, input().split())
x = list(range(1,n+1))

p = list(combinations(x, m))

for i in p: 
  print(*i, end="\n")