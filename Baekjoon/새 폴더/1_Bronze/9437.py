while True:
    numbers = list(map(int, input().split()))
    # 주어지는 시험지의 정보를 받아줍니다
    if numbers[0] == 0:
        break
    # 주어진 입력이 0이라면 작동을 멈추어줍니다
    else:
        n, p = numbers[0], numbers[1]
        result = []
        # 결과를 담을 변수를 설정해줍니다
        if p % 2:
            result.append(p + 1)
            result.append(n - p + 1)
            result.append(n - p)
        else:
            result.append(p - 1)
            result.append(n - p + 1)
            result.append(n - p + 2)
        # 사라진 페이지가 홀수인지 짝수인지에 따라 나머지 페이지를 리스트에 담아줍니다
        result.sort()
        print(*result)
        # 리스트를 오름차순으로 정렬하여 값을 출력해줍니다