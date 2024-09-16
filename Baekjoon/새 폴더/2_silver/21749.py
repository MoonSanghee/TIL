from collections import deque

n, m = map(int, input().split())
maps = [input() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
# 캠퍼스의 크기와 정보를 받고 방문처리할 리스트를 만들어줍니다.

q = deque()
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'I':
            q.append((i, j))
            visited[i][j] = True
            break
# 이동을 담을 큐를 만들고 도연이의 위치를 찾아 표시해줍니다.

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 4방향으로 이동이 가능하므로 4방향을 설정해줍니다.
cnt = 0
# 만든 친구의 수를 담을 변수를 설정해줍니다.
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == False and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                q.append((nx, ny))
                if maps[nx][ny] == 'P':
                    cnt += 1
# bfs를 통해 만날수 있는 친구를 확인해줍니다.
if cnt:
    print(cnt)
else:
    print("TT")
# 조건에 따라 결과를 출력해줍니다.