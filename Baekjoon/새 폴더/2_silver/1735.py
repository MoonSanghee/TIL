import math
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
# 두 분수를 받아줍니다.
c = math.gcd(a1 * b2 + a2 * b1, b1 * b2)
# 분자를 다른 분수의 분모로 곱해주고 분모 곱과의 최대 공약수를 구해줍니다.
print((a1 * b2 + a2 * b1) // c, b1 * b2 // c)
# 분자와 분모를 최대 공약수로 나누어줍니다.