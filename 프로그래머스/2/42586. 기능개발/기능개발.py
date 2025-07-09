def solution(progresses, speeds):
    answer = []
    
    result = []
    
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i] == 0:
            x = (100 - progresses[i]) // speeds[i]
        else:
            x = (100 - progresses[i]) // speeds[i] + 1
        result.append(x)
        
    first = result[0]
    count = 1
    
    for i in result[1:]:
        if i <= first:
            count +=1
        else:
            answer.append(count)
            count = 1
            first = i
    
    answer.append(count)
    return answer