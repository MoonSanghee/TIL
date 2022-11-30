word = str(input())
words = []

for _ in word:
    words.append(word)
    word = word[1:]

for i in sorted(words):
    print(i)