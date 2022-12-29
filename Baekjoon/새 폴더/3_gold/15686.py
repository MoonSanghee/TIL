from itertools import combinations

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]

homes = []
chicken = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            homes.append([i, j])
        elif maps[i][j] == 2:
            chicken.append([i, j])
# 지도를 탐색하며 각 집의 위치와 치킨집의 위치 좌표를 리스트에 넣어줍니다.
lefts = combinations(chicken, m)
# itertools 라이브러리에서 combinations메서드를 이용하여 치킨집이 m개 일 경우 조합을 찾아줍니다.
result = []

for left in lefts:
    cnt = 0
    # 각 조합을 확인해서 최종 치킨 거리값을 cnt에 담아줍니다.
    for home in homes:
        distance = []
        # 각 집을 돌면서 남은 치킨집과의 거리를 비교해 담아주고 가장 짧은 거리를 cnt에 더해줍니다.
        for c in left:
            distance.append(abs(home[0] - c[0]) + abs(home[1] - c[1]))
        cnt += min(distance)
    result.append(cnt)
    # 모든 집을 돌았다면 result에 담아줍니다.
print(min(result))
# result에 담긴 값중에서 가장 작은 값을 출력해줍니다.