switch_len = int(input())
switch = list(map(int, input().split()))

n = int(input())

def change(i):
    switch[i] = 1 - switch[i]

for _ in range(n):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(switch_len):
            if (i+1) % num == 0:
                change(i)
    
    else:
        num -= 1  
        change(num)

        i = 1

        while (num - i) >=0 and (num + i) < switch_len:
            if switch[num - i] != switch[num + i]:
                break
            change(num - i)
            change(num + i)
            i += 1
            


for i in range(switch_len):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0:
        print()