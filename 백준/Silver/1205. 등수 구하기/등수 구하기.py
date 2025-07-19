n, score, p = map(int, input().split())

if n == 0:
    print(1)
    exit()

songs = list(map(int, input().split()))

if n == p and score <= songs[-1]:
    print(-1)
else:
    rank = 1
    for s in songs:
        if s > score:
            rank += 1
    print(rank)