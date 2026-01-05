while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    # 두 수를 받고 마지막 입력인지 확인해줍니다
    result = 0
    check = 0
    # 받아올림이 발생했는지와 총 발생한 횟수를 담을 변수를 설정해줍니다
    while a > 0 or b > 0:
        if a % 10 + b % 10 + check>= 10:
            result += 1
            check = 1
        else:
            check = 0
        a //= 10
        b //= 10
    # 양수가 존재한다면 마지막 자리 수를 더하며 받아올림이 발생하는지 확인해줍니다
    print(result)
    # 결과를 출력해줍니다