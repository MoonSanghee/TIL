from heapq import heappop, heappush

n = int(input())
m = int(input())
# 도시의 개수와 간선의 개수를 받아줍니다.
graph = [[] for _ in range(n + 1)]
INF = 1e9
dp = [[INF, [i]] for i in range(n + 1)]
# 도시의 개수 + 1 개만큼 빈 리스트를 그래프에 큰 값과 도시를 시작점으로하는
# 리스트를 dp에 넣어줍니다.
for i in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    # 간선의 개수만큼 숫자쌍을 입력받아 s,e,c로 받아주고
    # graph의 s번 인덱스에 e와 c의 튜플 형태로 묶어줍니다.

start, target = map(int, input().split())
# 시작과 목표지점을 받아줍니다

def dijkstra(x):
    dp[x][0] = 0
    # dp[x]에 가는 비용을 0으로 갱신해주고
    heap = []
    heappush(heap, [0, x])
    # 비용과 좌표의 리스트 형태로 힙에 넣어줍니다.
    while heap:
        cost, point = heappop(heap)
        if dp[point][0] < cost:
            continue
        # dp[point]에 저장되어있는 비용이 현재까지 소요된 비용보다 적다면 continue를
        # 통해 넘어가줍니다.
        for t, v in graph[point]:
            new_cost = cost + v
            # t점으로 이동하는데 드는 비용을 계산하여
            if dp[t][0] > new_cost:
                # 현재까지 저장된 t까지 가는 비용보다 큰지 확인해주고
                dp[t][0] = new_cost
                dp[t][1] = dp[point][1] + [t]
                # 적다면 dp[t]까지 가는 비용을 갱신해준 뒤 dp[t]까지 가는 경로를
                # dp[point]까지 가는 경로에 t를 더한 값으로 바꾸어준 다음
                heappush(heap, [new_cost, t])
                # 소요한 비용과 목적지를 리스트로 힙에 넣어줍니다.

dijkstra(start)
# 함수를 작동시키고
print(dp[target][0])
print(len(dp[target][1]))
print(*dp[target][1])
# 목적지까지 이동하는데 필요한 비용과 루트의 길이 루트를 차례로 출력해줍니다.