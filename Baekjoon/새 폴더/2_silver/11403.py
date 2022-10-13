from collections import deque

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
check = [[0 for _ in range(n)] for _ in range(n)]

def bfs(a):
    q = deque()
    for i in range(n):
        if maps[a][i] == 1:
            q.append(i)
            check[a][i] = 1
    # 2차원 리스트의 각 줄을 확인하여 연결 상태를 이어 주기 위해 
    # 각 줄의 연결된 값을 q에 넣어주었습니다.
    while q:
        x = q.popleft()
        for i in range(n):
            if check[a][i] == 0 and maps[x][i] == 1:
                check[a][i] = 1
                q.append(i)
    # 2차원 리스트 체크는 이 줄의 자릿값이 연결됬는지 확인하고
    # 맵에서 연결된 점의 연결 점중 체크와 아직 연결 되지 않은 점이 있는지 확인해줍니다.
for i in range(n):
    bfs(i)
    # n번을 시행하며 n개의 줄의 연결 상태를 확인해 줍니다.
for i in check:
    print(*i)
    # 각 줄을 줄 안에서는 칸을 줄이 바뀌면서 줄을 바꾸어 출력하여 줍니다.