m = ['a', 'e', 'i', 'o', 'u']
while True:
    pwd = input()

    if pwd == 'end':
        break

    has_vowel = False # 모음 여부
    vowel_streak = 0 # 모음 연속
    consonant_streak = 0 # 자음 연속
    acceptable = True # 가능 여부
    prev_char = '' # 이전 문자 
    repeat_count = 1 # 연속 횟수

    for char in pwd:
        if char == prev_char:
            repeat_count += 1
            if char not in ['e', 'o'] and repeat_count > 1:
                acceptable = False
                break
        else:
            repeat_count = 1
        

        if char in m:
            has_vowel = True
            vowel_streak += 1
            consonant_streak = 0
        else:
            consonant_streak += 1
            vowel_streak = 0
        
        if vowel_streak > 2 or consonant_streak > 2:
            acceptable = False
            break

        prev_char = char

    
    if not has_vowel:
        acceptable = False
    
    print("<"+pwd+"> is acceptable." if acceptable else "<"+pwd+"> is not acceptable.")
