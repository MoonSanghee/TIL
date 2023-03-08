from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [101, 0]

def bfs(a):
    q = deque()
    q.append((a, 0))
    visited = [0 for _ in range(n + 1)]
    visited[a] = 1
    while q:
        x, c = q.popleft()
        for t in graph[x]:
            if not visited[t]:
                visited[t] = c + 1
                q.append((t, c + 1))    
    return c
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt < result[0]:
        result[0] = cnt
        result[1] = i
print(result)