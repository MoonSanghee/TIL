n,m = map(int, input().split())
result = 1
if m > n:
    n, m = m, n
for i in range(n - m + 1, n + 1):
    result *= i
for i in range(1, m + 1):
    result //= i
print(result)

