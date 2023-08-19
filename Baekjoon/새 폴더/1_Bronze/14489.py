a, b = map(int, input().split())
# 두 통장의 잔고를 받아줍니다.
c = int(input())
# 치킨 한 마리 값을 받아줍니다.
if (a + b) >= c * 2:
    print(a + b - c * 2)
    # 통장의 잔고가 치킨 두 마리를 살 수 있으면 치킨 두마리를 산 차액을
else:
    print(a + b)
    # 아니면 통장 잔액의 합을 출력해줍니다.