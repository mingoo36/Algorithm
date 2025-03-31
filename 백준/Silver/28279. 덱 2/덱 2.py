import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
mydeq = deque([])

for _ in range (n):
  cmd = list(map(int,input().split()))
  key = cmd[0]

  if key == 1:
    mydeq.appendleft(cmd[1])
  
  elif key ==2:
    mydeq.append(cmd[1])
  
  elif key ==3:
    if mydeq:
      print(mydeq[0])
      mydeq.popleft()
    else:
      print(-1)
  
  elif key ==4:
    if mydeq:
      print(mydeq[-1])
      mydeq.pop()
    else:
      print(-1)
  
  elif key ==5:
    print(len(mydeq))
  
  elif key ==6:
    if mydeq:
      print(0)
    else:
      print(1)
  
  elif key ==7:
    if mydeq:
      print(mydeq[0])
    else:
      print(-1)
    
  elif key ==8:
    if mydeq:
      print(mydeq[-1])
    else:
      print(-1)