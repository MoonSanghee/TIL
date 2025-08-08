T = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(T):
    n, m, k, d = map(int, input().split())
    # 주어지는 변수들을 받아줍니다
    b = 2 * d // (k * n * m * (m - 1) + m * m * n * (n - 1))
    # 주어지는 변수들을 이용해 b를 구하여줍니다
    if b:
        print(k * n * m * (m - 1) * b // 2 + m * m * n * (n - 1) * b // 2)
    else:
        print(-1)
        # 자연수 b가 존재할 수 있다면 최대 경기수를 없다면 -1을 출력해줍니다