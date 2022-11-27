n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]

C = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]

for i in range(n):
    print(*C[i])