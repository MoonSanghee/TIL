from collections import deque

t = int(input())
# 테슽트의 개수를 받아줍니다.
for tc in range(t):
    h, w = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    cnt = 0
    # 높이와 너비를 받고 영역을 받은뒤 cnt를 0으로 설정해줍니다

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx in range(h) and ny in range(w):
                    if maps[nx][ny] == '#':
                        maps[nx][ny] = '.'
                        q.append((nx, ny))
    # 4방향 탐색을 통해 연결된 무리를 전부 확인하였다고 표시해줍니다.
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '#':
                cnt += 1
                bfs(i, j)
    # 영역을 탐색하며 양이 있다면 함수를 실행시키고 무리를 1 더해줍니다.
    print(cnt)
    # 몇 개의 무리가 있는지 출력해줍니다.