n, k = map(int, input().split())
desk = list(input())

count = 0

for i in range(n):
    if desk[i] == 'P':
        for j in range(i-k,i+k+1):
            if 0<=j<n and desk[j] == 'H':
                desk[j] = 'X'
                count += 1
                break

print(count)