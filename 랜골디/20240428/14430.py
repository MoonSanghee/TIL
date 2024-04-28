n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 영역의 크기와 상태를 받아줍니다.
visited = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
# 주어진 영역보다 가로와 세로로 1씩 더 큰 크기의 방문 영역을 만들어줍니다.
for i in range(1, n + 1):
    for j in range(1, m + 1):
        visited[i][j] = maps[i - 1][j - 1] + max(visited[i - 1][j], visited[i][j - 1])
        # 각 방문 영역은 이전에 도달할수있는 영역의 두 값중 큰 값과 그 영역에서 획득할수 있는 점수의 합으로 갱신해줍니다

print(visited[-1][-1])
# 최종 영역에서 얻는 값을 출력해줍니다.