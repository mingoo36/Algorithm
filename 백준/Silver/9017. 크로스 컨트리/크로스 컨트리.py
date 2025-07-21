from collections import Counter, defaultdict
n = int(input())

for _ in range(n):
    p = int(input())

    rank = list(map(int, input().split()))

    team_count = Counter(rank)
    
    rank = [i for i in rank if team_count[i] >= 6]

    team_count = defaultdict(list)

    score = 1
    for i in rank:
        team_count[i].append(score)
        score += 1

    min_sum = min(sum(v[:4]) for v in team_count.values())

    min_teams = [k for k,v in team_count.items() if sum(v[:4]) == min_sum]
    
    if len(min_teams) == 1:
        print(min_teams[0])
    else:
        result = min(min_teams, key=lambda x: team_count[x][4])
        print(result)