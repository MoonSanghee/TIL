from collections import deque

n, k = map(int, input().split())
check = [0 for _ in range(100001)]
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(check[k])
            break
        for nx in (x - 1, x + 1, 2 * x):
            if nx in range(100001) and check[nx] == 0:
                q.append(nx)
                check[nx] = check[x] + 1

bfs()