n = int(input())
check = [[0] * 10 for _ in range(n)]
for i in range(1, 10):
    check[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            check[i][j] = check[i - 1][1]
        elif j == 9:
            check[i][j] = check[i - 1][8]
        else:
            check[i][j] = check[i - 1][j + 1] + check[i - 1][j - 1]
print(sum(check[n - 1]) % 1000000000)
# print(check[n - 1])