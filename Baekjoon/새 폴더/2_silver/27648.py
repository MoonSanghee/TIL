n, m, k = map(int, input().split())
if k >= m + n - 1:
    print("YES")
    for i in range(n):
        line = []
        for j in range(m):
            line.append(i + j + 1)
        print(*line)
else:
    print("NO")