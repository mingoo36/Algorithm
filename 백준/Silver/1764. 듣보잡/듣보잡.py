n,m = map(int, input().split())

x = {input() for _ in range(n)}
y = {input() for _ in range(m)}
z = sorted(x&y)

print(len(z))
print(*z, sep='\n')