r, c = map(int, input().split())
seet = []
for i in range(r):
    line = list(input())
    seet.append(line)

result = 0
alpha = set()
alpha.add(seet[0][0])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, z):
    global result
    result = max(result, z)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(r) and ny in range(c) and seet[nx][ny] not in alpha:
            alpha.add(seet[nx][ny])
            dfs(nx, ny, z + 1)
            alpha.remove(seet[nx][ny])
    return

dfs(0, 0, 1)
print(result)