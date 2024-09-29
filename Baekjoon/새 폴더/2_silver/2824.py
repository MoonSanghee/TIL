from math import gcd

n = int(input())
numbers1 = list(map(int, input().split()))
m = int(input())
numbers2 = list(map(int, input().split()))
# 주어지는 두 수열의 길이와 수열을 받아줍니다.
number1 = 1
number2 = 1
for i in numbers1:
    number1 *= i

for j in  numbers2:
    number2 *= j
# 각 수열의 곱을 구해줍니다.

print(str(gcd(number1, number2))[-9:])
# 두 수열의 곱의 최대 공약수를 구해 앞에서 9자리를 출력해줍니다.