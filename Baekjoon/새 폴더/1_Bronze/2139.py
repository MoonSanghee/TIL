while True:
    d, m, y = map(int, input().split())
    result = 0
    # 주어지는 날짜정보를 받고 몇번째 날인지 담을 변수를 설정해줍니다
    if d == m == y and d == 0:
        break
    # 마지막입력인지 확인해줍니다
    yoon = False
    if y % 400 == 0:
        yoon = True
    elif y % 100 != 0 and y % 4 == 0:
        yoon = True
    # 윤년인지 확인해줍니다
    cnt = 1
    while cnt < m:
        if cnt in [1, 3, 5, 7, 8, 10, 12]:
            result += 31
        elif cnt == 2:
            result += 28
            if yoon:
                result += 1
        else:
            result += 30
        cnt += 1
    # 각 달별로 지난 일수를 더해줍니다
    result += d
    print(result)
    # 남은 날을 더해 결과를 출력해줍니다