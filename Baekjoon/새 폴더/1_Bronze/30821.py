n = int(input())
# 주어지는 꼭지점의 수를 받아줍니다
def factorial(x):
    number = 1
    while x:
        number *= x
        x -= 1
    return number
# 팩토리얼을 정의해줍니다
print(factorial(n) // (factorial(5) * factorial(n - 5)))
# 주어지는 n개의 꼭지점에서 임의의 5개 꼭지점을 골르는 방법의 수를 출력해줍니다