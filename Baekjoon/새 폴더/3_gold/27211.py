n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
# 영역의 크기와 영역의 상태를 입력받아줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방위 이동을 설정해줍니다.
def walk(a, b):
    stack = []
    stack.append((a, b))
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx == n:
                nx = 0
            elif nx < 0:
                nx = n - 1
            elif ny == m:
                ny = 0
            elif ny < 0:
                ny = m - 1
            # 도넛형으로 연결되어있으므로 범위보다 커지면 0으로 돌아가고
            # 0보다 작아지면 뒤 영역으로 돌아가줍니다.
            if not maps[nx][ny]:
                maps[nx][ny] = 1
                stack.append((nx, ny))
            # 이동한 자리가 연결되어 있으면 이동해줍니다.
            # 이를 통해 연결된 모든 영역을 탐험해줍니다.
cnt = 0
for i in range(n):
    for j in range(m):
        if not maps[i][j]:
            walk(i, j)
            cnt += 1
            # 탐험이 가능하면 횟수를 더해줍니다.

print(cnt)
# 몇 번의 탐험이 되는지 확인해줍니다.