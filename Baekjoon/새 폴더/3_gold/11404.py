import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
# 도시와 버스 노선의 개수를 입력받아줍니다.
INF = 1e9
graph = [[INF]*(n + 1) for _ in range(n + 1)]
# 모든 도시사이 걸리는 비용을 INF로 설정하여줍니다.

for _ in range(m):
    s, e, dis = map(int, input().split())
    graph[s][e] = min(dis, graph[s][e])
    # 입력받은 버스 노선 정보에 따라 s에서 출발하여 e에 도착하는 비용을 갱신하여줍니다.

# 플로이드 워셜 알고리즘을 활용하여 모든 노드 쌍에 대하여 최단거리를 확인하여줍니다.
# 플로이드 워셜 기본 점화식 : Dab = min(Dab, Dak + Dkb)

for k in range(1, n + 1):
    # 모든 경로를 확인해야하기 때문에 가장 먼저 선언하여줍니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 2중 리스트에서 모든 지점을 확인해야합니다.
            if i == j:
                graph[i][j] == 0
                # i와 j의 값이 같은경우 출발 도시와 도착 도시가 같으므로 이동이 필요 없습니다.
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                # 그 외의 경우 최단 거리를 확인하고 갱신하여줍니다.
            

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
        # 모든 지점을 순회하며 방문하지 못하였다면 0으로 표시하여준다하였으므로
        # INF의 경우 0을 출력하고 이외의 경우 저장값을 출력해줍니다.
    print()
    # 매 줄의 리스트의 모든 값이 출력되면 줄을 바꾸어줍니다.