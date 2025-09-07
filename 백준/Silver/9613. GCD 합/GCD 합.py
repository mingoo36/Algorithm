import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


t = int(sys.stdin.readline())
for _ in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    sumNumber = 0
    for i in range(1, n[0] + 1):
        for j in range(i+1, n[0] + 1):
            sumNumber += gcd(n[i], n[j])
    print(sumNumber)