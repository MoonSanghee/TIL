from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
# 정점의 개수와 도로의 개수를 받아줍니다.
dots = [[]for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dots[a].append(b)
    dots[b].append(a)
# 정점의 연결을 표시해줍니다.

s, e = map(int, input().split())
# 시작과 도착을 받아줍니다.
for i in range(n):
    dots[i + 1].sort()
# 사전순으로 도달할 예정이므로 각 정점에서 연결된 도로를 사전순으로 정렬해줍니다.
visited = [False] * (n + 1)
# 방문을 처리할 리스트를 만들어줍니다.
route = set()
# 경로를 담을 세트를 만들어줍니다
def bfs(start, end):
    # 출발 좌표와 목표 좌표를 받아줍니다.
    global route
    q = deque()
    q.append((start, 0, set()))

    visited[start] = True
    visited[end] = False
    # 시작 좌표를 방문처리하고 목표 좌표를 방문하지 않았다고 표시해줍니다.
    while q:
        now, cnt, passed = q.popleft()
        if now == end:
            route = passed
            return cnt
        # 원하는 좌표에 도달하면 경로를 담고 거리를 리턴해줍니다.
        for i in dots[now]:
            if visited[i] == False:
                record = deepcopy(passed)
                record.add(i)
                visited[i] = True
                q.append((i, cnt + 1, record))
            # 연결 좌표를 확인하며 사용한적 없는 도로라면 사용한 루트를 q에 넣어줍니다.
toEnd = bfs(s, e)
# 주어진 출발부터 도착까지 거리를 구해줍니다. 
visited = [False] * (n + 1)

for i in route:
    visited[i] = True
# 도착까지 도달하는데 지나갔던 정점을 표시해줍니다.
toStart = bfs(e, s)
# 도착지부터 출발지까지 거리를 구해줍니다.
print(toEnd + toStart)
# 도착지를 찍고 다시 출발지로 오는 거리를 출력해줍니다.