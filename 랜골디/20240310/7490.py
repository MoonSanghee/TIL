t = int(input())
# 입력받을 테스트 케이스의 수를 받아줍니다.
def pick(idx, now):
    if idx == n + 1:
        result.append(now)
        # 마지막 수까지 사용하여 수식을 만들었다면 리스트에 담아줍니다.
    else:
        pick(idx + 1, now + " " + str(idx))
        pick(idx + 1, now + "+" + str(idx))
        pick(idx + 1, now + "-" + str(idx))
        # ASCII 순서로 정렬이 되어야하므로 빈 값, +, -를 차례대로 추가하여 재귀를 시행해줍니다.

for _ in range(t):
    n = int(input())
    result = []
    # 수의 범위를 받고 수식을 담을 리스트를 만들어줍니다.
    pick(2, '1')
    # 수식을 만들어 리스트에 담아줍니다.
    for i in result:
        new = i.replace(' ', '')
        # 수식을 확인하기위해 공백을 뺀 수식을 만들어줍니다.
        if eval(new) == 0:
            print(i)
            # 문자열로된 수식을 eval함수를 이용해 계산하여 0이라면 수식 i를 출력해줍니다
    print()
    # 각 입력 사이의 출력을 줄바꿈해줍니다.