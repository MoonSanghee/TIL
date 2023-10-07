n = int(input())
words = []
for _ in range(n):
    words.append(input())

for word in words:
    if word[::-1] in words:
        length = len(word)
        mid = length//2
        print(length, word[mid])
        break