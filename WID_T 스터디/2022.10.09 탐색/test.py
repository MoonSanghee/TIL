from collections import deque

s, t = map(int, input().split())
maps = [0 for _ in range(100001)]
def find(x, y):
    q = deque()
    q.append((x, y))
    while True:
        p, c = q.popleft()
        for i in [p - 1, p + 1, p * 2]:
            if i in range(100001):
                maps
            if i == t:
                return c + 1
            else:
                q.append((i, c + 1))
result = maps[t]
print(result)