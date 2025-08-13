import sys
input = sys.stdin.readline

n, b = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]
items.sort(key=lambda x: x[0] + x[1])
# 선물의 개수와 예산을 받고 각 선물의 가격과 배송비의 합을 기준으로 오름차순 정렬을 해줍니다

maximum = 0
# 결과를 담을 변수를 설정해줍니다
for i in range(n):
    budget = b
    coupon_price = items[i][0] // 2 + items[i][1]
    # 예산을 복사하고 쿠폰을 사용하여 선물을 살 때 가격을 구해줍니다
    if budget >= coupon_price:
        budget -= coupon_price
        count = 1
        # 현재 선물을 살 수 있다면 예산에서 쿠폰 적용 구매가격을 빼고 구매 수량을 변수에 담아줍니다
        for j in range(n):
            if i == j:
                continue
            # i와 j가 같다면 이미 구매하였으므로 넘어갑니다
            price = items[j][0] + items[j][1]
            if budget >= price:
                budget -= price
                count += 1
            else:
                break
            # 물건의 가격을 차례로 확인하며 예산을 초과하지 않는다면 선물을 사고 초과한다면 반복을 멈추어줍니다
        maximum = max(maximum, count)
        # 선물을 사는 최대 수량과 비교하여 갱신해줍니다
    
print(maximum)
# 결과를 출력해줍니다