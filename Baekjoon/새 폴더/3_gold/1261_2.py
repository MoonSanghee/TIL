from collections import deque
from heapq import heappop, heappush

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(m)]
INF = int(1e9)
visited = [[INF] * n for _ in range(m)]
# 영역과 방문 확인을 표시할 리스트를 만들어줍니다,
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방위 이동을 지정해줍니다.
result = []
heappush(result, (0, 0, 0))
visited[0][0] = 0
# 현재 위치까지 벽을 얼마나 부수었는지와 x, y좌표를 튜플로 묶어 heappush해줍니다.
while result:
    cost, x, y = heappop(result)
    if x == m - 1 and y == n - 1:
        print(cost)
        # x, y가 목적지라면 부순 벽의 횟수를 출력해줍니다.
        break
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx in range(m) and ny in range(n):
            new_cost = cost + maps[nx][ny]
            # 현재까지 부순 벽의 수에 이동하는데 필요한 벽을 더하여 new_cost라 정하고
            if new_cost < visited[nx][ny]:
                visited[nx][ny] = new_cost
                heappush(result, (new_cost, nx, ny))
                # new_cost가 현재 저장된 부수어야하는 벽보다 적다면 값을 갱신하고
                # 현 좌표에 도착하기위해 최소로 부수어야하는 벽의 수를 갱신해주고
                # heappush로 부순 벽의 수와 좌표를 넣어줍니다. 