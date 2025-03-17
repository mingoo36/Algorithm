n = int(input())

for _ in range(n):
    x = input()
    score = 0
    bonus = 0
    for i in x:
        if i == 'O':
            bonus += 1
        else:
            bonus = 0
        score += bonus
    print(score)