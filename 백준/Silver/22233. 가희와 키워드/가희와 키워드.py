import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words_set = set()

for _ in range(n):
    word = input().strip()

    words_set.add(word)

for _ in range(m):

    x = input().strip().split(',')

    for i in x:
        if i in words_set:
            words_set.remove(i)
    
    print(len(words_set))