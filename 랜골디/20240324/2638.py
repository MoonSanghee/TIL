from collections import deque
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
t = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 영역의 크기와 영역을 받아주고 다 녹는데 걸리는 시간을 담을 변수와 4방향 탐색을 설정해줍니다.

def change(a, b):
    # 외부의 공기에 노출되는 영역을 확인하고 -1로 바꿔 표시해줍니다.
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[a][b] = True
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if maps[x][y] == 0:
            maps[x][y] = -1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and maps[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def melt():
    # 녹아야하는 부분을 확인하고 -1로 바꾸었던 녹아야하는 부분을 공기를 의미하는 0으로 다시 바꾸어줍니다.
    for i in range(n):
        for j in range(m):
            cnt = 0
            if maps[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if maps[nx][ny] == -1:
                        cnt += 1
            if cnt > 1:
                maps[i][j] = 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == -1:
                maps[i][j] = 0
                
while True:
    cheese = False
    # 치즈가 남았는지 확인하는 변수를 선언해줍니다
    for i in range(n):
        if 1 in maps[i]:
            cheese = True

    if cheese:
        change(0, 0)
        melt()
        t += 1
    else:
        break
    # 치즈가 남았는지 확인하고 남아있다면 녹이는 작업을 진행한 다음 시간을 1만큼 추가해주고
    # 남은 치즈가 없다면 반복을 멈추어줍니다.

print(t)
# 치즈가 다 녹는데 걸린 시간을 출력해줍니다.