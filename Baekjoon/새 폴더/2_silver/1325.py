from collections import deque

def bfs(start):
    cnt = 1
    q = deque()
    q.append(start)
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return cnt
# 방문을 함수 안에서 해주어 들어갈 수 있는 최대 길이를 찾는다.
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
maxi = 1
ans = []
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > maxi:
        maxi = cnt
        ans = [i]
    elif cnt == maxi:
        ans.append(i)
# bfs 적용 값이 가장 긴 값을 갱신했으면 그 때의 값만을 가지는 리스트를 만들고 같은 길이면 리스트에 값을 추가해준다.
print(*ans)