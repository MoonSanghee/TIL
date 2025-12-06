from math import gcd
x, y = map(int, input().split())
print(x + y - gcd(x, y))
# 주어진 두 수의 합에서 최대 공약수를 빼줍니다