n = int(input())
mat = []
check = []
mx = 2
mn = 100
for i in range(n):
    line = list(map(int, input().split()))
    mat.append(line)
    mx = max(max(line), mx)
    mn = min(min(line), mn)

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i, j, high):
    stack = list()
    stack.append((i, j))
    check[i][j] = 1

    while stack:
        x, y = stack.pop()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if ni in range(n) and nj in range(n):
                if mat[ni][nj] >= high and check[ni][nj] == 0:
                    check[ni][nj] = 1
                    stack.append((ni, nj))
result = 0
for high in range(mn, mx + 1):
    check = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        check.append(l)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] >= high and check[i][j] == 0:
                cnt += 1
                dfs(i, j, high)
    result = max(result, cnt)
print(result)