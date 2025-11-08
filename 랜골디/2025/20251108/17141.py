from collections import deque
import itertools

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 주어지는 변수를 받아줍니다
spots = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            spots.append((i, j))
# 바이러스를 놓을수 있는 좌표를 받아줍니다
coms = itertools.combinations(spots, m)
result = n * n
# 바이러스를 놓을 좌표의 조합을 뽑고 결과를 n의 제곱으로 설정해줍니다
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방위 이동을 설정해줍니다
for com in coms:
    q = deque(com)
    visited = [[-1] * n for _ in range(n)]
    cnt = 0
    for x, y in com:
        visited[x][y] = 0
    # 최초의 바이러스를 놓은 자리를 방문처리해줍니다
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1 and maps[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    # 너비우선탐색을 통해 바이러스를 놓은 위치에서 연결된 모든 좌표를 방문해줍니다
    if visited[nx][ny] >= result:
        continue
    # 모든 좌표를 방문하는데 이전의 기록과 같거나 오래걸렸다면 다음 조합을 확인해줍니다
    flag = True
    for i in range(n):
        for j in range(n):
            if maps[i][j] != 1:
                if visited[i][j] != -1:
                    cnt = max(cnt, visited[i][j])
                else:
                    flag = False
    # 방문하지 못한 자리가 있는지 확인해줍니다
    if flag:
        result = result = min(result, cnt)
    # 방문하지 못한 자리가 없다면 결과값을 갱신해줍니다

if result != n * n:
    print(result)
else:
    print(-1)
    # result값이 갱신된적 있는지 확인하여 결과를 출력해줍니다