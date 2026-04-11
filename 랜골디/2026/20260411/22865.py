from heapq import heappush, heappop

N = int(input())
A, B, C = map(int, input().split())
M = int(input())
# 주어지는 후보의 개수와 친구들이 사는곳 길의 수를 받아줍니다
graph = [[] for _ in range(N + 1)]
distance = [[1e9] * 3 for _ in range(N + 1)] 
result = [1, 0]
# 연결된 길의 정보를 담을 변수와 각 땅간의 거리를 담을 변수, 결과를 담을 변수를 설정해줍니다
for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append((E, L))
    graph[E].append((D, L))
# 주어지는 각 양방향 길의 정보를 추가해줍니다
def dijkstra(start, x):
    # 몇번째 친구의 집을 기준으로 확인하는지 알기위해 집의 위치와 친구의 번호를 받아줍니다
    q = []
    heappush(q, (0, start))
    distance[start][x] = 0
    # 큐에 시작점을 넣고 거리를 0으로 설정해줍니다
    while q:
        d, now = heappop(q)
        if distance[now][x] < d:
            continue
            # 시작점에서 거리가 갱신되지 않는다면 다음 값으로 넘어갑니다
        for i in graph[now]:
            if d + i[1] < distance[i[0]][x]:
                distance[i[0]][x] = d + i[1]
                heappush(q, (d + i[1], i[0]))
        # 이동한 좌표에서 추가로 최단거리가 갱신되는 후보가 있다면 큐에 정보를 담고 거리를 갱신해줍니다
dijkstra(A, 0)
dijkstra(B, 1)
dijkstra(C, 2)
# 각 친구 집에서 각 후보지까지의 거리를 구해줍니다
for i in range(N):
    if min(distance[i + 1]) > result[1]:
        result[0] = i + 1
        result[1] = min(distance[i + 1])
# 거리가 같을 경우 후보의 번호가 작은것을 출력하므로 오름차순으로 순회하며 각 후보지에서 친구들의 집이 가장 먼 곳을 찾아줍니다
print(result[0])
# 결과를 출력해줍니다