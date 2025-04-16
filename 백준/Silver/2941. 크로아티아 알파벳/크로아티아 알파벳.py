x = input()
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c:
  x = x.replace(i, '*')

print(len(x))