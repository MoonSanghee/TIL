cnt = 1
while True:
    cnt += 1
    # 간격을 갱신해줍니다
    sentence = input()
    # 주어지는 입력을 받아줍니다
    if cnt != 2:
        print()
        # 첫 문장이 아니라면 줄바꿈을 실행해줍니다
    if sentence == 'Was it a cat I saw?':
        break
    # 마지막 입력인지 확인해줍니다
    else:
        for i in range(0, len(sentence), cnt):
            print(sentence[i], end = '')
    # 암호를 확인해 출력해줍니다