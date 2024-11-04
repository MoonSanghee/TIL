n, m = map(int, input().split())
maps = []
# 영역의 크기를 받아줍니다.
row, column = [], []
# 가로, 세로 줄마다 들어있는 9의 개수를 담을 리스트를 만들어줍니다.
for _ in range(n):
    line = input()
    tmp = list(line.split())
    maps.append(tmp)

    cnt = line.count('9')
    row.append(cnt)
# 가로줄을 입력받아 맵에 담고 9의 개수를 확인해 담아줍니다.
for i in range(m):
    cnt = 0

    for j in range(n):
        cnt += maps[j][i].count('9')
    column.append(cnt)
# 세로 줄별 9의 개수를 담아줍니다.
print(sum(row) - max(max(row), max(column)))
# 최소한으로 남는 9의 개수를 출력해줍니다.