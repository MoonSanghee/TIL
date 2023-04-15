# import sys
# sys.stdin = open('input.txt')
from collections import deque

def DFS(start):
    order.append(start)
    visited_DFS[start] = True
    for i in graph[start]:
        if not visited_DFS[i]:
            DFS(i)

def BFS(start):
    queue = deque()
    queue.append(start)
    visited_BFS[start] = True
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for i in graph[cur]:
            if not visited_BFS[i]:
                visited_BFS[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
visited_DFS = [False] * (N + 1)
# print(visitedDFS)

graph = [[] for _ in range(N+1)]
# print(graph)

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

order = [] # 방문된 순서 기록
DFS(V)

print(order)

order = []
visited_BFS = [False] (N + 1)

BFS(V)
print(order)
