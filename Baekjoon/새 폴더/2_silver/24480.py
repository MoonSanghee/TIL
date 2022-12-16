n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
# 정점의 관계 그래프와 방문표시를 해줄 리스트를 만들어줍니다.
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 양방향 그래프이므로 간선의 개수만큼 입력받은 두 수를 양방향으로 입력해줍니다.
cnt = 1
# 몇 번째 방문한 노드인지 표시해 줄 값을 설정해줍니다.
def dfs(a):
    global cnt
    if visited[a] == 0:
        # 방문한 적 없는 노드라면
        graph[a].sort(reverse=True)
        # 그래프를 내림차순으로 확인을 할 것이기에 sort메서드에 reverse=True라고 입력해줍니다.
        visited[a] = cnt
        cnt += 1
    for i in graph[a]:
        if visited[i] == 0:
            dfs(i)
            # 노드를 방문처리해주었으면 연결된 노드중에 방문한적 없는 노드가 있는지 확인해주고
            # dfs를 작동시켜줍니다.
dfs(s)
for i in range(n):
    print(visited[i + 1])
    # visted리스트를 순회하며 1번부터 n + 1 번 인덱스의 방문 순서를 차례대로 출력해줍니다.