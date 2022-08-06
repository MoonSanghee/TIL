for test in range(1, 11):
    length, word = map(str, input().split())
    word = list(word)
    done = 0
    while done == 0:
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                word = word[:i:] + word[i + 2::]
                break
        else:
            done = 1
    password = ''
    for i in word:
        password += str(i)
    print(f'#{test} {password}')