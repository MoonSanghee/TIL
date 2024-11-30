t = int(input())
# 테스트 케이스의 수를 받아줍니다
for tc in range(t):
    n = int(input())
    # 주어지는 정수를 받아줍니다
    num = 1
    for i in range(1, n + 1):
        num *= i
        while num % 10 == 0:
            num //= 10
        # 주어지는 정수의 팩토리얼 값을 계산하며 맨 오른쪽 수가 0이 아닐때까지 10으로 나누어줍니다
    print(num % 10)
    # 0이 아닌 최우측수를 출력해줍니다