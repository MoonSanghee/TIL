from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(m)]
# 영역의 크기와 영역의 상태를 받아줍니다.
visited = [[[0, 10000]]*n for _ in range(m)]
visited[0][0] = [0, 0]
# 최대 사이즈가 100*100이므로 비용이 0만큼 들고 10000번 벽을 부쉈다는 리스트로
# 영역의 크기와 같은 방문확인할 리스트를 만들엊줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방위 탐색을 지정해줍니다.
def move(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(m) and ny in range(n):
                if maps[nx][ny] == 0:
                    # 영역에서 벽이 아니라면
                    if visited[nx][ny][1] > visited[x][y][1]:
                        visited[nx][ny] = [visited[x][y][0] + 1, visited[x][y][1]]
                        q.append((nx, ny))
                        # 벽을 최소로 부수었는지 확인해주고 벽을 최소로 부수고
                        # 도달하도록 갱신해준 다음 좌표를 넣어주고
                    elif visited[nx][ny][1] == visited[x][y][1]:
                        if visited[nx][ny][0] > visited[x][y][0] + 1:
                            visited[nx][ny][0] = visited[x][y][0] + 1
                            q.append((nx, ny))
                        # 벽이라면 최단거리인지 확인해주고 최단거리로 갱신한 후 좌표를 넣어줍니다.
                else:
                    if visited[nx][ny][1] > visited[x][y][1] + 1:
                        visited[nx][ny] = [visited[x][y][0] + 1, visited[x][y][1] + 1]
                        q.append((nx, ny))
                        # 영역에서 벽이라면 벽을 1번 더 부수었을때 최소로 부수는 것인지 확인해주고
                        # 값을 갱신해 넣어주고
                    elif visited[nx][ny][1] == visited[x][y][1] + 1:
                        if visited[nx][ny][0] > visited[x][y][0] + 1:
                            visited[nx][ny][0] = visited[x][y][0] + 1
                            q.append((nx, ny))
                        # 최소로 부수는 것이라면 최단거리인지 확인해주고 좌표를 넣어줍니다.

move(0, 0)
print(visited[-1][-1][1])
# 목적지에 저장된 최소로 부순 벽의 개수를 출력해줍니다.