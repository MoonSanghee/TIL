from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
seet = []
for i in range(n):
    seet.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m) and check[nx][ny] != 0:
                check[nx][ny] = 0
                q.append((nx, ny))
cnt = 0
check = [[0 for _ in range(m)] for _ in range(n)]
while True:
    cnt += 1
    for i in range(n):
        for j in range(m):
            zero = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx in range(n) and ny in range(m) and seet[nx][ny] == 0:
                    zero += 1
            if seet[i][j] > zero:
                check[i][j] = seet[i][j] - zero
    for i in range(n):
        for j in range(m):
            seet[i][j] = check[i][j]
    block = 0
    for i in range(n):
        for j in range(m):
            if check[i][j] != 0:
                check[i][j] = 0
                bfs(i, j)
                block += 1
    if block == 0:
        print(0)
        break
    elif block > 1:
        print(cnt)
        break