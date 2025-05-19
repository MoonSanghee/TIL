for _ in range(3):
    start, end = input().split()
    start = list(map(int, start.split(':')))
    end = list(map(int, end.split(":")))
    result = 0
    # 시작 시간과 끝나는 시간을 받고 3의 개수를 확인하여 담을 변수를 설정해줍니다
    while True:
        if (start[0] * 10000 + start[1] * 100 + start[2]) % 3 == 0:
            result += 1
        # 시작 시간을 시계정수로 바꾸어 3의 배수라면 카운팅해줍니다
        if start == end:
            break
        # 진행 시간이 끝나는 시간에 도착하면 반복을 멈추어줍니다
        start[2] += 1
        # 끝나는 시간에 도달하지 못하였다면 초를 1만큼 지나가게 해줍니다
        if start[2] == 60:
            start[2] = 0
            start[1] += 1
            # 60초가 되었다면 00초로 바꾸고 분을 1만큼 지나게 합니다
            if start[1] == 60:
                start[1] = 0
                start[0] += 1
                # 분도 60분이 되었다면 00분으로 바꾸고 시간이 1만큼 지나게 해줍니다
                if start[0] == 24:
                    start[0] = 0
                    # 시간이 24시를 지나면 00시로 바꾸어줍니다
    print(result)
    # 3의 배수 개수를 출력해줍니다