from math import gcd

n = int(input())
nums = []
# 수의 개수와 공약수를 담을 리스트를 생성해줍니다.

if n == 2:
    a, b = map(int, input().split())
    gcd_ = gcd(a, b)
if n == 3:
    a, b, c = map(int, input().split())
    gcd_ = gcd(gcd(a, b), c)
# 주어진 수의 최대공약수를 구해줍니다.

for i in range(1, int((gcd_)) + 1):
    if gcd_ % i == 0:
        nums.append(i)
# 공약수를 확인해 리스트에 담아줍니다..

for num in nums:
    print(num)
# 오름차순으로 출력해줍니다.