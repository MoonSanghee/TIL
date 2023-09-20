while True:
    coconuts = int(input())
    # 코코넛의 개수를 받아줍니다.
    if coconuts == -1:
        break
    # -1이라면 연산을 멈추어줍니다.
    for i in range(coconuts, 1, -1):
        n = coconuts
        flag = True
        # 계속 반복하였는지 확인할 변수를 정해줍니다.
        for _ in range(i):
            # 사람수만큼의 날동안
            if (n - 1) % i == 0:
                n = (n - 1) - (n - 1) // i
                # 원숭이에게 코코넛을 하나 주면 딱 맞게 코코넛을 나눌수 있다면
                # 원숭이에게 코코넛을 주고 1명의 몫을 빼줍니다.
            else:
                flag = False
                break
                # 아니라면 반복을 못했다고 표시한 후 멈추어줍니다.
        if flag == True and n % i == 0:
            print(f'{coconuts} coconuts, {i} people and 1 monkey')
            break
            # 반복을 계속했고 사람수에 맞게 나눌수 있다면 몇 명이 나누었는지
            # 양식에 맞게 출력해줍니다.
    else:
        print(f'{coconuts} coconuts, no solution')
        # 못 나눈 경우 양식에 맞게 출력해줍니다.