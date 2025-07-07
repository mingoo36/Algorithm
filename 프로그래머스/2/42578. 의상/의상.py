from collections import defaultdict
def solution(clothes):
    
    x = defaultdict(list)
    
    for n,k in clothes:
        x[k].append(n)
    
    answer = 1
    
    for items in x.values():
        answer *= (len(items) + 1)
    
    return answer-1



