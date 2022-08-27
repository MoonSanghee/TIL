n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

size = 1
for i in range(1, n):
    for a in range(n):
        for b in range(m):
            if a + i < n and b + i < m:
                if matrix[a][b] == matrix[a + i][b] == matrix[a][b + i] == matrix[a + i][b + i]:
                    size = (i + 1) ** 2
                    