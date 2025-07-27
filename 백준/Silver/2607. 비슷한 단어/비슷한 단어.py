from collections import Counter

n = int(input())
target = input()
words = [input() for _ in range(n-1)]

target_count = Counter(target)
result = 0

for word in words:
    word_count = Counter(word)

    diff = (target_count - word_count) + (word_count - target_count)
    diff_sum = sum(diff.values())

    if diff_sum == 0:
        result += 1
    elif diff_sum == 1 and abs(len(target)-len(word)) == 1:
        result += 1
    elif diff_sum == 2 and len(target) == len(word):
        result += 1

print(result)