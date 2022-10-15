import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
alpha = set()
alpha.add(maps[0][0])
cnt = 0

def dfs(x, y, z):
    global cnt
    cnt = max(cnt, z)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(r) and ny in range(c) and maps[nx][ny] not in alpha:
            alpha.add(maps[nx][ny])
            dfs(nx, ny, z + 1)
            alpha.remove(maps[nx][ny])
    return

dfs(0, 0, 1)
print(cnt)