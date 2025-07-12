a= input().upper()
x= list(set(a))

p=[]
for i in x:
    count=a.count(i)
    p.append(count)

if p.count(max(p))>1:
    print("?")
else:
    max_index=p.index(max(p))
    print(x[max_index])