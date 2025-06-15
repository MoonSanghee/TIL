import heapq
n, m = map(int, input().split())

elist = [[] for _ in range(n)]
visited = [False] * (n)
points = [list(map(int, input().split())) for _ in range(n)]
heap = [[0, 0]]

for i in range(n):
    for j in range(i + 1, n):
        distance = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
        elist[i].append((distance, j))
        elist[j].append((distance, i))

for _ in range(m):
    a, b = map(int, input().split())
    elist[a - 1].append((0, b - 1))
    elist[b - 1].append((0, a - 1))

result = 0
cnt = 0

while heap:
    if cnt == n:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        result += w
        cnt += 1
        for i in elist[s]:
            heapq.heappush(heap, i)

print(f"{result:.2f}")