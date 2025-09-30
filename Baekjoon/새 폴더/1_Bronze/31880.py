n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 주어지는 수를 받아줍니다
result = 1
# 곱으로 만들수 있는 최대값을 담을 변수를 담아줍니다
for i in b:
    if i != 0:
        result *= i
# 주문서는 0이상의 정수이므로 0을 제외한 모든 수는 곱하였을때 수가 커집니다
print(result * sum(a))
# a에는 음수가 없으므로 모든 a의 값을 더해 result를 곱한 결과를 출력해줍니다