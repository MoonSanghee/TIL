cnt = 1
# 테스트 케이스 번호를 담을 변수를 설정해줍니다.
while True:
    word1 = input()
    word2 = input()
    if word1 == word2 and word1 == 'END':
        break
    # 'END'가 두 개 들어오면 작동을 멈추어줍니다.

    d = dict()
    for i in word1:
        d[i] = d.get(i, 0) + 1
    # 단어 1이 어떤 문자가 몇개로 이루어졌는지 확인해줍니다.
    for i in d:
        if word2.count(i) != d[i]:
            print(f'Case {cnt}: different')
            break
    else:
        print(f'Case {cnt}: same')
    # 단어 1의 문자들이 담긴 딕셔너리를 순회하며 key 값이 단어2의 문자 개수와 다른 경우가 있는지 확인하고 주어진 양식대로 출력해줍니다.
    cnt += 1
    # 테스트 케이스의 번호를 1 늘려줍니다.