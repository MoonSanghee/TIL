from collections import deque

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 아기 상어가 있는 영역을 확인해줍니다.

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
# 8방향 이동을 설정해줍니다.

q = deque()
for i in range(n):
    for j in range(m):
        if maps[i][j]:
            q.append((i, j))
# 아기상어가 있는 위치를 q에 받아줍니다.

longest = 0
while q:
    x, y = q.popleft()
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx in range(n) and ny in range(m):
            if not maps[nx][ny]:
                maps[nx][ny] = maps[x][y] + 1
                longest = maps[nx][ny]
                q.append((nx, ny))
                # 큐의 값을 빼내면서 확인하여 8방향 이동이 가능한지 확인하고 상어로부터
                # 얼마나 떨어져있는지 값을 저장하여줍니다.

print(longest - 1)
# 상어가 있는 1부터 값을 더하여주었으므로 마지막에 저장된 값에 1을 뺀 값을 출력해줍니다.