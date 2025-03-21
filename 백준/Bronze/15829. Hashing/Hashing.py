a= int(input())
x=input()
p=0

for i in range(a):
    p+= (ord(x[i])-96)*(31**i)
print(p%1234567891)