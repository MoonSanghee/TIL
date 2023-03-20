from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, status):
    q = deque()
    visited[start] = status
    q.append(start)
    # 덱 자료형에 시작점을 넣고 방문처리를 해줍니다.
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] * -1
                q.append(i)
                # x에 연결된 정점에 방문한 적 없다면 다른 그룹임을 표시해주고 방문처리 해줍니다.
            elif visited[i] == visited[x]:
                return  False
            # 연결된 접점중 같은 그룹이 있다면 이분 그래프가 아니기때문에 false를 돌려줍니다.
    return True


n = int(input())
# 몇 개의 그래프를 확인할것인지 받아줍니다.
for _ in range(n):
    u, v = map(int, input().split())
    # 정점과 간선의 개수를 받아줍니다.
    graph =[[] for _ in range(u + 1)]
    visited = [0 for _ in range(u + 1)]
    # 방문 처리할 변수와 연결 그래프를 입력해줍 변수를 지정해줍니다.

    for _ in range(v):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)
    # 간선의 개수만큼 연결된 두 정점을 입력받아 양방향 연결을 표시해줍니다.

    for i in range(1, u + 1):
        if not visited[i]:
            result = bfs(i, 1)
            # 정점을 순회하며 방문한적 없다면 이분 그래프로 연결된 형태인지 확인해줍니다.
            if not result:
                break
            # 한 정점이라도 이분 그래프로 연결된 형태가 아니라면 반복을 멈추어줍니다.
    if result:
        print("YES")
        # 모든 정점이 이분 그래프라면 'YES'를
    else:
        print("NO")
        # 아니라면 'NO'를 출력해줍니다.