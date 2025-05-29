board = input()

parts = list(board.split('.'))

for i in range(len(parts)):
    if len(parts[i]) % 2 != 0:
        print(-1)
        exit()
    
    a = len(parts[i]) // 4
    b = (len(parts[i]) % 4) // 2
    parts[i] = 'AAAA' * a + 'BB' * b

print('.'.join(parts))