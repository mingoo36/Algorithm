import sys
def input():
    return sys.stdin.readline()

n = int(input())
cow = [-1 for _ in range(11)]
count = 0

for _ in range(n):
    a, b = map(int, input().split())

    if cow[a] == -1:
        cow[a] = b
    elif cow[a] != b:
        cow[a] = b
        count +=1
    else:
        continue

print(count)