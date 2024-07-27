n, m = map(int, input().split())
n -= m
# 두 수를 받고 n에서 m을 빼줍니다.
result = 0
# 나눌 값의 합을 담을 변수를 설정해줍니다.
for i in range(1, int(n ** 0.5) + 1):
    # n의 제곱근의 정수 + 1까지를 확인해줍니다.
    if n % i == 0:
        # n이 나누어떨어진다면
        if i > m:
            result += i
        # i가 m보다 크다면 result에 i를 더해줍니다.
        if i ** 2 != n and n // i > m:
            result += n // i
        # i의 제곱이 n이 아니고 n을 i로 나눈값이 m보다 크다면 result에 n // i를 더해줍니다.

print(result)
# 결과를 출력해줍니다.