n, game = input().split()

people = set()

for _ in range(int(n)):
    people.add(input())

if game == 'Y':
    print(len(people))
elif game == 'F':
    print(len(people) // 2)
elif game == 'O':
    print(len(people) // 3)