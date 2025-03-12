import sys
n=int(sys.stdin.readline())
x=[]
for i in range(n):
    a,b=map(str,sys.stdin.readline().split())
    x.append([int(a),b])
x.sort(key=lambda x:x[0])
for i in x:
    print(*i)