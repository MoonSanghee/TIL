from collections import deque
import sys
input = sys.stdin.readline

n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
check = [0 for _ in range(n + 1)]
# n개의 정점의 연결 그래프와 방문 표시를 해줄 리스트를 만들어줍니다.
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # 간선의 갯수만큼 주어지는 두 점을 양방향 그래프로 표시해 줍니다.

def bfs(x):
    check[x] = 1
    q = deque()
    q.append(x)
    cnt = 2
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)
        for i in graph[v]:
            if check[i] == 0:
                check[i] = cnt
                cnt += 1
                q.append(i)
                # bfs를 설계해주는데 관계를 내림차순으로 방문한다고 하였으니 
                # 꺼내어 방문할때 연결 그래프를 내림차순으로 정렬해줍니다.

bfs(s)

for i in range(n):
    print(check[i + 1])
    # 1번째 인덱스부터 몇 번째에 방문하였는지 출력하요줍니다.