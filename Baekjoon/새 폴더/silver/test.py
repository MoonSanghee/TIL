n, m, r = list(map(int, input().split()))

gragh =[[]]
for _ in range(n):
    gragh.append([])
for _ in range(m):
    i, j = list(map(int, input().split()))
    gragh[i].append(j)
check = [0] * (n + 1)
cnt = 1
def dfs(x, count):
    check[x] = count
    re = sorted(gragh[x])
    for i in re:
        if check[i] == 0:
            count += 1
            dfs(i)
dfs(1, cnt)

print(check)
