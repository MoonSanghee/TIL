from collections import deque

n, m = map(int, input().split())
maps = [list(map(int ,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
# 영역의 크기와 이동 가능한지 표시된 지도를 받아주고
# 영역의 크기와 같은 방문 처리를 할 이중리스트를 만들어줍니다.

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            target = [i, j]
# maps을 순회하며 2를 값으로 가지는 목적지를 찾아줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 이동을 설정해줍니다.
def move(a, b):
    q = deque()
    q.append((a, b))
    # q라는 이름의 덱을 만들고 좌표를 넣어줍니다.
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m):
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    # 4방위 탐색을 통해 영역의 안에 들어있는지와
                    # 이동 가능하고 방문한 적이 없는지 확인해 줍니다.
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    # 방문처리를 이동 전 위치보다 1만큼 떨어져있을으로 표시해주고
                    # q에 nx, ny의 좌표를 넣어줍니다.
                    
move(target[0],target[1])
# 목적지를 기준으로 함수를 작동시켜 방문 가능한 위치라면 떨어진 거리를 표시해줍니다.
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and not visited[i][j]:
            visited[i][j] = -1
            # 모든 영역을 확인하여 이동이 갈 수 있는 땅인데 방문하지 못하는 위치라면
            # -1로 방문처리를 해줍니다.
    print(*visited[i])
    # 각 줄 별로 가지고있는 값들을 출력해줍니다.