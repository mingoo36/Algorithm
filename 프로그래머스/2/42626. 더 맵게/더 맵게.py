import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K:
        if len(scoville)  <= 1:
            return -1
        
        count +=1
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + (2 * y))
        
    return count