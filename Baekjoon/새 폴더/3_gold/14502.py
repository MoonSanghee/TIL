from collections import deque
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

def virus(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m) and check[nx][ny] == 0:
                check[nx][ny] = 2
                q.append((nx, ny))
# 바이러스를 확산시키는 함수

def safe():
    zone = 0
    for i in range(n):
        for j in range(m):
            if check[i][j] == 0:
                zone += 1
    return zone
# 안전 영역을 확인하는 함수

def dfs(cnt):
    global result
    if cnt == 3:
        # 벽을 다 세웠다면
        for i in range(n):
            for j in range(m):
                check[i][j] = maps[i][j]
        # 벽을 세운 상태를 입력
        for i in range(n):
            for j in range(m):
                if check[i][j] == 2:
                    virus(i, j)
        # 바이러스를 확산시키는 함수를 가동
        result = max(result, safe())
        # 안전구역의 너비 비교
        return 
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                cnt += 1
                dfs(cnt)
                cnt -= 1
                maps[i][j] = 0
                # 재귀를 통해 모든 벽을 세울 수 있는 경우 확인

dfs(0)
print(result)
