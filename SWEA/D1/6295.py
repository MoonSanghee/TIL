row, column = map(int, input().split(','))

maps = [[0] * column for _ in range(row)]

for i in range(row):
    for j in range(column):
        maps[i][j] = i * j

print(maps)