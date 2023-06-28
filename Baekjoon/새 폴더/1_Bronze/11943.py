basket1 = list(map(int, input().split()))
basket2 = list(map(int, input().split()))
# 두 바구니를 받아줍니다.
print(min(basket1[0] + basket2[1], basket2[0] + basket1[1]))
# 1번 바구니에 사과를 2번 바구니에 오렌지를 모으는 경우와
# 1번에 오렌지 2번에 사과를 모으는 경우에 과일 이동 횟수를 비교하여 적은 경우를 출력해줍니다.