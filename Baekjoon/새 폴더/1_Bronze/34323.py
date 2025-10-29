n, m, s = map(int, input().split())
# 주어지는 변수를 받아줍니다
a = int((((m + 1) * s) * (100 - n)) // 100)
b = m * s
# 각각의 할인을 적용한 가격을 구해줍니다
print(min(a, b))
# 저렴한 가격을 출력해줍니다