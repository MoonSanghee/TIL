T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    result = []
    # 주어지는 문장의 수와 결과를 담을 리스트를 만들어줍니다
    cnt = 0
    name = 0
    # 문장의 수와 문장별 이름의 수를 확인할 변수를 설정해줍니다
    while True:
        if cnt == n:
            break
        # 문장이 모두 나왔다면 반복을 멈추어줍니다
        sentence = list(input().split())

        for word in sentence:
            if word[-1] in '.!?':
                cnt += 1
                if word[0].isupper():
                    for i in range(1, len(word) - 1):
                        if word[i].islower() == False:
                            break
                    else:
                        name += 1
                result.append(name)
                name = 0
            # 문장이 끝났다면 마지막 단어가 이름인지 확인하고 그 문장에 나온 이름의 수를 리스트에 넣은후 이름의 수를 갱신해줍니다
            else:
                if word[0].isupper():
                    for i in range(1, len(word)):
                        if word[i].islower() == False:
                            break
                    else:
                        name += 1
            # 문장이 계속되고있다면 주어진 단어가 이름인지 확인하고 갱신해줍니다
    
    print(f'#{tc}', end = ' ')
    for i in result:
        print(i, end = ' ')
    print()
    # 각 테스트케이스의 결과를 출력해줍니다