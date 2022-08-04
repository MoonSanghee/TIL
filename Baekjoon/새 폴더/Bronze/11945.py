n, m = map(int, input().split())
seet = []

for i in range(n):
    line = list(map(str, input()))
    line = line[::-1]
    seet.append(line)

for i in range(n):
    for j in range(m):
        print(seet[i][j], end = '')
    print()