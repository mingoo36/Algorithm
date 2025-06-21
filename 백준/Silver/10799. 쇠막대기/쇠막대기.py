x = input()
x = x.replace('()', '@')  

stack = []
result = 0

for ch in x:
    if ch == '(':
        stack.append('(')  
    elif ch == '@':
        result += len(stack)  
    elif ch == ')':
        stack.pop()  
        result += 1

print(result)
