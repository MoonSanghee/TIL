n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
# n * m의 크기의 2중 리스트를 받아줍니다.
dp = [[0]*(m+1) for _ in range(n + 1)]
# 가로, 세로가 n, m 보다 각 1씩 더 크고 각 값을 0으로 가지는 2중 리스트를 만들어줍니다.
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = maps[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        # x축만 1만큼, y축만 1만큼, x,y축 모두 1만큼 간 자리에 올 수 있는 가장 큰 수는
        # dp에서 x축만 1만큼, y축만 1만큼, x,y축 모두 1만큼 이전 자리에서 3자리의 값중 가장 큰 경우에서 올 경우입니다.

print(dp[n][m])
# 이를 다 모아 dp[n][m]에 담긴 값을 출력해줍니다.