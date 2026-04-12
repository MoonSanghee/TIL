T = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(T):
    N = int(input())
    # 문제수를 받아줍니다
    for _ in range(N):
        a, b = map(int, input().split())
        print(a + b, a * b)
        # 두 수를 받아 계산한 값을 출력해줍니다