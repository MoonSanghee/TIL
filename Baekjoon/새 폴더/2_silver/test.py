n = int(input())

m = int(input())

words = input()
p = 'IO' * n + 'I'
cnt = 0

for i in range(m - len(p)):
    if words[i:i + len(p)] == p:
        cnt += 1

print(cnt)