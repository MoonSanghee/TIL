from heapq import heappop, heappush

n, m = map(int, input().split())
# 정점과 그래프의 개수를 받아줍니다.
graph = [[] for _ in range(n + 1)]
INF = 1e11
visited = [INF for _ in range(n + 1)]

for i in range(m):
    p1, p2, d = map(int, input().split())
    graph[p1].append((d, p2)), graph[p2].append((d, p1))
# 간선을 입력받고 각 정점에 도달하는 값으로 최댓값을 입력해줍니다.

def dijkstra(a):
    heap = []
    heappush(heap, (0, a))
    visited[a] = 0
    # a에 가는 비용을 0으로 만들고 힙에 0, a를 튜플 형태로 넣어줍니다.
    while heap:
        cost, p = heappop(heap)
        if visited[p] < cost:
            continue
        for dis, e in graph[p]:
            new = cost + dis
            if visited[e] > new:
                visited[e] = new
                heappush(heap, (new, e))
                # 연결된 정점에 더 적은 비용으로 이동 가능하면 값을 갱신하고 힙에 넣어줍니다.

start, end = map(int, input().split())
dijkstra(start)
print(visited[end])
# 확인할 두 정점을 받고 시작점에서 각 정점에 도달하는 최소 비용을 확인후 도착 정점까지
# 드는 비용을 출력해줍니다.