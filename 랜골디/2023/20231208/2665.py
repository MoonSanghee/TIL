from collections import deque

n = int(input())
sheet = [list(input()) for _ in range(n)]
# 지도의 크기와 상태를 받아줍니다.
visited = [[1e9] * n for _ in range(n)]
visited[0][0] = 0
# 모든 방을 방문한 적 없다고 가장 큰 수를 넣고 출발점을 0으로 방문처리 해줍니다.

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방향 이동을 설정해줍니다.

queue = deque([(0, 0, 0)])
# 시작점과 벽을 깬 수를 q에 담아줍니다.
while queue:
    x, y, cnt = queue.popleft()
    # 좌표와 벽을 깬 횟수를 q에서 빼줍니다.

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 4방향 탐색을 통해 이동가능한지 확인해줍니다.
            if sheet[nx][ny] == '1':
                if visited[nx][ny] > cnt:
                    visited[nx][ny] = cnt
                    queue.append((nx, ny, cnt))
                    # 벽을 깰 필요가 없다면 visted[nx][ny]에 최소 벽 깨어 도달하는 횟수와 비교하여 갱신하여줍니다.
            else:
                if visited[nx][ny] > cnt + 1:
                    visited[nx][ny] = cnt + 1
                    queue.append((nx, ny, cnt + 1))
                    # 깰 필요가 있는경우 cnt에 1을 더한 횟수와 비교하여 값을 갱신하여줍니다.

print(visited[-1][-1])
# 도착점에 최소로 벽을 깨고 도달할 때 깨야하는 벽의 수를 출력해줍니다.