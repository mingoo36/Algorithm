import sys
input = sys.stdin.readline

x = input().rstrip()

stack = []
answer = 0
tmp = 1

for i in range(len(x)):
    if x[i] == '(':
        stack.append(x[i])
        tmp *= 2
    elif x[i] == '[':
        stack.append(x[i])
        tmp *= 3
    elif x[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if x[i-1] == '(':
            answer += tmp
        
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if x[i-1] == '[':
            answer += tmp
        
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)