n = int(input())

for _ in range(n):
    x = input()
    stack = []
    ps = True
    for i in x:

        if i == '(':
            stack.append(i)
        
        elif i == ')':
            if stack:
                stack.pop()
            else:
                ps = False
                break 
        
    if stack:
        ps = False

    print('YES' if ps else 'NO')
