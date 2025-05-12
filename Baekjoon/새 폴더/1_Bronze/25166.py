S, M = map(int, input().split())
# 샌드위치 가격과 쿠기가 가진 돈의 총액을 받아줍니다
if S < 1024:
    print("No thanks")
    # 쿠기에게 돈을 빌릴 필요가 없다면 주어진 값을 출력해줍니다
else:
    S -= 1023
    coins = []
    cnt = 0
    # 아리가 가진 돈만으로 부족하다면
    while M:
        coins.append((M % 2, 2 ** cnt))
        M //= 2
        cnt += 1
    # 쿠기가 가진 동전들을 확인해줍니다
    while coins:
        x, price = coins.pop()
        if x == 1:
            if S >= price:
                S -= price
    # 비싼 코인부터 확인하며 코인을 빌릴때 잔돈이 필요 없는지 확인해줍니다
    if S == 0:
        print("Thanks")
    else:
        print("Impossible")
    # 필요한 금액을 만들수 있는지 확인하여 결과를 출력해줍니다