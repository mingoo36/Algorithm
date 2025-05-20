import sys

def input():
    return sys.stdin.readline()

n = input()
result = bin(int(n,8))[2:]
print(result)