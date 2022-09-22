# 찾아본 코드 1
n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)
for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])


# 찾아본 코드 2
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n):
    for j in range(i + li[i][0], n + 1):
        if dp[j] < dp[i] + li[i][1]:
            dp[j] = dp[i] + li[i][1]

print(dp[-1])