i, j = map(int, input().split())
# 두 수를 받아줍니다

a = 100 - i
b = 100 - j
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100
# 필요한 계산을 실행해줍니다.
print(a, b, c, d, q, r)
print(c + q, r)
# 요청한 값을 차례대로 출력해줍니다.