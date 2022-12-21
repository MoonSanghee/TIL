import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        # m개의 간선을 통해 양방향 그래프를 표시하여줍니다.

    visited = [0] * (n + 1)
    # 방문 확인을 해 줄 리스트를 만들어줍니다.

    def dfs(x, cnt):
        visited[x] = 1
        # 시작 노드를 방문처리해주고
        for i in graph[x]:
            if visited[i] == 0:
                cnt = dfs(i, cnt + 1)
                # 연결 그래프를 확인하며 방문하지 않은 국가라면 방문처리하고 이동을 표시하고
                # 재귀를 통해 완전히 방문할 때까지 반복하여줍니다.
        return cnt
    result = dfs(1, 0)
    # cnt에 이동한 횟수를 리턴 받아 result에 저장하고 출력하여줍니다.
    print(result)