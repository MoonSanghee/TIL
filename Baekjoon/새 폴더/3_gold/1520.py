import sys
sys.setrecursionlimit(10**8)
# 재귀를 이용한 dfs를 사용할것이기에 재귀의 최대 깊이를 늘려줍니다.
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 가로 세로 크기를 받고 값을 입력받습니다.
dp = [[-1] * m for _ in range(n)]
# 가로 세로 크기에 맞는 방문 가짓수를 표시할 표를 만들어 줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 상하좌우 4방향 탐색을 할것이기 때문에 4방위 이동을 저장해줍니다.
def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
        # 3. x, y 가 목적좌표라면 1을 돌려 더해줍니다.
    if dp[x][y] != -1:
        return dp[x][y]
        # 2. dp 표에서 x, y를 방문한 적 있다면 그 값을 되돌려 줍니다.
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(n) and ny in range(m):
            if maps[x][y] > maps[nx][ny]:
                dp[x][y] += dfs(nx, ny)
                # 1. x,y값의 4방위 탐색한 값에서 내려갈 곳이 있다면 dp[x][y]에 내려갈 수 있는 자리의
                # dp값을 더해주고 dp 좌표에 대해 dfs를 작동시켜줍니다.
    return dp[x][y]
    # 4. 4방위 탐색이 불가하면 현재 좌표의 dp값을 돌려줍니다.
dfs(0, 0)
# 0, 0에 대하여 dfs를 실행하고
print(dp[0][0])
# dp 표에서 0, 0에 위치한 값을 출력해줍니다.

# dp에 방문 할 수 없는 좌표를 계속하여 확인하는 방식의 코드를 구현하여 계속하여 실패하였음.
# 여러 방향으로 바라보는 연습이 더 필요하다고 느낌.