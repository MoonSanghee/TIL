n, m, k = map(int, input().split())

S2D2 = [list(map(int, input().split())) for _ in range(n)]
trees = [[[]for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = list(map(int, input().split()))
    trees[x - 1][y - 1].append(z)

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

field = [[5] * n for _ in range(n)]

for _ in range(k):
    # 봄
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                trees[i][j].sort()
                grown = []
                nutrient = 0
                for k in trees[i][j]:
                    if k > field[i][j]:
                        nutrient += k // 2
                    else:
                        field[i][j] -= k
                        grown.append((k + 1))
                trees[i][j] = grown
                field[i][j] += nutrient

    new = []
    for x in range(n):
        for y in range(n):
            if trees[x][y]:
                for k in trees[x][y]:
                    if k % 5 == 0:
                        for i in range(8):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if 0 <= nx < n and 0 <= ny < n:
                                new.append((nx, ny))
    
    for x, y in new:
        trees[x][y].append(1)
    
    for i in range(n):
        for j in range(n):
            field[i][j] += S2D2[i][j]
    
result = 0
for i in range(n):
    for j in range(n):
        result += len(trees[i][j])

print(result)