from collections import deque

n, m = map(int, input().split())
# n과 m의 개수를 받아줍니다

visited = [-1 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 방문처리할 리스트와 연결 그래프를 받아줍니다.

visited[1] = 0
q = deque()
q.append(1)
# visited[1]을 0만큼의 비용으로 방문처리 해주고 덱에 1을 넣어줍니다.
while q:
    x = q.popleft()
    # q의 값을 앞에서부터 빼면서
    for i in graph[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)
        # 연결된 헛간을 확인하여 방문한적 없다면 x에서 1만큼 떨어졌다고 표시하고
        # 덱에 값을 넣어줍니다.
dis = 0
target = 0
cnt = 0
# 거리, 목적지, 동일한 개수를 표시할 변수를 지정해줍니다.
for i in range(n + 1):
    if visited[i] > dis:
        dis = visited[i]
        target = i
        cnt = 1
    elif visited[i] == dis:
        cnt += 1
    # 모든 헛간을 확인하며 거리가 더 멀어진 헛간이 있다면 dis와 target을 갱신해주고
    # cnt를 1로 바꾸어줍니다.
    # 거리가 현재 위치와 동등한 헛간이 나오면 cnt를 1 더해줍니다.
print(target, dis, cnt)
# 숨을 위치와 떨어진 거리, 개수를 차례로 출력해줍니다.