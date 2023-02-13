n = int(input())

dp = [0, 3, 7]

for i in range(2, n):
    dp.append(((dp[i] - dp[i - 1]) * 2 + dp[i - 1] * 3)%9901)

print(dp[n])