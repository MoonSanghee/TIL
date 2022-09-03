n, m = map(int, input().split())
if n == 1:
    result = 1
elif n == 2:
    result = min(4, (m - 1) // 2 + 1)
elif m > 6:
    result = m - 2
else:
    result = min(4, m)
print(result)