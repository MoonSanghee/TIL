T = int(input())
# 테스트케이스의 수를 받아줍니다
for _ in range(T):
    n = input()
    d = dict()
    # 주어지는 수를 받아줍니다
    for i in range(10):
        d[i] = []
    # 모든 수의 위치를 담을 딕셔너리를 만들어줍니다
    for i in range(len(n)):
        j = int(n[i])
        d[j].append(i)
    # 각 수의 자리를 담아줍니다
    for i in d:
        # 모든 자릿수를 확인하며
        if len(d[i]) not in (0, 2):
            print('no')
            break
        # 사용하지 않았거나 2개가 아니라면 no를 출력해줍니다
        elif len(d[i]) == 2:
            if d[i][1] - d[i][0] != int(i) + 1:
                print('no')
                break
        # 2개일경우 두 수의 거리를 확인하여 충분한 수가 들어가있는지 확인해줍니다
    else:
        print('yes')
    # 결과를 출력해줍니다