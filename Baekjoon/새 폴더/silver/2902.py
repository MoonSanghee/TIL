sentence = input()
word = sentence[0]

for i in range(len(sentence)):
    if sentence[i] == '-':
        word += sentence[i + 1]

print(word)