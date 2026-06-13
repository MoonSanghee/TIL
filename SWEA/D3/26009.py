T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    a, b, c = map(int, input().split())
    A = a * (a + 1) // 2
    B = b * (b + 1) // 2
    C = c * (c + 1) // 2
    # 주어지는 세 수를 받고 세 수까지의 정수 누적합을 구해줍니다
    print(A * B * C % 998244353)
    # 세 수의 누적합을 곱하고 주어진 수로 나눈 나머지를 출력해줍니다