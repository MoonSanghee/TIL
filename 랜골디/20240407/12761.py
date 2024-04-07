from collections import deque

a, b, n, m = map(int, input().split())

visited = [0 for _ in range(100001)]
visited[n] = 1

def move():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m:
            return visited[m]
        if 0 <= x + 1 <= 100000 and visited[x + 1] == 0:
            visited[x + 1] = visited[x] + 1
            q.append(x + 1)
        if 0 <= x - 1 <= 100000 and visited[x - 1] == 0:
            visited[x - 1] = visited[x] + 1
            q.append(x - 1)
        if 0 <= x + a <= 100000 and visited[x + a] == 0:
            visited[x + a] = visited[x] + 1
            q.append(x + a)
        if 0 <= x - a <= 100000 and visited[x - a] == 0:
            visited[x - a] = visited[x] + 1
            q.append(x - a)
        if 0 <= x + b <= 100000 and visited[x + b] == 0:
            visited[x + b] = visited[x] + 1
            q.append(x + b)
        if 0 <= x - b <= 100000 and visited[x - b] == 0:
            visited[x - b] = visited[x] + 1
            q.append(x - b)
        if 0 <= x * a <= 100000 and visited[x * a] == 0:
            visited[x * a] = visited[x] + 1
            q.append(x * a)
        if 0 <= x * b <= 100000 and visited[x * b] == 0:
            visited[x * b] = visited[x] + 1
            q.append(x * b)

print(move() - 1)