import sys
input = sys.stdin.readline

n, m = map(int, input().split())



name_list = [None] * (n+1)
name_dict = {}

for i in range(1,n+1):
    pok  = input().rstrip()
    name_list[i] = pok
    name_dict[pok] = i


for _ in range(m):
    x = input().rstrip()

    if x.isdigit():
        print(name_list[int(x)])
    else:
        print(name_dict[x])
