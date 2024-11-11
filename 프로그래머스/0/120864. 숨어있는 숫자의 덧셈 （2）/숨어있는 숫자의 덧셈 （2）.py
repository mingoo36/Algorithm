def solution(my_string):
    answer = ''
    result = 0 
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            answer += my_string[i]
        else:
            if answer:
                result += int(answer)
                answer = ''
    if answer:
        result += int(answer)
    return result