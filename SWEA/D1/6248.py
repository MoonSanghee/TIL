word = input()
result = ''

for i in range(0, len(word), 2):
    result += word[i]

print(result)