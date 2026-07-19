T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n = int(input())
    numbers = list(map(int, input().split()))
    # 수의 개수와 수열을 받아줍니다
    dp = [0] * n
    dp[0] = numbers[0]
    result = numbers[0]
    # dp리스트를 만들고 첫 값을 갱신해줍니다
    for i in range(1, n):
        dp[i] = max(numbers[i], dp[i - 1] + numbers[i])
        # 누적합이 더 커지는지 확인하여 dp값을 갱신해줍니다
        if dp[i] > result:
            result = dp[i]
        # 최대값을 확인하고 갱신해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 출력해줍니다