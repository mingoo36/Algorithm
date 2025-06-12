def solution(n, lost, reserve):
    x = []
    for i in lost:
        if i in reserve:
            x.append(i)
    
    for i in x:
        lost.remove(i)
        reserve.remove(i)
    
            
    result = n - len(lost)
    
    for i in sorted(lost):
        if i-1 in reserve:
            result +=1
            reserve.remove(i-1)
        elif i+1 in reserve:
            result +=1
            reserve.remove(i+1)
        else:
            continue
        
    
    
    return result 