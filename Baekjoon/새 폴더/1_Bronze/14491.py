n = int(input())
# 정수를 받아줍니다.
result = ''
while n:
    result += str(n % 9)
    n //= 9
print(result[::-1])
# 9진수로 변환한 값을 출력해줍니다.