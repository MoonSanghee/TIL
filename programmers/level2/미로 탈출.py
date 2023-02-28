from collections import deque

def solution(maps):
    answer = 0
    open = False
    # 레버를 내려 나갈 수 있는지 여부를 False로 만들어줍니다.

    visited = [[0] *len(maps[0]) for _ in range(len(maps))]
    # 주어진 지도와 같은 크기의 방문표시할 이중리스트를 만들어줍니다.

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
                visited[i][j] = 1
                break
    # 주어진 지도를 순회하면 시작점을 찾고 방문표시를 위해 1로 만들어줍니다.

    q = deque()
    q.append((start[0], start[1]))
    # 덱에 시작좌표를 넣어줍니다.

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 이동 가능한 4방위 탐색을 설정해줍니다.

    while q:
        x, y = q.popleft()
        if maps[x][y] == 'L' and not open:
            answer += visited[x][y]
            open = True
            visited = [[0] *len(maps[0]) for _ in range(len(maps))]
            visited[x][y] = 1
            q = deque()
            q.append((x, y))
            continue
        # 레버의 위치에 도달하였는데 열리지 않은 상태라면 열렸다고 표시를 바꾸어주고 
        # answer에 레버의 위치까지 오는 데 걸린 시간을 더해주고 방문 리스트를 
        # 새로 만들어 레버의 위치를 1로 방문 표시해준 다음 덱을 비우고 
        # 레버의 위치를 넣어 while 반복문을 다시 실행해줍니다.

        if maps[x][y] == 'E' and open:
            answer += visited[x][y]
            return answer - 2
        # 문에 도달하였고 레버를 내려 문이 열려있다면 answer에 문까지 오는데 걸린
        # 시간을 더해주고 시작점을 차별화하기 위해 1을 넣어 시작하였으므로 
        # answer에 저장된 값에서 2를 뺀 값을 돌려줍니다.

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx in range(len(maps)) and ny in range(len(maps[0])):
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    # 4방향 탐색을 하며 벽('X')가 아니고 방문한적 없다면
                    # 시간이 1더 걸린다고 방문처리를 한 다음 덱에 넣어줍니다.
    answer = -1
    return answer
    # q가 비는동안 리턴된적이 없다면 탈출을 못 한다는 의미이므로 -1을 리턴하여줍니다.