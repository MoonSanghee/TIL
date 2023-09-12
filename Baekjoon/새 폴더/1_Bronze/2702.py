from math import lcm, gcd

n = int(input())
# 수가 몇 쌍인지 받아줍니다.
for _ in range(n):
    a, b = map(int, input().split())
    # 두 수를 입력받아줍니다.
    print(lcm(a, b), gcd(a, b))
    # math라이브러리를 이용하여 최소 공배수와 최대 공약수를 출력해줍니다.