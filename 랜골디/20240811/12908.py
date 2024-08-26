xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
# 출발 좌표와 도착 좌표를 받아줍니다.
def simulate(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])
# 두 좌표를 점프로 이동하는데 걸리는 시간을 계산하는 함수를 만들어줍니다.
points = []
points.append((xs, ys))
time = [[1e9 for _ in range(8)] for _ in range(8)]
# 출발, 도착 좌표와 텔레포트 할 수 있는 좌표를 담을 리스트를 만들고 
# 각 좌표간 시간이 얼마나 걸리는지 담을 2중리스트를 만들어줍니다.
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    points.append((x1, y1))
    points.append((x2, y2))
    time[len(points) - 1][len(points) - 2] = min(simulate((x1, y1), (x2, y2)), 10)
    time[len(points) - 2][len(points) - 1] = time[len(points) - 1][len(points) - 2]
    # 텔레포트 좌표를 받고 텔레포트 하는 시간과 점프해서 이동하는 경우를 비교해서 시간이 짧은쪽을 담아줍니다.

points.append((xe, ye))
# 도착 좌표를 담아줍니다.
time[0][7] = simulate(points[0], points[7])
time[7][0] = time[0][7]
# 시작 좌표에서 점프를 통해 도착 좌표에 도달하는 시간을 확인해줍니다.
for i in range(8):
    for j in range(8):
        time[i][j] = min(time[i][j], simulate(points[i], points[j]))
# 출발, 도착 좌표와 각 텔레포트 좌표간의 점프를 통해 이동하는데 필요한 최소 시간을 갱신해줍니다.
for k in range(8):
    for i in range(8):
        for j in range(8):
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])
# 각 좌표간 텔레포트를 이용하여 도착하는 시간과 비교해 최단 시간을 갱신해줍니다.
print(time[0][7])
# 결과를 출력해줍니다.