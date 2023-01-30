from collections import deque
n = int(input())
graph = [[] for _ in range(n + 1)]
# 노드간의 연결 그래프를 표시해줄 리스트를 만들어 줍니다/
visited = [False] * (n + 1)
# 방문처리를 해줄 리스트를 만들어 줍니다.
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
# n - 1 번만큼 관계를 받아주고 1번 노드를 방문처리 하여줍니다.
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in graph[x]:
        if visited[i] == False:
            visited[i] = x
            q.append(i)
    # q라는 이름의 덱을 만들고 1을 넣어줍니다. q의 가장 앞의 값을 뽑아 연결된 
    # 노드들을 방문처리 해주고 부모 노드를 기록해 줍니다. 
    # 모든 연결된 노드를 방문할 때 까지 시행하여 줍니다.
for i in range(2, n + 1):
    print(visited[i])
    # 2번 노드부터 부모 노드를 차례로 출력하여 줍니다.