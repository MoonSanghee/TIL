from collections import deque
t = int(input())
# 테스트를 몇 번 시행할지 받아줍니다.
for tc in range(t):
    n = int(input())
    # 영역의 크기를 받아줍니다.
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    # 시작점과 목적지를 받아줍니다.
    visited = [[False]*n for _ in range(n)]
    # 방문 확인을 할 영역의 크기와 같은 리스트를 만들어줍니다.
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    # 나이트의 이동 방향을 설정해줍니다.
    def move(a, b, c):
        q = deque()
        q.append((a, b, c))
        # q라는 이름의 deque을 만들고 좌표와 이동 횟수를 넣어줍니다.
        while q:
            x, y, cnt = q.popleft()
            if [x, y] == target:
                return cnt
                break
            # x, y의 좌표가 목적지이면 이동 횟수를 돌려줍니다.
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx in range(n) and ny in range(n):
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny, cnt + 1))
                        # 각 자리에서 나이트의 이동가능한 8방향 이동을 실행했을때
                        # 방문한 적이 있는지 확인하고 방문한 적이 없다면 좌표와
                        # 이동을 얼마만큼하고 도착했는지를 q에 넣어줍니다.
    print(move(start[0], start[1], 0))
    # 함수를 작동한 결과 돌려받은 이동 횟수를 돌려받습니다.