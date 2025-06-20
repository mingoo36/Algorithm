n = int(input())


formula = input()

x= {}
for i in range(n):
    key = chr(ord('A') + i)
    x[key] = int(input())

stack = []


for i in formula:
    if i.isalpha():
        stack.append(x[i])
    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if i == '+':
            stack.append(num1 + num2)
        elif i == '-':
            stack.append(num1 - num2)
        elif i == '*':
            stack.append(num1 * num2)
        elif i == '/':
            stack.append(num1 / num2)

print('{:.2f}'.format(stack.pop()))