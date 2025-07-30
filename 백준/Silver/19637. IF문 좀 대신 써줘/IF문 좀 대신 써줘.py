import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grade = []

for _ in range(n):
    a,b = input().split()
    grade.append((a,int(b)))

names = [a for a,_ in grade]
scores = [b for _,b in grade]

import bisect

for _ in range(m):
    score = int(input())

    idx = bisect.bisect_left(scores,score)
    print(names[idx])