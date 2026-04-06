while True:
    n = int(input())
    # 주어지는 기록의 수를 받아줍니다
    if n == -1:
        break
    # 마지막 입력인지 확인해줍니다
    else:
        numbers = [list(map(int, input().split())) for _ in range(n)]
    result = numbers[0][0] * numbers[0][1]
    # 첫 구간의 이동 거리를 결과에 담아줍니다
    for i in range(1, n):
        result += (numbers[i][1] - numbers[i - 1][1]) * numbers[i][0]
    # 이어지는 구간들의 거리를 더해줍니다
    print(f'{result} miles')
    # 결과를 출력해줍니다