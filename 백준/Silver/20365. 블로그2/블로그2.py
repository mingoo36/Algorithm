n = int(input())

text = input()

color = {
    'B':0,
    'R':0
}

color[text[0]] += 1 

for i in range(1, n):
    if text[i] != text[i-1]:
        color[text[i]] += 1 

print(min(color['B'],color['R'])+1)