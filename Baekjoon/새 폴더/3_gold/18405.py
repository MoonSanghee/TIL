from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
virus = []
maps = [[] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        maps[i].append([line[j], 0])
        if line[j]:
            virus.append([i, j, maps[i][j][0]])
# 전체 영역의 상태를 maps이라는 2중 리스트에 virus라는 리스트에는 바이러스가 있는 위치를 모아줍니다

virus = deque(sorted(virus, key=lambda x : x[2]))
# 바이러스들을 오름차순으로 정렬시켜줍니다.

s, x, y = map(int, input().split())
# 지난 시간과 찾고자하는 위치를 받아줍니다.

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방위로 퍼져나가기에 상하좌우 4방향을 설정해줍니다.

def spread():
    while virus:
        a, b, c = virus.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b
            if nx in range(n) and ny in range(n):
                if not maps[nx][ny][0]:
                    # 4방위 이동했을때 nx, ny가 범위안에 있고
                    # 아직 도착한 적이 없다면
                    maps[nx][ny] = [maps[a][b][0], maps[a][b][1] + 1]
                    # 지도에 방문 표시를 해주고
                    virus.append([nx, ny, c])
                    # 바이러스 deque에 nx, ny, c를 다시 넣어주고 virus가 빌때까지
                    # (모든 영역에 퍼질때까지) 진행시켜줍니다.

spread()
# 정의한 함수를 실행시키고

if maps[x - 1][y - 1][1] <= s:
    print(maps[x - 1][y - 1][0])
    # 원하는 시간에 바이러스가 도착했으면 입력된 바이러스값을
else:
    print(0)
    # 아니면 0을 출력해줍니다.