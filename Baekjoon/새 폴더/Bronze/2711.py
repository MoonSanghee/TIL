test_case = int(input())
for i in range(test_case):
    num, word = map(str, input().split())
    new_word =''
    for i in range(1, len(word) + 1):
        if i != int(num):
            new_word += word[i - 1]
    print(new_word)