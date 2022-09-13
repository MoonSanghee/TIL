n = int(input())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += numbers[i]
print(max(dp))