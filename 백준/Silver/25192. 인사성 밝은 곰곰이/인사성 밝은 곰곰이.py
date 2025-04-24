# 25192번
n = int(input())

chat = [input() for _ in range(n)]
count = 0
gom = []

for line in chat:
  if line == 'ENTER':
    count += len(set(gom))
    gom = []
  else:
    gom.append(line) 

print(count + len(set(gom)))