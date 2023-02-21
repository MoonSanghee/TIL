from heapq import heappop, heappush

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
graph2 = [[] for _ in range(n + 1)]

for i in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))
    graph2[e].append((d, s))
# 두 정점을 받으면 도달하는 그래프와 출발하는 그래프 2개를 만들어 줍니다.

INF = 1e9

go = [INF] * (n + 1)
come = [INF] * (n + 1)
# 정점의 개수만큼 출발하고 도달하는 비용을 기록할 리스트 2개를 만들어줍니다.

def Go(a):
    go[a] = 0
    heap = []
    heappush(heap, (0, a))
    while heap:
        dis, p = heappop(heap)
        for cost, t in graph[p]:
            new = dis + cost
            if go[t] > new:
                go[t] = new
                heappush(heap, (new, t))
# 각 정점에서 출발하는 그래프를 이용하여 목적지에서 각 정점으로 가는데 드는 비용을 구해줍니다.

def Come(a):
    come[a] = 0
    heap = []
    heappush(heap, (0, a))
    while heap:
        dis, p = heappop(heap)
        for cost, t in graph2[p]:
            new = dis + cost
            if come[t] > new:
                come[t] = new
                heappush(heap, (new, t))
# 마찬가지로 각 정점에 도달하는 그래프를 이용하여 목적지로 도달하는데 드는 비용을 구해줍니다.

Go(x)
Come(x)
# 목적지에 도달하는 비용과 목적지에서 마을로 돌아가는 비용을 확인해줍니다.

result = 0
for i in range(n):
    total = go[i + 1] + come[i + 1]
    result = max(result, total)

print(result)
# 1부터 n번 정점까지 합이 가장 큰 값을 구하여 출력해줍니다.