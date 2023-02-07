from heapq import heappop, heappush

n = int(input())
m = int(input())
# 도시의 수와 교통편의 가짓수를 받아줍니다.

graph = [[] for _ in range(n + 1)]
INF = 1e9
dp = [INF for _ in range(n + 1)]
# 각 도시에서 출발하는 교통편을 그래프에 넣어주고 도시에 도착하는 최소비용을 높은 매우 큰 수를 넣어줍니다.

for i in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
# 3개의 숫자를 받아 시작도시에서 출발하는 경로에 도착 도시와 소요 비용을 튜플로 묶어 넣어줍니다. 
start, target = map(int, input().split())
# 시작 도시와 목적지를 받아줍니다
def dijkstra(x):
    dp[x] = 0
    # dp[x]에 0의 비용으로 도착한다고 갱신해줍니다.
    heap = []
    heappush(heap, [0, x])
    # 힙 push를 통해 비용과 현재 좌표의 리스트로 값을 넣어줍니다.
    while heap:
        cost, point = heappop(heap)
        if dp[point] < cost:
            continue
        # dp[point]에 저장되어있는 비용이 지금까지 든 비용보다 적다면 넘어가줍니다.
        for t, v in graph[point]:
            # 좌표에서 출발하는 이동경로를 순회하며
            new_cost = cost + v
            # 여태까지 들었던 비용에 경로의 비용을 더해
            if dp[t] > new_cost:
                # dp[t]에 저장되어있는 비용과 비교해주고
                dp[t] = new_cost
                heappush(heap, [new_cost, t])
                # 더 적은 비용으로 도착하였다면 dp[t]를 new_cost로 갱신해줍니다.
                # 힙에 t로 가는데 든 비용과 t를 묶어 넣어줍니다.

dijkstra(start)
print(dp[target])
# 함수를 작동시키고 dp[target]에 저장된 값을 출력해줍니다.