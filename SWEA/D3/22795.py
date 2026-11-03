T = int(input())
# 테스트케이스의 수를 받아줍니다
for _ in range(T):
    info = list(map(int, input().split()))
    # 가지고있는 부하들의 키를 받아줍니다
    x = max(info) + 1
    # 사라진 부하가 가장 키가 크므로 남은 부하중 가장 큰 부하 + 1 값으로 설정해줍니다
    while True:
        if (x + sum(info)) % 7 == 0:
            break
        else:
            x += 1
    # 평균값이 나누어 떨어질때까지 1씩 더해줍니다
    print(x)
    # 결과를 출력해줍니다