n = int(input())


for _ in range(n):
  stack = []
  x = input()
  valid = True
  
  for i in x:
    if i == '(':
      stack.append(i)
    else:
      if stack:
        stack.pop()
      else:
        valid = False
        break
        
  if valid and not stack:
    print("YES")
  else:
    print("NO")