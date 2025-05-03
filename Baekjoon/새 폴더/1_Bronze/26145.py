n, m = map(int, input().split())
S = list(map(int, input().split()))
result = S + [0] * m

for i in range(n):
    T = list(map(int, input().split()))
    for j in range(n + m):
        result[i] -= T[j]
        result[j] += T[j]

print(*result)