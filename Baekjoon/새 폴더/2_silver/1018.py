def pprint(x):
    for i in range(len(x)):
        print(x[i])

sero, garo = map(int, input().split())
maps = []
for i in range(sero):
    maps.append(list(input()))
# pprint(maps)
mini = 32
for i in range(sero - 7):
    for j in range(garo - 7):
        cnt =0
        color = maps[i][j]
        for i2 in range(i, i + 8):
            for j2 in range(j, j + 8):
                if (i2 + j2) % 2 == 0 and maps[i2][j2] != color:
                    cnt += 1
                elif (i2 + j2) % 2 == 1 and maps[i2][j2] == color:
                    cnt += 1
        if cnt > 32:
            cnt = 64 - cnt
        if mini > cnt:
            mini = cnt
print(mini)