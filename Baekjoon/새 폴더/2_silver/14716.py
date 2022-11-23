from collections import deque
m, n = map(int ,input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
cnt = 0

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def bfs(a, b):
    maps[a][b] = 0
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(m) and ny in range(n) and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny))

for i in range(m):
    for j in range(n):
        if maps[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)
# 상하, 좌우 혹은 대각선에 1이 있으면 이어져있는 글자라고 했으니 8방 탐색으로 연속한 
# 글자가 있는지 확인해서 하나의 문자를 찾는 bfs코드를 짜주고 주어진 크기의 맵을 전체탐색하며
# 이어진 글자를 하나씩 지워가면서 1씩 더해주어 답을 구하였습니다.