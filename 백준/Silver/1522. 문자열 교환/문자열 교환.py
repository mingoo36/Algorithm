import sys
input = sys.stdin.readline

s = input().strip() 
a = s.count('a') 

s += s 
min_val = float('inf') 

for i in range(len(s) // 2):
    min_val = min(min_val, s[i:i+a].count('b')) 

print(min_val)