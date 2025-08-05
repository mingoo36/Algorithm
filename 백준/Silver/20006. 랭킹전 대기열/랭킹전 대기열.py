import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    l, n = input().split()
    l = int(l)

    matched= False
    for room in rooms:
        base_lavel, members = room
        if abs(base_lavel - l) <= 10 and len(members) < m:
            members.append((l,n))
            matched = True
            break
    
    if not matched:
        rooms.append((l,[(l,n)]))


for _, members in rooms:
    if len(members) == m:
        print("Started!")
    else:
        print("Waiting!")

    for l,n in sorted(members, key =lambda x: x[1]):
        print(l, n)