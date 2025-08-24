n = int(input())

x = list(map(int, input().split()))
x.sort()

if n == 1:
    print(x[0] ** 2)
else:
    print(x[0] * x[-1])