def solution(s):
    words = s.split(' ')
    result = []

    for word in words:
        if word:  # 빈 문자열(공백) 아니면
            result.append(word[0].upper() + word[1:].lower())
        else:
            result.append('')  # 공백 그대로 유지

    return ' '.join(result)
