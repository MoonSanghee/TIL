t = int(input())
# 입력받는 경우의 수를 받아줍니다.
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    # 수의 개수와 수열을 받아줍니다.
    dp = [0] * n
    dp[0] = li[0]
    # n개의 0을 가지는 dp리스트를 만들고 0번 인덱스를 li[0]으로 만들어줍니다.
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + li[i], li[i])
    # 연속하는 경우와 각 자리에서 시작하는 경우 중 더 큰 값을 dp의 각 자리에 넣어줍니다.
    print(max(dp))
    # dp 리스트에서 가장 큰 값을 출력해줍니다.