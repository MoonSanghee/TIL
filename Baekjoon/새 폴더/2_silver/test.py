n, m = map(int, input().split())

friends = [[n]*(n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a][b] = 1
    friends[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
               friends[i][j] = 0
            else:
               friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])

total = n ** 2
now = 0
for i in range(1, n + 1):
    if sum(friends[i]) < total:
        total = sum(friends[i])
        now = i
print(now)