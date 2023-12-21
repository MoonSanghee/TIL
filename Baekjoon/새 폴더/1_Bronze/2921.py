n = int(input())
result = 0

for i in range(n + 1):
    for j in range(i, n + 1):
        result += (i + j)

print(result)