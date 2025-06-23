import heapq, sys
# 파이썬에서 heapq은 기본적으로 최소 힙임, 최대힙 구현하려면 value 음수로 바꿔 넣고 나중에 다시 양수로 바꿈
# 힙은 푸시팝가능 푸시합(힙, 벨류) -> 벨류를 넣으면서 최소값 꺼냄

input = sys.stdin.readline
heap = []

n = int(input())

# 프린트했을때는 정렬된게 안보임

for _ in range(n):
    nums = list(map(int, input().split()))

    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

print(heap[0])