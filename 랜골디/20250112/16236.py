from collections import deque

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기를 받고 최초 영역의 상태를 받아줍니다

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            shark = (i, j)
# 상어의 위치를 받아줍니다
size = 2
need = 2
time = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
# 상어의 성장 상태와 시간을 담을 변수를 설정하고 탐색 가능한 4방향을 설정해줍니다

def search():
    global shark, time, need, size
    visited = [[0] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = 1
    # 주어지는 영역의 크기와 같은 방문 처리할 리스트를 만들어주고 상어의 위치를 표시해줍니다
    fish = []
    # 영역을 탐색하여 먹이를 먹을 수 있다면 먹이의 위치를 담을 리스트를 만들어줍니다
    q = deque()
    q.append(shark)
    # 이동을 담을 큐를 만들고 상어의 위치를 넣어줍니다
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    # 4방향 탐색을 통해 이동 가능하고 방문 한 적 없는지 확인해줍니다
                    if maps[nx][ny] == 0 or maps[nx][ny] == size:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        # 영역에서 물고기가 없거나 상어의 크기와 같아 이동만 가능하다면 이동만 표시하고 큐에 값을 넣어줍니다
                    elif maps[nx][ny] < size and maps[nx][ny] != 0:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        fish.append((visited[nx][ny], nx, ny))
                        # 영역에서 물고기를 먹을수 있는 위치라면 이동을 표시하고 먹이 리스트에 정보를 담고 큐에 값을 넣어줍니다
    
    if fish:
        fish.sort(key = lambda x : (x[0], x[1], x[2]))
        target = fish[0]
        # 먹을수 있는 물고기가 존재한다면 거리, 상하 좌우 순으로 정렬을 실행해줍니다
        time += target[0] - 1
        maps[shark[0]][shark[1]] = 0
        maps[target[1]][target[2]] = 9
        shark = (target[1], target[2])
        # 물고기까지 걸리는 시간을 더해주고 상어가 있던 자리는 0으로 타겟이 있는 자리는 9로 바꾼후 상어의 위치 정보를 바꾸어줍니다
        need -= 1
        if need == 0:
            size += 1
            need = size
        # 먹이를 먹고 상어의 성장을 실행해줍니다
        search()
        # 재귀를 통해 먹을수있는 물고기가 더 있는지 확인해줍니다
    
search()
print(time)