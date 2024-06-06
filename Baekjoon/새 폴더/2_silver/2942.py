from math import gcd

r, g = map(int, input().split())
number = gcd(r, g)
# 두 수를 받고 최대공약수를 구해줍니다.
for i in range(1, int(number ** 0.5) + 1):
    # 최대공약수의 제곱근까지를 순회하면서
    if number % i == 0:
        print(i, r // i, g // i)
        j = number // i
        if i != j:
            print(j, r // j, g // j)
        # 약제곱근이 아닌 약수일 경우 약수와 약수로 나눈 값만큼의 선수들에게 나눠지는 경우를 출력해줍니다.