from collections import deque

s, t = map(int, input().split())
maps = [0 for _ in range(100001)]
def find(x):
    q = deque()
    q.append(x)
    while q:
        p = q.popleft()
        if p == t:
            return maps[p]
        for i in (p - 1, p + 1, p * 2):
            if i in range(100001):
                if maps[i] == 0:
                    q.append(i)
                    maps[i] = maps[p] + 1

print(find(s))