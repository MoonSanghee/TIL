n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
# n줄의 색 가격을 받아주고 그 크기에 맞추어 이중 리스트 형태의 dp라는 리스트를 만들어줍니다.
dp[0] = maps[0]
# dp 첫 번째 자리는 이전 값이 없으므로 0에 본인을 더한 값이 가장 작은 경우이므로 maps[0]을 넣어줍니다.

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + maps[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + maps[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + maps[i][2]
    # dp각 행의 자리에 이전 자리 본인을 제외한 두 수중 작은것을 더한 값으로 갱신해줍니다.

print(min(dp[n - 1]))
# dp리스트의 마지막 리스트에 온 값중 가장 작은 값을 출력해줍니다.