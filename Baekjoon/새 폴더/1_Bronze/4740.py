while True:
    Sentence = input()
    # 주어지는 문장을 받아줍니다
    if Sentence == '***':
        break
    else:
        print(Sentence[::-1])
    # 작동을 멈추는 문장이 아니라면 문장을 뒤집어 출력해줍니다