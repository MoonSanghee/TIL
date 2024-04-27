n = int(input())
price = [350.34, 230.90, 190.55, 125.30, 180.90]
# 입력되는 조합의 수와 부품별 가격을 받아줍니다.
for _ in range(n):
    parts = list(map(int, input().split()))
    result = 0
    # 각 부품이 필요한 갯수를 받고 금액을 담을 변수를 만들어줍니다.
    for i in range(5):
        result += parts[i] * price[i]
    # 부품 가격과 필요한 부품의 수를 곱하여 결과에 더해줍니다.
    print("$%.2f" % (result))
    # 결과값을 소수점 2번째 자리까지 출력하여줍니다.