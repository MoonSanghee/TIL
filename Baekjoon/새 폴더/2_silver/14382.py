t = int(input())
# 테스트 케이스의 수를 받아줍니다.
for tc in range(t):
    n = int(input())
    used = set()
    now = n
    # 최초 주어지는 수를 받고 사용된 수를 담을 세트와 현재 사용중인 수를 담을 변수를 설정해줍니다.
    if n == 0:
        print(f'Case #{str(tc + 1)}: INSOMNIA')
    # 주어지는 수가 0이라면 잠에 들 수 없습니다.
    else:
        while True:
            numbers = str(now)
            for i in numbers:
                used.add(i)
            if len(used) == 10:
                print(f'Case #{str(tc + 1)}: {str(now)}')
                break
            else:
                now += n
        # 아니라면 수를 갱신하면서 모든 수가 나오는 경우를 찾아줍니다.