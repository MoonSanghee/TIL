n = int(input())
result = 0
# 주어지는 정수를 받고 결과를 담을 변수를 설정해줍니다
for i in range(n):
    result += (n % 10) ** 5
    n //= 10
# 각 자리수의 5제곱을 결과에 더해줍니다
print(result)
# 결과를 출력해줍니다