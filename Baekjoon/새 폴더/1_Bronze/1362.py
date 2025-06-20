cnt = 0
# 시나리오 번호를 담을 변수를 설정해줍니다
while True:
    cnt += 1
    o, w = map(int, input().split())
    # 시나리오 번호를 1 더해주고 주어지는 표준 체중과 현재 체중을 받아줍니다
    if o == w == 0:
        break
    # 시나리오를 끝내는 입력이 들어오면 반복을 멈추어줍니다
    while True:
        command, number = input().split()
        if command == '#' and number == '0':
            break
        # 주어지는 입력이 그만을 뜻할때까지 받아줍니다
        number = int(number)
        if w > 0:
            if command == 'E':
                w -= number
            else:
                w += number
            # 펫이 살아있다면 운동을 시키거나 먹이를 주는 입력에 따라 무게를 변화시켜줍니다
    if w <= 0:
        print(f'{cnt} RIP')
    elif o * 0.5 < w < o * 2:
        print(f'{cnt} :-)')
    else:
        print(f'{cnt} :-(')
        # 시나리오 번호와 함께 펫의 상태를 출력해줍니다