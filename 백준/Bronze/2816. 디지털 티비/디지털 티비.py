n = int(input())

ch = [input() for _ in range(n)]

result = ''

k1_idx = ch.index('KBS1') # 1

result += '1' * k1_idx + '4' * k1_idx

ch.remove('KBS1')
ch.insert(0,'KBS1')

k2_idx = ch.index('KBS2') # 2

result += '1' * k2_idx + '4' * (k2_idx - 1)

ch.remove('KBS2')
ch.insert(1,'KBS2')

print(result)