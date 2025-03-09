import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

graphs = [[0] * (n + 1) for _ in range(n + 1)]
dp = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b, c = map(int, input().split())
    if a > b:
        continue
    graphs[a][b] = max(graphs[a][b], c)

for i in range(2, n + 1):
    dp[i][2] = graphs[1][i]

for i in range(2, n + 1):
    for j in range(i, m + 1):
        for l in range(1, i):
            if graphs[l][i] and dp[l][j - 1]:
                dp[i][j] = max(dp[i][j], dp[l][j - 1] + graphs[l][i])

print(max(dp[-1]))