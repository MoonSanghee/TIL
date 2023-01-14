from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
# 영역의 크기 n과 m, 크기에 맞는 지도 방문표시를 해주고 값을 넣어줄 visited를 만들어줍니다.
visited[0][0][0] = 1
# visited 0, 0자리에 부수지 않고 도착했다는 의미에서 0번 인덱스 값을 1로 바꾸어줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 이동을 설정해줍니다.
def bfs(a, b, c):
    q = deque()
    q.append((a, b, c))
    # 시작좌표와 벽 뚫기를 시행했는지를 덱에 넣어줍니다.
    while q:
        x, y, broken = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]
            # 덱에서 x, y값이 목적지라면 visited에 저장한 값을 출력해줍니다.
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(n) and ny in range(m):
                # 4방향으로 이동하여 영역 안에 있는지 확인하여주고
                if maps[nx][ny] == 1 and broken == 0:
                    # 지도에서 벽이라면 벽뚫기를 시행 한 적이 없을때만 이동이 가능합니다.
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    # 이동시 visited의 nx,ny 1번 인덱스에 visited x,y 0번 인덱스값에 1을 더하여 넣어줍니다.
                    q.append((nx, ny, 1))
                    # q에 이동한 좌표와 벽을 뚫었다는것을 저장해줍니다.
                elif maps[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    # 이동할 위치가 벽이 아니고 벽 뚫기 상태가 동일할때 방문한 적이 없어야 최단 경로이므로 
                    # 방문한적이 있는지 확인해줍니다.
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append((nx, ny, broken))
                    # visited[nx][ny][broken] 값을 갱신해주고 (nx, ny, broken)을 q에 넣어줍니다.
    return -1
    # q가 비었는데 리턴된적이 없다면 목적지에 도달하지 못했다는 의미이므로 -1을 돌려줍니다.

print(bfs(0, 0, 0))
# bfs실행 결과를 출력해줍니다.