from collections import deque

cnt = 0
while True:
    n = int(input())
    cnt += 1
    if n == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(n)]
    INF = 1e9
    visited = [[INF]*n for _ in range(n)]
    # 영역의 크기를 받아 0인지 확인하고 0이 아니라면 영역의 내용을 받고
    # 영역의 크기와 같은 가장 큰수들은 값으로 가지는 최소 줄어든값이 저장될 리스트를 만들어줍니다.
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 4방위 탐색을 지정해줍니다.
    def move(a, b):
        q = deque()
        q.append((a, b))
        visited[a][b] = maps[a][b]
        # 시작점을 받아 덱에 넣어주고 시작점의 영역값으로 방문처리를 해줍니다.
        while q :
            x, y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx in range(n) and ny in range(n):
                    if visited[nx][ny] > visited[x][y] + maps[nx][ny]:
                        visited[nx][ny] = visited[x][y] + maps[nx][ny]
                        q.append((nx, ny))
                        # 4방위 탐색을 통해 영역의 크기 안에 들어와있는지 확인하고
                        # 현재 이동하는 방법의 비용이 덜 든다면 값을 갱신해주고 덱에 좌표를 넣어줍니다.

    move(0, 0)
    cost = visited[-1][-1]
    print(f'Problem {cnt}: {cost}')
    # 함수를 작동시키고 visited의 가장 마지막의 값을 확인하여 출력해줍니다.