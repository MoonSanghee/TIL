n, m, k = map(int, input().split())
# 주어지는 변수를 받아줍니다
S2D2 = [list(map(int, input().split())) for _ in range(n)]
trees = [[[]for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = list(map(int, input().split()))
    trees[x - 1][y - 1].append(z)
# 로봇이 돌아다니며 추가해줄 양분의 정보를 받고 최초 주어지는 나무들의 정보를 받아줍니다

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
# 번식을 확인할 8방향을 변수에 담아줍니다
field = [[5] * n for _ in range(n)]
# 최초에는 모든 칸에 5만큼 양분이 들어있다고 주어졌으므로 5만큼의 양분을 가진 n * n크기의 땅을 만들어줍니다

for _ in range(k):
    # 봄, 여름
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
    # 나무가 심어진 칸을 찾아 나무가 있다면 자랄 나무와 죽을 나무를 확인하여 자랄 나무를 갱신하고 죽은 나무를 통해 땅에 양분을 추가해줍니다

    # 가을
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
    # 번식하는 나무가 있는지 확인하여 상도의 땅 안이라면 위치를 담아줍니다
    for x, y in new:
        trees[x][y].append(1)
    # 번식하여 추가된 나무의 정보를 담아줍니다
    
    # 겨울
    for i in range(n):
        for j in range(n):
            field[i][j] += S2D2[i][j]
    # 로봇이 돌아다니며 양분을 추가해줍니다
result = 0
for i in range(n):
    for j in range(n):
        result += len(trees[i][j])
# 각 칸의 나무의 수를 확인해줍니다
print(result)
# 결과를 출력해줍니다