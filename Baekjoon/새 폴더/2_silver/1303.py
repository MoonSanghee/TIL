from collections import deque
m, n = map(int, input().split())
# 가로와 세로를 받아줍니다.
maps = []
for _ in range(n):
    maps.append(list(map(str, input())))
    # 세로길이 만큼 입력받아 맵에 추가해줍니다.
visited = [[0]*m for _ in range(n)]
# 방문표시해줄 리스트를 만들어줍니다.
power = [0, 0]
# 뭉쳐있는 위력을 저장할 변수를 만들어줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방위에 연결되있는것 확인해 줄것이기때문에 설정해줍니다.
def cheer(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    # a, b를 방문처리해줍니다.
    cnt = 1
    # 얼마나 뭉쳐있는지 표시해줄 변수를 만들어줍니다
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(m):
                if not visited[nx][ny] and maps[x][y] == maps[nx][ny]:
                    visited[nx][ny] = 1
                    cnt += 1
                    # 4방위 탐색결과 범위안에 있고 방문한 적 없으면서 이동 전과 후
                    # 병사가 같으면 방문표시하고 cnt를 증가시키고 q에 좌표를 넣어줍니다. 
                    q.append((nx, ny))
    return cnt**2
    # 뭉쳐있는 병사의 제곱한 값을 돌려줍니다.

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if maps[i][j] == 'W':
                power[0] += cheer(i, j)
            else:
                power[1] += cheer(i, j)
            # 맵을 전부 확인하면서 방문한 적이 없으면 아군일 경우 power의 0번 인덱스에
            # 함수를 작동시킨 결과를 넣어주고 적이면 1번 인덱스에 넣어줍니다.
print(*power)
# 각 값을 출력해줍니다.