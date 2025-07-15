n, k = map(int, input().split())
countries = []

for _ in range(n):
    country = list(map(int, input().split()))
    countries.append(country)

# 금, 은, 동 기준 내림차순 정렬
countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1  # 현재 등수
same = 1  # 공동 등수 카운터
prev = countries[0][1:]  # 이전 메달

# 국가 번호: 등수 저장
ranks = {countries[0][0]: 1}

for i in range(1, n):
    curr = countries[i][1:]
    
    if curr == prev:
        # 공동 등수
        ranks[countries[i][0]] = rank
        same += 1
    else:
        # 새로운 등수
        rank = i + 1
        ranks[countries[i][0]] = rank
        prev = curr
        same = 1

print(ranks[k])
