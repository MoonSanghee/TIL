n, m, h = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 시작 체력, 회복하는 체력을 받고 영역의 상태를 받아줍니다.
milkSpots = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            start = (i, j)
        elif maps[i][j] == 2:
            milkSpots.append((i, j))
# 초코우유가 위치한 자리를 빈 리스트에 담아주고 시작 좌표를 확인해줍니다.
visited = [False for _ in range(len(milkSpots))]
# 방문을 확인할 리스트를 만들어줍니다.
result = 0
# 우유를 몇개나 마실수 있는지 담을 변수를 설정해줍니다.
def move(x, y, depth, left):
    global result
    for i in range(len(milkSpots)):
        distance = abs(milkSpots[i][0] - x) + abs(milkSpots[i][1] - y)
        if not visited[i] and distance <= left:
            visited[i] = True
            move(milkSpots[i][0], milkSpots[i][1], depth + 1, left - distance + h)
            visited[i] = False
        # 초코우유가 위치한 자리를 순회하며 도달할수 있고 아직 간 적 없는 자리라면 이동하여 초코우유를 먹는다고 표시한 다음 재귀를 실행해줍니다.
    if abs(start[0] - x) + abs(start[1] - y) <= left:
        result = max(result, depth)
        # 현재 위치에서 시작점으로 돌아갈 수 있는지 확인하고 먹은 우유의 수를 비교하여 최대값을 갱신해줍니다.

move(start[0], start[1], 0, m)
print(result)
# 함수를 실행하고 우유를 몇개나 마실 수 있는지 확인해줍니다.