n = int(input())
cnt = [[0] * 10 for _ in range(n)]
for i in range(10):
    cnt[0][i] = 1
for i in range(1, n):
    for j in range(10):
        cnt[i][j] = sum(cnt[i - 1][:j + 1])
print(sum(cnt[n - 1]) % 10007)