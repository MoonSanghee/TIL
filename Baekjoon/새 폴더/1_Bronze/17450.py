result = 0
cost = 0
snack = 'SNU'
# 어떤 과자를 살지와 가성비를 담을 변수를 설정해줍니다
for i in range(3):
    price, weight = map(int, input().split())
    price *= 10
    weight *= 10
    # 무게와 가격을 받아 10을 곱해줍니다
    if price >= 5000:
        price -= 500
    # 쿠폰을 사용할 수 있다면 적용하여줍니다
    if weight / price > cost:
        cost = weight / price
        result = i
    # 가성비가 더 좋은 과자라면 값을 갱신해줍니다
print(snack[result])
# 결과를 출력해줍니다