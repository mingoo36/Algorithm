import sys
input = sys.stdin.readline

n, game = input().split()

people = {input() for _ in range(int(n))}

if game == 'Y':
    print(len(people))
elif game == 'F':
    print(len(people) // 2)
elif game == 'O':
    print(len(people) // 3)