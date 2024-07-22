n, a, b, c = map(int, input().split())
# 주어지는 4개의 정수를 받아줍니다.
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)
# x이하의 모든 자연수를 곱하는 팩토리얼 함수를 정의해줍니다.

print(factorial(n) // (factorial(a) * factorial(b) * factorial(c)))
# 조합의 가짓수를 출력해줍니다.