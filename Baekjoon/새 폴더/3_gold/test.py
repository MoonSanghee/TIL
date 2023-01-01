from collections import deque

n, m = map(int, input().split())
t, c, v = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
maps = maps[::-1]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(a, b):
    q = deque()
    q.append([a, b])
    cnt = 1
    maps[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(v, v + 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m):
                if maps[nx][ny] == 0:
                    maps[nx][ny] = 1
                    cnt += 1
                    q.append([nx, ny])
                    break
    return cnt

print(clean(n - t, c))