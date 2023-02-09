from heapq import heappop, heappush
import sys
input = sys.stdin.readline

t = int(input())
# 시행횟수를 받아줍니다.
for tc in range(t):
    # 테스트 횟수만큼 시행합니다.
    n, d, c = map(int ,input().split())
    # 컴퓨터의 수와 연결된 관계 수, 시작 컴퓨터를 받아줍니다.
    graph = [[] for _ in range(n + 1)]
    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    # 관계 그래프를 표시해줍니다.
    INF = 1e9
    visited = [INF for _ in range(n + 1)]
    visited[c] = 0
    # 방문 표시를 해줄 리스트를 만들어줍니다. 
    result = [0, 0]

    def bfs(a):
        heap = []
        heappush(heap, (0, a))
        # 힙에 시작점까지의 비용이 0이라는 형태로 묶은 리스트를 넣어줍니다.
        while heap:
            # 힙에 값이 빌 때까지 반복합니다.
            cost, p = heappop(heap)
            # 힙에서 꺼낸 비용과 위치를 담아줍니다.
            for e, t in graph[p]:
                # p의 연결 그래프를 확인해줍니다.
                if visited[e] > cost + t:
                    visited[e] = cost + t
                    heappush(heap, [t + cost, e])
                    # 더 적은 시간으로 컴퓨터가 감염된다면 감염되는데 걸리는 시간을
                    # 줄여주고 걸린 시간과 감염된 컴퓨터를 리스트로 힙에 넣어줍니다.

    bfs(c)
    for i in visited:
        if i != INF:
            result[0] += 1
            result[1] = max(result[1], i)
    print(*result)
    # 방문확인을 하면서 컴퓨터가 감염됬는지와 시간이 가장 오래 걸린지를 확인해줍니다.