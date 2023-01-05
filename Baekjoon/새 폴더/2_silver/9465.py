t = int(input())
# 테스트 케이스의 횟수와
for tc in range(t):
    n = int(input())
    # 우표의 길이를 입력받아줍니다.
    maps = [list(map(int, input().split())) for _ in range(2)]
    # 우표의 길이를 입력받아줍니다.
    for i in range(1, n):
        if i == 1:
            maps[0][i] += maps[1][i - 1]
            maps[1][i] += maps[0][i - 1]
            # 1번 인덱스의 경우 1번줄이라면 2번줄 1번 2번줄이라면 1번줄 1번을 더해주는게 최대값이니
            # 그 값을 넣어줍니다.
        else:
            maps[0][i] += max(maps[1][i - 1], maps[1][i - 2])
            maps[1][i] += max(maps[0][i - 1], maps[0][i - 2])
            # 그 외의 경우 다른 줄의 이전 값과 그 이전값중 큰 수를 마지막까지 더해나갑니다.
    print(max(maps[0][-1], maps[1][-1]))
    # 두 줄의 마지막 인덱스에 위치한 값중 큰 값을 출력해줍니다.
