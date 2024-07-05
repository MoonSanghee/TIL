a, b, c = map(int, input().split())
x, y, z = map(int, input().split())
# 곰곰이들이 먹고싶어하는 메뉴와 쿠폰의 수를 받아줍니다.
result = 0
# 먹고싶은 음식을 먹은 곰곰이의 수를 담을 변수를 설정합니다.
for _ in range(3):
    # 쿠폰을 3번 교환하면 원래 가지고있던 쿠폰이 되므로 3번까지만 반복합니다
    chicken = min(a, x)
    result += chicken
    a -= chicken
    x -= chicken

    pizza = min(b, y)
    result += pizza
    b -= pizza
    y -= pizza

    burger = min(c, z)
    result += burger
    c -= burger
    z -= burger
    # 사용 가능한 티켓의 수만큼 사용하여 각 음식을 먹은것을 확인해줍니다.
    x, y, z = z // 3, x // 3, y // 3
    # 쿠폰을 교환하여줍니다.

print(result)
# 결과를 출력해줍니다.