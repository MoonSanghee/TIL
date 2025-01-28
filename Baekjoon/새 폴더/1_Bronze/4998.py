while True:
    try:
        numbers = list(map(float, input().split()))
        cnt = 0
        # 주어지는 세 수를 받고 몇 년이 필요한지 담을 변수를 설정해줍니다
        while numbers[0] < numbers[2]:
            numbers[0] += numbers[0] * numbers[1] / 100
            cnt += 1
        # 이자를 더하고 1년을 갱신해 원하는 값을 넘을때까지 반복해줍니다
        print(cnt)
        # 몇해가 필요한지 출력해줍니다
    except:
        break