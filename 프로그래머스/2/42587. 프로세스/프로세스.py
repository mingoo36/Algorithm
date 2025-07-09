from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    count = 0
    while queue:
        curr = queue.popleft()
        
        if any(curr[0] < item[0] for item in queue):
            queue.append(curr)
        else:
            count += 1
            if curr[1] == location:
                return count
                
                
    
