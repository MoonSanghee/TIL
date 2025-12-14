while True:
    s = input()
    if s == '#':
        break
    # 주어지는 입력이 마지막인지 확인해줍니다
    word = s[0]
    result = 0
    # 첫 문자와 문장에 나타난 개수를 담을 변수를 설정해줍니다
    for i in s[1:].lower():
        if i == word:
            result += 1
    # 찾는 문자의 수를 세어줍니다
    print(word, result)
    # 결과를 출력해줍니다