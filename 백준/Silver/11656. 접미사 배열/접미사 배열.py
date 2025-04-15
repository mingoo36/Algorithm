x = input()
p = []
for i in range(len(x)):
  p.append(x[i:])


print(*sorted(p), sep='\n')