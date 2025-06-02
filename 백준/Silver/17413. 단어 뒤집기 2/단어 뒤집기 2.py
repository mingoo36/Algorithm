s = input()
stack = []
result = ''
check = False

for ch in s:
    if ch == '<':
        while stack:
            result += stack.pop()
        check = True
        result += ch
    elif ch == '>':
        check = False
        result += ch
    elif check:
        result += ch
    elif ch == ' ':
        while stack:
            result += stack.pop()
        result += ' '
    else:
        stack.append(ch)

while stack:
    result += stack.pop()

print(result)
