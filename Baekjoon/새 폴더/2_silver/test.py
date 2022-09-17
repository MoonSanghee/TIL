n = int(input())
maps = []
for i in range(n):
    maps.append(int(input()))
dp = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if maps[i] > maps[j]:
            if dp[j] > dp[i]:
                dp[i] = dp[j]
    dp[i] += maps[i]
print(dp)