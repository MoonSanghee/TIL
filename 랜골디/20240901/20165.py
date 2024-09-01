from collections import deque

n, m, r = map(int, input().split())
# 도미노의 크기와 게임을 진행할 라운드를 받아줍니다.
domino = [list(map(int, input().split())) for _ in range(n)]
isStanding = [['S' for _ in range(m)] for _ in range(n)]
# 도미노의 크기와 상태를 각각 이중리스트에 담아줍니다.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
# 4방향과 도미노를 넘어뜨리고 획득한 점수를 담을 변수를 설정해줍니다
for _ in range(r):
    x, y, v = input().split()
    x, y = int(x) - 1, int(y) - 1
    if v == 'N':
        v = 3
    elif v == 'S':
        v = 2
    elif v == 'E':
        v = 0
    else:
        v = 1
    # 공격시 주어지는 세 변수를 받고
    # 주어지는 변수를 정수형 좌표와 설정한 dx, dy에 따라 방향으로 맞추어줍니다.
    q = deque()
    if isStanding[x][y] == 'S':
        q.append((x, y))
    # 좌표의 도미노가 서있다면 큐에 담아줍니다.
    while q:
        x, y = q.popleft()
        isStanding[x][y] = 'F'
        result += 1
        # 도미노를 넘어뜨린 표시를하고 점수를 획득합니다.
        for i in range(1, domino[x][y]):
            nx = x + dx[v] * i
            ny = y + dy[v] * i
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in q and isStanding[nx][ny] == 'S':
                    q.append((nx, ny))
            # 방향을 확인하고 연속해서 넘어져야하는 도미노를 큐에 담아줍니다.
    x2, y2 = map(int, input().split())
    isStanding[x2 - 1][y2 - 1] = 'S'
    # 세울 도미노의 좌표를 받고 도미노를 세워줍니다.

print(result)
# 점수를 출력해줍니다.
for i in isStanding:
    print(*i)
# 이어서 도미노의 형태를 줄별로 출력해줍니다.