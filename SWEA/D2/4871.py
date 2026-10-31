from collections import deque

T = int(input())

for tc in range(1, T + 1):
    v, e =map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    start, target = map(int, input().split())
    q = deque()
    q.append(start)
    visited = [False] * (v + 1)

    while q:
        x = q.popleft()
        visited[x] = True
        
        if x == target:
            print(f'#{tc} 1')
            break
        for i in graph[x]:
            if visited[i] == False:
                q.append(i)
    else:
        print(f'#{tc} 0')