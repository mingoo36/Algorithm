import sys
input = sys.stdin.readline

while True:
    x = list(map(int, input().split()))
    x = sorted(x)

    if x[0] == 0 and x[1] == 0 and x[2] == 0:
        break

    if x[0] + x[1] <= x[2]:
        print('Invalid')
    elif x[0] == x[1] == x[2]:
        print('Equilateral')
    elif x[0] == x[1] or x[1] == x[2]:
        print('Isosceles')
    else:
        print('Scalene')
