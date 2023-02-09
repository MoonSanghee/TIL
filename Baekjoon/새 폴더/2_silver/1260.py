from collections import deque

n, m, v = map(int, input().split())
# 정점과 간선의 개수, 시작점을 받아줍니다.
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited2 = [0] * (n + 1)
# 정점 + 1만큼의 연결 그래프를 그려줄 리스트를 만들고 dfs와 bfs가 시행되며 방문처리할
# 리스트를 만들어줍니다.
for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    # 간선의 개수만큼 연결 그래프를 표시해줍니다.
    # 양방향 그래프이니 양쪽에서 출발하여 서로에 도착하도록 두 경우 다 넣어줍니다.

dl = []
# dfs의 결과를 넣을 리스트를 만들어줍니다.
def dfs(a):
    graph[a].sort()
    # a의 연결 그래프를 오름차순으로 정렬하고
    for i in graph[a]:
        if not visited[i]:
            # a에 연결된 정점중에 방문한 적 없는 점이라면
            visited[i] = 1
            dl.append(i)
            dfs(i)
            # 방문처리하고 dl에 넣어준뒤 재귀를 통해 먼저 시행되도록 합니다.

visited[v] = 1
graph[v].sort()
dl.append(v)
dfs(v)
print(*dl)
# visited[v]를 방문 처리해주고 graph[v]를 정렬해준뒤 dl에 v 값을 넣고 v에서 시작하도록
# dfs를 시행한 다음 dl의 값들을 출력해줍니다.

bl = []
# bfs의 결과가 저장될 리스트를 만들어줍니다.
def bfs(a):
    q = deque()
    q.append(a)
    # 덱을 만들어 시작점을 넣어줍니다.
    while q:
        x = q.popleft()
        graph[x].sort()
        # 덱에서 꺼낸값과 연결된 그래프를 정렬해주고
        for i in graph[x]:
            if not visited2[i]:
                # 연결된 정점을 방문한적 없다면
                visited2[i] = 1
                q.append(i)
                bl.append(i)
                # visited2에 방문처리를 해준뒤 q와 bl에 방문한 좌표를 넣어줍니다.

visited2[v] = 1
bl.append(v)
bfs(v)
print(*bl)
# visited2의 인덱스를 방문처리해주고 bl에 시작점을 넣어준 뒤 
# v를 시작점으로하는 bfs를 실행시키고 bl에 입력된 값들을 출력해줍니다.