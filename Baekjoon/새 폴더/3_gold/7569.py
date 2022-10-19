from collections import deque

m,n,h = map(int, input().split())
maps = []
for i in range(h):
    floor = []
    for j in range(n):
        floor.append(list(map(int, input().split())))
    maps.append(floor)

# 3중 리스트 형태이기에 m,n의 2중 리스트를 h 만큼 넣어줍니다.

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(a, b, c):
    q = deque()
    q.append((a, b, c))
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            # 동서남북상하 6방위에 대해 탐색하여 확인해야 합니다.
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if nx in range(h) and ny in range(n) and nz in range(m) and (maps[nx][ny][nz] == 0 or maps[nx][ny][nz] > maps[x][y][z] + 1):
                # 각 값이 범위 안에 있는지 확인 해 주고 maps[nx][ny][nz]가 0일때뿐 아니라 maps[nx][ny][nz]의 현재 값이 들어갈 값보다 클 경우 갱신해 줘야 합니다. .
                maps[nx][ny][nz] = maps[x][y][z] + 1
                q.append((nx, ny, nz))

days = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if maps[i][j][k] == 1:
                bfs(i, j, k)
                # 좌표값이 1일 때 영향을 받아 변하지 않았으므로 bfs를 돌려줍니다.
made = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            days = max(days, maps[i][j][k])
            if maps[i][j][k] == 0:
                made = False
            # 모든 좌표를 돌며 0이 있는지 확인해주고 최대 값도 구하여줍니다.

if made:
    print(days - 1)
    # 0이 없다면 최대 값에 1을 뺀 값을 출력합니다.
else:
    print(-1)