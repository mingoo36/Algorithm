import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

x = list(range(1,n+1))

p = list(combinations_with_replacement(x, m))

for i in p:
  print(*i, end="\n")