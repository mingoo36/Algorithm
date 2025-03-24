n, m = map(int, input().split())

x = [input() for _ in range(n)]
x_dic = {value:idx+1 for idx, value in enumerate(x)}

y = [input() for _ in range(m)]

for i in y:
  if i.isdigit():
    print(x[int(i)-1])
  else:
    print(x_dic[i])