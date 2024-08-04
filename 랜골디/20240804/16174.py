from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
flag = False
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 영역의 크기와 영역의 상태를 받고 같의 크기의 방문처리할 리스트를 만들어줍니다
q = deque()
q.append((0, 0))
# 큐을 만들어 시작 좌표를 넣어줍니다.
while q:
    x, y = q.popleft()
    # 큐의 왼쪽에 있는 값들을 차례로 빼서 확인합니다
    if maps[x][y] == -1:
        flag = True
        break
    # 목표에 도착하였으면 도착을 표시하고 반복을 멈추어줍니다.
    if 0 <= x + maps[x][y] < n and visited[x + maps[x][y]][y] == False:
        q.append((x + maps[x][y], y))
        visited[x + maps[x][y]][y] = True
    if 0 <= y + maps[x][y] < n and visited[x][y + maps[x][y]] == False:
        q.append((x, y + maps[x][y]))
        visited[x][y + maps[x][y]] = True
    # 아니라면 현재 자리 값만큼 이동가능한지 확인하고 이동한다음 방문처리를 해줍니다.
if flag:
    print("HaruHaru")
else:
    print("Hing")
# 목표에 도달하였는지 확인하여 결과를 출력해줍니다.