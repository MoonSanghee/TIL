from collections import deque

n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 영역의 크기와 상태를 받고 각 영역의 방문을 확인할 리스트를 만들어줍니다.
q = deque()
# 이동을 시작할 좌표를 담을 q를 만들어줍니다.
q.append((0,0))
visited[0][0] = True
# q에 시작 좌표를 넣고 방문처리를 해줍니다.
while q:
    x, y = q.popleft()
    if x == n - 1 and y == n - 1:
        print("HaruHaru")
        break
    # 목적지에 도달한다면 정해진 출력을하고 반복을 멈추어줍니다.
    nx, ny = x + maps[x][y], y + maps[x][y]
    # 목적지에 도달하지 못했다면 각 자리에서 이동할 위치를 받고
    if ny < n:
        if visited[x][ny] == False:
            q.append((x, ny))
            visited[x][ny] = True

    if nx < n:
        if visited[nx][y] == False:
            q.append((nx, y))
            visited[nx][y] = True
    # 이동할 수 있는지 확인하여 q에 담아줍니다.
else:
    print("Hing")
    # 반복을 마쳤을때 목적지에 도달하지 못했다면 Hing을 출력해줍니다.