n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 영역의 상태를 받아줍니다.
p = []

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            p.append((i, j))
# 영역을 순회하며 경로의 출발과 도착을 받아줍니다.
print(abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]))
# 두 좌표간의 거리를 출력해줍니다.