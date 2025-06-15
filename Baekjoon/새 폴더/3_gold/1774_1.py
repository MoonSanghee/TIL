import heapq

n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]
parents = [i for i in range(n)]

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        a, b = b, a
    parents[b] = a

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

edges = []

for i in range(n):
    for j in range(i + 1, n):
        distance = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
        edges.append((distance, i, j))

edges.sort()
result = 0

for distance, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        result += distance

print(f"{result:.2f}")