n = int(input())
words = [input() for _ in range(n)]
words.sort()
cnt = 0
for i in range(n - 1):
    if len(words[i]) <= len(words[i + 1]):
        if words[i] == words[i + 1][:len(words[i])]:
            cnt += 1
print(n - cnt)