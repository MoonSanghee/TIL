from collections import deque
import sys

input = sys.stdin.readline
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 주어지는 영역의 크기와 이동 가능한 인구차이 범위를 받고 영역의 상태를 받아줍니다
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 인접한 4방향을 탐색도록 설정해줍니다
def bfs(x, y):
    q = deque()
    group = [(x, y)]
    total = A[x][y]
    q.append((x, y))
    # bfs 탐색을 위한 덱 자료구조와 인구가 이동할 영역 담을 리스트를 만들고 주어지는 좌표를 받아줍니다
    # 영역의 인구 합을 담을 변수도 설정해줍니다
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == False:
                    if L <= abs(A[x][y] - A[nx][ny]) <= R:
                        # 주어진 좌표에서 4방향 탐색을 하며 영역을 벗어나지 않고 방문한적 없으면 인구가 이동가능한지 확인해줍니다
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        group.append((nx, ny))
                        total += A[nx][ny]
                        # 영역의 방문 처리를 해주고 덱과 그룹에 좌표를 더한후 영역의 값을 더해줍니다
    if len(group) <= 1:
        return False
        # 영역의 길이가 1 이하라면 이동할 수 있는 인구가 없으므로 False를 리턴해줍니다
    else:
        for x, y in group:
            A[x][y] = total // len(group)
        return True
        # 영역이 1을 넘는다면 주어진 영역의 인구 평균으로 값을 수정해주고 True를 리턴해줍니다 

result = 0
# 며칠간 진행되는지 담을 변수를 설정해줍니다
while True:
    stop = 0
    # 이동이 일어났는지 확인하기위한 변수를 설정해줍니다
    visited = [[False] * N for _ in range(N)]
    # 영역을 사용하였는지 확인할 변수를 만들어줍니다
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                stop += bfs(i, j)
                # 방문한 적 없는 영역에서 함수를 실행시켜 결과를 더해줍니다
    if stop == 0:
        break
    result += 1
    # 이동이 일어나지 않았다면 반복을 멈추고 발생하였다면 하루가 지났음을 표시하고 반복을 진행해줍니다

print(result)
# 결과를 출력해줍니다