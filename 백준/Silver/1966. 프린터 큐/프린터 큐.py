from collections import deque



x = int(input())

for _ in range(x):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = deque((i, p) for i, p in enumerate(priorities))

    count = 0
    while queue:
        idx, val = queue.popleft()

        if any(val < other_val for _, other_val in queue):
            queue.append((idx, val))
        else:
            count += 1
            if idx == m:
                print(count)
                break