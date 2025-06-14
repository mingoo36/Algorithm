def solution(arr):
    stack = []
    
    for i in arr:
        if not stack:
            stack.append(i)
        if i == stack[-1]:
            continue
        stack.append(i)
    
    return stack