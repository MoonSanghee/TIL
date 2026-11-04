T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dp = [1 for _ in range(N)]
    numbers = list(map(int, input().split()))

    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(f'#{tc} {max(dp)}')