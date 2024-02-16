while True:
    word = input()
    if word == 'end':
        break
    # 'end'가 입력될때까지 작동합니다.
    acceptable = True
    # acceptable을 True로 설정해둡니다.
    past = ''
    gather = 'aeiou'
    # 연속한지 확인할 앞의 낱말을 담을 변수와 모음을 담은 변수를 설정해줍니다.

    for i in word:
        if len(past):
            if i == past[-1]:
                if i != 'e' and i != 'o':
                    acceptable = False
                    break
                elif past == 'ee' or past == 'oo':
                    acceptable = False
                    break
                # 연속한 글자가 나왔을때 e혹은 o인지 확인해주고 e나 o여도 3번 연속하는지 확인해줍니다.
            elif i in gather:
                if len(past) == 2:
                    if past[0] in gather and past[1] in gather:
                        acceptable = False
                        break
            elif i not in gather:
                if len(past) == 2:
                    if past[0] not in gather and past[1] not in gather:
                        acceptable = False
                        break
                    # 모음 혹은 자음이 3개 연속으로 오는지 확인해줍니다.
            past += i
            if len(past) > 2:
                past = past[1:]
                # 최근 2개의 글자인지 확인하고 갱신해줍니다.
        else:
            past = i
            # 지난 글자가 없을경우 지난 글자를 1개 추가하고 다음 글자들을 확인합니다.
    
    for i in gather:
        if i in word:
            break
    else:
        acceptable = False
    # 모음이 있는지 확인하고 없다면 acceptable을 False로 만들어줍니다.
    
    if acceptable:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
        # acceptable 상태에 따라 입력받은 단어가 유효한지 출력해줍니다.