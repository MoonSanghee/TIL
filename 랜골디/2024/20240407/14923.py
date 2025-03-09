from collections import deque
# collections라이브러리에서 deque을 불러와줍니다.
n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
hx, hy, ex, ey = hx - 1, hy -1, ex - 1, ey - 1
maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 출발 위치 목적지를 받고 인덱스값과 좌표값을 매칭하기위해 출발값과 목표값의 x, y 값에서 1씩을 빼줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 탐색을 설정해줍니다.
def bfs():
    q = deque()
    q.append((hx, hy, 0, 1))
    # 덱을 생성하고 시작 좌표와 이동하는데 걸린 시간 마법을 쓸 수 있는 상태인지를 담아줍니다.
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    visited[hx][hy][1] = True
    # 영역의 크기와 맞게 마법을 사용했을때와 안 했을때 방문을 처리해줄 visited 리스트를 만들고 시작 좌표를 방문처리해줍니다.
    while q:
        x, y, cnt, wand = q.popleft()
        if x == ex and y == ey:
            return cnt
            # 목적지에 도달하였다면 걸린 시간을 출력해줍니다.
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny][wand]:
                    if maps[nx][ny] == 1 and wand == 1:
                        visited[nx][ny][0] = True
                        q.append((nx, ny, cnt + 1, 0))
                    elif maps[nx][ny] == 0:
                        visited[nx][ny][wand] = True
                        q.append((nx, ny, cnt + 1, wand))
                    # 4방향 탐색을 통해 이동이 가능하면 이동을 표시하고 덱에 담아줍니다.
    return -1
    # 목적지에 도달하지 못하였다면 -1을 출력하므로 -1을 return해줍니다
print(bfs())
# 함수를 실행시키고 결과를 출력해줍니다.