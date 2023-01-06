from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [input() for _ in range(n)]
# 주어진 크기의 맵을 입력받습니다.
cnt = 0
# 최대 길이를 입력해줄 변수를 설정해줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 탐색을 진행하도록 설정해줍니다.
def bfs(a, b):
    c = 0
    q = deque()
    q.append([a, b])
    check[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            # 4방향 탐색을 해줍니다.
            if nx in range(n) and ny in range(m):
                # 주어진 크기의 맵에 속해있는지 확인합니다.
                if maps[nx][ny] == 'L' and check[nx][ny] == -1:
                    # 땅인지와 방문여부를 확인합니다.
                    check[nx][ny] = check[x][y] + 1
                    c = max(c, check[nx][ny])
                    q.append([nx, ny])
                    # 새로 방문할 check의 자릿값을 갱신해주고 최대값과 비교해준뒤 deque에 값을 추가해줍니다.
    return c
    # maps[a][b]에서 가지는 최대 길이를 돌려줍니다.

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            # 맵을 돌면서 땅인지 확인하고
            check = [[-1]*m for _ in range(n)]
            # 맵과 같은 크기의 방문처리를 해줄 2중 리스트를 만들어줍니다.
            cnt = max(bfs(i, j), cnt)
            # cnt 값과 그 자리에서 나온 최장 길이를 비교해줍니다.
print(cnt)
# 최종적으로 cnt에 갱신되어있는 값을 출력해줍니다.