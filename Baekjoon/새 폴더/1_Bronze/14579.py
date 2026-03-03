a, b = map(int, input().split())
# 주어지는 두 수를 받아줍니다
result = 1
number = 0
# 수의 합을 답을 변수와 결과를 담을 변수를 설정해줍니다
for i in range(a):
    number += i
# a - 1 까지의 누적합을 담아줍니다
for j in range(a, b + 1):
    number += j
    result *= number
# b까지의 누적합을 곱해줍니다
print(result % 14579)
# 정해집수로 나눈 나머지를 출력해줍니다 