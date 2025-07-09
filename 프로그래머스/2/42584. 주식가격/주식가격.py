from collections import deque

def solution(prices):
    
    answer = []
    
    queue = deque(prices)
    
    while queue:
        x = queue.popleft()
        
        count = 0
        
        for q in queue:
            count += 1
            
            if x > q:
                break
        answer.append(count)
                
        
            
    
    
    return answer