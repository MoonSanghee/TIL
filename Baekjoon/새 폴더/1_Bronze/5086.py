while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    # 입력된 두 수가 0이라면 멈추어줍니다.
    if a % b == 0:
        print('multiple')
    # a가 b로 나누어 떨어진다면 a는 b의 배수이고  
    elif b % a == 0:
        print('factor')
    # b가 a로 나누어 떨어진다면 b가 a의 배수입니다.
    else:
        print('neither')
    # 나머지 경우 서로의 배수나 약수가 아닙니다.