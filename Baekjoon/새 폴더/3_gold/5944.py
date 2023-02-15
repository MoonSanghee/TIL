from heapq import heappop, heappush

C, P, PB, PA1, PA2 = map(int, input().split())
# 간선의 개수, 정점의 개수, 시작점, 2 목적지를 받아줍니다.

graph = [[] for _ in range(P + 1)]
# 간선간의 연결 관계를 저장할 그래프를 만들어줍니다.

for _ in range(C):
    p1, p2, d = map(int, input().split())
    graph[p1].append((d, p2))
    graph[p2].append((d, p1))
    # C번만큼 간선을 받아 거리와 다른 지점과의 튜플 형태로 묶어 
    # 시작점에서의 연결 그래프를 표시해줍니다.

INF = 1e11
visited = [INF] * (P + 1)
visited2 = [INF] * (P + 1)
# 두 점에서 각 지점까지의 비용을 표시해줄 그래프를 만들어줍니다.

def move(a ,b):
    heap = []
    heappush(heap, (0, a))
    visited[a] = 0
    heap2 = []
    heappush(heap2, (0, b))
    visited2[b] = 0
    # 힙을 2개 만들어 각각 두 목적지까지 거리를 0으로 만들고 거리, 좌표의 튜플로 넣어줍니다.
    while heap:
        cost, p = heappop(heap)
        for dis, t in graph[p]:
            new = cost + dis
            if new < visited[t]:
                visited[t] = new
                heappush(heap, (new, t))
                # 힙에서 나온 정점에서 연결되는 좌표들로 이동했을때 이동하는 비용을 더
                # 줄일수 있으면 이동하고 힙에 넣어줍니다.
    while heap2:
        cost, p = heappop(heap2)
        for dis, t in graph[p]:
            new = cost + dis
            if new < visited2[t]:
                visited2[t] = new
                heappush(heap2, (new, t))
                # 힙2도 힙1과 같이 진행하여 두 목적지에서 각 정점으로 가는 비용을 구해줍니다.

move(PA1, PA2)

print(min(visited[PB] + visited[PA2], visited2[PA1] + visited2[PB]))
# 첫번째 목적지를 경유지로 하는 경우와 두번째 목적지를 경유지로 하는 경우의 
# 비용을 비교하여 적은 것을 출력해줍니다.