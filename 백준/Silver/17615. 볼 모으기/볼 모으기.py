import sys
input = sys.stdin.readline

n = int(input())
balls = input().strip()

if len(set(balls)) == 1:
    print(0)
    sys.exit(0)

total_R = balls.count('R')
total_B = n - total_R

lR = 0
for i in balls:
    if i == 'R':
        lR += 1
    else:
        break

rR = 0
for i in reversed(balls):
    if i == 'R':
        rR += 1
    else:
        break

lB = 0
for i in balls:
    if i == 'B':
        lB += 1
    else:
        break

rB = 0
for i in reversed(balls):
    if i == 'B':
        rB += 1
    else:
        break

result = min(
    total_R - lR,
    total_R - rR,
    total_B - lB,
    total_B - rB
)

print(result)