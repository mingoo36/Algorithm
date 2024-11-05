def solution(keyinput, board):
    col = board[0]
    row = board[1]
    result1 = [0, 0]
    for i in keyinput:
        if i == "left" and result1[0]-1 >= -(col // 2):
            result1[0] -= 1
        elif i == "right" and result1[0]+1 <= (col // 2):
            result1[0] += 1
        elif i == "up" and result1[1]+1 <= (row // 2):
            result1[1] += 1
        elif i == "down" and result1[1]-1 >= -(row // 2):
            result1[1] -= 1
    return result1