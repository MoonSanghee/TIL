from heapq import heappop, heappush

cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(a,b):
    heap = []
    heappush(heap, (maps[a][b], a, b))
    while heap:
        cost, x, y = heappop(heap)

        if visited[x][y] < cost:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(n) and ny in range(n):
                new_cost = cost + maps[nx][ny]
                if visited[nx][ny] > new_cost:
                    visited[nx][ny] = new_cost
                    heappush(heap, (new_cost, nx, ny))


while True:
    n = int(input())
    cnt += 1
    if n == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(n)]
    INF = 1e9
    visited = [[INF]*n for _ in range(n)]

    move(0, 0)

    print(f'Problem {cnt}: {visited[-1][-1]}')