from collections import deque
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    # 모든 높이가 주어진 정보를 받고 모든 경로로 이동하는데 드는 비용을 담을 변수를 만들어줍니다
    sheet = [list(map(int, input().split())) for _ in range(n)]
    cost = [[1e9] * n for _ in range(n)]
    # 시작점의 비용을 초기화하고 4방향 이동을 설정한 뒤 큐에 시작점을 넣어줍니다
    cost[0][0] = 0
    q = deque()
    q.append((0, 0))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 큐의 가장 앞의 값을 빼서 4방향 탐색을 통해 이동할 수 있다면 현재 위치에서 이동하였을때 비용을 
    # 확인해 비용이 줄어든다면 비용값을 갱신하고 큐에 넣어줍니다
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                extra = sheet[nx][ny] - sheet[x][y]
                extra = max(extra, 0)
                if cost[nx][ny] > cost[x][y] + extra + 1:
                    cost[nx][ny] = cost[x][y] + extra + 1
                    q.append((nx, ny))
    # 결과를 출력해줍니다
    print(f'#{tc} {cost[-1][-1]}')