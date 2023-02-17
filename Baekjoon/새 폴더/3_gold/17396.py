from heapq import heappop, heappush

n, m = map(int, input().split())
status = list(map(int, input().split()))
status[-1] = 0
# 정점과 간선의 개수를 입력받고 지나갈 수 있는 정점인지를 받아줍니다.
# 마지막 정점으로는 이동해야하지만 무조건 밝혀져있다는 1이 들어온다고했으니
# 0으로 바꾸어줍니다.

graph = [[] for _ in range(n)]
for i in range(m):
    p1, p2, dis = map(int, input().split())
    graph[p1].append((dis, p2)), graph[p2].append((dis, p1))
# 그래프로 각 정점간의 거리를 양방향으로 받아줍니다.

INF = 1e11
visited = [INF]*(n)
# 각 정점까지의 최단거리를 확인하여 저장할 리스트를 만들어줍니다.

h = []
heappush(h, (0, 0))
visited[0] = 0
# 0번 노드까지 거리를 0으로 만들어주고 거리와 목적지를 튜플로 힙에 넣어준 다음
while h:
    cost, p = heappop(h)
    if cost > visited[p]:
        continue
    for d, t in graph[p]:
        new = cost + d
        if not status[t] and visited[t] > new:
            # 저 적은 비용으로 방문 가능하고 시야가 밝혀지지 않은 곳이라면
            visited[t] = new
            heappush(h, (new, t))
            # 이동 처리를하고 힙에 새로 이동하는데 든 비용과 목적지의 좌표를 넣어줍니다.

if visited[-1] == INF:
    print(-1)
else:
    print(visited[-1])
    # 마지막 정점의 값이 갱신되었다면 갱신된 값을 아니라면 -1을 출력합니다