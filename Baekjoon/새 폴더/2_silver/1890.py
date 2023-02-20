n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        nx = maps[i][j] + i
        ny = maps[i][j] + j
        if i == n- 1 and j == n - 1:
            print(dp[-1][-1])
            break
        if nx < n:
            dp[nx][j] += dp[i][j]
        if ny < n:
            dp[i][ny] += dp[i][j]
