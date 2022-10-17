from collections import deque

tc = int(input())

def bfs(a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if abs(x - e[0]) + abs(y - e[1]) <= 1000:
            return print('happy') 
        for i in range(n):
            if not check[i]:
                if abs(maps[i][0] - x) + abs(maps[i][1] - y) <= 1000:
                    q.append((maps[i][0], maps[i][1]))
                    check[i] = 1
    return print('sad')

for t in range(tc):
    n = int(input())
    s = list(map(int, input().split()))
    maps = [list(map(int, input().split())) for _ in range(n)]
    check = [0 for _ in range(n)]
    e = list(map(int, input().split()))
    bfs(s[0], s[1])