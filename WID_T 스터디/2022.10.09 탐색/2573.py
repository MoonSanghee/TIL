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
                # 연결된 빙산 덩어리 확인
cnt = 0
# 지나간 연수 확인
check = [[0 for _ in range(m)] for _ in range(n)]
# 녹은 결과를 기록
while True:
    cnt += 1
    # 1년마다 cnt 값 증가
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
                # 위치 기준 4방위 탐색으로 얼마나 녹는지 확인하여 결과 기록
    for i in range(n):
        for j in range(m):
            seet[i][j] = check[i][j]
            # 녹은 상태 적용
    block = 0
    # 연결된 덩어리 확인
    for i in range(n):
        for j in range(m):
            if check[i][j] != 0:
                check[i][j] = 0
                bfs(i, j)
                block += 1
    if block == 0:
        print(0)
        break
    # 연결된 덩이가 없으면 한 번에 다 녹아 없어졌으므로 쪼개어 지지 않으므로 0 출력
    elif block > 1:
        print(cnt)
        break
        # 덩어리가 2개 이상이라면 기록해둔 지난 햇수 출력