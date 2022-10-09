t = int(input())
for _ in range(t):
    n, m, l = map(int, input().split())
    seet = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(l):
        i, j = map(int, input().split())
        seet[i][j] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def dfs(a, b):
        stack = []
        stack.append([a, b])
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx in range(n) and ny in range(m) and seet[nx][ny] == 1:
                    stack.append([nx, ny])
                    seet[nx][ny] = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if seet[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)