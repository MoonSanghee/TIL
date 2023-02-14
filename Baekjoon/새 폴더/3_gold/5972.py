import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 헛간의 개수와 노선의 개수를 받아줍니다.

INF = 1e8
# 노선의 개수는 50000이고 각 길에 있는 최대 소의 수는 1000이므로 둘의 곱보다 큰 수를
# 방문하지 않은 헛간까지의 거리로 만들어줍니다.

graph = [[] for _ in range(n + 1)]
visited = [INF for _ in range(n + 1)]
# 모든 헛간에 방문처리를 할 리스트와 헛간에서 출발하는 그래프를 표시할 리스트를 만들어줍니다.

for i in range(m):
    s, e, need = map(int, input().split())
    graph[s].append((need, e))
    graph[e].append((need, s))
    # m번만큼 양방향 노선과 소가 얼마나 있는지 받아주고
    # 양 헛간에서 맞은편 헛간으로 이동하는 방법을 graph에 넣어 추가해줍니다.

def dijkstra(a):
    heap = []
    heapq.heappush(heap, (0, a))
    visited[a] = 0
    # 힙을 만들어 시작점에 가는데 필요한 비용과 시작점을 튜플로 묶은 값을 넣어주고
    # 시작점을 0의 비용이 든다고 방문처리를 해줍니다.

    while heap:
        cost, p = heapq.heappop(heap)
        # 힙에서 꺼낸값을 각각 그 자리까지 도착하는데 든 비용과 위치로 지정해줍니다.

        if visited[p] >= cost:
            for food, target in graph[p]:
                # graph[p]와 연결된 노선을 순회하며 
                new = cost + food
                if visited[target] > new:
                    # 연결된 접점으로 이동하는데 저장되있는 비용보다 적게든다면
                    visited[target] = new
                    heapq.heappush(heap, (new, target))
                    # 이동하고 비용을 갱신해준 뒤 힙에 넣어줍니다.

dijkstra(1)
print(visited[-1])
# 함수를 실핼하고 목적지의 값을 출력해줍니다.