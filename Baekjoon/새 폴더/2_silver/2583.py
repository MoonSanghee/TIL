from collections import deque

m, n, k = map(int,input().split())
maps = [[0 for _ in range(n)] for _ in range(m)]

def pill(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            maps[j][i] = 1
            # k번 입력받을 삼각형의 영역만큼 표시해줄 함수를 정의함.

for i in range(k):
    a, b, c, d = map(int, input().split())
    pill(a, b, c, d)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b):
    cnt = 1
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(m) and ny in range(n) and maps[nx][ny] == 0:
                maps[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1
    return cnt
    # 칠해지지 않고 연결된 영역의 크기를 bfs로 정의해줌.
result = []
for i in range(m):
    for j in range(n):
        if not maps[i][j]:
            maps[i][j] = 1
            result.append(bfs(i, j))
            # bfs의 결과물을 result라는 빈 리스트에 넣어줌

result.sort()
# 작은 영역의 크기부터 출력하므로 오름차순으로 정렬해주고
print(len(result))
print(*result)
# 영역의 개수와 각 영역의 크기를 순서대로 출력해줌.