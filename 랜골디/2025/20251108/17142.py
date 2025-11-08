from collections import deque
import itertools

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 주어지는 좌표를 받아줍니다
spots = []
wall = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            spots.append((i, j))
        elif maps[i][j] == 1:
            wall += 1
# 벽의 개수와 바이러스의 위치를 받아줍니다
coms = itertools.combinations(spots, m)
result = n * n
# 활성화시킬 바이러스의 조합과 결과를 담을 변수를 설정해줍니다
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 이동을 설정해줍니다
for com in coms:
    q = deque(com)
    visited = [[-1] * n for _ in range(n)]
    cnt = 0
    for x, y in com:
        if (x, y) in q:
            visited[x][y] = 0
    # 활성화 시킨 바이러스를 방문처리해줍니다
    target = n * n - len(spots) - wall
    # 남은 빈공간을 담을 변수를 설정해줍니다
    while q:
        if target == 0:
            break
        # 빈공간이 없다면 반복을 멈추어줍니다
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] != 1:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
        # 너비우선탐색을 이용하여 모든 빈공간을 방문할때까지 벽이 아닌곳을 모두 방문하여줍니다
    flag = True
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                if visited[i][j] == -1:
                    flag = False
                else:
                    cnt = max(cnt, visited[i][j])
    # 바이러스가 도달하지 못한 빈공간이 있는지 확인해줍니다
    if flag:
        result = min(result, cnt)
    # 바이러스가 도달하지 못한 빈공간이 없다면 걸린 시간을 갱신해줍니다
if result != n * n:
    print(result)
else:
    print(-1)
# 걸린 시간이 갱신된적 있는지 확인하여 결과를 출력해줍니다
