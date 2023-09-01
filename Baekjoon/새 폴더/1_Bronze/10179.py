n = int(input())
# 물건의 수를 받아줍니다.
for _ in range(n):
    price = float(input())
    # 소수점 2자리까지 가지는 수를 받아줍니다.
    print("$%.2f" % round(price*0.8, 2))
    # 20%센트 할인된 가격을 적용하여 출력해줍니다.