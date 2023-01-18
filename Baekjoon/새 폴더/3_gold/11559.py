from collections import deque

maps = []
for i in range(12):
    maps.append(list(map(str, input())))
maps = maps[::-1]
result = 0
# 현재 뿌요가 놓인 상태를 받고 실행횟수를 저장해줄 변수를 만들어줍니다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 4방 탐색을 설정해줍니다.
def chain(a, b, c):
    q = deque()
    q.append((a, b))
    pang = deque()
    pang.append((a, b))
    # 연결을 확인해나갈 q와 연결 길이를 확인할 pang을 deque으로 받아줍니다.
    visited = [[False]*6 for _ in range(12)]
    visited[a][b] = True
    # 시작점을 방문 표시해줍니다.
    cnt = 1
    flag = 0
    # 연결 길이가 팡이 일어나는지 세줄 변수와 표시해줄 변수를 만들어줍니다.
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(12) and ny in range(6):
                if maps[nx][ny] == c and not visited[nx][ny]:
                    q.append((nx, ny))
                    pang.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
                    # 4방 탐색을하며 pang에도 값을 넣어주고 방문 표시를 해줍니다.

    if cnt >= 4:
        flag = 1
        for x, y in pang:
            maps[x][y] = '.'
    # 길이가 4이상이라면 연쇄가 일어나므로 pang 안에 있는 좌표에 위치한 값들을 '.'으로 바꾸어줍니다.
    return flag

def gravity():
    for y in range(6):
        q = deque()
        for x in range(12):
            if maps[x][y] != '.':
                q.append(maps[x][y])
        for x in range(12):
            if q:
                maps[x][y] = q.popleft()
            else:
                maps[x][y] = '.'
    # 각줄에 남은 뿌요들을 확인하고 가장 아래부터 쌓은후 남은 칸은 '.'으로 채워주는
    # 함수를 만들어줍니다.
 
while True:
    count = 0
    for i in range(12):
        for j in range(6):
            if maps[i][j] != '.':
                count += chain(i, j, maps[i][j])
                # 모든 칸을 확인하며 뿌요가 놓여있다면 팡이 일어나는지 확인하고
    if count == 0:
        print(result)
        break
    # 일어나지 않았다면 연쇄가 일어난 횟수를 출력해주고
    else:
        result += 1
    gravity()
    # 일어났다면 연쇄를 1 추가해주고 뿌요들을 아래부터 메꾸어줍니다.