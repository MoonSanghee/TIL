t = int(input())
# 테스트 데이터의 수를 받아줍니다
for _ in range(t):
    n = int(input())
    # 거래일을 받아줍니다
    result = 0
    # 결과를 담을 변수를 설정해줍니다
    for _ in range(n):
        values = list(map(int, input().split()))
        high = max(values)
        if high > 0:
            result += high
    # 이득을 볼 수 있는 날만 거래를 진행하여줍니다
    print(result)
    # 결과를 출력해줍니다