from collections import deque

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 테스트케이스의 개수와 4방향 이동을 설정해줍니다
for t in range(T):
    n = int(input())
    # 주어지는 영역의 크기를 받아줍니다
    maps = []
    visited = [[False] * n for _ in range(n)]
    start = deque()
    # 주어지는 형태를 받고 방문 처리할 변수와 시작점을 담을 변수를 설정해줍니다
    for i in range(n):
        line = list(input())
        maps.append(line)
        if '3' in line:
            for j in range(n):
                if line[j] == '3':
                    target = [i, j]
                    break
        
        if '2' in line:
            for j in range(n):
                if line[j] == '2':
                    start.append((i, j))
                    visited[i][j] = True
                    break
        # 각 줄을 받아 지도에 넣고 시작점이나 목표점인지 확인해줍니다
    while start:
        x, y = start.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and maps[nx][ny] != '1':
                    start.append((nx, ny))
                    visited[nx][ny] = True
    # 시작점부터 4방향 탐색을 통해 방문한적이 없고 이동가능한 모든 좌표를 탐색해줍니다
    if visited[target[0]][target[1]] == True:
        print(f'#{t + 1} 1')
    else:
        print(f'#{t + 1} 0')
    # 목적지에 도달하였는지 확인하여 결과를 출력해줍니다