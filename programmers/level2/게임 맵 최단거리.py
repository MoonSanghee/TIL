from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    # 표시된 영역의 크기와 같은 방문처리를 할 리스트를 만들어줍니다.
    visited[0][0] = 1
    # 시작점을 1로 바꾸어줍니다.
    bfs(0, 0, maps, visited)
    # bfs를 통해 목적지를 도달할 수 있는지 확인해줍니다.
    if visited[-1][-1]:
        return visited[-1][-1]
    else:
        return -1
    # 도달했다면 걸린 비용, 아니라면 -1을 출력해줍니다.

def bfs(a, b, maps, visited):
    q = deque()
    q.append((a, b))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # q에 시작좌표를 넣고 4방위를 설정해줍니다.
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(len(maps)) and ny in range(len(maps[0])):
                if maps[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    # q에서 꺼낸 값을 기준으로 4방위를 탐색하여
                    # 방문한 적이 없고 갈 수 있는지 확인해줍니다.
                    # 조건에 맞다면 비용이 1만큼 더 든다고 표시해주고
                    # q에 이동한 좌표를 넣어줍니다.