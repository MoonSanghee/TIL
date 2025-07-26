R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
# 주어지는 지도의 크기를 받고 지도를 받아줍니다
counts = [[0 for _ in range(C)] for _ in range(R)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 각 영역이 바다와 인접한 면이 몇개인지 담을 리스트와 4방향 탐색을 위한 방향을 잡아줍니다
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'X':
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 0 <= nx < R and 0 <= ny < C:
                    if maps[nx][ny] == '.':
                        counts[i][j] += 1
                else:
                    counts[i][j] += 1
        # 모든 영역을 순회하며 인접한 영역이 섬이 아니라면 바다를 1만큼 더해줍니다
        # 확인하는 영역이 지도 밖을 벗어났다면 바다이므로 바다라고 표시된것처럼 1을 더해줍니다
for i in range(R):
    for j in range(C):
        if counts[i][j] >= 3:
            maps[i][j] = '.'
# 인접한면을 확인하는 리스트를 순회하며 잠길 섬을 수정해줍니다
RS, RE, CS, CE = R, 0, C, 0
# 새로 만들 지도의 영역을 담을 변수를 설정해줍니다
for i in range(R):
    for j in range(C):
        if maps[i][j] == 'X':
            RS = min(RS, i)
            CS = min(CS, j)
            RE = max(RE, i + 1)
            CE = max(CE, j + 1)
# 모든 영역을 순회하며 섬이 존재하는 곳이라면 현재 좌표가 새로 만들 지도에 들어가도록 값을 갱신해줍니다
for i in range(RS, RE):
    for j in range(CS, CE):
        print(maps[i][j], end='')
    print()
# 새로 만든 지도를 출력해줍니다