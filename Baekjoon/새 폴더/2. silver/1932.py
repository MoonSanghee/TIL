n = int(input())

tower = []
for i in range(n):
    tower.append(list(map(int, input().split())))

for i in range(n):
    for j in range(len(tower[i])):
        j1, j2 = 0, 0
        if j <= i - 1:
            j1 = tower[i - 1][j]
        if j > 0:
            j2 = tower[i - 1][j - 1]
        tower[i][j] += max(j1, j2)
print(max(tower[-1]))