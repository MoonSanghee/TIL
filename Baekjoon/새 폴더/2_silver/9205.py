from collections import deque

def bfs():
    q = deque()
    q.append([start[0], start[1]])
    while q:
        x, y = q.popleft()
        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = cvs[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = 1
    print('sad')
    return

tc = int(input())
for t in range(tc):
    n = int(input())
    start = list(map(int, input().split()))
    cvs = []
    for i in range(n):
        cvs.append(list(map(int, input().split())))
    end = list(map(int, input().split()))
    visited = [0 for i in range(n + 1)]
    bfs()