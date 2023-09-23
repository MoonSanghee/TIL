while True:
    number = input()
    # 수를 문자열로 받아줍니다.
    if number == '0':
        break
    # 받은 수가 0일때 멈추어줍니다.
    cnt = len(number) + 1
    # 각 숫자간 간격이 1이고 맨 앞과 뒤에도 1만큼 간격이 있으니 
    # number의 길이에 1을 더한값을 기본으로 설정해줍니다.
    for num in number:
        if num == '1':
            cnt += 2
        elif num == '0':
            cnt += 4
        else:
            cnt += 3
    # 숫자가 차지하는 너비만큼 더해줍니다.
    print(cnt)
    # 전체 너비를 출력해줍니다.