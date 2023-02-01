from collections import deque
t = int(input())
# 실행할 테스트의 회수를 받습니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 이동을 설정해줍니다.
def escape(a, b):
    q = deque()
    visited = [[0] * n for _ in range(m)]
    # 영역의 크기와 같은 방문처리를 해줄 리스트를 만들어줍니다.
    q.append((a, b))
    visited[a][b] = 1
    # 사람의 위치를 덱에 넣어주고 1로 방문처리를 해줍니다.
    for i in range(m):
        for j in range(n):
            if maps[i][j] == '*':
                visited[i][j] = -1
                q.append((i, j))
    # 모든 영역을 탐색하며 지도에서 '*'일 경우 불이 위치한 곳이므로 -1로 방문처리를 해주고
    # 덱에 좌표를 넣어줍니다.
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx not in range(m) or ny not in range(n):
            # 4방향 탐색을 통해 밖으로 나갔을때
                if visited[x][y] > 0:
                    return visited[x][y]
                    # 사람이 이동한 경우 출발점에 저장되어있는 값을 돌려줍니다.
                    # 움직이지 않은 상태에서 위치해 있는것을 1로 표시하였기 때문에 값을
                    # 수정하지 않고 visited[x][y]에 저장된 값을 그대로 출력해줍니다.
            elif nx in range(m) and ny in range(n):
                if maps[nx][ny] == '.':
                    # 이동한 좌표가 영역 안에있고 지형이 '.'이라면
                    if visited[x][y] > 0 and not visited[nx][ny]:
                        # 이동하는것이 사람일 경우 방문한 적을 확인햊주고 
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                        # 시간이 1만큼 들었다고 표시를 한 후 덱에 좌표를 추가해줍니다.
                    elif visited[nx][ny] >= 0 and visited[x][y] == -1:
                        # 이동하는 것이 불일 경우 도착지가 불이 아니라면
                        visited[nx][ny] = -1
                        q.append((nx,ny))
                        # 불을 확장해주고 덱에 좌표를 지정해줍니다.
    return 'IMPOSSIBLE'
    # 덱이 비었는데 탈출하지 못하였다면 탈출할 수 없으니 'IMPOSSIBLE'을 출력해줍니다.
            

for tc in range(t):
    n, m = map(int, input().split())
    maps = []
    for i in range(m):
        maps.append(list(map(str, input())))
    # n * m 크기의 영역의 상태를 maps에 받아줍니다.
    for i in range(m):
        for j in range(n):
            if maps[i][j] == '@':
                print(escape(i, j))
                # 사람이 위치한 자리라면 함수를 작동시킨 결과를 출력해줍니다.
                break