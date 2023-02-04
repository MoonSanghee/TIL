from collections import deque
from heapq import heappop, heappush

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(m)]
INF = int(1e9)
visited = [[INF] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = []
heappush(result, (0, 0, 0))
visited[0][0] = 0

while result:
    cost, x, y = heappop(result)
    if x == m - 1 and y == n - 1:
        print(cost)
        break
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if nx in range(m) and ny in range(n):
            new_cost = cost + maps[nx][ny]
            if new_cost + 1 < visited[nx][ny]:
                visited[nx][ny] = new_cost
                heappush(result, (new_cost, nx, ny))