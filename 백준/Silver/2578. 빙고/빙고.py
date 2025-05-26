import sys

def input():
    return sys.stdin.readline()

a = [list(input().split()) for _ in range(5)]
b = []

for i in range(5):
    b += list(input().split())

def check(board):
    check_num = 0
    
    for i in a:
        if i.count(0) == 5:
            check_num += 1
    
    for i in range(5):
        num = 0
        for j in range(5):
            if board[j][i] == 0:
                num +=1
            if num ==5:
                check_num += 1
    
    num =0
    for i in range(5):
        if board[i][i] ==0:
            num +=1
    if num == 5:
        check_num += 1
    
    num =0
    for i in range(5):
        if board[i][4-i] ==0:
            num +=1
    if num == 5:
        check_num += 1
    
    return check_num

count = 0

for k in b:
    for i in range(5):
        for j in range(5):
            if k == a[i][j]:
                a[i][j] = 0
                count += 1
    
    if check(a) >=3:
        print(count)
        break
