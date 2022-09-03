# import sys
# sys.stdin = open('test.txt', 'r')

size = int(input())
maps = []
for _ in range(size):
    sen = list(str(input()))
    line = []
    for j in range(size):
        line.append(int(sen[j]))
    maps.append(line)
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j):
    stack = list()
    stack.append([i, j])
    cnt = 1

    while stack:
        x, y = stack.pop()
        for d in range(4):
            ni = x + di[d]
            nj = y + dj[d]
            if ni in range(size) and nj in range(size):
                if maps[ni][nj] == 1:
                    maps[ni][nj] = 0
                    cnt += 1
                    stack.append([ni, nj])
    return cnt
connect = []
for i in range(size):
    for j in range(size):
        if maps[i][j] == 1:
            maps[i][j] = 0
            connect.append(dfs(i, j))
connect = sorted(connect)
print(len(connect))
for i in connect:
    print(i)