from collections import deque

T = int(input())

for tc in range(1, T + 1):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)
    
    visited = [False] * (v + 1)
    distance = [0] * (v + 1)

    start, end = map(int, input().split())
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        x = q.popleft()
        if x == end:
            break
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                distance[i] = distance[x] + 1
    
    print(f'#{tc} {distance[end]}')