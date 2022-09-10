from collections import deque
l, c = map(int, input().split())
letters = list(map(str, input().split()))
letters.sort()

def check(x):
    cnt = 0
    for i in x:
        if i in 'aeiou':
            cnt += 1
    if 1 <= cnt <= l - 2:
        print(x)

def bfs():
    q = deque()
    for i in range(c - l + 1):
        q.append((letters[i], i))
    while q:
        x, j = q.popleft()
        if len(x) == l:
            check(x)
        else:
            for k in range(j + 1, c):
                nx = x + letters[k]
                if len(nx) <= l:
                    q.append((nx, k))
bfs()