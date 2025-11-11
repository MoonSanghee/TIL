while True:
    words = []
    while True:
        word = input()
        if word == '#':
            break
        words.append(word)
    # 테스트 케이스의 주어지는 단어들을 받아줍니다
    if len(words) == 0:
        break
    # 입력이 끝나는지 확인해줍니다
    for i in range(len(words) - 1):
        cnt = 0
        for j in range(len(words[i])):
            if words[i][j] != words[i + 1][j]:
                cnt += 1
        if cnt != 1 or len(words[i]) != len(words[i + 1]):
            print('Incorrect')
            break
        # 연속한 단어의 길이가 다르거나 다른 글자가 하나가 아니라면 단어 사다리가 불가능합니다
    else:
        print('Correct')
        # 아니라면 단어 사다리가 가능합니다