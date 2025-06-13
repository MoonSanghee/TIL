# 프림(Prim) 알고리즘
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
# 주어지는 정점의 개수와 간선의 개수를 받아줍니다
visited = [False] * (V + 1)
Elist = [[] for _ in range(V + 1)]
# 각 정점이 연결되었는지 처리할 V + 1 크기의 리스트와 각 정점에서 출발하는 간선의 정보를 담을 이중리스트를 만들어줍니다
heap = [[0, 1]]
# 1번 정점과 0의 비용을 묶인 값이 들어간 힙을 만들어줍니다
for i in range(E):
    A, B, C = map(int, input().split())
    Elist[A].append((C, B))
    Elist[B].append((C, A))
    # 두개의 정점과 연결 비용의 정보를 받아 각 시작점에 연결된 간선의 정보를 비용과 도착점으로 묶어 담아줍니다
result = 0
cnt = 0
# 결과와 연결한 정점의 수를 담을 변수를 설정해줍니다
while heap:
    if cnt == V:
        break
    # 정점이 모두 연결되었다면 반복을 멈추어줍니다
    w, s = heapq.heappop(heap)
    # 연결하는데 비용이 적게드는 간선부터 차례대로 확인하여줍니다
    if not visited[s]:
        # 도착점이 연결된적 없는 정점이라면
        visited[s] = True
        result += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)
        # 도착점을 연결하고 비용을 결과에 더한후 도착점과 연결된 간선의 정보들을 힙에 추가해줍니다

print(result)
# 최소 비용을 출력해줍니다