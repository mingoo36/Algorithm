import sys

stack = []

n = int(sys.stdin.readline().strip())  

for _ in range(n):
    x = sys.stdin.readline().strip().split()

    cmd = x[0]
    if cmd == "1" :
      stack.append(x[1])

    elif cmd== "2" :
      if len(stack)==0:
        print(-1)
      else:
        print(stack.pop())

    elif cmd == "3":
      print(len(stack))

    elif cmd == "4":
      if len(stack)==0:
        print(1)
      else:
        print(0)

    elif cmd == "5":
      if len(stack)==0:
        print(-1)
      else:
        print(stack[-1])