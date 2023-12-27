from collections import deque

n, m = map(int, input().split())
# 영역의 크기를 받아줍니다.
sheet = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
alive = [0, 0]
# 영역의 상태와 방문처리할 지도 살아남은 늑대와 양을 기록할 리스트를 만들어줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 탐색을 만들어줍니다.
def bfs(a, b):
    q = deque()
    q.append((a, b))
    v, k = 0, 0
    # q에 받은 좌표를 넣고 울타리 안에 양과 늑대를 확인할 변수를 만들어줍니다.
    while q:
        x, y = q.popleft()
        if sheet[x][y] == 'v':
            v += 1
        elif sheet[x][y] == 'k':
            k += 1
        visited[x][y] = True
        # 좌표를 확인하여 늑대나 양이라면 값을 갱신해주고 방문처리를 합니다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and sheet[nx][ny] != '#':
                visited[nx][ny] = True
                q.append((nx, ny))
            # 4방향 탐색을 통해 이동이 가능하다면 이동처리를 하고 좌표를 큐에 넣어줍니다.
    if k > v:
        alive[0] += k
    else:
        alive[1] += v
    # 모든 울타리 영역을 확인했다면 늑대와 양의 수를 비교하여 값을 갱신해줍니다.

for i in range(n):
    for j in range(m):
        if sheet[i][j] != '#' and not visited[i][j]:
            bfs(i, j)
            # 방문한 적없는 영역을 찾아 살아남을 양과 늑대를 확인해줍니다.

print(*alive)
# 살아남은 개체를 출력해줍니다.