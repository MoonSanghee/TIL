from collections import deque
n, m, k, x = map(int, input().split())
li = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    # a에서 b로가는 단방향 그래프가 주어지니 2중 리스트에 a에 위치한 리스트에 b 값을 넣어준다.
    li[a].append(b)
arrival = [0 for _ in range(n + 1)]
# 도착하였는지 확인해줄 도시의 개수 +1 개의 0을 가진 리스트를 만들어 줍니다.

def bfs(a):
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        for i in li[x]:
            if arrival[i] == 0 and i != a:
                q.append(i)
                # arrival[i] = 0인경우 아직 도착 한 적이 없으므로 1을 더해줬을때 최소 거리를 확인할 수 있다.
                # a의 경우 출발점이기때문에 다시 돌아오는 경우 값이 갱신 되어서는 안 된다.
                arrival[i] = arrival[x] + 1
                # 모든 도로의 거리는 1이기에 이전 출발지의 값에서 1을 더해준다.

bfs(x)
# 출발지를 깆준으로 bfs를 시행해준다.
cnt = 0
# 원하는 거리를 최단거리로 가지는 도시가 있는지 확인해 주기 위한 cnt를 만들어준다.
# 불리언 타입을 이용하여 True, False로만 확인하여도 된다.
for i in range(1, n + 1):
    # 1번 인덱스부터 값을 넣어주었기 때문에 1번 인덱스부터 n번 인덱스까지 도착하는데 최단거리가 얼마나 걸렸나 확인해준다.
    if arrival[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)
# 원하는 거리만큼 걸린 경우가 없으면 조건에서 말하였듯 -1을 출력해준다.