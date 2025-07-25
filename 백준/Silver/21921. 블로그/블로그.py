import sys
input = sys.stdin.readline
n, x = map(int, input().split())
visitors = list(map(int, input().split()))

curr_sum = sum(visitors[:x])
max_sum = curr_sum
count = 1

for i in range(x,n):
    curr_sum += visitors[i] - visitors[i-x]
    if curr_sum > max_sum:
        max_sum = curr_sum
        count = 1
    elif curr_sum == max_sum:
        count += 1


if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)