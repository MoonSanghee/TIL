from math import gcd
# math 라이브러리에서 gcd(최대공약수)를 불러옵니다.
n, m = map(int, input().split(':'))
l = gcd(n, m)
n //= l
m //= l
# 두 정수를 입력받아 최대공약수로 나누어줍니다.
print(f"{n}:{m}")
# 최대공약수로 나눈값을 형태에 맞게 출력해줍니다.