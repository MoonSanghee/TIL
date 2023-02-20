n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
# 각 자리의 상태와 도달 가능한 방법의 수를 입력할 리스트를 만들어 줍니다.

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
        # 각 자리에서 이동가능한 자리에 현재 자리까지 올 수 있는 경우의수를 더해줍니다.
        # 목적지에 도착하였으면 저장된 값을 출력해줍니다.