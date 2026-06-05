T = int(input())
# 테스트 케이스의 수를 받아줍니다
for t in range(T):
    word = input()
    d = dict()
    for i in word:
        d[i] = d.get(i, 0) + 1
    # 단어를 받고 단어를 이루고있는 문자의 수를 딕셔너리에 담아줍니다
    for i in d:
        if d[i] != 2:
            print(f'#{t + 1} No')
            break
    else:
        print(f'#{t + 1} Yes')
    # 각 문자가 2개씩인지 확인하여 주어진 양식에 맞게 결과를 출력해줍니다