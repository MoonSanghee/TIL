from collections import deque
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
li = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
# 정점의 수만큼의 관계 리스트를 만들어 주고 도착 순서를 표시해줄 리스트를 만들어 줍니다.
for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)
# 간선을 입력받으면 쌍방향 관계이기에 a, b를 바꾸어 리스트에 각 값을 입력해줍니다.
def bfs(a):
    q = deque()
    q.append(a)
    cnt = 1
    visited[a] = cnt
    while q:
        x = q.popleft()
        li[x].sort()
        # 관계 그래프가 정렬되어있지 않으므로 정렬해줍니다.
        for i in li[x]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)
                # 관계 그래프를 순환하며 아직 도착하지 못한 자리이면 도착 표시를 해주고
                # q에 넣어줍니다.
bfs(r)
for i in range(1, n + 1):
    print(visited[i])
    # 표시해준 도착 그래프에 1부터 마지막까지 값을 차례대로 출력해줍니다.