n, d = map(int, input().split())
# 지름길의 개수와 목표지점을 받아줍니다.

dis = [i for i in range(d + 1)]
# 각 거리에 도달하는 시간을 각 거리만큼으로 정해줍니다.

shorts = [list(map(int, input().split())) for _ in range(n)]
# 시작, 끝 지점과 드는 시간을 리스트로 받아 shorts 리스트에 넣어줍니다.

for i in range(d + 1):
    if i > 0:
        dis[i] = min(dis[i], dis[i - 1] + 1)
    # 각 거리까지를 확인하며 시작점이 아닌경우 이 전 위치에 지름길을 통해 시간을
    # 단축시켰는지 확인하고 단축 시켰으면 현재 위치까지 드는 시간을 지름길을 이용해
    # 갱신한 시간에 1을 더한 값으로 바꾸어줍니다.
    for s, e, c in shorts:
        if s == i and e <= d and dis[i] + c < dis[e]:
            dis[e] = dis[i] + c
        # 각 지점에서 지름길을 확인하여 지름길의 시작 위치라면 도착 위치가
        # 목표지점을 벗어나지 않는지 확인해주고 지름길을 이용해 이동하는 시간이 더
        # 짧아지는지 확인해주고 이용하는게 좋다면 지름길을 사용한 값으로
        # 도착위치까지 걸리는 시간을 변경하여줍니다.
print(dis[d])
# 마지막에 걸린 시간을 출력하여줍니다.