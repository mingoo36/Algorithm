import sys
input = sys.stdin.readline

n = int(input())
balls = input().strip()

def count_balls(color, to_left):
    total = balls.count(color)

    if to_left:
        cnt = 0
        for i in balls:
            if i == color:
                cnt += 1
            else:
                break
        return total - cnt
    
    else:
        cnt = 0
        for i in reversed(balls):
            if i == color:
                cnt += 1
            else:
                break
        return total - cnt
    
result = min(
    count_balls('R', True),
    count_balls('R', False),
    count_balls('B', True),
    count_balls('R', False)
)

print(result)