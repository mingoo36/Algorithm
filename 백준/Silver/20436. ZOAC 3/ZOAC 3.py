keyboard = [
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l'],
    ['z','x','c','v','b','n','m']
]

left_keys = set('qwertasdfgzxcv')
right_keys = set('yuiophjklbnm')

l, r = input().split()
word = input()

def find_pos(char):
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            if keyboard[i][j] == char:
                return [i, j]

l_pos = find_pos(l)
r_pos = find_pos(r)
count = 0

for ch in word:
    pos = find_pos(ch)
    if ch in left_keys:
        count += abs(l_pos[0] - pos[0]) + abs(l_pos[1] - pos[1]) + 1
        l_pos = pos
    else:
        count += abs(r_pos[0] - pos[0]) + abs(r_pos[1] - pos[1]) + 1
        r_pos = pos

print(count)
