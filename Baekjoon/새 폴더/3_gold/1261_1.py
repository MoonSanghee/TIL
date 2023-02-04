from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(m)]

visited = [[[0, 10000]]*n for _ in range(m)]
visited[0][0] = [0, 0]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

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
                    if visited[nx][ny][1] > visited[x][y][1]:
                        visited[nx][ny] = [visited[x][y][0] + 1, visited[x][y][1]]
                        q.append((nx, ny))
                    elif visited[nx][ny][1] == visited[x][y][1]:
                        if visited[nx][ny][0] > visited[x][y][0] + 1:
                            visited[nx][ny][0] = visited[x][y][0] + 1
                            q.append((nx, ny))
                else:
                    if visited[nx][ny][1] > visited[x][y][1] + 1:
                        visited[nx][ny] = [visited[x][y][0] + 1, visited[x][y][1] + 1]
                        q.append((nx, ny))
                    elif visited[nx][ny][1] == visited[x][y][1] + 1:
                        if visited[nx][ny][0] > visited[x][y][0] + 1:
                            visited[nx][ny][0] = visited[x][y][0] + 1
                            q.append((nx, ny))

move(0, 0)
print(visited[-1][-1][1])