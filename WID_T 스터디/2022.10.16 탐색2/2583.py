from collections import deque

n, m, k = map(int, input().split())

maps = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            maps[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    cnt = 1
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(n) and ny in range(m) and maps[nx][ny] == 0:
                maps[nx][ny] = 1
                cnt += 1
                q.append((nx, ny))
    return cnt

result = []
for i in range(n):
    for j in range(m):
        if not maps[i][j]:
            maps[i][j] = 1
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result)