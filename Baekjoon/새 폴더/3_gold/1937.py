import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 숲의 상태를 입력받습니다.
dp = [[-1]*n for _ in range(n)]
# 영역의 크기와 같은 2중 리스트 형태로 이동할 수 있는 거리를 표시할 dp를 만들어 줍니다.
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
# 4방향 이동을 설정해줍니다.
result = 0
# 최대 이동거리를 담을 변수를 지정해줍니다.
def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 1
        # 현 위치가 처음 방문하는것이라면 방문처리를 해주고(현재 위치의 대나무를 먹은것을 표시해줌)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(n) and maps[nx][ny] > maps[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
                # 재귀를 통해 얼마나 이동할 수 있는지 확인해줍니다.
    return dp[x][y]
    # dp[x][y]의 값을 리턴합니다.

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))
        # 모든 자리에서 함수를 작동시켜 더 많이 먹을 수 있는 자리가있다면
        # 값을 갱신해줍니다. 
print(result)
# 담겨있는 최대로 먹은 값을 출력해줍니다.