from collections import deque
n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
# 영역의 크기와 현재 영역의 상태를 지도로 받아줍니다
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 이동을 설정해줍니다.
def bfs(a, b):
    q = deque()
    visited = [[0]* m for _ in range(n)]
    # 영역의 크기와 같은 방문 처리를 해 줄 리스트를 만들어줍니다.
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '*':
                q.append((i, j))
                visited[i][j] = -1
                # 모든 영역을 확인하며 물이 차오르는 위치라면
                # 덱에 넣고 -1로 방문처리를 해줍니다.
    q.append((a, b))
    # 덱에 고슴도치의 위치를 담아줍니다.
    visited[a][b] = 1
    # 고슴도치의 현재 위치를 방문처리 하기위해 1로 바꾸어줍니다.
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(n) and ny in range(m):
                # 덱에서 뺀 값이 4방위 이동하여도 영역의 안인지 확인해주고
                if maps[nx][ny] == 'D' and visited[x][y] > 0:
                    return visited[x][y]
                    # 비버의 소굴이고 고슴도치가 이동해온 것이라면 고슴도치가 이동하는데
                    # 든 시간이 얼마인지 되돌려줍니다. 시작위치를 1로 시작하였기 때문에
                    # visited[x][y]에 저장되어있는 값을 출력해줍니다.
                if maps[nx][ny] == '.':
                    if visited[nx][ny] == 0:
                    # 아니라면 지도에서 빈 공간인지 확인해주고
                    # 방문한 적이 있는지 확인해줍니다.
                        if visited[x][y] > 0:
                            visited[nx][ny] = visited[x][y] + 1
                            q.append((nx, ny))
                            # 고슴도치가 이동한 것이라면 시간이 1만큼 들었다고 표시해주고
                            # 덱에 좌표를 추가해주고
                        else:
                            visited[nx][ny] = -1
                            q.append((nx, ny))
                            # 물이 차오른것이라면 -1로 방문처리를 해주고 덱에 값을 추가해줍니다.
    return 'KAKTUS'
    # 덱이 비었다면 고슴도치가 탈출을 못 했다는 의미이므로 'KAKTUS'을 추가해줍니다.
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            print(bfs(i, j))
            # 영역을 순회하면 고슴도치의 위치를 찾아 함수를 실행시켜 받는 결과를 출력해줍니다.