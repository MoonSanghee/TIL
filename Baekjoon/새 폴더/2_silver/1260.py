import sys
from collections import deque
input = sys.stdin.readline
n, m, s = map(int, input().split())
gragh = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    gragh[i].append(j)
    gragh[j].append(i)

check = [0 for _ in range(n + 1)]
dl = []
def dfs(a):
    for i in gragh[a]:
        if check[i] == 0:
            gragh[i].sort()
            check[i] = 1
            dl.append(i)
            dfs(i)
check[s] = 1
gragh[s].sort()
dl.append(s)

dfs(s)
print(*dl)

check2 = [0 for _ in range(n + 1)]
bl = []
def bfs(a):
    q = deque()
    bl.append(a)
    q.append(a)
    check2[a] = 1
    while q:
        x = q.popleft()
        for i in gragh[x]:
            if check2[i] == 0:
                bl.append(i)
                q.append(i)
                check2[i] = 1
bfs(s)
print(*bl)