n = int(input())
maps = [list(map(str, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

check = [[0 for _ in range(n)] for _ in range(n)]
def dfs(x, y):
    stack = []
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(n) and maps[x][y] == maps[nx][ny] and check[nx][ny] == 0:
                check[nx][ny] = 1
                stack.append((nx, ny))
normal = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            dfs(i, j)
            normal += 1
print(normal, end=' ')
#  정상인이 보이는 구역의 수를 먼저 확인하고

for i in range(n):
    for j in range(n):
        if maps[i][j] == 'R':
            maps[i][j] = 'G'
        check[i][j] = 0
# 적녹색약으로 보이는 결과물로 바꾸어 준 다음

handi = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            dfs(i, j)
            handi += 1
print(handi)
# 적녹색약으로 보이는 결과물의 구역 수를 확인해 주었습니다.