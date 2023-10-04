while True:
    n = int(input())
    # 수를 받아줍니다.
    if n:
        # 0아니라면
        while(n > 9):
            n = sum(map(int, list(str(n))))
        print(n)
        # 1자리수가 될때까지 모든 자릿수를 더해줍니다.
    else:
        break
    # 입력값이 0이라면 확인을 멈추어줍니다.