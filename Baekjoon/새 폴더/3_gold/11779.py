from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
INF = 1e9
dp = [[INF, [i]] for i in range(n + 1)]

for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, target = map(int, input().split())

def dijkstra(x):
    dp[x][0] = 0
    heap = []
    heappush(heap, [0, x])
    while heap:
        cost, point = heappop(heap)
        if dp[point][0] < cost:
            continue
        for t, v in graph[point]:
            new_cost = cost + v
            if dp[t][0] > new_cost:
                dp[t][0] = new_cost
                dp[t][1] = dp[point][1] + [t]
                heappush(heap, [new_cost, t])

dijkstra(start)
print(dp[target][0])
print(len(dp[target][1]))
print(*dp[target][1])