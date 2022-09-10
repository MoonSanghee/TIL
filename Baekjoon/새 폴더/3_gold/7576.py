from collections import deque

m, n = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            q.append((i, j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m):
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx, ny))
bfs()
maxi = 0
for i in maps:
    maxi = max(maxi, max(i))
    if 0 in i:
        print(-1)
        break
else:
    print(maxi - 1)