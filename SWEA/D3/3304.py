T = int(input())

for tc in range(1, T + 1):
    first, second = input().split()

    dp = [[0] * (len(first) + 1) for _ in range((len(second) + 1))]
    
    for i in range(1, len(second) + 1):
        for j in range(1, len(first) + 1):
            if first[j - 1] == second[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    print(f'#{tc} {dp[-1][-1]}')