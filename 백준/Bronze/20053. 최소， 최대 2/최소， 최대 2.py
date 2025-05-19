import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
  a = int(input())
  b = list(map(int, input().split()))
  print(min(b), max(b))