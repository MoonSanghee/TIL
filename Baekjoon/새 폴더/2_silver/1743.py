from collections import deque
n,m,k = map(int, input().split())
maps = [[0 for _ in range(m)] for _ in range(n)]
# 가로m * 세로 n의 크기의 2중 리스트에
for _ in range(k):
    x, y = map(int, input().split())
    maps[x - 1][y - 1] = 1
    # x, y값이 주어지지만 인덱스는 0부터 시작하므로 받은 값의 가로, 세로 위치의 1씩 빼준 값을 표시해준다.

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    cnt = 1
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m) and maps[nx][ny]:
                maps[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

li = []
for i in range(n):
    for j in range(m):
        if maps[i][j]:
            maps[i][j] = 0
            li.append(bfs(i, j))
# bfs를 통해 연결되 쓰레기가 있는 구역의 크기를 구하여 빈 리스트에 넣어주고
# 가장 넓은 구역을 출력해주었습니다.

print(max(li))