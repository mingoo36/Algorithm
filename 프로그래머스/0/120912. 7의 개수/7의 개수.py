def solution(array):
    answer = 0
    count=0
    for i in array:
        count += str(i).count('7')
    return count