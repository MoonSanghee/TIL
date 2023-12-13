n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

c = [[0 for _ in range(k)] for _ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            c[x][y] += a[x][z] * b[z][y]

for i in c:
    for j in i:
        print(j, end = ' ')
    print()