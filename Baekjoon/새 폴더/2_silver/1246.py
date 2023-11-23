n, m = map(int, input().split())
# 달걀의 개수와 구매하려는 사람의 수를 받아줍니다.
wants = [int(input()) for _ in range(m)]
wants.sort()
# 구매하려는 사람들의 희망금액을 받아줍니다.

income = 0
price = 0
# 전체 판매수익과 판매금액을 담을 변수를 설정해줍니다.

for i in range(m):
    egg = min(m - i, n)
    # 사려는 사람이 달걀의 수보다 많을수 있으므로 판매할 수 있는 달걀을 확인해줍니다.
    if wants[i] * egg >= income:
        income = wants[i] * egg
        price = wants[i]
        # 수익을 갱신할 수 있다면 판매금액과 수익을 갱신해줍니다.

print(price, income)
# 판매금액과 수익을 출력해줍니다.