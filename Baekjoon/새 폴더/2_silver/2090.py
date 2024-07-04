from  math import gcd, lcm

n = int(input())
numbers = list(map(int, input().split()))
# 수의 개수와 수열을 받아줍니다.
l = numbers[0]
for i in range(1, n):
    l = lcm(l, numbers[i])
# 최소 공배수를 구해줍니다.
mother = l
son = 0
for i in numbers:
    son += l // i
# 분모와 분자를 구해줍니다.
g = gcd(mother, son)
print(f"{mother // g}/{son // g}")
# 두 수의 최대공약수를 구해 알맞은 형식으로 출력해줍니다.