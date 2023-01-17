import heapq, sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())
# 간선의 개수와 시작점을 입력받아줍니다.
graph = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
# 각 이동과 비용을 표시해줄 그래프를 받아줍니다.

INF = int(1e9)
distance = [INF] * (v + 1)
# 각 점에 도달하는데 매우 많은 비용이 든다고 설정해둡니다.

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 힙을 이용하여 시작점에서 거리가 0만큼 필요하고 시작점이라는것을 표시하여줍니다.
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 이미 방문한 지점이라면 넘어가줍니다.
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                # 현재 지점에서 이동 가능한 지점을 확인하며 이 지점에서 이동하였을 때
                # 거리가 저장되어있는 거리보다 짧다면 값을 갱신하고 heapq에 넣어줍니다.

dijkstra(s)
# 출발점에서 시작하는 함수를 작동시켜줍니다.
for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    # 1부터 차례대로 도달하는데 필요한 비용을 확인해주고 갱신된 적이 없다면 INF를 출력해줍니다.