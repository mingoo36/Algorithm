import sys

input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    x = list(input().split())
    cmd = x[0]

    if cmd == 'all':
        s = set(range(1,21))
        continue
    elif cmd == 'empty':
        s.clear()
        continue

    v = int(x[1])

    if cmd == 'add':
        s.add(v)
    
    elif cmd == 'remove':
        s.discard(v)

    elif cmd == 'check':
        print('1' if v in s else '0')

    elif cmd == 'toggle':
        if v in s:
            s.remove(v)
        else:
            s.add(v)
    