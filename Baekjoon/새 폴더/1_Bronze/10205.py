k = int(input())
# 테스트 케이스의 수를 받아줍니다
for i in range(k):
    h = int(input())
    # 최초 머리의 수를 받아줍니다
    print(f'Data Set {i + 1}:')
    # 테스트 케이스의 번호를 출력해줍니다
    actions = input()
    # 행동을 받아줍니다
    for i in actions:
        if i == 'c':
            h += 1
        else:
            h -= 1
            if h == 0:
                break
    # 행동을 실행한 후 머리의 수를 갱신해줍니다
    print(h)
    print()
    # 남은 머리의 수를 출력해줍니다