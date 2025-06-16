import sys
from collections import deque

input = sys.stdin.readline
n = int(input())


queue = deque()
for _ in range(n):
    cmd = input().strip()

    if cmd.startswith('push'):
        a, b = cmd.split()
        queue.append(int(b))
    elif cmd == 'pop':
        print(queue.popleft() if queue else -1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        print(0 if queue else 1)
    elif cmd == 'front':
        print(queue[0] if queue else -1)
    elif cmd == 'back':
        print(queue[-1] if queue else -1)



