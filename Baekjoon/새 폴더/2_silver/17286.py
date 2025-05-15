points = [list(map(int, input().split())) for _ in range(4)]
# 주어지는 네 좌표를 받아줍니다
routes = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1)]
result = 100
# 유미의 위치를 시작으로 이동할 수 있는 동선을 리스트에 담고 최장 거리 이상으로 결과값을 설정해줍니다
for route in routes:
    distance = 0
    for i in range(3):
        distance += (abs(points[route[i]][0] - points[route[i + 1]][0]) ** 2 + abs(points[route[i]][1] - points[route[i + 1]][1]) ** 2) ** 0.5
    result = min(result, int(distance))
    # 피타고라스의 정리를 이용하여 각 지점사이 이동의 거리를 구하여 최단 거리를 갱신해줍니다
print(result)
# 결과를 출력해줍니다