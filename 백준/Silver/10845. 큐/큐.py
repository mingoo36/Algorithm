import sys
a=int(sys.stdin.readline())
x=[]
for i in range(a):
    p= sys.stdin.readline().split()
    
    if p[0]=='push':
        x.append(p[1])
    elif p[0]=='pop':
        if len(x)==0:
            print(-1)
        else:
            print(x.pop(0))
    elif p[0]=='size':
        print(len(x))
    elif p[0]=='empty':
        if len(x)==0:
            print(1)
        else:
            print(0)
    elif p[0]=='front':
        if len(x)==0:
            print(-1)
        else:
            print(x[0])
    elif p[0]=='back':
        if len(x)==0:
            print(-1)
        else:
            print(x[-1])