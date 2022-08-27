n = int(input())
maps = []
check = []
for i in range(n):
    line = list(map(str, input()))
    lst = []
    for j in range(n):
        lst.append(0)
    maps.append(line)
    check.append(lst)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if maps[j][k] == 'Y' or (maps[j][i] == 'Y' and maps[i][k] == 'Y'):
                check[j][k] = 1
maxi = 0
for i in check:
    maxi = max(sum(i), maxi)
print(maxi)