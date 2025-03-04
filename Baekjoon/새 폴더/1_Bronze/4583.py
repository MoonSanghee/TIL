while True:
    word = input()
    if word == '#':break
    # 입력을 확인해 마지막 줄이라면 실행을 멈추어줍니다
    result = ''
    word = word[::-1]
    for i in word:
        if i == 'b':result += 'd'
        elif i == 'd':result += 'b'
        elif i == 'p':result += 'q'
        elif i == 'q':result += 'p'
        elif i in 'iovwx':result += i
        else:
            print('INVALID')
            break
    # 주어진 단어를 뒤집어 원래 단어의 마지막 문자부터 확인하여 거울상 관계가 아니라면 멈추어줍니다
    else:
        print(result)
    # 멈추지 않았다면 거울상의 모습을 출력해줍니다