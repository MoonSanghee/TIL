def solution(keymap, targets):
    answer = []
    d = dict()
    # 문자를 찍기위해 가장 적게 눌러야하는 버튼수를 담을 딕셔너리를 만들어줍니다.
    for key in keymap:
        for i in range(len(key)):
            # 각 키를 순환하며
            if key[i] not in d:
                d[key[i]] = i + 1
            elif key[i] in d and d[key[i]] > i + 1:
                d[key[i]] = i + 1
            # 딕셔너리에 들어간 적 없다면 넣어주고
            # 값이 존재한다면 적게 클릭수가 적어지는지 확인하여 값을 갱신해줍니다.
    
    for target in targets:
        cnt = 0
        # 타겟을 순회하며
        for i in target:
            if i in d:
                cnt += d[i]
            else:
                cnt = -1
                break
        # 버튼이 존재한다면 몇 번 클릭되어야하는지 확인하여 cnt에 더해주고
        # 존재하지 않는다면 만들수 없다고바꾸고 확인을 멈추어줍니다.
        answer.append(cnt)
        # answer에 target 단어를 만드는데 눌러야하는데 필요한 버튼의 횟수를 담아줍니다.
    return answer
    # answer를 return해줍니다.