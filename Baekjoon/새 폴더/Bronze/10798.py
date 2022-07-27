all_input = []
word_cnt = []
total = ''

for i in range(5):
    word = input()
    all_input.append(word)
    word_cnt.append(len(word))

for i in range(5):
    if word_cnt[i] != max(word_cnt):
        all_input[i] += '*' * (max(word_cnt) - word_cnt[i]) 

for i in range(max(word_cnt)):
    for j in range(5):
        if all_input[j][i] == '*':
            total += ''
        else:
            total += all_input[j][i]

print(total)