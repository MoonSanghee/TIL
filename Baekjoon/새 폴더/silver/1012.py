import sys
sys.stdin = open('test.txt', 'r')

test = int(input())
for i in range(test):
    m,n,k = list(map(int, input().split()))
    maps =[]
    for i in range(m):
        line = []
        for j in range(n):
            line.append(0)
        maps.append(line)

    for i in range(k):
        a, b = map(int, input().split())
        maps[a][b] = 1


    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    def dfs(i, j):
        stack = list()
        stack.append([i, j])

        while stack:
            x, y = stack.pop()
            for i in range(4):
                ni = x + di[i]
                nj = y + dj[i]
                if ni in range(m) and nj in range(n):
                    if maps[ni][nj] == 1:
                        maps[ni][nj] = 0
                        stack.append([ni, nj])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)