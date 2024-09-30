n = int(input())
price = int(input())
# 도장의 개수와 상품의 가격을 받아줍니다.
result = price
# 할인을 적용한 가격을 담을 변수를 설정해줍니다.
if n >= 5:
    result = min(result, price - 500)

if n >= 10:
    result = min(result, price * 0.9)

if n >= 15:
    result = min(result, price - 2000)

if n >= 20:
    result = min(result, price * 0.75)
# 혜택 적용이 가능한지 확인하고 최소가격을 갱신해줍니다.
if result < 0:
    result = 0

print(int(result))
# 최소 가격을 출력해줍니다.