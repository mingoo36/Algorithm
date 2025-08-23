from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    w = input()
    k = int(input())

    dic = defaultdict(list)

    for i in range(len(w)):
        if w.count(w[i]) >= k:
            dic[w[i]].append(i)

    if not dic:
        print(-1)
        continue

    min_len = float('inf')
    max_len = 0

    for char, lst in dic.items():
        for i in range(len(lst) - k + 1):
            length = lst[i+k-1] - lst[i] + 1

            min_len = min(min_len, length)
            max_len = max(max_len, length)
    
    print(min_len, max_len)