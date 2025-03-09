n = int(input())
RGB = [list(map(int, input().split())) for _ in range(n)]
# 집의 수와 색을 칠할때 비용을 받아줍니다.
INF = 1e6
result = INF
# 최대 1천의 집과 1천의 비용이므로 최대값을 100만으로 설정해주고 결과값을 최대값으로 설정해줍니다.

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    # RGB와 같은 크기의 dp리스트를 만들고 각 값을 설정한 최대값으로 세팅해줍니다.
    dp[0][i] = RGB[0][i]
    # 첫 집의 색을 정하여 RGB의 비용을 확인해 dp값을 갱신해줍니다.
    for j in range(1, n):
        dp[j][0] = RGB[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = RGB[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = RGB[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    # dp의 1번 인덱스 각 자리에 칠할 색과 다른 색들중 누적 비용이 적은 값과 색을 칠하는 비용의 합으로  dp 자리값을 갱신해줍니다.
    for j in range(3):
        if i != j:
            result = min(result, dp[-1][j])
    # 처음 설정한 색이 마지막 집의 색과 다르면 result값과 비교하여 총 사용된 비용을 계산해줍니다.

print(result)
# 결과를 출력해줍니다.