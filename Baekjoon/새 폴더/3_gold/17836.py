from collections import deque
n, m, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 지도를 받아줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 탐색을 정의합니다.

def gram(a, b):
    # 검을 찾아 걸리는 시간을 확인하는 함수입니다.
    global t
    q = deque()
    q.append((a, b, 0))
    visited = [[0]*m for _ in range(n)]
    visited[a][b] = 1
    # q라는 이름으로 덱을 만들어주고 영역의 크기와 같은 방문처리할 리스트를 만들어줍니다.
    while q:
        x, y, cnt = q.popleft()
        if maps[x][y] == 2:
            return cnt + (n + m - x - y - 2)
        # 검의 위치에 도달하였다면 검의 위치까지 걸리는 시간에 공주의 x, y 좌표에서 검의 x, y 좌표를
        # 빼준값을 더해줍니다.
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(n) and ny in range(m):
                if maps[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))
                    # 4방향 탐색을 통해 방문한적이 없고 벽이 아니라면 1의 시간이 더 걸린다고 표시하여 방문처리합니다.
    return t + 1
    # 검의 위치에 도달하지 못했다면 제한 시간 밖의 수를 돌려줍니다

def princess(a, b):
    # 공주 위치까지 바로 이동하는 함수입니다.
    global t
    q = deque()
    q.append((a, b, 0))
    visited = [[0]*m for _ in range(n)]
    visited[a][b] = 1
    # q라는 이름으로 덱을 만들어주고 영역의 크기와 같은 방문처리할 리스트를 만들어줍니다.
    while q:
        x, y, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt
        # 공주의 위치에 도착했으면 걸린 시간을 반환해줍니다.
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(n) and ny in range(m):
                if maps[nx][ny] != 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))
                    # 4방위 탐색을 통해 영역의 크기 안에있고
                    # 벽이 아니고 방문한 적이 없으면 방문 처리를 해주고
                    # q에 시간이 1만큼 더 들었다는 표시와 함께 q에 넣어줍니다.
    return t + 1
    # q에 값이 없는데 공주에게 도달하지 못했다면 제한시간보다 큰 숫자를 돌려줍니다.

p = princess(0, 0)
g = gram(0, 0)
result = min(p, g)
# 검을 찾고 공주에 도달하는 방법과 바로 도달하는 방법중 작은 수를 결과로 설정하고
if result <= t:
    print(result)
    # 제한시간 안이라면 값을 출력해주고
else:
    print('Fail')
    # 제한시간보다 더 걸린다면 'Fail'을 출력해줍니다.